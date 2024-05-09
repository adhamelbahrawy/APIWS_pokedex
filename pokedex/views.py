import json
from django.http import JsonResponse
from .models import Items
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, redirect, render

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
            item_id = data.get("id")

            if Items.objects.filter(id=item_id).exists():
                return JsonResponse({'error': f'Item with ID {item_id} already exists'}, status=400)
            
            item = Items.objects.create(
                id=item_id,
                identifier=data['identifier'],
                category_id=data['category_id'],
                cost=data['cost'],
                fling_power=data.get('fling_power', None),
                fling_effect_id=data.get('fling_effect_id', None),
            )
            return JsonResponse({'message': 'Item created successfully', 'id': item.id}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format in request body'}, status=400)
        except KeyError as e:
            return JsonResponse({'error': f'Missing required field: {e}'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def delete_item(request, item_id):
    try:
        item = Items.objects.get(id=item_id)
    except Items.DoesNotExist:
        return JsonResponse({'error': 'Item not found'}, status=404)

    if request.method == 'DELETE':
        item.delete()

        return JsonResponse({'message': 'Item deleted successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def update_item(request, item_id):
    try:
        item = Items.objects.get(id=item_id)
        data = json.loads(request.body)

        item.id = data["id"]
        item.identifier = data["identifier"]
        item.category_id = data["category_id"]
        item.cost = data["cost"]
        item.fling_power = data["fling_power"]
        item.fling_effect_id = data["fling_effect_id"]

        item.save()

        return JsonResponse({'message': 'Item updated successfuly'}, status=200)
    except Items.DoesNotExist:
        return JsonResponse({'error': 'Item not found'}, status=404)