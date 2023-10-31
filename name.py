from selenium import webdriver
from selenium.webdriver import ChromeOptions

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()
options= ChromeOptions()
options.add_experimental_option("detach",True)
# Navigate to the URL
url = 'https://www2.2checkout.com/checkout/purchase?PTCOID=19c741de0a301cc980319a6a4f086a7f'
driver.get(url)

# You can now interact with the web page or retrieve information using Selenium.

# Close the WebDriver when you're done
