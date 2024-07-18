from pathlib import Path
import json
import pandas as pd

file_path = Path(__file__).parent.absolute() / "output.csv"
df = pd.read_csv(file_path)

# ruta del json
BASE_DIR = Path(__file__).resolve().parent
CHANNELS_FILE = BASE_DIR / "channel_det.json"

# Cargar el archivo JSON con manejo de errores
try:
    with open(CHANNELS_FILE, "r", encoding="utf-8") as channel_f:
        channel_data = json.load(channel_f)
except FileNotFoundError:
    print(f"Error: El archivo {CHANNELS_FILE} no existe.")
    channel_data = {}
except json.JSONDecodeError:
    print(f"Error: El archivo {CHANNELS_FILE} no contiene un JSON válido.")
    channel_data = {}

channel_to_type = {}
channel_to_priv = {}

for chat_type, type in channel_data.items():
        for privacity_type, channels in type.items():
            for channel in channels:
                channel_to_type[channel] = chat_type
                channel_to_priv[channel] = privacity_type

def get_channel(channel):    
    return pd.Series({
        "Channel_privacity": channel_to_priv.get(channel, None),
        "Chat_type": channel_to_type.get(channel, None),
    })

# df[["Channel_privacity","Chat_type"]] = df['channel'].apply(get_channel)

