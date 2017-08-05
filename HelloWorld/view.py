# -*- coding: utf-8 -*-

from django.shortcuts import render


def base(request):
    return render(request,'base.html')
 
def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)
