from modules.checkpwn import check_pwned
from modules.entropy import calculate_entropy, find_char_set_size
from modules.password_strength import password_strength
import pandas as pd
from pathlib import Path
import json
import hashlib

file_path = Path(__file__).parent.absolute() / "output.csv"
df = pd.read_csv(file_path)

BASE_DIR = Path(__file__).resolve().parent
PASSWORDS_FILE = BASE_DIR / "password_det.json"

with open(PASSWORDS_FILE, "r") as pswd_f:
    pswd_data = json.load(pswd_f)

#Diccionario de búsqueda (password--> type; cambio=password for change)
pswd_to_type = {}
for password_type, pswds in pswd_data.items():
    for pswd in pswds:    
        pswd_to_type[pswd] = password_type
                    
def get_password(password):
    # Resultado de Password_update
    if "2024" in password or "2023" in password:
        actual = "actual"
    else:
        actual = "not actual"
    
    # Resultado de Password_type
    passwordtype = pswd_to_type.get(password, "personal password")  

    # Resultado de Leaked_password    
    pwned_results = check_pwned([password]) 
    pwned_count = pwned_results[0][1] # Dato de Leaked passwords
    
    # Resultado de Password_strength, Guesses_discover, Cracking_time, Password_entropy
    strength_result = password_strength(password)
    length, char_set_size = find_char_set_size(password)
    entropy_estimate = calculate_entropy(length, char_set_size)

    # Resultado de hashes
    if password is None:  # Asegura manejar NoneTypes también.
        return [''] * 4
    md5 = hashlib.md5(password.encode()).hexdigest()
    sha256 = hashlib.sha256(password.encode()).hexdigest()
    sha512 = hashlib.sha512(password.encode()).hexdigest()
    sha1 = hashlib.sha1(password.encode()).hexdigest()

    results = pd.Series(data=[md5, sha256, sha512, sha1, actual, passwordtype, pwned_count, strength_result['score'], strength_result['guesses_log10'], 
                              strength_result['online_no_throttling_10_per_second_seconds'], entropy_estimate
                              ], 
                        index=["MD5","SHA256","SHA512","SHA1","Pasword_update","Password_type", "Leaked_password", "Password_strength", "Guesses_discover", 
                               "Cracking_time", "Password_entropy"
                               ])
    return results

# def get_hash(password):
#     if password is None:  # Asegura manejar NoneTypes también.
#         return [''] * 4
#     md5 = hashlib.md5(password.encode()).hexdigest()
#     sha256 = hashlib.sha256(password.encode()).hexdigest()
#     sha512 = hashlib.sha512(password.encode()).hexdigest()
#     sha1 = hashlib.sha1(password.encode()).hexdigest()
#     results = pd.Series(data=[md5, sha256, sha512, sha1], index=["MD5","SHA256","SHA512","SHA1"])
#     return results

# df[["Pasword_update","Password_type", "Leaked_password", "Password_strength", "Guesses_discover", "Cracking_time", "Password_entropy"]] = df['password'].apply(get_password)

