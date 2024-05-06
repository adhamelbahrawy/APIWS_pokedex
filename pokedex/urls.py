from django.urls import path
from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path('api/items/<int:item_id>/', views.get_item, name='get_item'),
    # path('api/items/', views.get_item, name='get_item'),
]