import requests
import time

TOKEN = 'COLE_SEU_TOKEN_AQUI'
CHAT_ID = 'COLE_SEU_CHAT_ID_AQUI'

def enviar_mensagem(mensagem):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': mensagem
    }
    requests.post(url, data=payload)

# Exemplo de mensagem
enviar_mensagem('⚽ Palpite do dia: Mais de 2.5 gols no jogo do PSG!')
