from selenium import webdriver
from selenium.webdriver.common.by import By
import time



###INITIALIZE TINDERRR
TARGET_URL="https://tinder.com/"

options= webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver= webdriver.Chrome(options)
driver.get(TARGET_URL)


##CLICK LOGIN
time.sleep(2)
login= driver.find_element(By.XPATH,'//*[@id="q-1355571838"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login.click()


driver.get(TARGET_URL)


