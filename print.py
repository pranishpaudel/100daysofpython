import json
import base64
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
import requests

# Function to pad data with PKCS7
def PKCS7_pad(data):
    block_size = 8
    padding_size = block_size - (len(data) % block_size)
    padding = bytes([padding_size] * padding_size)
    return data + padding

# Your public key
public_key = "FLWPUBK-7adb6177bd71dd43c2efa3f1229e3b7f-X"

# Ravepay API charge endpoint
charge_endpoint = "https://ravesandboxapi.flutterwave.com/flwv3-pug/getpaidx/api/charge"

# Card details
card_data = {
    "card_number": "4556052704172643",
    "cvv": "899",
    "expiry_month": "01",
    "expiry_year": "23",
    "currency": "NGN",
    "amount": "7500",
    "email": "user@example.com",
    "fullname": "Flutterwave Developers",
    "tx_ref": "YOUR_PAYMENT_REFERENCE",
    "redirect_url": "https://example_company.com/success"
}

# Convert card data to JSON string
json_card_data = json.dumps(card_data)

# Generate a random encryption key
encryption_key = get_random_bytes(24)

# Create a 3DES cipher object with the encryption key and ECB mode
cipher = DES3.new(encryption_key, DES3.MODE_ECB)

# Pad the card data to be a multiple of 8 bytes
padded_card_data = PKCS7_pad(json_card_data.encode('utf-8'))

# Encrypt the padded card data
encrypted_card_data = cipher.encrypt(padded_card_data)

# Base64 encode the encrypted card data
encoded_card_data = base64.b64encode(encrypted_card_data).decode('utf-8')

# Create the payload with the public key, encrypted card data, and algorithm
payload = {
    "PBFPubKey": public_key,
    "client": encoded_card_data,
    "alg": "3DES-24"
}

# Make the request to the charge endpoint
response = requests.post(charge_endpoint, json=payload)

# Print the response
print(response.json())
