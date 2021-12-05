from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print(
    """Per favore, vai su my.telegram.org
Accedi utilizzando il tuo account di Telegram
Clicca su 'API Development Tools'
Crea una nuova applicazione inserendo i dati richiesti"""
)
APP_ID = int(input("Inserisci qui l'APP ID: "))
API_HASH = input("Inserisci qui l'API ASH: ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    print(client.session.save())
    client.send_message("me", client.session.save())
