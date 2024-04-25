# from django.http import JsonResponse
# from .models import Item
# from django.shortcuts import get_object_or_404

# def item_detail(request, item_id):
#     item = get_object_or_404(Item, id=item_id)
#     data = {
#         'id': item.id,
#         'identifier': item.identifier,
#         'category_id': item.category_id,
#         'cost': item.cost,
#         'fling_power': item.fling_power,
#         'fling_effect_id': item.fling_effect_id,
#     }
#     return JsonResponse(data)

from django.http import HttpResponse


def index(request):
    return HttpResponse("Le lien existe")