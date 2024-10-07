from flask import Flask, request
from .send_message import SendMessage
from .assistant_gpt import AssistantGPT
from dotenv import load_dotenv
import os

load_dotenv()
NUMBER_ALLOWED_UM = str(os.getenv('NUMBER_ALLOWED_UM'))
NUMBER_ALLOWED_DOIS = str(os.getenv('NUMBER_ALLOWED_DOIS'))
app = Flask(__name__)


@app.route('/webhook', methods=['GET', 'POST', 'PUT'])
def get_webhook():
    if request.method == 'POST':
        print('Entered POST Method')
        # Recebendo mensagens do webhook via PUT
        payload = request.get_json()
        print(f'payload: {payload}')
        
        if not payload:
            return "No JSON payload received", 400  # Tratamento de erro se o JSON estiver vazio
        
        print(f"Payload received in POST: {payload}")
        if 'text' in payload:
            message = payload['text']['message']
            phone = payload['phone']
            print(f'message: {message}')
            print(f'phone: {phone}')
            if phone == NUMBER_ALLOWED_UM or phone == NUMBER_ALLOWED_DOIS:
                send_message = SendMessage()
                # answer = f'Mensagem {message} recebida!'
                assistant_gpt = AssistantGPT()
                answer = assistant_gpt.execute(message)
                send_message.send_message(phone, answer)
                return "POST Message Received", 200  # Sucesso
            return "POST Message Received, Not the Right user", 201  # Sucesso

if __name__ == "__main__":
    app.run(port=8000, debug=True)