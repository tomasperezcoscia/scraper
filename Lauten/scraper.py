import requests
import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains



'''# Find all elements with data-testid="bed-bath-sqft-fact-container"
elements = driver.find_elements(By.CSS_SELECTOR, '[data-testid="bed-bath-sqft-fact-container"]')

data = []

for element in elements:
    number = element.find_element(By.CSS_SELECTOR, 'span:nth-child(1)').text.strip()
    name = element.find_element(By.CSS_SELECTOR, 'span:nth-child(2)').text.strip()
    data.append({"name": name, "number": number})

print(data)
'''



urls = []

with open('urls.json', 'r') as f:
	urls = json.loads(f.read())

driver = webdriver.Chrome()
	

def Get_Element_Text(driver, selector, mode='css'):
	try:
		if(mode == 'css'):
			element = driver.find_element(By.CSS_SELECTOR, selector)
		else:
			element = driver.find_element(By.XPATH, selector)

		if(element is not None):
			return element.get_attribute('innerHTML')
		else:
			return False
	except:
		print('NO SE LOGRO ENCONTRAR EL ELEMENTO -> {0}'.format(selector))
		return False

def Get_Page_Mode(driver):
	try:
		wait = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".styles__AddressWrapper-fs-hdp__sc-13x5vko-0 > h1")))
		return 'horizontal'
	except:
		return 'vertical'

def Scrape_Page_Data(mode):
	data = {}
	if(mode == 'horizontal'):
		print('Scrapeando data para modo horizontal')
		data['bedrooms'] = Get_Element_Text(driver, '/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/div[1]/span[1]', 'xpath')
		data['bathrooms'] = Get_Element_Text(driver, '/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/button/div/span[1]', 'xpath')
		data['squarefoot'] = Get_Element_Text(driver, '/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/div[2]/span[1]', 'xpath')
		data['price'] = Get_Element_Text(driver, 'span[data-testid="price"] > span')
		data['direction'] = Get_Element_Text(driver, '.styles__AddressWrapper-fs-hdp__sc-13x5vko-0 > h1')
		data['description'] = Get_Element_Text(driver, 'article .Text-c11n-8-99-3__sc-aiai24-0')

		data['features'] = []
		data['photos_url'] = []
		features = driver.find_elements(By.CSS_SELECTOR, '.styles__StyledContainer-fs-hdp__sc-6k0go5-0 span')
		for feature in features:
			data['features'].append(feature.text.strip())

		print(data)
		try:
			btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/button')
			btn.click()

			print('BUTTON DATA ->')
			print(btn)
			time.sleep(1)
			total_photos = driver.find_elements(By.CSS_SELECTOR, 'picture source')
			
			for photo in total_photos:
				data['photos_url'].append(photo.get_attribute('srcset'))
		except Exception as e:
			print('exploto obteniendo fotos ->')
			print(e)

	else:
		print('Scrapeando data para modo vertical')

	return data

for new_url in urls:

	#NAVEGAMOS A LA URL
	print('Scrapeando la URL -> {0}'.format(new_url))
	driver.get(new_url)

	#SCRIPT PARA SCROLLEAR
	driver.execute_script('''
    var element = document.querySelector('.layout-container-desktop');
    if (element) {
        element.scrollTop += 50; // Scroll down by 50 pixels
    }
	''')

	#ESPERAMOS LA PRESENCIA DE ELEMENTOS PARA EVITAR CRASHEOS
	try:
		page_mode = Get_Page_Mode(driver)
		page_data = Scrape_Page_Data(page_mode)
		print('DATA DE ESTA PAGINA -> ')
		print(page_data)
		input()
	except:
		print('HUBO UN ERROR ESPERANDO AL ELEMENTO.-')
		continue

	driver.delete_all_cookies()
	time.sleep(2)

input('gorreado')


'''

FACTORES BASICOS :


CARACTERISTICAS RANDOM
.styles__StyledContainer-fs-hdp__sc-1dg6897-0 (CONTAINER)
	-> DIV (SUBCONTAINER) -> SPAN (CARACTERISTICA)

INSIGHTS
.InsightsTagsstyles__TagContainer-fs-hdp__sc-rgxjfy-0 (CONTAINER) -> SPAN = CARACTERISTICA INDIVUAL (EXTRAER TEXTO)


Text-c11n-8-99-3__sc-aiai24-0 -> DESCRIPCION.-

'''