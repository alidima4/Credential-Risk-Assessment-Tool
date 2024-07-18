import pandas as pd
from pathlib import Path
import numpy as np
from user_details import get_user
from password_details import get_password
from file_details import country_file, files_data
from channel_details import get_channel

# Leer el archivo output.csv y se crea df
file_path = Path(__file__).parent.absolute() / "output.csv"
df = pd.read_csv(file_path)

# Contrucción del Dataframe
df[["VIP_credential","VIP_group","User_status"]] = df['username'].apply(get_user)
df[["MD5","SHA256","SHA512","SHA1","Pasword_update","Password_type", "Leaked_password", "Password_strength", "Guesses_discover", "Cracking_time", "Password_entropy"]] = df['password'].apply(get_password)
df['Country_file_name'] = df['file'].apply(lambda x: country_file(x, files_data))
df["Results_file"] = np.random.randint(1, 15, size=len(df))
df[["Channel_privacity","Chat_type"]] = df['channel'].apply(get_channel)
print(df)

df.to_csv("dataframe.csv", index=False)

