from django.urls import path
from .views import add_to_cart

urlpatterns = [
    path('cart/add/<lesson_id>/', cart.views.add_to_cart,
        name="add_to_cart")
]