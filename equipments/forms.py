from django import forms
from .models import  Utilisateur,Equipement, Incident,Technicien 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()




class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['équipement', 'description', 'état_incident']


class EquipementForm(forms.ModelForm):
    class Meta:
        model = Equipement
        fields = '__all__'  # Mets ici les champs nécessaires



class TechnicienRegisterForm(UserCreationForm):
    nom = forms.CharField(max_length=100)
    prénom = forms.CharField(max_length=100)
    email = forms.EmailField()
    téléphone = forms.CharField(max_length=20)

    class Meta:
        model = Utilisateur
        fields = ['username', 'password1', 'password2', 'nom', 'prénom', 'email', 'téléphone']



class TechnicienRegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = Technicien
        fields = ['nom', 'prénom', 'email', 'téléphone']

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )
        technicien = super().save(commit=False)
        technicien.user = user
        if commit:
            user.save()
            technicien.save()
        return technicien



