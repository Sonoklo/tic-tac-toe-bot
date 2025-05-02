from bot_controller import send_message
from file_controller import save_users,get_users

def comand_start(chat_id,first_name):
    keyboard = {
        "keyboard":[
        ["Start Game", "Stats"],
            ["/info"]
        ],
        'resize_keyboard': True
    }
    users = get_users()
    if first_name not in users:
        users[first_name] = {"wins": 0, "losses": 0, "draws": 0}
        save_users(users)
        send_message(chat_id, f"Добро пожаловать {first_name}", keyboard)
    else:
        send_message(chat_id, f"С возращением {first_name}", keyboard)

def comand_info(chat_id):
    send_message(chat_id, "Правила игры\n Камень бьет ножницы\n Бумага бьет камень\n Ножницы бьют бумагу")
       

