import requests
import base64
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

PREFIX_ID = "00000000"

public_key_str = """
vyYRQA3cS4wV9yk+6bFzA7KLDmE+D/SOP+Q5bNOPG9nUDkAPalRBz12KA5SDxTw2vO1BIeSFUQlYTpzEDb/XkfNNm5e6nqf12M4kdHP1F2EXW4WArilUZegAVw/Y7FvAkA8PQFbfgmBirSa5GS/fuAHjemqEf0DxIgq552IDeFw3nB0vccK6ePue5sVB9Sm2vWpKm/lj2UE4P6z2ngZr5V31cSAVN08USxHvz+MEnoUBKt6aKvfRUAp4iFyIpxlp4eylxY8zizPekS29lcRMsI9hGug2CoKFhhUJ1gD8G280zIoWCxysNvl40k/l8OTtPKrnlhAzQcIyy/RB0lwb6QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGVTU=
"""

def load_public_key():
    return serialization.load_pem_public_key(public_key_str.encode("utf-8"))

def encrypt_pan(pan, public_key):
    input_data = (PREFIX_ID + pan).encode("utf-8")
    encrypted_data = public_key.encrypt(
        input_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None
        )
    )
    return base64.b64encode(encrypted_data).decode("utf-8")

if __name__ == "__main__":
    public_key = load_public_key()
    pan = "4403931341740034"
    encrypted_pan = encrypt_pan(pan, public_key)
    print("Encrypted PAN:", encrypted_pan)
