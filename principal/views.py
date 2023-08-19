from django.shortcuts import render


def inicio_sesion(request):
    context={
        
    }
    return render (request, 'index.html', context)
  
def menu_ppal(request):
    context={
    
    }
    return render (request, 'main.html', context)
  
def rutero(request):
    context={
    
    }
    return render (request, 'rutero.html', context)

def cap_guia(request):
    context={
    
    }
    return render (request, 'cap-guia.html', context)

def seg_cliente(request):
    context={
    
    }
    return render (request, 'seg-cliente.html', context)

def proy_cumpl(request):
    context={
    
    }
    return render (request, 'proy-cumpl.html', context)

def eje_acu(request):
    context={
    
    }
    return render (request, 'eje-acu.html', context)

def form_gcom(request):
    context={
    
    }
    return render (request, 'form-gcom.html', context)