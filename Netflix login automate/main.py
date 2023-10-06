# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time

from netflix_actions import Netflix
USER_EMAIL= "bedul.ol123@gmail.com"
USER_PASS= ""
NEW_PASS= "sad32dasdas"
PROFILE_PIN= "4242"

PROFILE_TO_PIN= "swoyam"
IS_MASTER_PROFILE= True

INCORRECT_PASS_RES= "Incorrect password"
TECHNICAL_MSG="We are having technical difficulties"
WELCOME_MSG= "Welcome back"

netflix_data= open("Netflix login automate/netflixaccs.txt")

netflix_accounts= []
netflix_accounts=netflix_data.read().strip().split("\n")

for netflixx in netflix_accounts:

    netflix= Netflix(n_Email=netflixx.split("|")[0], n_Password=netflixx.split("|")[1])
    driver_message= netflix.login()
    if WELCOME_MSG.lower() in netflix.check_alive_netflix().lower():
        print(f"Netflix: THE NETFLIX ACCOUNT {netflixx} HAS DIED")
    elif not INCORRECT_PASS_RES.lower() in driver_message.lower() and not TECHNICAL_MSG.lower() in driver_message.lower():
        netflix.redir_next_page()

        time.sleep(0.9)
        returned_full_info, returned_all_profiles = netflix.extract_all_info()
        print(f"Netflix: {netflixx} || Full info: {returned_full_info} || Profiles {returned_all_profiles}")
        try:
            PROFILE_TO_PIN_FORMATTED= f"profile_{returned_all_profiles.index(PROFILE_TO_PIN.lower())}"
        except:
            print("Input Profile not found")
            exit()
        all_date, all_title= netflix.retrive_latest_watch(sprofile_name=PROFILE_TO_PIN_FORMATTED)
        if not all_date==[1,5,6]:
            formatted_title_list=[]
            number_of_watches= len(all_date)
            in_value=0
            while not number_of_watches==0:
                formatted_title_list.append(f"Date: {all_date[in_value].text} || Title: {all_title[in_value].text}")
                number_of_watches-=1
                in_value+=1

            print(formatted_title_list)
            netflix.close_driver()
        else:
            print("Error printing the watch history")
        # netflix.change_password(old_pass=NEW_PASS,new_pass="ASCIIEBCDIC1")
        
        # netflix.put_pin(profile_name=PROFILE_TO_PIN_FORMATTED,account_password=USER_PASS,pin_code=PROFILE_PIN)

    else:
        print(f"Netflix: {netflixx} || Driver Message: {driver_message}")



# PROFILE_TO_PIN_FORMATTED= f"profile_{returned_all_profiles.index(PROFILE_TO_PIN.lower())}"

# print(PROFILE_TO_PIN_FORMATTED)



# netflix.remove_pin(rprofile_name=PROFILE_TO_PIN_FORMATTED,raccount_password=USER_PASS,IS_MASTER=IS_MASTER_PROFILE)



