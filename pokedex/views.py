from django.http import JsonResponse
from .models import Items

def get_item(request, item_id):
    try:
        item = Items.objects.get(id=item_id)
        data = {
            'id': item.id,
            'identifier': item.identifier,
            'category_id': item.category_id,
            'cost': item.cost,
            'fling_power': item.fling_power,
            'fling_effect_id': item.fling_effect_id,
        }
        return JsonResponse(data)
    except Items.DoesNotExist:
        return JsonResponse({'error': 'Item not found'}, status=404)


# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Le lien existe")