from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from django.db.models import Q
from datetime import date

from lessons.models import Lesson

@login_required()
def add_to_cart(request, lesson_id):

    # the cart object is a dictionary
    cart = request.session.get('shopping_cart', {})

    # check if the lesson_id I want to add already exists inside the cart already
    # if the lesson is not in the shopping cart
    if lesson_id not in cart:
        lesson = get_object_or_404(Lesson, pk=lesson_id)

        # add the lesson to cart
        cart[lesson_id] = {
            'id': lesson_id,
            'title': lesson.title,
            'cost': float(lesson.cost),
            'qty': 1,
            'total_cost': float(lesson.cost)
        }

        messages.success(
            request, f"Added lesson '{lesson.title}' to the shopping cart")

    else:
        # if the lesson already exists in the cart
        cart[lesson_id]['qty'] += 1

    # save the shopping cart back to session
    request.session['shopping_cart'] = cart
    return redirect(reverse('view_cart'))

@login_required()
def view_cart(request):
    # loading the content of the 'shopping_cart' from the session
    cart = request.session.get('shopping_cart', {})

    total = 0
    for k, v in cart.items():
        # have to convert back to float because
        # session can only store strings
        total += float(v['cost']) * int(v['qty'])

    return render(request, 'cart/view_cart.html', {
        "cart": cart,
        "total": total
    })
@login_required()
def remove_from_cart(request, lesson_id):
    cart = request.session["shopping_cart"]
    if lesson_id in cart:
        # removew from the cart
        del cart[lesson_id]

        # save back the shopping cart into the session
        request.session['shopping_cart'] = cart

        messages.success(request, "The item has been removed")

    return redirect(reverse('view_cart'))
@login_required()
def update_quantity(request, lesson_id):
    # get the shopping cart
    cart = request.session["shopping_cart"]
    if lesson_id in cart:
        # update the quantity
        cart[lesson_id]['qty'] = request.POST['qty']
        cart[lesson_id]['total_cost'] = int(request.POST['qty']) * float(cart[lesson_id]['cost'])

        # save the cart back into the session
        request.session["shopping_cart"] = cart
        messages.success(request, f"Quantity for {cart[lesson_id]['title']} has been changed")

        return redirect(reverse('view_cart'))
    else:
        messages.success(request, "The lesson doesn't exist in your cart.")
        return redirect(reverse('view_cart'))