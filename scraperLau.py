import requests
import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

urls = []

with open('urls.json', 'r') as f:
	urls = json.loads(f.read())

driver = webdriver.Chrome()

def Get_Element_Text(driver, selector):
	try:
		element = driver.find_element(By.CSS_SELECTOR, selector)
		if(element is not None):
			return element.get_attribute('innerHTML')
		else:
			return False
	except:
		print('NO SE LOGRO ENCONTRAR EL ELEMENTO -> {0}'.format(selector))
		return False

for new_url in urls:

	#NAVEGAMOS A LA URL
	print('Scrapeando la URL -> {0}'.format(new_url))
	driver.get(new_url)

	#ESPERAMOS LA PRESENCIA DE ELEMENTOS PARA EVITAR CRASHEOS
	try:
		wait = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".styles__AddressWrapper-fs-hdp__sc-13x5vko-0 > h1")))
		direction = Get_Element_Text(driver, '.styles__AddressWrapper-fs-hdp__sc-13x5vko-0 > h1')
		print('DIRECCION DETECTADA -> {0}'.format(direction) )
	except:
		print('HUBO UN ERROR ESPERANDO AL ELEMENTO.-')
		continue

	driver.delete_all_cookies()

input('gorreado')