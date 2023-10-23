from django.shortcuts import render
# Create your views here.
def renderindex(request):
    return render (request, 'productosAPP/index.html')

def electronica (request):
    data={
        "titulo":"Electronica",
        'producto1':"MAC",
        'producto2':"Celular",
        'producto3': "PlayStation",
        'url':'/www.inacap.cl',
        'imagen':'images/xtreet-150.jpg'
    }
    return render (request,'productosAPP/productos.html',data)

def juguetes(request):
    data={
        "titulo":"Juguetes",
        'producto1':"Pelota",
        'producto2':"Figura de Acción",
        'producto3': "Juego de Mesa",
        'imagen':'images/xtreet-150.jpg'
    }
    return render (request,'productosAPP/productos.html',data)

def ropa(request):
    data={
        "titulo":"Ropa",
        'producto1':"Polera",
        'producto2':"Chaqueta",
        'producto3': "Zapatilla",
        'imagen':'images/xtreet-150.jpg'
    }
    return render (request,'productosAPP/productos.html',data)