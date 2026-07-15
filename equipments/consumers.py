import json
import dialogflow
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatbotConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'chatbot'
        # Autoriser la connexion
        await self.accept()

    async def disconnect(self, close_code):
        # Déconnecter le websocket
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        user_message = text_data_json['message']
        
        # Obtenir la réponse de Dialogflow
        dialogflow_response = await self.get_dialogflow_response(user_message)

        # Envoyer la réponse au front-end via WebSocket
        await self.send(text_data=json.dumps({
            'message': dialogflow_response
        }))

    async def get_dialogflow_response(self, user_message):
        session_client = dialogflow.SessionsClient()
        session = session_client.session_path('your-project-id', 'session-id')
        
        text_input = dialogflow.TextInput(text=user_message, language_code='fr')
        query_input = dialogflow.QueryInput(text=text_input)

        # Envoi du message à Dialogflow
        response = session_client.detect_intent(session=session, query_input=query_input)
        return response.query_result.fulfillment_text
