import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

urls = []
with open('urls.json', 'r') as file:
    urls = json.loads(file.read())

print(urls)
driver = webdriver.Chrome()

for new_url in urls:
    driver.get(new_url)
    print("Scraping URL:", new_url)
    print("\n")
    
    try:
        # Wait for the element with CSS selector ".stylesAddressWrapper-fs-hdpsc-13x5vko-0 > h1" to be present
        print("Waiting for the element to be present")
        wait = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".stylesAddressWrapper-fs-hdpsc-13x5vko-0 > h1")))
        print("Element found")
        
        # Find and print the innerHTML of the element with the specified CSS selector
        print("Finding element with CSS selector .stylesAddressWrapper-fs-hdpsc-13x5vko-0 > h1")
        element = driver.find_element(By.CSS_SELECTOR, ".stylesAddressWrapper-fs-hdpsc-13x5vko-0 > h1")
        print(element.get_attribute("innerHTML"))
    except Exception as e:
        print("Error:", e)
    
    # You can continue with other elements similarly using their data-testid or other attributes
    
    input("Press Enter to continue...")
