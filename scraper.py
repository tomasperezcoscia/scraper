import requests
import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


HORIZONTAL_ADDRESS = '.styles__AddressWrapper-fs-hdp__sc-13x5vko-0 > h1'
HORIZONTAL_FACT_CONTAINER = '[data-testid="bed-bath-sqft-fact-container"]'

DESCRIPTION = 'article .Text-c11n-8-99-3__sc-aiai24-0'

VERTICAL_ADDRESS = '.PriceChangeAndAddressRow__StyledPriceChangeAndAddressRow-fs-hdp__sc-riwk6j-0 > h1 '
VERTICAL_FACT_CONTAINER = '[data-testid="bed-bath-item"]'

PRICE = '[data-testid="price"]'



urls = []

with open('urls.json', 'r') as f:
	urls = json.loads(f.read())

driver = webdriver.Chrome()




def get_element_text(element):
    try:
        return element.get_attribute('innerHTML')
    except:
        return False

def get_element(driver, selector, mode='css'):
    try:
        if(mode == 'css'):
            element = driver.find_element(By.CSS_SELECTOR, selector)
        else:
            element = driver.find_element(By.XPATH, selector)

        get_element_text(element)
    except:
        print('NO SE LOGRO ENCONTRAR EL ELEMENTO -> {0}'.format(selector))
        return False

def get_page_mode(driver):
    wait = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1.Text-c11n-8-99-3__sc-aiai24-0")))
    try:
        address = driver.find_element(By.CSS_SELECTOR, ".styles__AddressWrapper-fs-hdp__sc-13x5vko-0 > h1")
        if address:
            return 'horizontal'
        else:
            return 'vertical'
    except:
        print ("No se encontro la direccion vertical ni horizontal")

def scrape_page_data(mode):
    data = {}
    if(mode == 'horizontal'):
        print('Scrapeando data para modo horizontal')      
    else:
        print('Scrapeando data para modo vertical')

    return data


for url in urls:
    #NAVEGAMOS A LA URL
    print('Scrapeando la URL -> {0}'.format(url))
    driver.get(url)

	#SCRIPT PARA SCROLLEAR
    driver.execute_script('''
    var element = document.querySelector('.layout-container-desktop');
    if (element) {
        element.scrollTop += 50; // Scroll down by 50 pixels
    }
	''')

	#ESPERAMOS LA PRESENCIA DE ELEMENTOS PARA EVITAR CRASHEOS
    try:
        page_mode = get_page_mode(driver)
        page_data = scrape_page_data(page_mode)
        print('DATA DE ESTA PAGINA -> ')
        print(page_data)
        
    except:
        print('HUBO UN ERROR ESPERANDO AL ELEMENTO.-')
        input()
        continue

    driver.delete_all_cookies()
    time.sleep(2)
    input()
    

input('gorreado')