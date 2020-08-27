from django.urls import path
import cart.views

urlpatterns = [
    path('add/<lesson_id>', cart.views.add_to_cart, name="add_to_cart"),
    path('view/', cart.views.view_cart, name="view_cart"),
    path('remove/<lesson_id>', cart.views.remove_from_cart, name="remove_from_cart"),
    path('update_quantity/<lesson_id>', cart.views.update_quantity, name="update_cart_quantity")
]