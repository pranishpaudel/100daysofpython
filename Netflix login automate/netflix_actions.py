from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


ENDPOINT= "https://www.netflix.com/np/login"
AFTER_LOGIN_ENDPOINT= "https://www.netflix.com/YourAccount"

class Netflix:


    def __init__(self,n_Email,n_Password):

        self.email= n_Email
        self.password= n_Password
        options= webdriver.ChromeOptions()
        options.add_experimental_option("detach",True)
        self.driver= webdriver.Chrome(options)
        self.driver.get(ENDPOINT)
        self.all_profiles=[]

    
    def login(self):
        
        netflix_email= self.driver.find_element(By.NAME,"userLoginId")

        netflix_email.send_keys(self.email)

        netflix_pass= self.driver.find_element(By.NAME,"password")

        netflix_pass.send_keys(self.password)


        sign_in_button= self.driver.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button')

        sign_in_button.click()

    
    def redir_next_page(self):

        self.driver.get(AFTER_LOGIN_ENDPOINT)

    
    def extract_all_info(self):

        last_four_digits= self.driver.find_element(By.CSS_SELECTOR,".account-section-item .wallet--mop").text[15:]
        card_brand= self.driver.find_element(By.CSS_SELECTOR,".account-section-item .wallet--mop img").get_attribute("alt")

        account_status= self.driver.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div/div/div[2]/div/div/div[6]/div[1]/section/div[2]/div/div/div[1]/div[2]').text


        account_payment_plan= self.driver.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div/div/div[2]/div/div/div[6]/div[2]/section/div/div[1]/div[1]/div/b').text

        account_status= self.driver.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div/div/div[2]/div/div/div[6]/div[1]/section/div[2]/div/div/div[1]/div[2]').text
        print(account_status)

        profile_names= self.driver.find_elements(By.CSS_SELECTOR,".profile-hub ul .single-profile")

        for profiles in profile_names:

            self.all_profiles.append(profiles.text.split("\n")[0].lower())

        full_info= f"Account Status: {account_payment_plan} [ {account_status} ] || Card Brand: {card_brand} || Last Four Digits: {last_four_digits}"
        return full_info, self.all_profiles
    
    def close_driver(self):
        self.driver.close()

    
    def put_pin(self,profile_name,account_password,pin_code):

        self.profile= profile_name
        self.password=account_password
        self.pin_code=pin_code
        formatted_XPATH= f'//*[@id="{self.profile}"]/ul/li[3]/a'
        normal_click= self.driver.find_element(By.CSS_SELECTOR,f".profile-hub ul #{self.profile}")
        normal_click.click()
        change_pin= self.driver.find_element(By.XPATH,formatted_XPATH)
        change_pin.click()
        self.password_field= self.driver.find_element(By.NAME,"input-account-content-restrictions")
        self.password_field.send_keys(self.password)
        self.password_field.send_keys(Keys.ENTER)
        time.sleep(2)
        self.checkpoint= self.driver.find_element(By.CLASS_NAME,'ui-binary-input')
        self.checkpoint.click()
        time.sleep(1)
        self.pin_entry1= self.driver.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div/div/div[2]/div/div/div[2]/div[3]/input[1]')
        self.pin_entry1.send_keys(self.pin_code[0])
        time.sleep(0.4)
        self.pin_entry2= self.driver.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div/div/div[2]/div/div/div[2]/div[3]/input[2]')
        self.pin_entry2.send_keys(self.pin_code[1])
        time.sleep(0.4)
        self.pin_entry3= self.driver.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div/div/div[2]/div/div/div[2]/div[3]/input[3]')
        self.pin_entry3.send_keys(self.pin_code[2])
        time.sleep(0.4)
        self.pin_entry4= self.driver.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div/div/div[2]/div/div/div[2]/div[3]/input[4]')
        self.pin_entry4.send_keys(self.pin_code[3])

        self.pin_save= self.driver.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div/div/div[2]/div/div/div[2]/div[4]/button[1]')
        self.pin_save.click()



        




