from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path('', views.item_list),
    path('create/', views.item_create),
    path('item/<int:pk>/', views.item_retrieve),
    path('update/<int:pk>/', views.item_update),
    path('item/<int:pk>/delete/', views.item_delete),
]