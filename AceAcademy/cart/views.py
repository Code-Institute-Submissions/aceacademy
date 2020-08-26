from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.contrib import messages
from lessons.models import Lesson

# Create your views here.
def add_to_cart(request, lesson_id):
    # attempt to get existing cart from the session using the key "shopping_cart"
    # the second argument will be the default value if 
    # if the key does not exist in the session
    cart = request.session.get('shopping_cart', {})
    
    # we check if the book_is not in the cart. If so, we will add it
    if lesson_id not in cart:
        lesson = get_object_or_404(Lesson, pk=lesson_id)
        # book is found, let's add it to the cart
        cart[lesson_id] = {
            'id':lesson_id,
            'title': lesson.title,
            'cost': 99,
            'qty': 1
        } 
        
        # save the cart back to sessions
        request.session['shopping_cart'] = cart
        
        messages.success(request, "Lesson has been added to your cart!")
        return HttpResponse("Done")
    else:
        cart[lesson_id]['qty'] +=1
        request.session['shopping_cart'] = cart
        return HttpResponse("Done")