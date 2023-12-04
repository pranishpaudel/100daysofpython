from selenium import webdriver
import time

for i in range(1, 1000):

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(options=options)


    try:
        driver.get("https://github.com/pranishpaudel")
        time.sleep(3)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the browser window after each iteration
        driver.quit()
