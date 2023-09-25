from selenium import webdriver
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import csv

from page_objects.constants import Constants
from page_objects.page import Page

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(Constants.WEBSITELINK)
time.sleep(5)
# def set_up():
#     driver.get(Constants.WEBSITELINK)
#     time.sleep(5)
#
# set_up()

class_page = Page(driver)

class_page.closeCookiesPopup()
class_page.inputlocation()
class_page.selectPricefilter()
class_page.selectRoomsfilter()
class_page.selectSortingfilter()


rooms_dictionary= dict()
class_page.showAllSearchResults()
class_page.extractAllRooms(rooms_dictionary)

print(rooms_dictionary)

class_page.writeToCSV(rooms_dictionary,Constants.CSVHEADERS,Constants.CSVFILEPATH)



