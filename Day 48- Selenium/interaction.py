from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


webdriver_config= webdriver.ChromeOptions()
webdriver_config.add_experimental_option("detach", True)
driver= webdriver.Chrome(webdriver_config)


ENDPOINT= "https://en.wikipedia.org/wiki/Main_Page"


endpoint_data= driver.get(ENDPOINT)
# endpoint_value= driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# endpoint_value.click()

search= driver.find_element(By.NAME, 'search')
search.send_keys("python")
search.send_keys(Keys.ENTER)
search.send_keys


