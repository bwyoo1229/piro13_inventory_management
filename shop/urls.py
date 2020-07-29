from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path('', views.item_list),
    path('create/', views.item_create),
    path('<int:pk>/', views.item_retrieve),
]