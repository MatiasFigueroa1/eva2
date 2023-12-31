from django.shortcuts import render

# Create your views here.
def renderS13(request):
    data={
        "card": "c2",
        "Modelo":"S13",
        'src':'images/S13.jpg',
        'color':"Azul",
        'motor': "CA18DET",
        'año':'1989',
        'HP':'176'
    }
    return render(request,'templatesAutos/index.html',data)

def renderR33(request):
    data={
        "card": "c2",
        "Modelo":"R33",
        'src':'images/r33.jpg',
        'color':"gris",
        'motor': "RB26DETT",
        'año':'1995',
        'HP':'305'
    }
    return render(request,'templatesAutos/index.html',data)

def render350z(request):
    data={
        "card": "c2",
        "Modelo":"350z",
        'src':'images/350z.jpg',
        'color':"Figura de Acción",
        'motor': "VQ35DE",
        'año':'2004',
        'HP':'291'
    }
    return render(request,'templatesAutos/index.html',data)

def render240z(request):
    data={
        "card": "c2",
        "Modelo":"240z",
        'src':'images/240z.webp',
        'color':"Figura de Acción",
        'motor': "DOHC",
        'año':'1975',
        'HP':'162'
    }
    return render(request,'templatesAutos/index.html',data)

def renderAutos(request):
    data={
        "card" : 'c1'
    }
    return render(request, "templatesAutos/index.html",data)