from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import main, cart, add_to_cart, clear_cart, update_quantity, pizza_1, pizza_2, pizza_3, login, \
    RegisterUser, profile, logout_user, add_review_1, delete_review, add_like, checkout, order_success

urlpatterns = [
    path('', main, name='main'),
    path('cart/', cart, name='cart'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('update_quantity/', update_quantity, name='update_quantity'),  # New path for updating quantity
    path('clear_cart/', clear_cart, name='clear_cart'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', login, name='login'),
    path('pizza_1/', pizza_1, name='pizza_1'),
    path('pizza_2/', pizza_2, name='pizza_2'),
    path('pizza_3/', pizza_3, name='pizza_3'),
    path('profile/', login_required(profile), name='profile'),
    path('logout/', login_required(logout_user), name='logout_user'),
    path('add_review_1/', add_review_1, name='add_review_1'),
    path('checkout/', checkout, name='checkout'),
    path('order_success/', order_success, name='order_success'),
    path('delete_review/<int:review_id>/', delete_review, name='delete_review'),
    path('add_like/<int:review_id>/', add_like, name='add_like'),

]