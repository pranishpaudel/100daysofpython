ENDPOINT= "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A-122.67022170019531%2C%22east%22%3A-122.19643629980469%2C%22south%22%3A37.59923537951954%2C%22north%22%3A37.950929272115715%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

LINKS_OF_PROPERTY=[]
PRICES_OF_PROPERTY= []
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup


class Property:

    def  __init__(self):
        self.options= webdriver.ChromeOptions()
        self.options.add_experimental_option("detach",True)
        self.driver=webdriver.Chrome(self.options)
        self.driver.get(ENDPOINT)
        self.webdata= self.driver.page_source

    def click_next(self):
        self.next= self.driver.find_element(By.CSS_SELECTOR,".PaginationJumpItem-c11n-8-84-3__sc-18wdg2l-0.jRUCrX .StyledButton-c11n-8-84-3__sc-wpcbcc-0.dZFSon.PaginationButton-c11n-8-84-3__sc-si2hz6-0.wfluH")
        self.next.click()


    def extract_link(self):
 
        for i in range(10):
            self.soup= BeautifulSoup(self.webdata,'html.parser')
            self.links= self.soup.select(".StyledPropertyCardDataWrapper-c11n-8-84-3__sc-1omp4c3-0.bKpguY.property-card-data a")
            LINKS_OF_PROPERTY.extend(self.links)
            self.prices= self.soup.select(".PropertyCardWrapper__StyledPriceGridContainer-srp__sc-16e8gqd-0.kSsByo .PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1.iMKTKr")
            PRICES_OF_PROPERTY.extend(self.prices)
            time.sleep(3)
            self.click_next()
        return LINKS_OF_PROPERTY,PRICES_OF_PROPERTY
    





