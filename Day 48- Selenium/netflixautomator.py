from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

N_EMAIL= f"sdd33{random.randint(0,1000)}23d@gmail.com"
N_PASSWORD= "dsad3dasdas"

webdriver_config= webdriver.ChromeOptions()
webdriver_config.add_experimental_option("detach", True)
driver= webdriver.Chrome(webdriver_config)


ENDPOINT= "https://netflix.com/np"

driver.get(ENDPOINT)
email= driver.find_element(By.NAME,"email")
email.send_keys(N_EMAIL)

next_page= driver.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/form/div/button')
next_page.click()
time.sleep(3)

next_page1= driver.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div/div/div[2]/div/div[2]/button')
next_page1.click()

time.sleep(3)

password_click= driver.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div/div/div[2]/div/form/div/div[1]/div[2]/ul/li[2]/div/div[1]')
password_click.click()

password= driver.find_element(By.NAME,'password')
password.send_keys(N_PASSWORD)


create_account= driver.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div/div/div[2]/div/form/div/div[2]/button')
create_account.click()

time.sleep(2)

next_page3= driver.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div/div/div[2]/div/div[2]/button')
next_page3.click()

time.sleep(2)
next_page4= driver.find_element(By.CSS_SELECTOR,'div .submitBtnContainer button')
next_page4.click()

next_page5= driver.find_element(By.CSS_SELECTOR,'div .default-ltr-cache-1qs5ngv button')
next_page5.click()

driver.close()

# Simulate typing with delays between keystrokes

# next_page2=  driver.find_element(By.CSS_SELECTOR,value="")
# next_page2.click()

