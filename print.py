from selenium import webdriver
from selenium.webdriver.common.by import By

NETFLIX_ENDPOINT= "https://www.netflix.com"

chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver= webdriver.Chrome(options= chrome_options)

driver.get(NETFLIX_ENDPOINT)