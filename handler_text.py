from bot_controller import send_message


def handler_start_game(chat_id,first_name):
    keyboard = {
        "inline_keyboard": [
            [{'text': 'Камень', 'callback_data': 'Камень'}, {'text':'Ножницы', 'callback_data': 'Ножницы'}, {'text':'Бумага', 'callback_data': 'Бумага'}],
        ]
    }
    send_message(chat_id, f"{first_name} игра начата", keyboard)