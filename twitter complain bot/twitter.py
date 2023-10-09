from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep





PROMISED_UP = 100
PROMISED_DOWN= 200

TWITTER_EMAIL= "gambhirsochma@gmail.com"
TWIITER_PASSWORD= '#topper77'
INTERNET_SPEED_TEST= "https://www.speedtest.net/"
TWITTER_URL= "https://twitter.com/i/flow/login"
USERNAME="@ona_linda2285"


class Twitter:

    def __init__(self):
        self.options= webdriver.ChromeOptions()
        self.options.add_experimental_option("detach",True)

        self.driver= webdriver.Chrome(self.options)


    def get_internet_speeds(self):
        self.driver.get(INTERNET_SPEED_TEST)
        sleep(2)
        self.gooption= self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        self.gooption.click()
        sleep(55)
        self.download_speed= self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        return self.download_speed.text
    

    def complain_twitter(self):
        self.driver.get(TWITTER_URL)
        sleep(2)
        self.email= self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        self.email.click()
        self.email.send_keys(TWITTER_EMAIL)
        self.email.send_keys(Keys.ENTER)
        sleep(2)
        try:
            self.errorhandle= self.driver.find_element(By.XPATH,'//*[@id="modal-header"]/span/span')
        except:
            self.errorhandle= "MOOMOEOSd"
        if "enter your" in self.errorhandle.text.strip().lower():
            self.username=self.driver.find_element(By.CLASS_NAME,'r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu')
            self.username.click()
            self.username.send_keys(USERNAME)
            self.username.send_keys(Keys.ENTER)
        self.password= self.driver.find_element(By.NAME,'password')
        self.password.click()
        self.password.send_keys(TWIITER_PASSWORD)
        self.password.send_keys(Keys.ENTER)









