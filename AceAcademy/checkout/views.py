from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, HttpResponse, reverse, redirect
from django.contrib.sites.models import Site
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

# import in the settings
from django.conf import settings

# import in stripe
import stripe

# import in the lesson
from lessons.models import Lesson

# import in the purchase
from .models import Purchase
from django.contrib.auth.models import User

endpoint_secret = "whsec_POYY2lesxtDj0w3b2rS7xeGFPSLsZYnf"

# Create your views here.

@login_required()
def checkout(request):
    # tell Stripe what my api_key is
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # retrieve my shopping cart
    cart = request.session.get('shopping_cart', {})

    # create our line items
    line_items = []

    # stores all the ids of the lessons which we are purchasing
    all_lesson_ids = []

    # go through each lesson in the shopping cart
    for lesson_id, lesson in cart.items():
        # retrieve the lesson by its id from the database
        lesson_model = get_object_or_404(Lesson, pk=lesson_id)

        # create line item
        # you see all the possible properties of a line item at:
        # https://stripe.com/docs/api/invoices/line_item
        item = {
            "name": lesson_model.title,
            "amount": int(lesson_model.cost * 100),
            "quantity": lesson['qty'],
            "currency": "usd",
         }

        line_items.append(item)
        all_lesson_ids.append(str(lesson_model.id))

    # get the current website
    current_site = Site.objects.get_current()

    # get the domain name
    domain = current_site.domain

    # create a payment session to represent the current transaction
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],  # take credit cards
        line_items=line_items,
        metadata={'all_lessons_id': ",".join(all_lesson_ids)},
        client_reference_id=request.user.id,
        success_url=domain + reverse("checkout_success"),
        cancel_url=domain + reverse("checkout_cancelled")
    )

    return render(request, "checkout/checkout.html", {
        "session_id": session.id,
        "public_key": settings.STRIPE_PUBLISHABLE_KEY
    })

@login_required()
def checkout_success(request):
    request.session["shopping_cart"] = {}
    messages.success(request, "Your purchases been completed")
    return redirect(reverse('view_all_lessons'))
    # return HttpResponse("checkout success")

@login_required()
def checkout_cancelled(request):
    return redirect(reverse('view_all_lessons'))

@login_required()
@csrf_exempt
def payment_completed(request):
    # retrieve the information from the payment (also known as the payload)
    # this will contains the information sent out, like the line items
    payload = request.body

    # verify that the payment is legit
    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]

    endpoint_secret = settings.SIGNING_SECRET
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret)
    except ValueError:
        # invalid payload
        # status 400 means forbidden (this means someone tried to s
        # poof a stripe payemnt)
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        # invalid signature
        return HttpResponse(status=400)

    # handle the payment proper
    if event["type"] == "checkout.session.completed":
        # retrieve the session data
        session = event['data']['object']

        # do whatever I want with the session
        handle_payment(session)

    # status 200 means everything's ok
    return redirect(reverse('view_all_lessons'))

@login_required()
def handle_payment(session):

    user = get_object_or_404(User, pk=session["client_reference_id"])
    all_lesson_ids = session['metadata']['all_lessons_id'].split(",")

    for lesson_id in all_lesson_ids:
        lesson_model = get_object_or_404(Lesson, pk=lesson_id)

        # create the purchase model
        purchase = Purchase()
        purchase.lesson_id = lesson_model
        purchase.user_id = user
        purchase.save()