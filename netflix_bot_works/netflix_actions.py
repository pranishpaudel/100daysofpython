from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

ENDPOINT= "https://www.netflix.com/np/login"
AFTER_LOGIN_ENDPOINT= "https://www.netflix.com/YourAccount"

class Netflix:
    def __init__(self, n_Email, n_Password):
        self.email = n_Email
        self.password = n_Password

        options = Options()
        options.add_argument("--headless")  # Run in headless mode
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(ENDPOINT)
        self.all_profiles = []

    
    def login(self):
        
        netflix_email= self.driver.find_element(By.NAME,"userLoginId")

        netflix_email.send_keys(self.email)

        netflix_pass= self.driver.find_element(By.NAME,"password")

        netflix_pass.send_keys(self.password)


        sign_in_button= self.driver.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button')

        sign_in_button.click()

        time.sleep(1)

        try:
            driver_message= self.driver.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/div/div[2]').text
            return driver_message
        except:
            return "NO ERROR"
        
    def check_alive_netflix(self):
         
        try:
            netflix_message= self.driver.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div/div/div[2]/div/div[1]/div[2]/div/h1').text
            return netflix_message
        except:
            return "OKOKOKOK"


    def redir_next_page(self):

        self.driver.get(AFTER_LOGIN_ENDPOINT)

    
    def extract_all_info(self):
        
            last_four_digits= self.driver.find_element(By.CSS_SELECTOR,".account-section-item .wallet--mop").text[15:]
            account_status= self.driver.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div/div/div[2]/div/div/div[6]/div[1]/section/div[2]/div/div/div[1]/div[2]').text
            card_brand= self.driver.find_element(By.CSS_SELECTOR,".account-section-item .wallet--mop img").get_attribute("alt")
            if last_four_digits.strip().lower()=="credit":
                 last_four_digits= self.driver.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div/div/div[2]/div/div/div[6]/div[1]/section/div[2]/div/div/div[1]/div[3]/div/span').text[15:]
                 account_status= self.driver.find_element(By.CSS_SELECTOR,"[data-uia='gift-credit-content-subhead']").text
                 card_brand= self.driver.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div/div/div[2]/div/div/div[6]/div[1]/section/div[2]/div/div/div[1]/div[1]/div[1]').text
            account_payment_plan= self.driver.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div/div/div[2]/div/div/div[6]/div[2]/section/div/div[1]/div[1]/div/b').text

            

            profile_names= self.driver.find_elements(By.CSS_SELECTOR,".profile-hub ul .single-profile")

            for profiles in profile_names:

                self.all_profiles.append(profiles.text.split("\n")[0].lower())

            full_info= f"Account Status: {account_payment_plan} [ {account_status} ] || Card Brand: {card_brand} || Last Four Digits: {last_four_digits}"
            return full_info, self.all_profiles

    
    def close_driver(self):
        self.driver.quit()

    def change_password(self,old_pass,new_pass):
        self.clickchpass= self.driver.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div/div/div[2]/div/div/div[6]/div[1]/section/div[1]/div/div[2]/div[2]/a')
        self.clickchpass.click()
        old_pass_sec= self.driver.find_element(By.XPATH,'//*[@id="id_currentPassword"]')
        old_pass_sec.send_keys(old_pass)
        new_pass_sec= self.driver.find_element(By.XPATH,'//*[@id="id_newPassword"]')
        new_pass_sec.send_keys(new_pass)
        new_pass_con= self.driver.find_element(By.XPATH,'//*[@id="id_confirmNewPassword"]')
        new_pass_con.send_keys(new_pass)
        blue_button= self.driver.find_element(By.XPATH,'//*[@id="btn-save"]')
        blue_button.click()
        
    
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



    def remove_pin(self,rprofile_name,raccount_password,IS_MASTER):


            self.declare= IS_MASTER
            if self.declare==True:
                self.rprofile= "profile_0"
            else:
                self.rprofile= rprofile_name
            self.rpassword=raccount_password
            rformatted_XPATH= f'//*[@id="{self.rprofile}"]/ul/li[3]/a'
            rnormal_click= self.driver.find_element(By.CSS_SELECTOR,f".profile-hub ul #{self.rprofile}")
            rnormal_click.click()
            rchange_pin= self.driver.find_element(By.XPATH,rformatted_XPATH)
            rchange_pin.click()
            self.rpassword_field= self.driver.find_element(By.NAME,"input-account-content-restrictions")
            self.rpassword_field.send_keys(self.rpassword)
            self.rpassword_field.send_keys(Keys.ENTER)
            time.sleep(2)
            self.rcheckpoint= self.driver.find_element(By.CLASS_NAME,'ui-binary-input')
            self.rcheckpoint.click()
            time.sleep(1)

            self.rpin_save= self.driver.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div/div/div[2]/div/div/div[2]/div[3]/button[1]')
            self.rpin_save.click()

        
    def retrive_latest_watch(self,sprofile_name):
         try:
            self.sprofile_name= sprofile_name
            snormal_click= self.driver.find_element(By.CSS_SELECTOR,f".profile-hub ul #{self.sprofile_name}")
            snormal_click.click()  
            swatch_click= self.driver.find_element(By.XPATH,f'//*[@id="{self.sprofile_name}"]/ul/li[5]')
            swatch_click.click()    
            all_netflix_date= self.driver.find_elements(By.CSS_SELECTOR,'.responsive-account-container div .structural.retable.stdHeight .retableRow .col.date.nowrap') 
            all_netflix_title= self.driver.find_elements(By.CSS_SELECTOR,'.responsive-account-container div .structural.retable.stdHeight .retableRow .col.title') 
            return all_netflix_date,all_netflix_title
         except:
              return [1,5,6],[5,7,2]