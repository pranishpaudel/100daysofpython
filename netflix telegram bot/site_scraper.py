import requests
from bs4 import BeautifulSoup
import re
from colorama import Fore, Style


def get_site_details(url: str) -> str:
    if not url.startswith("http://") and not url.startswith("https://"):
        url = f"https://{url}"
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.content, 'html.parser')

        payment_gateway = get_payment_gateway(soup, response, url)
        has_captcha_value = has_captcha(soup)

        if payment_gateway:
            result = f"*Payment Gateway:* {payment_gateway}\n"
        else:
            result = f"*Payment Gateway:* No payment gateway found.\n"

        if has_cloudflare_protection(response):
            result += f"*Cloudfare Status:* Enabled\n"
        else:
            result += f"*Cloudfare Status:* Disabled\n"

        if has_captcha_value:
            result += f"*Captcha Status:* Enabled\n"
        else:
            result += f"*Captcha Status:* Disabled\n"

        if "shopify" in response.headers.get("x-powered-by", "").lower() or "cdn.shopify.com" in response.url:
            shopify_payment_gateway = get_shopify_payment_gateway(soup)
            if shopify_payment_gateway:
                result += f"*Shopify Payment Gateway:* {shopify_payment_gateway}\n"

        return result

    except requests.exceptions.RequestException as e:
        return f"*An error occurred:* {e}"
        raise Exception(f"Unable to connect to website: {e}")



def get_payment_gateway(soup: BeautifulSoup, response: requests.Response, url: str) -> str:


    payment_gateways = ["2checkout", "achpayments", "adyen", "aligncommerce", "amazon pay", "american express", "apple pay", "authorize.net", "avangate", "axcess merchant services", "azimo", "bambora", "beanstream", "bill.com", "bitcoin", "bitpay", "bluesnap", "bluefin", "bluepay", "braintree", "c2bpayments", "cardconnect", "cardknox", "cashnetusa", "ccavenue", "chargebee", "checkout.com", "chronopay", "clickandbuy", "cloudpayments", "coinbase", "compropago", "creditcall", "cybersource", "dibs", "digital river", "dwolla", "e-gold", "easypay", "ebanx", "ecomm365", "elavon", "emerchantpay", "epay", "eprocessing network", "eway", "fastcharge", "fastspring", "fattmerchant", "first data", "fiserv", "forte", "global payments", "gocardless", "google pay", "heartland payment systems", "humm", "ingenico", "instamojo", "intuit", "ipay88", "kabbage", "klik & pay", "klarna", "komoju", "lawpay", "liqpay", "mastercard", "mercadopago", "mirjeh", "mollie", "moneris", "neonpay", "netbilling", "neteller", "obopay", "ogone", "optimal payments", "paya", "paybox", "payeezy", "payfast", "payflow", "paygate", "payjunction", "payline", "paymill", "payment express", "paymentwall", "payone", "payoneer", "paypal", "paypoint", "payplug", "paysafe", "payson", "payscout", "paysera", "paytm", "payu", "payvision", "payza", "pin payments", "pivotal payments", "plastiq", "postfinance", "psigate", "quickbooks payments", "quickpay", "razorpay", "realex payments", "redsys", "sagepay", "securepay", "skrill", "skypay", "spreedly", "square", "stripe", "tap payment gateway", "tender retail", "transact24", "usa epay", "venmo", "verifone", "visa", "we pay", "wirecard", "worldnet", "worldpay", "zooz"]

    # Additional payment gateways to add horizontally
    additional_payment_gateways = ["aliexpress", "bluesnap", "checkoutfi", "dalenys", "epayco", "klarupay", "mangopay", "paddle", "qiwi", "revolut", "robokassa", "sezzle", "viva wallet"]

    # Adding the additional payment gateways to the list horizontally
    payment_gateways += additional_payment_gateways

    # Check script and link tags for known payment gateways
    for tag in soup.find_all(["script", "link"]):
        for gateway in payment_gateways:
            if gateway in str(tag):
                return gateway
                return gateway

    # Check for known payment gateway names in meta tags
    meta_tags = soup.find_all("meta")
    for gateway in payment_gateways:
        for tag in meta_tags:
            if tag.has_attr("content"):
                if gateway in tag["content"].lower():
                    return gateway

    # Check for known payment gateway headers
    for gateway in payment_gateways:
        if gateway in str(response.headers):
            return gateway
    # Check script and link tags for known payment gateways
    for tag in soup.find_all(["script", "link"]):
        for gateway in payment_gateways:
            if gateway in str(tag):
                return gateway

    # Check for known payment gateway names in meta tags
    meta_tags = soup.find_all("meta")
    for gateway in payment_gateways:
        for tag in meta_tags:
            if tag.has_attr("content"):
                if gateway in tag["content"].lower():
                    return gateway

    # Check for known payment gateway headers
    for gateway in payment_gateways:
        if gateway in str(response.headers):
            return gateway


    # Check for known payment gateway names in cookies
    for gateway in payment_gateways:
        if gateway in str(response.cookies):
            return gateway

    return ""

