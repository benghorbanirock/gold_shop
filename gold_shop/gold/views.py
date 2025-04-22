from django.shortcuts import render

# Create your views here.
# In views.py
from .models import gold_hand, gold_ring, gold_goshvareh, silver_hand, silver_ring, silver_goshvareh, stones

def product_list(request):
    products = list(gold_hand.objects.all()) + \
               list(gold_ring.objects.all()) + \
               list(gold_goshvareh.objects.all()) + \
               list(silver_hand.objects.all()) + \
               list(silver_ring.objects.all()) + \
               list(silver_goshvareh.objects.all()) + \
               list(stones.objects.all())
    
    return render(request, 'products.html', {'products': products})

