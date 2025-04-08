from flask import Flask, request, jsonify
from services.waha import Waha
from services.botAI import BotAI

app = Flask(__name__)

@app.route('/chatbot/webhook/', methods=['POST'])
def webhook():
    data = request.json
    waha = Waha()
    bot = BotAI()

    chat_id = data['payload']['from']

    message = data['payload']['body']

    resposta = bot.assistente_RAG(message)

    waha.SendMessage(resposta, chat_id)

    return jsonify({'status': resposta}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)