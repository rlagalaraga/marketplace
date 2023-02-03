from django.urls import path
from transaction import views, api

app_name = 'transaction'

urlpatterns = [
    path('buyer/', views.BuyerView.as_view(), name='buyer'),
    path('seller/', views.SellerView.as_view(), name='seller'),
    
    path('transact/', api.TransactionViewSet.as_view({
        'get': 'get',
        'post': 'post',
    }), name="transact")
]