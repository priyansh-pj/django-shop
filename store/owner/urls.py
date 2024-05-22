from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('users/new/', views.user_create, name='user_create'),
    path('users/edit/<int:id>/', views.user_edit, name='user_update'),
    path('users/delete/<int:id>/', views.user_delete, name='user_delete'),
]
