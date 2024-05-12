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
]


# urlpatterns = [
#     # path("", views.index, name="index"),
#     path('api/items/<int:item_id>/', views.get_item),
#     path('api/items/', views.post_item),
#     # path('api/items/<int:item_id>', views.update_item),
#     # path('api/items/<int:item_id>', views.delete_item),
# ]