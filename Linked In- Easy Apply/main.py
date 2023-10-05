from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

USER_EMAIL= "anguthikajin@gmail.com"
USER_PASS= "#topper77"

options= webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver= webdriver.Chrome(options)



ENDPOINT= "https://www.linkedin.com/login"

AFTER_LOGIN_ENDPOINT= "https://www.linkedin.com/jobs/search/?currentJobId=3733902672&f_AL=true&keywords=junior%20python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER"

driver.get(ENDPOINT)

time.sleep(3)
email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(USER_EMAIL)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(USER_PASS)
password_field.send_keys(Keys.ENTER)

time.sleep(2)

driver.get(AFTER_LOGIN_ENDPOINT)
# driver.close()
easy_apply= driver.find_element(By.CLASS_NAME,'jobs-apply-button artdeco-button artdeco-button--3 artdeco-button--primary ember-view')
easy_apply.click()