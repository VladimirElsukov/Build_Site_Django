from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request):

    categories = Categories.objects.all()

    context: dict = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели Home',
        'categories': categories
        
    }
    return render(request, 'main/index.html', context)

def about(request):
    context: dict = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Осветить преимущества магазина, его выделение на фоне конкурентов.',
        
    }
    return render(request, 'main/about.html', context)