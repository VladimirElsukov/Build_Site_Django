from django.db.models import Q

from goods.models import Products

def g_search(query):
    # Алгоритм поиска по id товара
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    keywords = [word for word in query.split() if len(word) > 2]

    # алгоритм поиска товара по названию и описанию через Q токен
    q_objects = Q()
    for token in keywords:
        q_objects |= Q(name__icontains=token)
        q_objects |= Q(description__icontains=token)

    return Products.objects.filter(q_objects)
