import requests
import json

r = requests.get("https://www.zillow.com/xml/sitemaps/us/hdp/for-sale-by-owner/latest.xml.gz")

if(r.status_code != 200 and r.status_code != '200'):
	print('FALLO LA REQUEST.-')
	input()
else:
	print('REQUEST SUCCESSFULLY')

arr = r.text.splitlines()

total_urls = []

for elem in arr:
	if('<loc>' in elem and '</loc>' in elem):
		url_trimmed = elem.strip()
		url_trimmed = url_trimmed.replace('<loc>', '')
		url_trimmed = url_trimmed.replace('</loc>', '')
		total_urls.append(url_trimmed)

print('FINISHED')
print(total_urls[0])


array_converted = json.dumps(total_urls)

f = open('urls.json', 'w')
f.write(array_converted)
f.close()

input('Presione cualquier tecla para finalizar')



'''

FACTORES BASICOS :

data-testid="bed-bath-sqft-fact-container"[0] -> SPAN -> HABITACIONES
data-testid="bed-bath-sqft-fact-container"[1] -> SPAN -> BAÑOS
data-testid="bed-bath-sqft-fact-container"[2] -> SPAN -> SQUARE FOOT

data-testid="price" -> SPAN -> Precio (EN USD)
.styles__AddressWrapper-fs-hdp__sc-13x5vko-0 > h1 -> DIRECCION

CARACTERISTICAS RANDOM
.styles__StyledContainer-fs-hdp__sc-1dg6897-0 (CONTAINER)
	-> DIV (SUBCONTAINER) -> SPAN (CARACTERISTICA)

INSIGHTS
.InsightsTagsstyles__TagContainer-fs-hdp__sc-rgxjfy-0 (CONTAINER) -> SPAN = CARACTERISTICA INDIVUAL (EXTRAER TEXTO)


Text-c11n-8-99-3__sc-aiai24-0 -> DESCRIPCION.-

'''
