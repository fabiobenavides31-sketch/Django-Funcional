from django.shortcuts import render

# Create your views here.
def index(reques):
    return render(reques,'mainapp/index.html',{
        'title': 'inicio'
    })

def about(request):
    return render(request, 'mainapp/about.html',{
        'title': 'Sobre Nosotros'
    })