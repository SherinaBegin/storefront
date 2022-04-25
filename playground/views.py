from django.shortcuts import render
from django.db.models import Q, F
# from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Customer, OrderItem
# Create your views here.
# view function takes request and returns a response
# request handler
# action


def say_hello(request):
    queryset = Product.objects.select_related('collection').all()

    # return HttpResponse('Hello World!')
    return render(request, 'hello.html', {'name': 'Sherina', 'products': list(queryset)})
