class Constants():
    UA_LABEL_LOCATION = 'місто Вінниця, Вінницька область'
    UA_LABEL_ACCEPT_ALL  = 'Приймаю всі'
    UA_LABEL_PRICE = 'ціна'
    UA_LABEL_CURRENCY = 'Грн'
    UA_LABEL_ROOMS =  'Кімнати'
    UA_LABEL_ROOM = 'Кімнат'
    UA_LABEL_SORTING = 'Сортування звичайне'
    UA_LABEL_SORTING_CHEAPEST = 'Спочатку дешеві'

    PRICEFROM = '9000'
    PRICETO = '10000'



    WEBSITELINK = "https://dom.ria.com/uk/arenda-kvartir/"
    CLOSECOOKIESPOPUP = "//button[contains(text(),'"+UA_LABEL_ACCEPT_ALL+"')]"

    LOCATIONINPUT = "//input[@class='e-form']"
    SELECTLOCATION = "//span[contains(text(),'"+UA_LABEL_LOCATION+"')]"
    CLOSEINFOPOPUP = "//a[@class='close unlink pointer']"

    OPENPRICEFILTER = "//div[contains(@class, 'first-letter')]/../div[contains(text(), '"+UA_LABEL_PRICE+"')]"
    SELECTFROMPRICEFILTER = "//input[contains(@id, '235_from')]"
    SELECTTOPRICEFILTER = "//input[contains(@id, '235_to')]"
    SELECTPRICEFILTER = "//span[contains(text(),'"+UA_LABEL_CURRENCY+"')]/../../../../../../../../../../../../../button[contains(@class, 'button-search')]"

    OPENROOMSFILTER = "//div[contains(@class, 'first-letter')]/../div[contains(text(), '"+UA_LABEL_ROOMS+"')]"
    SELECTROOMSFILTER = "//label[contains(text(), '1')]"
    APPLYROOMSFIILTER = "//label[contains(text(), '"+UA_LABEL_ROOM+"')]/../../../../../../button[contains(@class,'button-search')]"

    OPENSORTINGFILTER = "//span[contains(text(),'"+UA_LABEL_SORTING+"') and contains(@class,'el-select')]"
    SELECSORTINGFILTERS = "//span[contains(text(),'"+UA_LABEL_SORTING_CHEAPEST+"')]"

    ALLFOUNDROOMSADDRESS = "//section[contains(@class,'realty-item')]//a[contains(@class,'realty-link')]"
    ALLFOUNDROOMSPRICES = "//section[contains(@class,'realty-item')]//b[contains(@class,'size22')]"
    ALLFOUNDROOMSDATE = "//time[contains(@class,'withDate')]"

    SHOWMOREBUTTON = "//button[contains(@class, 'button-moreItems')]"
    FOOTER = "//div[contains(@class, 'cr i-block')]"

    CSVHEADERS = ['Room Number', 'Address', 'Price', 'Date']
    CSVFILEPATH = 'rooms.csv'



