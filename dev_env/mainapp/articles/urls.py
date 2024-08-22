from django.urls import path
from . views import article_list, article_detail

from django.conf import settings
from django.conf.urls.static import static

app_name = "articles"



urlpatterns = [
    path("", article_list, name="article_list"),
    path("articles/<slug:slug>/", article_detail, name="article_detail"),
    # Другие ваши маршруты...
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
