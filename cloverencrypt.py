import requests
import base64
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Public encryption keys are hosted on a CDN.
PUBLIC_ENCRYPTION_KEYS_URL = "https://checkout.clover.com/assets/keys.json"
PREFIX_ID = "00000000"

# Production: https://api.clover.com" - Sandbox: https://apisandbox.dev.clover.com
BASE_URL = "https://apisandbox.dev.clover.com"
# Production: https://token.clover.com/v1/tokens - Sandbox: https://token-sandbox.dev.clover.com/v1/tokens
TOKEN_URL = "https://token-sandbox.dev.clover.com/v1/tokens"
ACCESS_TOKEN = "bc22012281f7c86f7aa9b5c865b718c0"

# Test Credit Card Info
CC_NUMBER = "6011361000006668"
CVV_NUMBER = "123"
EXP_MONTH = "07"
EXP_YEAR = "2030"

def main():
    try:
        test_tokenize()
    except Exception as e:
        print(e)

def test_tokenize():
    # Once you have the PAKMS for a given merchant, you should cache it (you do not need to retrieve it
    # each time you need to tokenize a card).
    print("Get PAKMS")
    pakms_response = send_get(BASE_URL, "/pakms/apikey", True)
    pakms = pakms_response["apiAccessKey"]

    print("Get Public Encryption Key from CDN ...")
    keys_response = send_get(PUBLIC_ENCRYPTION_KEYS_URL, "", False)
    ta_public_key = keys_response["TA_PUBLIC_KEY_PROD"]

    public_key = get_public_key(ta_public_key)

    cc_encrypted = encrypt_pan(CC_NUMBER, public_key)

    token_request = {
        "card": {
            "encrypted_pan": cc_encrypted,
            "exp_month": EXP_MONTH,
            "exp_year": EXP_YEAR,
            "first6": CC_NUMBER[:6],
            "last4": CC_NUMBER[-4:],
            "cvv": CVV_NUMBER
        }
    }
    
    token_response = send_token_post(pakms, token_request)

    if "id" in token_response:
        print("Your card token, pass this token in payment requests:", token_response["id"])
    else:
        print("An invalid token response was returned.")

def get_public_key(ta_public_key):
    key_bytes = base64.b64decode(ta_public_key)
    public_key = serialization.load_der_public_key(key_bytes)
    return public_key

def encrypt_pan(pan, public_key):
    input_data = (PREFIX_ID + pan).encode("utf-8")
    encrypted_data = public_key.encrypt(input_data, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA1()), algorithm=hashes.SHA1(), label=None))
    return base64.b64encode(encrypted_data).decode("utf-8")

def send_get(base_url, endpoint, bearer_required):
    headers = {}
    if bearer_required:
        headers["Authorization"] = "Bearer " + ACCESS_TOKEN

    response = requests.get(base_url + endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def send_token_post(pakms, data):
    headers = {"apikey": pakms}
    response = requests.post(TOKEN_URL, json=data, headers=headers)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    main()
