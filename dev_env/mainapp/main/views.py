from django.http import HttpRequest, HttpResponse
from django.shortcuts import render



def index(request):
    context: dict = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели для дома',
        
    }
    return render(request, 'main/index.html', context)

def about(request):
    context: dict = {
        'title': 'Home - Про нас',
        'content': 'О нас',
        'text_on_page': 'Преимущества магазина на фоне конкурентов.',
        
    }
    return render(request, 'main/about.html', context)