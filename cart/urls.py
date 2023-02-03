from django.urls import path
from cart import views, api

app_name = 'cart'

urlpatterns = [
    path('cart-page/', views.CartView.as_view(), name="cart-page"),
    path('cart-detail/<int:id>/', views.DetailView.as_view(), name="cart-detail-page"),

    path('cartAPI/', api.CartViewSet.as_view({
        'get': 'get',
        'post': 'post',
    }), name="cart_api"),

    path('cart-detail-api/<int:id>/', api.CartViewSet.as_view({
        'post': 'delete',
        'get': 'get_detail'
    }), name="cart-delete"),
]