import json
import random
import string
from pathlib import Path
import csv


BASE_DIR = Path(__file__).resolve().parent
FILES = {
    "users": BASE_DIR / "user_ran.json",
    "diccionario": BASE_DIR / "password_ran.json",
    "channels": BASE_DIR / "channel_ran.json",
    "file_name": BASE_DIR / "file_ran.json"}

data = {}

for key, file_path in FILES.items():
    if file_path.is_file():
        with open(file_path, "r", encoding="utf-8") as f:
            data[key] = json.load(f)
    else:
        data[key] = None  

users = data["users"]
diccionario = data["diccionario"]
channels = data["channels"]
file_name = data["file_name"]

def pasw_gen():
    usar_diccionario = random.choice([True, False])
    if usar_diccionario and diccionario:
        return random.choice(diccionario)

    s1 = list(string.ascii_lowercase)
    s2 = list(string.ascii_uppercase)
    s3 = list(string.digits)
    s4 = list(string.punctuation)

    longitud = random.randint(4, 12)

    num_s1 = random.randint(1, longitud - 3)
    num_s2 = random.randint(1, longitud - num_s1 - 2)
    num_s3 = random.randint(1, longitud - num_s1 - num_s2 - 1)
    num_s4 = longitud - num_s1 - num_s2 - num_s3

    contraseña = (
        random.choices(s1, k=num_s1) +
        random.choices(s2, k=num_s2) +
        random.choices(s3, k=num_s3) +
        random.choices(s4, k=num_s4)
    )
    random.shuffle(contraseña)
    return ''.join(contraseña)

output_csv = BASE_DIR / "output.csv"

# Crear y escribir en el archivo CSV
with open(output_csv, "w", newline='', encoding="utf-8") as csvfile:
    fieldnames = ['username', 'password', 'channel', 'file']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    
    for _ in range(20):
        username = random.choice(users)
        password = pasw_gen()
        channel = random.choice(channels)
        file = random.choice(file_name)

        writer.writerow({'username': username, 'password': password, 'channel': channel, 'file': file})

# Con este script se crea un csv con una simulación de muestras que contienen username, password, channel y file