import time
import config 
import file_controller
from bot_controller import get_message,send_message
from utils import parse_message, random_move, predict, parse_message_callback
from handler_commands import comand_start,comand_info
from handler_text import handler_start_game

if __name__ == "__main__":
    while True:
        for message in get_message():
            if "callback_query" in message:
                # parse_message_callback
                text,chat_id,first_name = parse_message_callback(message)
                
                # Не хватает проверки какой конкретно коллбек срабатывает
                if text == "Камень" or text == "Ножницы" or text == "Бумага":
                    bot_choice = random_move()

                    # Разобраться в работе функции на 101% понимать все до мелочей
                    result, answer = predict(text, bot_choice)
                    send_message(chat_id, answer)
                    file_controller.update_stats(first_name, result)
            else:
                text,chat_id,first_name = parse_message(message)
                if text.startswith("/"):
                    if text == "/start":  
                        comand_start(chat_id, first_name)
                    elif text == "/info":
                        comand_info(chat_id)
                else:
                    if text == "start game":
                        handler_start_game(chat_id,first_name)
                    elif text == "stats":
                        file_controller.get_stats(chat_id, first_name)
            config.offset = message["update_id"] + 1
        time.sleep(1)    
            
           
        