from django.contrib import admin
from django.urls import path
from storeItem.views import (
    SuccessView,
    CancelView,
    CreateCheckoutSessionView,
    ItemPage,
    CreateCheckoutSessionOrderView,
    OrderPage,
)

urlpatterns = [
    path('cancel/', CancelView.as_view(), name = 'cancel'),
    path('success/', SuccessView.as_view(), name= 'success'),
    path('buy/<pk>', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('order/<pk>', CreateCheckoutSessionOrderView.as_view(), name='order'),
    path('item/<pk>', ItemPage.as_view(), name='item'),
    path('order/', OrderPage.as_view(), name='order_page'),
    
]
