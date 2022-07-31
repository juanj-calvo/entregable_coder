from multiprocessing import context
from django.shortcuts import render
from familiaap.models import family
# Create your views here.

def create_member(request):
    new_member = family.objects.create(integrant= 'Hija',name= 'Lucia Calvo',age= 22 )
    context= {
        'new_member':new_member
    }
    return render(request,'familia_1.html',context=context)

def list_members(request):
    members = family.objects.all()
    context= {
        'members':members
    }
    return render(request,'familia_2.html',context=context)
