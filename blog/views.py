from django.shortcuts import render
from .models import Article, Category

def list(request):
    # Asegúrate de usar .all() y no .get()
    articles = Article.objects.all()
    
    return render(request, 'articles/list.html', {
        'title': 'Artículos',
        'articles': articles
    })