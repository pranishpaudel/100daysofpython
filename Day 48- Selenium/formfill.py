from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


webdriver_config= webdriver.ChromeOptions()
webdriver_config.add_experimental_option("detach", True)
driver= webdriver.Chrome(webdriver_config)


ENDPOINT= "http://secure-retreat-92358.herokuapp.com/"


endpoint_data= driver.get(ENDPOINT)


first_n= driver.find_element(By.NAME,"fName")
first_n.send_keys("PRanish")
last_n= driver.find_element(By.NAME,"lName")
last_n.send_keys("Poudel")
email_n= driver.find_element(By.NAME,"email")
email_n.send_keys("insa@gmail.com")
submit= driver.find_element(By.XPATH,"/html/body/form/button")
submit.click()
