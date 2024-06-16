import json
from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate
from datetime import datetime, timedelta
import jwt
from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password

# SECRET_KEY = settings.SECRET_KEY

SECRET_KEY = "django-insecure-ynapegk1fh*ckenqp$wgx76wz^4@#^yzjco0mkfz_uww7^h6*v"

@csrf_exempt
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

@csrf_exempt
def get_pokemon(request, pokemon_id):
    try:
        pokemon = Pokemon.objects.get(id=pokemon_id)
        data = {
            'id': pokemon.id,
            'identifier': pokemon.identifier,
            'species_id': pokemon.species_id,
            'height': pokemon.height,
            'weight': pokemon.weight,
            'base_experience': pokemon.base_experience,
            'order': pokemon.order,
            'is_default': pokemon.is_default,
        }
        
        return JsonResponse(data)
    
    except Pokemon.DoesNotExist:
        return JsonResponse({'error': 'Pokemon not found'}, status=404)
    
@csrf_exempt
def post_pokemon(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            pokemon_id = data.get("id")

            if Pokemon.objects.filter(id=pokemon_id).exists():
                return JsonResponse({'error': f'Pokemon with ID {pokemon_id} already exists'}, status=400)
            
            pokemon = Pokemon.objects.create(
                id=pokemon_id,
                identifier = data["identifier"],
                species_id = data["species_id"],
                height = data["height"],
                weight = data["weight"],
                base_experience = data["base_experience"],
                order = data["order"],
                is_default = data["is_default"]
            )
            
            return JsonResponse({'message': 'Pokemon created successfully', 'id': pokemon.id}, status=201)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format in request body'}, status=400)
        except KeyError as e:
            return JsonResponse({'error': f'Missing required field: {e}'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
@csrf_exempt
def delete_pokemon(request, pokemon_id):
    try:
        pokemon = Pokemon.objects.get(id=pokemon_id)
    except Pokemon.DoesNotExist:
        return JsonResponse({'error': 'Pokemon not found'}, status=404)

    if request.method == 'DELETE':
        pokemon.delete()
        
        return JsonResponse({'message': 'Pokemon deleted successfully'}, status=200)
    
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def update_pokemon(request, pokemon_id):
    try:
        pokemon = Pokemon.objects.get(id=pokemon_id)
        data = json.loads(request.body)

        pokemon.id = pokemon_id
        pokemon.identifier = data["identifier"]
        pokemon.species_id = data["species_id"]
        pokemon.height = data["height"]
        pokemon.weight = data["weight"]
        pokemon.base_experience = data["base_experience"]
        pokemon.order = data["order"]
        pokemon.is_default = data["is_default"]

        pokemon.save()

        return JsonResponse({'message': 'Pokemon updated successfully'}, status=200)
    
    except Pokemon.DoesNotExist:
        return JsonResponse({'error': 'Pokemon not found'}, status=404)
    
@csrf_exempt
def get_pokemon_by_name(request, name_pokemon):
    try:
        pokemon = Pokemon.objects.get(identifier=name_pokemon)
        data = {
            'id': pokemon.id,
            'identifier': pokemon.identifier,
            'species_id': pokemon.species_id,
            'height': pokemon.height,
            'weight': pokemon.weight,
            'base_experience': pokemon.base_experience,
            'order': pokemon.order,
            'is_default': pokemon.is_default
        }
        
        return JsonResponse(data)
    
    except Pokemon.DoesNotExist:
        return JsonResponse({'error': 'Pokemon not found'}, status=404)

@csrf_exempt
def update_pokemon_by_name(request, name_pokemon):
    try:
        pokemon = Pokemon.objects.get(identifier=name_pokemon)
        data = json.loads(request.body)

        pokemon.species_id = data["species_id"]
        pokemon.height = data["height"]
        pokemon.weight = data["weight"]
        pokemon.base_experience = data["base_experience"]
        pokemon.order = data["order"]
        pokemon.is_default = data["is_default"]

        pokemon.save()

        return JsonResponse({'message': 'Pokemon updated successfully'}, status=200)
    
    except Pokemon.DoesNotExist:
        return JsonResponse({'error': 'Pokemon not found'}, status=404)

@csrf_exempt
def delete_pokemon_by_name(request, name_pokemon):
    try:
        pokemon = Pokemon.objects.get(identifier=name_pokemon)
    
    except Pokemon.DoesNotExist:
        return JsonResponse({'error': 'Pokemon not found'}, status=404)

    if request.method == 'DELETE':
        pokemon.delete()
        return JsonResponse({'message': 'Pokemon deleted successfully'}, status=200)
    
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

#
#Pas d'intérêt réel de faire un endppint pour créer un Type de pokémon
#

@csrf_exempt
def get_pokemon_type(request, identifier_pokemon):
    try:
        pokemon = Pokemon.objects.get(identifier=identifier_pokemon)
        data = {
            'identifier': pokemon.identifier,
            'type_id': pokemon.type_id,
            # Add other attributes as needed
        }
        
        return JsonResponse(data)
   
    except Pokemon.DoesNotExist:
        return JsonResponse({'error': 'Pokemon not found'}, status=404)

@csrf_exempt
def update_pokemon_type(request, identifier_pokemon):
    try:
        pokemon = Pokemon.objects.get(identifier=identifier_pokemon)
        data = json.loads(request.body)

        # Update the type_id attribute
        pokemon.type_id = data['type_id']
        # Update other attributes as needed
        
        pokemon.save()

        return JsonResponse({'message': 'Pokemon type updated successfully'}, status=200)
    
    except Pokemon.DoesNotExist:
        return JsonResponse({'error': 'Pokemon not found'}, status=404)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id = data.get('id')
            email = data.get('email')
            identifier = data.get('identifier')
            password = data.get('password')

            if Users.objects.filter(email=email).exists():
                return JsonResponse({'error': 'Email already exists'}, status=400)
            if Users.objects.filter(identifier=identifier).exists():
                return JsonResponse({'error': 'Identifier already exists'}, status=400)
            if Users.objects.filter(id=id).exists():
                return JsonResponse({'error': 'ID already exists'}, status=400)

            hashed_password = make_password(password)      

            user = Users.objects.create(
                id=id,
                email=email,
                identifier=identifier,
                password=hashed_password,
            )
            return JsonResponse({'message': 'User registered successfully', 'id': user.id}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format in request body'}, status=400)
        except KeyError as e:
            return JsonResponse({'error': f'Missing required field: {e}'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def connexion(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')

            if not email or not password:
                return JsonResponse({'error': 'Missing email or password'}, status=400)

            try:
                user = Users.objects.get(email=email)
            except Users.DoesNotExist:
                return JsonResponse({'error': 'Invalid email or password'}, status=400)

            if check_password(password, user.password):
                payload = {
                    'user_id': user.id,
                    'exp': datetime.utcnow() + timedelta(minutes=30),  # Token expires in 1 day
                    'iat': datetime.utcnow()
                }
                token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
                return JsonResponse({'token': token}, status=200)
            else:
                return JsonResponse({'error': 'Invalid email or password'}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format in request body'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def token_required(f):
    def wrap(request, *args, **kwargs):
        token = request.headers.get('Authorization', None)
        if not token:
            return JsonResponse({'error': 'Token is missing!'}, status=401)
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            user = Users.objects.get(id=data['user_id'])
            request.user = user
        except jwt.ExpiredSignatureError:
            return JsonResponse({'error': 'Token has expired!'}, status=401)
        except (jwt.InvalidTokenError, Users.DoesNotExist):
            return JsonResponse({'error': 'Invalid token!'}, status=401)
        return f(request, *args, **kwargs)
    return wrap

@csrf_exempt
@token_required
def mes_pokemons(request):
    if request.method == 'GET':
        pokemons = UserPokemon.objects.filter(user=request.user)
        data = [{'pokemon_id': pokemon.pokemon_id} for pokemon in pokemons]
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            pokemon_id = data['pokemon_id']
            if UserPokemon.objects.filter(user=request.user, pokemon_id=pokemon_id).exists():
                return JsonResponse({'error': 'Pokemon already in list'}, status=400)
            UserPokemon.objects.create(user=request.user, pokemon_id=pokemon_id)
            return JsonResponse({'message': 'Pokemon added successfully'}, status=201)
        except KeyError:
            return JsonResponse({'error': 'Missing pokemon_id in request body'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format in request body'}, status=400)
    elif request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            pokemon_id = data['pokemon_id']
            pokemon = UserPokemon.objects.filter(user=request.user, pokemon_id=pokemon_id)
            if not pokemon.exists():
                return JsonResponse({'error': 'Pokemon not found in your list'}, status=404)
            pokemon.delete()
            return JsonResponse({'message': 'Pokemon removed successfully'}, status=200)
        except KeyError:
            return JsonResponse({'error': 'Missing pokemon_id in request body'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format in request body'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)