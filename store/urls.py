from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path('', views.home, name="home"),
    path('category/<str:category_title>', views.category_product, name="category"),
    path('product/info/<int:product_id>', views.product_info, name="product_info"),
    path('cart/add/<int:product_id>', views.add_cart, name="add_card"),
    path('cart/info/<int:user_id>', views.cart_info, name="cart_info"),
    path('comment/add/<int:product_id>', views.add_comment, name="add_comment"),
]