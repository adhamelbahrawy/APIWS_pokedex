from django.contrib import admin
from django.urls import path
from .pokedex import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/items/<int:item_id>/', views.get_item, name='get_item'),
]
