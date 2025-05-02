from bot_controller import send_message
from file_controller import get_users,save_users
import random
import config
def parse_message(message):
    text = message["message"]["text"].lower()
    chat_id = message["message"]["from"]["id"]   
    first_name = message["message"]["from"]['first_name']
    return [text,chat_id,first_name]

def parse_message_callback(message):
    text = message['callback_query']['data']
    chat_id = message['callback_query']['message']['chat']['id']
    first_name = message['callback_query']['from']['first_name']
    return[text,chat_id,first_name]

def find_user(first_name):
    with open(config.USERS_PATH, "r") as file:
        lines = file.readlines()
        for line in lines:
            if line.strip().split(":")[0] == first_name:
                return False
        return True

def random_move():
    option_list = ["Камень","Ножницы","Бумага"]
    
    return option_list[random.randint(0,2)]

def predict(user_choice, bot_choice):
    winning_combinations = {
        "Камень": "Ножницы",
        "Ножницы": "Бумага",
        "Бумага": "Камень"
    }
    
    if user_choice == bot_choice:
        return ("draw", f"Ты выбрал {user_choice}, я выбрал {bot_choice}. Ничья")

    if winning_combinations[user_choice] == bot_choice:
        return ("win", f"Ты выбрал {user_choice}, я выбрал {bot_choice}. Победа за тобой")
    else:
        return ("loss", f"Ты выбрал {user_choice}, я выбрал {bot_choice}. Победа за мной")

def get_stats(chat_id,first_name):
    users = get_users()
    if first_name in users:
        stats = users[first_name]
        total = stats["wins"] + stats["losses"] + stats["draws"]
        if total > 0:    
            win_percent = (stats["wins"] / total * 100) 
        else:
            win_percent = 0
        send_message(chat_id, f"Игр: {total}\n Побед: {stats['wins']}\n Поражений: {stats['losses']}\n Ничьих: {stats['draws']}\n Процент побед: {win_percent:.0f}%")
    else:        
        send_message(chat_id, "Статистики нету")

def update_stats(first_name, result):
    users = get_users()
    if first_name not in users:
        users[first_name] = {"wins": 0, "losses": 0, "draws": 0}
   
    if result == "win":
        users[first_name]["wins"] += 1
    elif result == "loss":
        users[first_name]["losses"] += 1
    else:
        users[first_name]["draws"] += 1
    
    save_users(users)


