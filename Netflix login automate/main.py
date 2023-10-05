# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time

from netflix_actions import Netflix
USER_EMAIL= "insay.un.ga@gmail.com"
USER_PASS= "@thenew56"
PROFILE_PIN= "4242"

PROFILE_TO_PIN= "khusboo.t_"


# ENDPOINT= "https://www.netflix.com/np/login"
# AFTER_LOGIN_ENDPOINT= "https://www.netflix.com/YourAccount"
# options= webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver= webdriver.Chrome(options)
# driver.get(ENDPOINT)
# netflix_email= driver.find_element(By.NAME,"userLoginId")

# netflix_email.send_keys(USER_EMAIL)

# netflix_pass= driver.find_element(By.NAME,"password")

# netflix_pass.send_keys(USER_PASS)


# sign_in_button= driver.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button')

# sign_in_button.click()
# time.sleep(2)
# driver.get(AFTER_LOGIN_ENDPOINT)
# time.sleep(2)

# last_four_digits= driver.find_element(By.CSS_SELECTOR,".account-section-item .wallet--mop").text[15:]
# card_brand= driver.find_element(By.CSS_SELECTOR,".account-section-item .wallet--mop img").get_attribute("alt")
# print(last_four_digits)
# print(card_brand)

# account_payment_plan= driver.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div/div/div[2]/div/div/div[6]/div[2]/section/div/div[1]/div[1]/div/b').text

# account_status= driver.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div/div/div[2]/div/div/div[6]/div[1]/section/div[2]/div/div/div[1]/div[2]').text
# print(account_status)
# print(account_payment_plan)

# profile_names= driver.find_elements(By.CSS_SELECTOR,".profile-hub ul .single-profile")

# all_profiles= []
# for profiles in profile_names:
#    all_profiles.append(profiles.text.split("\n")[0])



netflix= Netflix(n_Email=USER_EMAIL, n_Password=USER_PASS)
netflix.login()
time.sleep(2)
netflix.redir_next_page()

time.sleep(2)
returned_full_info, returned_all_profiles = netflix.extract_all_info()
print(returned_full_info)
print(returned_all_profiles)

PROFILE_TO_PIN_FORMATTED= f"profile_{returned_all_profiles.index(PROFILE_TO_PIN.lower())}"

print(PROFILE_TO_PIN_FORMATTED)

netflix.put_pin(profile_name=PROFILE_TO_PIN_FORMATTED,account_password=USER_PASS,pin_code=PROFILE_PIN)



