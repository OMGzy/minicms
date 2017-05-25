from django.shortcuts import render, redirect
from django.http import HttpResponse
from news.models import *

def index(request):
    # columns = Column.objects.all()
    nav_display_columns = Column.objects.filter(nav_display=True)
    home_display_columns = Column.objects.filter(home_display=True)
    return render(request, 'index.html', {'nav_display_columns':nav_display_columns,
                                          'home_display_columns':home_display_columns})

def column_detail(request, column_slug):
    column = Column.objects.get(slug=column_slug)
    return render(request, 'news/column.html', {'column':column})

def article_detail(request, pk, article_slug):
    article = Article.objects.get(pk=pk)
    print('============\n',article)
    if article_slug != article.slug:
        return redirect(article, permanent=True)
    return render(request, 'news/article.html', {'article':article})
