from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from articles.models import BlogPost


def article_list(request):
    articles = (BlogPost.get_published())  # Получаем статьи
    blog_posts = BlogPost.objects.all()  # Получаем все посты 
    return render(
        request,
        "articles/article_list.html",
        {"articles": articles, "blog_posts": blog_posts},
    )


def article_detail(request, slug):
    article = get_object_or_404(BlogPost, slug=slug)
    return render(request, "articles/article_detail.html", {"article": article})
