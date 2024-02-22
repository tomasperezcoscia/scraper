import requests
import json
from bs4 import BeautifulSoup

# URL of the XML file
url = "https://www.zillow.com/xml/sitemaps/us/hdp/for-sale-by-owner/latest.xml.gz"

# Send an HTTP request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the XML data using BeautifulSoup with 'html.parser'
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <loc> tags
    loc_tags = soup.find_all('loc')

    # Extract URLs
    urls = [loc.text.strip() for loc in loc_tags]

    # Print the URLs
    for url in urls:
        print(url)
        print("\n")
        
    print("Finished printing the URLs")  
    total_urls = len(urls)
    print("Total number of URLs:", total_urls)  

    array_converted = json.dumps(urls)

    f = open('urls.json', 'w')
    f.write(array_converted)
    f.close()

    


else:
    print("Failed to retrieve data from the URL:", response.status_code)


    '''
    ELEMENTO[0] -> NUMERO DE ELEMENTOS

    data-testid="bed-bath-sqft-fact-container"
    bed-bath-sqft-fact-container[0] -> Habitaciones [0] -> Cant de habitaciones
    bed-bath-sqft-fact-container[1] -> Baños [0] -> Cant de baños
    bed-bath-sqft-fact-container[2] -> M2 [0] -> Cant de m2

    data-testid="price" -> Precio

    class="styles__AddressWrapper-fs-hdp__sc-13x5vko-0" > h1 .innerHTML -> Dirección

    class="styles__StyledContainer-fs-hdp__sc-1dg6897-0" -> Datos random (CONTAINER)
        ->Div 
            ->SPAN (CARACTERISTICA)
            

    class="Text-c11n-8-99-3__sc-aiai24-0" -> Descripción      
            '''



