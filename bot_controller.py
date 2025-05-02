import requests
import config
import json
def get_message():
    params = {"offset": config.offset}
    resp = requests.get(f"https://api.telegram.org/{config.TOKEN}/getUpdates", params = params)
    data = resp.json()
    return data["result"]

def send_message(chat_id, text, keyboard=None):
    params = {"chat_id": chat_id, "text": text}
    if keyboard:
        params["reply_markup"] = json.dumps(keyboard)

    requests.get(f"https://api.telegram.org/{config.TOKEN}/sendMessage", params=params)