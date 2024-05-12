import json
from django.http import JsonResponse
from .models import Items, Moves
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

@csrf_exempt
def get_move(request, move_id):
    try:
        move = Moves.objects.get(id=move_id)
        data = {
            "id" : move.id,
            "identifier" : move.identifier,
            "generation_id" : move.generation_id,
            "type_id" : move.type_id,
            "power" : move.power,
            "pp" : move.pp,
            "accuracy" : move.accuracy,
            "priority" : move.priority,
            "target_id" : move.target_id,
            "damage_class_id" : move.damage_class_id,
            "effect_id" : move.effect_id,
            "effect_chance" : move.effect_chance,
            "contest_type_id" : move.contest_type_id,
            "contest_effect_id" : move.contest_effect_id,
            "super_contest_effect_id" : move.super_contest_effect_id
        }
        return JsonResponse(data)
    except Items.DoesNotExist:
        return JsonResponse({'error': 'Item not found'}, status=404)

@csrf_exempt
def post_move(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            move_id = data.get("id")

            if Moves.objects.filter(id=move_id).exists():
                return JsonResponse({'error': f'Move with ID {move_id} already exists'}, status=400)
            
            move = Moves.objects.create(
                id=move_id,
                identifier = data["identifier"],
                generation_id = data["generation_id"],
                type_id = data["type_id"],
                power = data["power"],
                pp = data["pp"],
                accuracy = data["accuracy"],
                priority = data["priority"],
                target_id = data["target_id"],
                damage_class_id = data["damage_class_id"],
                effect_id = data["effect_id"],
                effect_chance = data["effect_chance"],
                contest_type_id = data["contest_type_id"],
                contest_effect_id = data["contest_effect_id"],
                super_contest_effect_id = data["super_contest_effect_id"]
            )
            return JsonResponse({'message': 'Move created successfully', 'id': move.id}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format in request body'}, status=400)
        except KeyError as e:
            return JsonResponse({'error': f'Missing required field: {e}'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
@csrf_exempt
def delete_move(request, move_id):
    try:
        item = Moves.objects.get(id=move_id)
    except Moves.DoesNotExist:
        return JsonResponse({'error': 'Moves not found'}, status=404)

    if request.method == 'DELETE':
        item.delete()

        return JsonResponse({'message': 'Moves deleted successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def update_move(request, move_id):
    try:
        move = Moves.objects.get(id=move_id)
        data = json.loads(request.body)

        move.id=move_id
        move.identifier = data["identifier"]
        move.generation_id = data["generation_id"]
        move.type_id = data["type_id"]
        move.power = data["power"]
        move.pp = data["pp"]
        move.accuracy = data["accuracy"]
        move.priority = data["priority"]
        move.target_id = data["target_id"]
        move.damage_class_id = data["damage_class_id"]
        move.effect_id = data["effect_id"]
        move.effect_chance = data["effect_chance"]
        move.contest_type_id = data["contest_type_id"]
        move.contest_effect_id = data["contest_effect_id"]
        move.super_contest_effect_id = data["super_contest_effect_id"]

        move.save()

        return JsonResponse({'message': 'Move updated successfuly'}, status=200)
    except Items.DoesNotExist:
        return JsonResponse({'error': 'Move not found'}, status=404)
# id
# identifier
# generation_id
# type_id
# power
# pp
# accuracy
# priority
# target_id
# damage_class_id
# effect_id
# effect_chance
# contest_type_id
# contest_effect_id
# super_contest_effect_id


# id = models.IntegerField(primary_key=True)
# identifier = models.CharField(max_length=79)
# generation_id = models.IntegerField()
# type_id = models.IntegerField()
# power = models.SmallIntegerField(blank=True, null=True)
# pp = models.SmallIntegerField(blank=True, null=True)
# accuracy = models.SmallIntegerField(blank=True, null=True)
# priority = models.SmallIntegerField()
# target_id = models.IntegerField()
# damage_class_id = models.IntegerField()
# effect_id = models.IntegerField()
# effect_chance = models.IntegerField(blank=True, null=True)
# contest_type_id = models.IntegerField(blank=True, null=True)
# contest_effect_id = models.IntegerField(blank=True, null=True)
# super_contest_effect_id = models.IntegerField(blank=True, null=True)