from django.contrib import admin

from .models import Equipement, Incident, Maintenance, Technicien, Notification, Admin, Utilisateur

# Enregistrer les modèles dans l'administration
admin.site.register(Equipement)
admin.site.register(Incident)
admin.site.register(Maintenance)
admin.site.register(Technicien)
admin.site.register(Notification)
admin.site.register(Admin)
admin.site.register(Utilisateur)  # Pour le modèle Utilisateur personnalisé



