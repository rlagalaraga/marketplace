from django.urls import path
from market import views, api

app_name = 'market'

urlpatterns = [

    path('dashboard/', views.DashboardView.as_view(), name="dashboard"),
    path('product-view/<int:id>/', views.DetailView.as_view(), name="productDetail"),
    path('wishlist-page/', views.WishlistView.as_view(), name="wishlist-page"),

    path('list/', api.ProductViewSet.as_view({
        'get': 'get_all',
    }), name="product_list"),

    path('product/', api.ProductViewSet.as_view({
        'get': 'get_owned',
        'post': 'post',
    }), name="product"),

    path('product-detail/<int:id>/', api.ProductViewSet.as_view({
        'get': 'get',
        'put': 'put',
        'post': 'delete',
        'patch': 'patch',
    }), name="product-detail"),

    path('product-wishlist/<int:id>/', api.ProductViewSet.as_view({
        'post': 'wishlist_product'
    }), name="product-wishlist")
]