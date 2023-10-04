from selenium import webdriver
from selenium.webdriver.common.by import By

AMAZON_ENDPOINT= "https://www.python.org"

chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver= webdriver.Chrome(options= chrome_options)

driver.get(AMAZON_ENDPOINT)

price_dollar= driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')

event_with_time_list= price_dollar[0].text.strip().split("\n")

events_list= [event_with_time_list[i] for i in range (1,len(event_with_time_list), 2)]
time_list= [event_with_time_list[i] for i in range (0,len(event_with_time_list), 2)]

print(events_list)
print(time_list)

event_dict = {}

for i in range (0,len(events_list)):
    event_dict[i]= {"Time": time_list[i][5:],"event_name":events_list[i]}


print(event_dict)
# price_cents= driver
# .find_element(By.CLASS_NAME, value="a-price-fraction").text
# print(f"{price_dollar}.{price_cents}")
driver.quit()