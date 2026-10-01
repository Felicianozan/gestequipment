# GestEquipment

GestEquipment est une application web développée avec Django pour la gestion et le suivi du matériel informatique.

## Présentation

L'objectif de GestEquipment est de faciliter la gestion des équipements informatiques au sein d'une organisation.

L'application permet de centraliser les informations relatives aux équipements, de suivre leur état et de faciliter leur administration à travers une interface web.

Ce projet a été réalisé avec Django afin de mettre en pratique le développement web, la gestion d'une base de données, les modèles Django, les vues, les formulaires et l'administration des données.

## Fonctionnalités

* Ajout de matériel informatique
* Consultation des équipements
* Modification des informations d'un équipement
* Suppression d'un équipement
* Gestion des informations relatives au matériel
* Suivi des équipements
* Gestion des données avec une base de données
* Interface web
* Administration des données avec Django Admin

## Technologies utilisées

* Python
* Django
* HTML5
* CSS3
* Bootstrap
* SQLite3
* Javascript
* Git
* GitHub

## Prérequis

Avant d'installer le projet, vous devez disposer de :

* Python 3.11 ou plus
* pip
* Git

## Installation

Cloner le projet :

```bash
git clone https://github.com/Felicianozan/GestEquipment.git
cd GestEquipment
```

Créer un environnement virtuel sous Windows :

```bash
python -m venv venv
venv\Scripts\activate
```

Sous Linux/macOS :

```bash
python3 -m venv venv
source venv/bin/activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

Si le fichier `requirements.txt` n'existe pas :

```bash
pip install django
```

## Configuration de la base de données

Le projet utilise SQLite3 par défaut.

La configuration peut être définie dans `settings.py` :

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

## Migrations

Exécuter les migrations :

```bash
python manage.py makemigrations
python manage.py migrate
```

## Lancer le projet

Démarrer le serveur Django :

```bash
python manage.py runserver
```

L'application sera accessible à l'adresse :

```text
http://127.0.0.1:8000/
```

## Interface d'administration

Pour créer un compte administrateur :

```bash
python manage.py createsuperuser
```

Puis accéder à :

```text
http://127.0.0.1:8000/admin/
```

L'interface Django Admin permet notamment d'administrer les données enregistrées dans l'application.

## Commandes utiles

Créer les migrations :

```bash
python manage.py makemigrations
```

Appliquer les migrations :

```bash
python manage.py migrate
```

Créer un administrateur :

```bash
python manage.py createsuperuser
```

Lancer le serveur :

```bash
python manage.py runserver
```

Exécuter les tests :

```bash
python manage.py test
```

## Compétences mises en pratique

Ce projet m'a permis de mettre en pratique :

* Développement web avec Django
* Programmation Python
* Conception et gestion de modèles de données
* Utilisation d'une base de données
* Création de vues et d'URL
* Gestion des formulaires
* Création de templates HTML
* Utilisation de Django Admin
* Gestion des migrations
* Utilisation de Git et GitHub

## Améliorations possibles

Le projet peut évoluer avec l'ajout de fonctionnalités telles que :

* Authentification et gestion des utilisateurs
* Gestion des rôles et permissions
* Recherche et filtrage des équipements
* Pagination
* Notifications et alertes
* Statistiques et tableaux de bord
* API REST
* Migration vers MySQL
* Déploiement en ligne

## Auteur

Feliciano Zannou

GitHub : https://github.com/Felicianozan

Portfolio : https://feliciano-zan.netlify.app

## Licence

Projet réalisé dans le cadre de l'apprentissage et de la mise en pratique du développement web avec Django.
