import hashlib
import requests


class PwnedPassphraseException(Exception):
    pass

def check_pwned(passwords, **kwargs):
    if not isinstance(passwords, list):
        passwords = [passwords]

    results = []
    for passphrase in passwords:
        if not passphrase:
            raise ValueError("Los valores no se pueden dejar vacios")

        # Envio de contraseñas hasheadas y no texto plano
        hashed_passphrase = hashlib.sha1(passphrase.encode()).hexdigest().upper()
        prefix, suffix = hashed_passphrase[:5], hashed_passphrase[5:]
        # Requests a la api
        url = f'https://api.pwnedpasswords.com/range/{prefix}'
        try:
            response = requests.get(url, **kwargs)
            response.raise_for_status()  # Raise exception for non-200 status codes
        except requests.RequestException as e:
            raise RuntimeError(f'Error fetching {url}: {e}') from e

        # Check if passphrase hash suffix exists in response
        pwned = False
        for line in response.text.splitlines():
            suffix_, count = line.split(':')
            if suffix_ == suffix:
                results.append((passphrase, count))
                pwned = True
                break

        if not pwned:
            results.append((passphrase, 0))

    return results

    