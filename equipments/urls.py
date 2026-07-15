# equipments/urls.py
from django.urls import path
from . import views  
from .views import  index_view

app_name = 'equipments'

urlpatterns = [
    
    path('tableau_de_bord/', views.tableau_de_bord, name='tableau_de_bord'),
    
    path('', index_view, name='index'),  
    path('chatbot/', views.chatbot_view, name='chatbot'),
    
    
]