from pathlib import Path
import json
import pandas as pd

# Ruta del archivo CSV
file_path = Path(__file__).parent.absolute() / "output.csv"
df = pd.read_csv(file_path)

# Ruta del archivo JSON
BASE_DIR = Path(__file__).resolve().parent
FILES_JSON = BASE_DIR / "file_det.json"

# Cargar el archivo JSON
with open(FILES_JSON, "r") as files_f:
    files_data = json.load(files_f)

# Función para obtener el nombre del país según el archivo y los datos del JSON
def country_file(file, files_data):
    for file_country, tokens in files_data.items():
        for token in tokens:
            if token.lower() in file.lower(): # discriminar mayus/minus     
                return file_country
    return "Other"


# Aplicar la función de mapeo para cada archivo en el DataFrame
df['Country_file_name'] = df['file'].apply(lambda x: country_file(x, files_data))

# Mostrar el DataFrame actualizado
print(df)

