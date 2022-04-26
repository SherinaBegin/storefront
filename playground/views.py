import imp
from django.shortcuts import render
# from django.db.models import Value, Q, F, Func, Count
# from django.http import HttpResponse
# from django.core.exceptions import ObjectDoesNotExist
# from django.contrib.contenttypes.models import ContentType
from django.db import transaction
from store.models import Product, Customer, OrderItem, Order, Collection

# Create your views here.
# view function takes request and returns a response
# request handler
# action


def say_hello(request):
    queryset = Product.objects.raw('SELECT * FROM store_product')

    return render(request, 'hello.html', {'name': 'Sherina', 'result': list(queryset)})
