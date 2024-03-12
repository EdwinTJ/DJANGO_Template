from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/new/', views.create_user, name='new_user'),
    path('sessions/new/', views.create_session, name='new_session'),
    # path('users/', views.create_user, name='create_user'),
    # path('sessions/', views.create_session, name='create_session'),
    path('sessions/destroy/', views.destroy_session, name='destroy_session'),
    path('destinations/', views.destinations, name='destinations'),
    path('destinations/new/', views.create_destination, name='new_destination'),
    path('destinations/<int:id>/', views.edit_destination, name='edit_destination'),
    path('destinations/<int:id>/delete/', views.destroy_destination, name='delete_destination'),
]