from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import csv
import pandas as pd


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://dom.ria.com/uk/arenda-kvartir/")
time.sleep(2)
closePopup = driver.find_element(By.XPATH,
"//button[contains(text(),'Приймаю всі')]").click()



inputlocation = driver.find_element(By.XPATH,
"//input[@class='e-form']").click()
time.sleep(1)
selectLocation = driver.find_element(By.XPATH,
"//span[contains(text(),'місто Вінниця, Вінницька область')]").click()
time.sleep(1)
closePopup = driver.find_element(By.XPATH,
"//a[@class='close unlink pointer']").click()
time.sleep(2)




opePricefilter = driver.find_element(By.XPATH,
"//div[contains(@class, 'first-letter')]/../div[contains(text(), 'ціна')]").click()
time.sleep(1)
selectFromPricefilter = driver.find_element(By.XPATH,
"//input[contains(@id, '235_from')]").send_keys('9000')
selectToPricefilter = driver.find_element(By.XPATH,
"//input[contains(@id, '235_to')]").send_keys('10000')
selectToPricefilter = driver.find_element(By.XPATH,
"//span[contains(text(),'Грн')]/../../../../../../../../../../../../../button[contains(@class, 'button-search')]").click()




openRoomsfilter = driver.find_element(By.XPATH,
"//div[contains(@class, 'first-letter')]/../div[contains(text(), 'Кімнати')]").click()
time.sleep(1)
selectRoomsfilter = driver.find_element(By.XPATH,
"//label[contains(text(), '1')]").click()
applyRoomsfilter = driver.find_element(By.XPATH,
"//label[contains(text(), 'Кімнат')]/../../../../../../button[contains(@class,'button-search')]").click()




openSortingfilter =  driver.find_element(By.XPATH,
"//span[contains(text(),'Сортування звичайне') and contains(@class,'el-select')]").click()
time.sleep(1)
selectRoomsfilter = driver.find_element(By.XPATH,
"//span[contains(text(),'Спочатку дешеві')]").click()
# -------------------------------------------------------------------------------------------------------------------------


rooms_dictionary= dict()
rooms_headers = ["id","address", "price"]
def extractAllRooms(dictionary):
    time.sleep(5)
    allfoundRoomsAddress = driver.find_elements(By.XPATH,
    "//section[contains(@class,'realty-item')]//a[contains(@class,'realty-link')]")
    allfoundRoomsPrices = driver.find_elements(By.XPATH,
    "//section[contains(@class,'realty-item')]//b[contains(@class,'size22')]")
    # allfoundRoomsDescription = driver.find_elements(By.XPATH,
    #                                            "//div[contains(@class,'desc-hidden')]")
    allfoundRoomsPublicationDate = driver.find_elements(By.XPATH,
                                               "//time[contains(@class,'withDate')]")


    # for i in range(len(dictionary),(len(dictionary)+len(allfoundRoomsAddress))):
    for j in range(0,len(allfoundRoomsAddress)):
        dictionary[len(dictionary)] = {
                        'address':allfoundRoomsAddress[j].text,
            'price':allfoundRoomsPrices[j].text,
            # 'description':allfoundRoomsDescription[j].text,
            'date': allfoundRoomsPublicationDate[j].text
        }
        # print(dictionary)






numberofPages = driver.find_element(By.XPATH,
"//span[contains(@class,'pagerMobileScroll')]//a[contains(@class,'page-item button-border')][4]")


for i in range(1, int(numberofPages.text)+1):
    page = driver.find_element(By.XPATH,
                        "//span[contains(@class,'pagerMobileScroll')]//a[contains(@class,'page-item button-border')]["+str(i)+"]")
    driver.execute_script("arguments[0].scrollIntoView();", page)
    # time.sleep(5)
    driver.execute_script("arguments[0].click();", page)

    extractAllRooms(rooms_dictionary)
    print(i)

print(rooms_dictionary)

df = pd.DataFrame(rooms_dictionary)
df = df.transpose()
df.to_csv('C:/Kaggle/test_scraper/output.csv')



