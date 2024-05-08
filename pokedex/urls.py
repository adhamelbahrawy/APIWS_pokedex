from django.urls import path
from . import views


urlpatterns = [
    path('api/items/<int:item_id>/', views.get_item, name='get_item'),
    path('api/items/create/', views.post_item),
    path('api/items/<int:item_id>/update/', views.update_item),
    path('api/items/<int:item_id>/delete/', views.delete_item),
]


# urlpatterns = [
#     # path("", views.index, name="index"),
#     path('api/items/<int:item_id>/', views.get_item),
#     path('api/items/', views.post_item),
#     # path('api/items/<int:item_id>', views.update_item),
#     # path('api/items/<int:item_id>', views.delete_item),
# ]