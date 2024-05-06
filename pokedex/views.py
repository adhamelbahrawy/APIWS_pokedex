import json
from django.http import JsonResponse
from .models import Items
from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt
def post_item(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Access data as a dictionary
            item = Items.objects.create(
                id = data["id"],
                identifier = data['identifier'],
                category_id = data['category_id'],
                cost = data['cost'],
                fling_power = data.get('fling_power', None),
                fling_effect_id = data.get('fling_effect_id', None),
            )
            return JsonResponse({'message': 'Item created successfully', 'id': item.id}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format in request body'}, status=400)
        except KeyError as e:
            return JsonResponse({'error': f'Missing required field: {e}'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Le lien existe")