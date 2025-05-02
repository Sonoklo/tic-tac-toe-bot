import config
from bot_controller import send_message
def get_users():
    users = {}
    with open(config.USERS_PATH, "r") as file:
        lines = file.readlines()
        for line in lines:
            if ":" in line:
                parts = line.strip().split(":")
                first_name = parts[0]
                stats = parts[1].split(",")
                wins = int(stats[0])
                losses = int(stats[1])
                draws = int(stats[2])
                users[first_name] = {"wins": wins, "losses": losses, "draws": draws}
        return users
    
def save_users(users):
    with open(config.USERS_PATH, "w") as file:
        for name, stats in users.items():
            line = f"{name}:{stats['wins']},{stats['losses']},{stats['draws']}\n"
            file.write(line)
    
