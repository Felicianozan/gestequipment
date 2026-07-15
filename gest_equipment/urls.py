
from django.contrib import admin
from django.urls import path, include
import equipments.views as views 
from django.contrib.auth import views as auth_views
from equipments.views import liste_equipements, ajouter_equipement, modifier_equipement, supprimer_equipement
from equipments import views
from equipments.views import MaintenanceListView, MaintenanceCreateView, MaintenanceUpdateView, MaintenanceDeleteView
from django.urls import path
from equipments.views import liste_incidents, ajouter_incident, modifier_incident, supprimer_incident

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
  

urlpatterns = [
   
    path('', views.index , name="home"),
    path('logout/', auth_views.LogoutView.as_view(next_page='login_technicien'), name='logout'),
    
 
    path('connexion/', views.technicien_login, name='connexion'),
    path('technicien/dashboard', views.dashboard_technicien, name='dashboard_technicien'),
      
   
    path('login-technicien/', views.technicien_login, name='login_technicien'),
   
    path('admin/', admin.site.urls),
    path('tableau_de_bord/', views.tableau_de_bord, name='tableau_de_bord'),
    path('', include('equipments.urls')),
    path('incidents/', liste_incidents, name='liste_incidents'),
    path('ajouter/', ajouter_incident, name='ajouter_incident'),
    path('modifier/<int:incident_id>/', modifier_incident, name='modifier_incident'),
    path('supprimer/<int:incident_id>/', supprimer_incident, name='supprimer_incident'),
   
    path('notifications/', views.notifications_list, name='notifications_list'),
   
    
  
    path('equipements/', views.liste_equipements, name='liste_equipements'),

    path('equipments/ajouter/', ajouter_equipement, name='ajouter_equipement'),
    path('equipments/modifier/<int:equipement_id>/', modifier_equipement, name='modifier_equipement'),
    path('equipments/supprimer/<int:equipement_id>/', supprimer_equipement, name='supprimer_equipement'),
    
    
    path('maintenances/', MaintenanceListView.as_view(), name='maintenance_list'),
    path('maintenances/nouveau/', MaintenanceCreateView.as_view(), name='maintenance_create'),
    path('maintenances/<int:pk>/modifier/', MaintenanceUpdateView.as_view(), name='maintenance_update'),
    path('maintenances/<int:pk>/supprimer/', MaintenanceDeleteView.as_view(), name='maintenance_delete'),
   
]
 
    




