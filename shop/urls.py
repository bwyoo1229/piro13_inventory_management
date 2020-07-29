from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('create/', views.item_create, name='item_create'),
    path('item/<int:pk>/', views.item_retrieve, name='item_retrieve'),
    path('item/<int:pk>/delete/', views.item_delete, name='item_delete'),
    path('account/', views.account_list, name='account_list'),
    path('account/create/', views.account_create, name='account_create'),
    path('account/<int:pk>/', views.account_retrieve, name='account_retrieve'),
    path('account/<int:pk>/delete/', views.account_delete, name='account_delete'),
]