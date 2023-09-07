from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('livestreaming/', views.livestream, name='livestreaming'),
    path('join/', views.join_room, name='join')
]