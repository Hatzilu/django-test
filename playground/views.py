from django.shortcuts import render
from django.http import HttpResponse

def calculate(): 
    x = 1
    y = 2
    return x + y


def sayHello(request): 
    x = calculate()
    print(request)
    return render(request, 'hello.html', { 'request': request})
