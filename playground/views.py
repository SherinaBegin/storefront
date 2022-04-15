from re import X
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# view function takes request and returns a response
# request handler
# action 


def say_hello(request):
   # return HttpResponse('Hello World!')
   return render(request, 'hello.html', {'name': 'Sherina'})
