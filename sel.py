from selenium.webdriver.common.by import By
from selenium import webdriver
import time





driver= webdriver.ChromeOptions()
driver.add_experimental_option("detach",True)

driver= webdriver.Chrome()

driver.get("https://www.shopworn.com/shop/karl-lagerfeld-paris-hermine-almond-leather-wallet-lh9qr5avalm")


time.sleep(2)
add_cart= driver.find_element(By.XPATH,'//*[@id="addToBag_101055"]')
add_cart.click()
time.sleep(2)
print(driver.get_cookies())

