from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


webdriver_config= webdriver.ChromeOptions()
webdriver_config.add_experimental_option("detach", True)
driver= webdriver.Chrome(webdriver_config)


ENDPOINT= "https://orteil.dashnet.org/cookieclicker/"

driver.get(ENDPOINT)

consent= driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]/p")
consent.click()

english= driver.find_element(By.XPATH,'//*[@id="langSelect-EN"]')
english.click()

endpoint_data= driver.get(ENDPOINT)