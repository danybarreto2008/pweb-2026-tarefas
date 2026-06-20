from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('jogos/', views.jogos, name='jogos'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
]
