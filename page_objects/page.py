from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import csv
import pandas as pd
from page_objects.constants import Constants


class Page():
    def  __init__(self,driver):
        self.driver= driver
        self.EC =  expected_conditions
        self.NoSuchElementException =  NoSuchElementException

    def closeCookiesPopup(self):
        closeCookiesPopup = self.driver.find_element(By.XPATH,Constants.CLOSECOOKIESPOPUP).click()



    def inputlocation(self):
        inputlocation = self.driver.find_element(By.XPATH,Constants.LOCATIONINPUT).click()
        time.sleep(2)
        selectLocation = self.driver.find_element(By.XPATH,Constants.SELECTLOCATION).click()
        time.sleep(2)
        closePopup = self.driver.find_element(By.XPATH,Constants.CLOSEINFOPOPUP).click()




    def selectPricefilter(self):
        opePricefilter = self.driver.find_element(By.XPATH,Constants.OPENPRICEFILTER).click()
        time.sleep(2)
        selectFromPricefilter = self.driver.find_element(By.XPATH,Constants.SELECTFROMPRICEFILTER).send_keys(Constants.PRICEFROM)
        selectToPricefilter = self.driver.find_element(By.XPATH,Constants.SELECTTOPRICEFILTER).send_keys(Constants.PRICETO)
        selectPricefilter = self.driver.find_element(By.XPATH,Constants.SELECTPRICEFILTER).click()



    def selectRoomsfilter(self):
        openRoomsfilter = self.driver.find_element(By.XPATH,Constants.OPENROOMSFILTER).click()
        time.sleep(2)
        selectRoomsfilter = self.driver.find_element(By.XPATH,Constants.SELECTROOMSFILTER).click()
        applyRoomsfilter = self.driver.find_element(By.XPATH,Constants.APPLYROOMSFIILTER).click()



    def selectSortingfilter(self):
        openSortingfilter =  self.driver.find_element(By.XPATH,Constants.OPENSORTINGFILTER).click()
        time.sleep(1)
        selectSortingfilter = self.driver.find_element(By.XPATH,Constants.SELECSORTINGFILTERS).click()
    # -------------------------------------------------------------------------------------------------------------------------
    def scrollToTheBottom(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    def showAllSearchResults(self):
        wait = WebDriverWait(self.driver, 15)
        while True:
           try:
            self.scrollToTheBottom()
            clickShowMore =  wait.until(self.EC.element_to_be_clickable(self.driver.find_element(By.XPATH,Constants.SHOWMOREBUTTON)))
            clickShowMore.click()
           except self.NoSuchElementException:
               break


    def extractAllRooms(self,dictionary):
        time.sleep(5)
        allfoundRoomsAddress = self.driver.find_elements(By.XPATH,    Constants.ALLFOUNDROOMSADDRESS)
        allfoundRoomsPrices = self.driver.find_elements(By.XPATH,    Constants.ALLFOUNDROOMSPRICES)
        # allfoundRoomsDescription = driver.find_elements(By.XPATH,
        #                                            "//div[contains(@class,'desc-hidden')]")
        allfoundRoomsPublicationDate = self.driver.find_elements(By.XPATH,                                               Constants.ALLFOUNDROOMSDATE)

        for j in range(0,len(allfoundRoomsAddress)):
            dictionary[len(dictionary)] = {
                            'address':allfoundRoomsAddress[j].text,
                'price':allfoundRoomsPrices[j].text,
                'date': allfoundRoomsPublicationDate[j].text
            }


    def writeToCSV(self,dictionary,headers,csv_file_path):
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)

            # Write the header row
            writer.writeheader()

            # Write the data rows
            for room_number, room_info in dictionary.items():
                writer.writerow({'Room Number': room_number, 'Address': room_info['address'], 'Price': room_info['price'],
                                 'Date': room_info['date']})


    def goThroughPages(self):
        numberofPages = self.driver.find_element(By.XPATH,
        "//span[contains(@class,'pagerMobileScroll')]//a[contains(@class,'page-item button-border')][3]")
        for i in range(1, int(numberofPages.text)+1):
            page =  self.driver.find_element(By.XPATH,
                                "//span[contains(@class,'pagerMobileScroll')]//a[contains(@class,'page-item button-border')]["+str(i)+"]")
            driver.execute_script("arguments[0].scrollIntoView();", page)
            driver.execute_script("arguments[0].click();", page)
