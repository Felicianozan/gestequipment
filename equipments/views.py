from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm 
from .models import Equipement, Incident, Maintenance, Technicien, Notification,Incident
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import EquipementForm,IncidentForm
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
User = get_user_model()     

from django.contrib import messages
from django.http import HttpResponse

from django.contrib.auth import authenticate, login
from .forms import TechnicienRegisterForm

from django.contrib.auth.decorators import login_required




def index_view(request):
    return render(request, 'equipments/index.html')





def notifications_list(request):
    # Récupérer toutes les notifications de l'utilisateur connecté
    notifications = Notification.objects.filter(utilisateur=request.user).order_by('-date_envoi')
    
    # Rendre la page de notifications
    return render(request, 'equipments/notifications_list.html', {'notifications': notifications})



def liste_incidents(request):
    incidents = Incident.objects.all().order_by('-date_signalement')
    return render(request, 'incidents/liste.html', {'incidents': incidents})

def ajouter_incident(request):
    if request.method == "POST":
        form = IncidentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_incidents')
    else:
        form = IncidentForm()
    return render(request, 'incidents/form.html', {'form': form})

def modifier_incident(request, incident_id):
    incident = get_object_or_404(Incident, id=incident_id)
    if request.method == "POST":
        form = IncidentForm(request.POST, instance=incident)
        if form.is_valid():
            form.save()
            return redirect('liste_incidents')
    else:
        form = IncidentForm(instance=incident)
    return render(request, 'incidents/form.html', {'form': form})



def supprimer_incident(request, incident_id):
    incident = get_object_or_404(Incident, id=incident_id)
    if request.method == "POST":
        incident.delete()
        return redirect('liste_incidents')
    return render(request, 'incidents/supprimer.html', {'incident': incident})


class MaintenanceListView(ListView):
    model = Maintenance
    template_name = 'maintenance/list.html'
    context_object_name = 'maintenances'
    ordering = ['-date_maintenance']
    paginate_by = 10
    
class MaintenanceCreateView(CreateView):
    model = Maintenance
    fields = ['équipement', 'type_maintenance', 'date_maintenance', 'technicien', 'commentaire']
    template_name = 'maintenance/form.html'
    success_url = reverse_lazy('maintenance_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['date_maintenance'].widget.attrs.update({'class': 'datetimepicker'})
        return form
    
        
class MaintenanceUpdateView(UpdateView):
    model = Maintenance
    fields = ['équipement', 'type_maintenance', 'date_maintenance', 'technicien', 'commentaire']
    template_name = 'maintenance/form.html'
    success_url = reverse_lazy('maintenance_list')

class MaintenanceDeleteView(DeleteView):
    model = Maintenance
    template_name = 'maintenance/confirm_delete.html'
    success_url = reverse_lazy('maintenance_list')

    

def tableau_de_bord(request):
    stats_statut = Equipement.objects.values('etat').annotate(
        total=Count('id')
    ).order_by('etat')

    # Derniers équipements ajoutés (10 derniers)
    derniers_equipements = Equipement.objects.order_by('-id')[:10]

    # Conversion des données pour Chart.js
    etat_labels = [statut['etat'] for statut in stats_statut]
    etat_data = [statut['total'] for statut in stats_statut]

    context = {
        'etat_labels': etat_labels,
        'etat_data': etat_data,
        'derniers_equipements': derniers_equipements,
        'total_equipements': sum(etat_data)
    }

    return render(request, 'equipments/tableau_de_bord.html', context)

def index(request):
    equipements = Equipement.objects.all()
    incidents = Incident.objects.all()
    maintenances = Maintenance.objects.all()

    return render(request, 'equipments/index.html', {
        'equipements': equipements,
        'incidents': incidents,
        'maintenances': maintenances,
    })


def index(request):
    notifications_non_lues = Notification.objects.filter(utilisateur=request.user, lu=False).count()
    return render(request, "equipments/index.html", {"notifications_non_lues": notifications_non_lues})



def liste_equipements(request):
    equipements = Equipement.objects.all()
    return render(request, 'equipments/equipements.html', {'equipements': equipements})

def ajouter_equipement(request):
    if request.method == "POST":
        form = EquipementForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data.get('nom')

            # Vérifie si un équipement avec ce nom existe déjà
            if Equipement.objects.filter(nom__iexact=nom).exists():
                form.add_error('nom', "Un équipement avec ce nom existe déjà.")
            else:
                form.save()
                return redirect('liste_equipements')
    else:
        form = EquipementForm()

    return render(request, 'equipments/ajouter_equipement.html', {'form': form})


def modifier_equipement(request, equipement_id):
    equipement = Equipement.objects.get(id=equipement_id)
    
    if request.method == "POST":
        form = EquipementForm(request.POST, instance=equipement)
        if form.is_valid():
            form.save()
            return redirect('liste_equipements')
    else:
        form = EquipementForm(instance=equipement)
    
    return render(request, 'equipments/modifier_equipement.html', {'form': form})

def supprimer_equipement(request, equipement_id):
    equipement = Equipement.objects.get(id=equipement_id)
    
    if request.method == "POST":
        equipement.delete()
        return redirect('liste_equipements')
    
    return render(request, 'equipments/supprimer_equipement.html', {'equipement': equipement})


def chatbot_view(request):
    return render(request, 'equipments/chatbot.html')

def dashboard_technicien(request):
    return render(request, 'technicien/dashboard.html')


def technicien_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print("Tentative avec :", username, password)  # Ajout temporaire pour debug

        user = authenticate(request, username=username, password=password)
        if user is not None:
            try:
                Technicien.objects.get(user=user)
                login(request, user)
                return redirect('dashboard_technicien')
            except Technicien.DoesNotExist:
                messages.error(request, "Vous n'êtes pas autorisé à accéder ici.")
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")

    return render(request, 'technicien/login.html')



