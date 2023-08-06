from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def guia(request):

    context={

    }
    return render(request,'guia/guia.html',context)