"""
ASGI config for gest_equipment project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from equipments import consumers  # Importer les consumers de l'application 'equipments'

# Assurer que le paramètre d'environnement pour les paramètres Django est défini
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gest_equipment.settings')

application = ProtocolTypeRouter({
    # Ici on gère les connexions HTTP classiques
    "http": get_asgi_application(),
    
    # Gestion des connexions WebSocket
    "websocket": AuthMiddlewareStack(
        URLRouter([
            # Définir la route pour WebSocket
            path('ws/chat/', consumers.ChatbotConsumer.as_asgi()),  # Connexion au Chatbot Consumer
        ])
    ),
})

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gest_equipment.settings')


application = get_asgi_application()

