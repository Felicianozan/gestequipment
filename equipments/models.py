from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings 
 





# Classe Utilisateur personnalisé (hérite de AbstractUser)
class Utilisateur(AbstractUser):
    # Ajoute ici les champs supplémentaires si nécessaire
    téléphone = models.CharField(max_length=20, blank=True, null=True)
    adresse = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.username


# Classe pour représenter un équipement
class Equipement(models.Model):
    STATUTS = [
        ('fonctionnel', 'Fonctionnel'),
        ('panne', 'En panne'),
        ('maintenance', 'En maintenance'),
    ]
    
    nom = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    etat = models.CharField(max_length=50, choices=STATUTS, default='fonctionnel')

    def __str__(self):
        return self.nom


# Classe pour représenter un incident sur un équipement
class Incident(models.Model):
    équipement = models.ForeignKey(Equipement, on_delete=models.CASCADE, related_name='incidents')
    description = models.TextField()
    date_signalement = models.DateTimeField(auto_now_add=True)
    état_incident = models.CharField(max_length=50, choices=[('Non résolu', 'Non résolu'), ('Résolu', 'Résolu')], default='Non résolu')
    résolu = models.BooleanField(default=False)

    def __str__(self):
        return f"Incident sur {self.équipement.nom}"


# Classe pour représenter une maintenance sur un équipement
class Maintenance(models.Model):
    TYPE_MAINTENANCE_CHOICES = [
        ('Préventive', 'Préventive'),
        ('Corrective', 'Corrective'),
    ]
    
    équipement = models.ForeignKey(Equipement, on_delete=models.CASCADE, related_name='maintenances')
    type_maintenance = models.CharField(max_length=50, choices=TYPE_MAINTENANCE_CHOICES)
    date_maintenance = models.DateTimeField(null=True,blank=True)
    technicien = models.ForeignKey('Technicien', on_delete=models.SET_NULL, null=True, related_name='maintenances')
    commentaire = models.TextField()
    
    def __str__(self):
        return f"Maintenance de {self.équipement.nom} - {self.type_maintenance}"


# Classe pour représenter un technicien


class Technicien(models.Model):
    user = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)  # Lien avec l'utilisateur
    nom = models.CharField(max_length=100)
    prénom = models.CharField(max_length=100)
    email = models.EmailField()
    téléphone = models.CharField(max_length=20)
   

    def __str__(self):
        return f"{self.nom} {self.prénom}"


# Classe pour représenter une notification

class Notification(models.Model):
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)
    type_notification = models.CharField(max_length=50)
    lu = models.BooleanField(default=False)  

    def __str__(self):
        return f"Notification for {self.utilisateur.username} - {'Read' if self.lu else 'Unread'}"

# Classe pour représenter un administrateur (hérite de Utilisateur)
class Admin(models.Model):
    user = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)  # Lien avec l'utilisateur (admin)
    rôle = models.CharField(max_length=50, choices=[('Admin', 'Admin')])

    def __str__(self):
        return f"Admin: {self.user.username}"
    






