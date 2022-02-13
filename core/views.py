from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, name, age):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(name, age))


def sum(request, num1, num2):
    result = num1+num2
    return HttpResponse('<h1>The sum of numbers is: {}'.format(result))
