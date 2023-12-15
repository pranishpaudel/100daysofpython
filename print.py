# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# from time import sleep

# ENDPOINT = "https://flutterwave.com/pay/lesvamp"

# options = webdriver.ChromeOptions()


# options.add_experimental_option("detach", True)


# driver = webdriver.Chrome(options=options)

# driver.get(ENDPOINT)

# sleep(0.5)
# ####USD INPUT
# usd_input= driver.find_element(By.XPATH,'//*[@id="amount"]')
# for _ in range(3):
#     usd_input.send_keys("1")

# f_name= driver.find_element(By.XPATH,'//*[@id="first-name"]')
# f_name.send_keys("Insa")
# l_name= driver.find_element(By.XPATH,'//*[@id="last-name"]')
# l_name.send_keys("Linda")
# email= driver.find_element(By.XPATH,'//*[@id="email"]')
# email.send_keys("insalinda@gmail.com")

# pay_button= driver.find_element(By.XPATH,'//*[@id="payment-link"]/div/section/div/div[2]/div/button')
# pay_button.click()

# sleep(10)

# card_num= driver.find_element(By.XPATH,'//*[@id="cardnumber"]')
# card_num.send_keys("4189530001812214")
# # card_month= driver.find_element(By.XPATH,'//*[@id="last-name"]')
# # card_month.send_keys("Linda")
# # card_year= driver.find_element(By.XPATH,'//*[@id="email"]')
# # card_year.send_keys("insalinda@gmail.com")
# # card_cvv= driver.find_element(By.XPATH,'//*[@id="email"]')
# # card_cvv.send_keys("insalinda@gmail.com")

import requests

api_key = "AIzaSyDVWvmrxC19sXSEw0NOwyBhxt9LqQKaARg"
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + api_key

headers = {
    "Content-Type": "application/json"
}

data = {
    "contents": [{
        "parts": [{
            "text": input("Enter your question")
        }]
    }]
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    result = response.json()
    # Process the result as needed
    print(result['candidates'][0]['content']['parts'][0]['text'])
else:
    print(f"Error: {response.status_code}, {response.text}")