from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def template_1(request):
    today = datetime.now()
    lista=[1,2,3,4,5]
    context={
        'prueba':'prueba de context',
        'today' : today,
        'lista' : lista
    }
    return render(request,'template_1.html',context=context)

