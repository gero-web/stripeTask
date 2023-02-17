from django.http import JsonResponse
import stripe

from django.shortcuts import render
from django.conf import settings
from django.views import View
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from storeItem.models import Item,Order

stripe.api_key = settings.STRIPE_SECRET_KEY
DOMAIN = settings.DOMAIN

# Create your views here.
class CreateCheckoutSessionView(View):
    
    def get(self, request, *args, **kwargs):
        
       
        item = get_object_or_404(Item, pk=kwargs['pk'])
        price = item.price
       
        metadata = {
            "item_id": 0,
        }
        checkout_session = stripe.checkout.Session.create(
            payment_method_types = ['card'],
            line_items = [
                {
                   'price_data':{
                       'currency': 'usd',
                       'product_data': {
                            'name': item.name
                        },
                       'unit_amount': price,
                    } ,
                    
                    'quantity':1,
                },
            ],
            metadata=metadata,
            mode='payment',
            success_url=DOMAIN + '/success/',
            cancel_url=DOMAIN + '/cancel/',  
        )
        
        return JsonResponse({
            'id': checkout_session.id
        })
        
        
class CreateCheckoutSessionOrderView(View):
    
    def get(self, request, *args, **kwargs):
        
       
        order = get_object_or_404(Order, pk=kwargs['pk'])
        items = []
         
        for x in order.item.all():
            item = {
                    'price_data':{
                        'currency': 'usd',
                        'product_data': {
                                'name': x.name
                            },
                        'unit_amount': x.price,
                        } ,
                        
                        'quantity':1,
                }
            items.append(item)
            
       
        checkout_session = stripe.checkout.Session.create(
            payment_method_types = ['card'],
            line_items = items,
            mode='payment',
            success_url=DOMAIN + '/success/',
            cancel_url=DOMAIN + '/cancel/',  
        )
        
        return JsonResponse({
            'id': checkout_session.id
        })
        
        

class ItemPage(TemplateView):
    template_name = 'item.html'
    
    def get_context_data(self, **kwargs):
        pk = self.kwargs["pk"]
        item = get_object_or_404(Item, pk=pk)
        context = super().get_context_data(**kwargs)
        context.update({
            "item":item,
            "STRIPE_PUBLICK_KEY": settings.STRIPE_PUBLICK_KEY,
        })
        return context

class OrderPage(TemplateView):
    template_name = 'order.html'
    
    def get_context_data(self, **kwargs):
      
        order = get_object_or_404(Order, pk=1)
        context = super().get_context_data(**kwargs)
        context.update({
            "items":order.item.all(),
            "STRIPE_PUBLICK_KEY": settings.STRIPE_PUBLICK_KEY,
        })
        return context

class SuccessView(TemplateView):
    template_name = "success.html"

class CancelView(TemplateView):
    template_name = "cancel.html"