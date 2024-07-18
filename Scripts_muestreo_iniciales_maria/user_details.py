from pathlib import Path
import json
import pandas as pd

file_path = Path(__file__).parent.absolute() / "output.csv"
df = pd.read_csv(file_path)

# ruta del json
BASE_DIR = Path(__file__).resolve().parent
USERS_FILE = BASE_DIR / "user_det.json"

# cargar el json
with open(USERS_FILE, "r") as users_f:
    users_data = json.load(users_f)

#Diccionario de búsqueda (user--> group; a@telebot.com=CEO)
user_to_group = {}
user_to_vip = {}
user_to_status = {}
for category, groups in users_data.items():
    for group_name, status in groups.items():
        for status_type, users in status.items():
            for user in users:
                user_to_group[user] = group_name
                user_to_vip[user] = category
                user_to_status[user] = status_type

def get_user(username):    
    return pd.Series({
        "VIP_credential": user_to_vip.get(username, None),
        "VIP_group": user_to_group.get(username, None),
        "User_status": user_to_status.get(username, None)
    })

# df[["VIP_credential","VIP_group","User_status"]] = df['username'].apply(get_user)




