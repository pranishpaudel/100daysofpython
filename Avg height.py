import requests


params= {
    "clientKey":"76c073d0fe63e566c3e7b6c3db8e4993",
    "task": {
        "type":"RecaptchaV2TaskProxyless",
       "websiteURL":"https://2captcha.com/demo/recaptcha-v2",
        "websiteKey":"6LfD3PIbAAAAAJs_eEHvoOl75_83eXSqpPSRFJ_u",
        "isInvisible":"false"
    }
}


now= requests.post(url="https://api.2captcha.com/createTask",json=params).json()
print(now)