def has_captcha(soup: BeautifulSoup) -> bool:
    captcha_keywords = ["captcha", "recaptcha", "hCaptcha", "image challenge", "human verification"]
    for script in soup.find_all("script"):
        for keyword in captcha_keywords:
            if keyword in str(script):
                return True
        if "google.com/recaptcha/api.js" in str(script) and "render" in str(script):
            return True
    for input_field in soup.find_all("input"):
        for keyword in captcha_keywords:
            if keyword in input_field.get("name", "") or keyword in input_field.get("id", ""):
                return True
    return False

def has_cloudflare_protection(response: requests.Response) -> bool:
    return "cf_ray" in response.headers or "cloudflare" in response.headers.get("server", "").lower()

def get_shopify_payment_gateway(soup: BeautifulSoup) -> str:
    cybersource_keywords = ["cybersource"]
    paypal_keywords = ["paypal"]
    stripe_keywords = ["stripe"]
    adyen_keywords = ["adyen"]
    braintree_keywords = ["braintree"]
    shopify_keywords = ["shopify"]
    additional_payment_gateways = ["2checkout", "aligncommerce", "amazon pay", "apple pay", "authorize.net", "avangate", "azimo", "bambora", "beanstream", "bill.com", "bitcoin", "bitpay", "bluesnap", "bluefin", "bluepay", "c2bpayments", "cardconnect", "cardknox", "cashnetusa", "ccavenue", "chargebee", "checkout.com", "chronopay", "clickandbuy", "cloudpayments", "coinbase", "compropago", "creditcall", "cybersource", "dibs", "digital river", "dwolla", "easypay", "ebanx", "ecomm365", "elavon", "emerchantpay", "epay", "eprocessing network", "eway", "fastcharge", "fastspring", "fattmerchant", "first data", "fiserv", "forte", "global payments", "gocardless", "google pay", "heartland payment systems", "humm", "ingenico", "instamojo", "intuit", "ipay88", "kabbage", "klik & pay", "klarna", "komoju", "lawpay", "liqpay", "mastercard", "mercadopago", "mirjeh", "mollie", "moneris", "neonpay", "netbilling", "neteller", "obopay", "ogone", "optimal payments", "paya", "paybox", "payeezy", "payfast", "payflow", "paygate", "payjunction", "payline", "paymill", "payment express", "paymentwall", "payone", "payoneer", "paypal", "paypoint", "payplug", "paysafe", "payson", "payscout", "paysera", "paytm", "payu", "payvision", "payza", "pin payments", "pivotal payments", "plastiq", "postfinance", "psigate", "quickbooks payments", "quickpay", "razorpay", "realex payments", "redsys", "sagepay", "securepay", "skrill", "skypay", "spreedly", "square", "stripe", "tap payment gateway", "tender retail", "transact24", "usa epay", "venmo", "verifone", "visa", "we pay", "wirecard", "worldnet", "worldpay", "zooz"]
    payment_gateway_priority = [cybersource_keywords, additional_payment_gateways, shopify_keywords, stripe_keywords, adyen_keywords, braintree_keywords, paypal_keywords]

    for priority_keywords in payment_gateway_priority:
        for tag in soup.find_all(["script", "link"]):
            for keyword in priority_keywords:
                if keyword in str(tag):
                    return keyword

        meta_tags = soup.find_all("meta")
        for tag in meta_tags:
            if tag.has_attr("content"):
                for keyword in priority_keywords:
                    if keyword in tag["content"].lower():
                        return keyword


if __name__ == "__main__":
    url = "https://example.com"
    print(get_site_details(url))      