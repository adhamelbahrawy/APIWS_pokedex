from django.urls import path
from . import views


urlpatterns = [
    path('api/items/<int:item_id>/', views.get_item),
    path('api/items/create/', views.post_item),
    path('api/items/<int:item_id>/update/', views.update_item),
    path('api/items/<int:item_id>/delete/', views.delete_item),
    path('api/moves/<int:move_id>/', views.get_move),
    path('api/moves/create/', views.post_move),
    path('api/moves/<int:move_id>/delete/', views.delete_move),
    path('api/moves/<int:move_id>/update/', views.update_move),
    path('api/pokemon/<int:pokemon_id>/', views.get_pokemon),
    path('api/pokemon/create/', views.post_pokemon),
    path('api/pokemon/<int:pokemon_id>/delete/', views.delete_pokemon),
    path('api/pokemon/<int:pokemon_id>/update/', views.update_pokemon),
    path('api/pokemon/<str:name_pokemon>/', views.get_pokemon_by_name),
    path('api/pokemon/<str:name_pokemon>/update/', views.update_pokemon_by_name),
    path('api/pokemon/<str:name_pokemon>/delete/', views.delete_pokemon_by_name),
    path('api/pokemon/types/<str:identifier_pokemon>/', views.get_pokemon_type, name='get_pokemon_type_by_name'),
    path('api/pokemon/types/<str:identifier_pokemon>/update/', views.update_pokemon_type, name='update_pokemon_type_by_name'),
]