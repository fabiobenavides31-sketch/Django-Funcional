from django.shortcuts import render, get_object_or_404
from .models import Article, Category

def list(request):
    # Asegúrate de usar .all() y no .get()
    articles = Article.objects.all()
    
    return render(request, 'articles/list.html', {
        'title': 'Artículos',
        'articles': articles
    })

def category(request,category_id):
    category = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(categories=category)
    return render(request,'categories/category.html',{
        'category' : category,
       
    })