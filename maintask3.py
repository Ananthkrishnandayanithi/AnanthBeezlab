import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the initial page
driver.get("https://www.exito.com/")
time.sleep(3)

# Maximize the window
driver.maximize_window()
time.sleep(3)
driver.maximize_window()
time.sleep(3)

wait = WebDriverWait(driver, 10)
sco = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/main/section[2]/div/div/a/img')))
driver.execute_script("arguments[0].scrollIntoView();", sco)
time.sleep(3)

spirit = driver.find_element(By.XPATH, "(//div[@data-fs-categorie-buble-box='true'])[5]")
spirit.click()
time.sleep(3)

'''brandy = driver.find_element(By.XPATH, '//input[@id="desktop-store-filter-Categoría-Brandy"]')
brandy.click()
time.sleep(3)'''

scot = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/main/section[5]')))
driver.execute_script("arguments[0].scrollIntoView();", scot)
time.sleep(3)

button_xpath = '//*[@id="desktop-store-filter-Categoría-Brandy"]'  # Replace with your button's XPath
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))

# Click the button
button.click()
time.sleep(3)

spirit = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[6]/div/div[1]/div[2]/button')
spirit.click()
time.sleep(3)
product_info = []

spirit = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[6]/div/div[1]/div[2]/button')
spirit.click()
time.sleep(5)

'''cross = driver.find_element(By.XPATH, '//*[@id="wps-overlay-close-button"]')

# If the close button exists, click on it
if cross:
    cross.click()
else:
    print("no")'''

time.sleep(3)
product_data = []

# XPath for the next button
next_button_xpath = '//*[@id="ArrowBreadcrumb"]'

# Loop to scrape data from multiple pages
while True:
    # Find all elements containing product name, price, and quantity
    product_elements = driver.find_elements(By.XPATH, '//*[@id="__next"]/main/section[6]/div/div[2]/div[2]/div[2]/ul')

    print("Number of product elements found:", len(product_elements))

    # Iterate over the found elements and collect data
    for element in product_elements:
        # Find the product name, price, and quantity elements within the product element
        name_elements = element.find_elements(By.XPATH, '//div[@data-fs-product-card-heading="true"]')
        price_elements = element.find_elements(By.XPATH, "//div[contains(@class,'ProductPrice_container__CkWjL')]")

        # Extract text from the name, price, and quantity elements
        for name_element, price_element in zip(name_elements, price_elements):
            product_name = name_element.text.strip().split("Ml")[0].strip()
            product_price = price_element.text.strip()

            # Add the name, price, and quantity to the product_data list as a dictionary
            product_data.append({
                "Product": product_name,  # Changed column name to "Product"
                "Regular Price": product_price,  # Changed column name to "Regular Price"
                "Category": "barndy"
            })

    try:
        # Look for the 'Next' button and click on it to navigate to the next page
        time.sleep(10)
        next_button = driver.find_element(By.XPATH, next_button_xpath)
        if next_button.is_enabled():
            next_button.click()
            time.sleep(5)  # Adjust sleep time as needed
    except Exception:
        break  # Exit the loop if the 'Next' button is not found

# Convert product_data list to DataFrame and print
product_data_df = pd.DataFrame(product_data)
print("product_data DataFrame:")
print(product_data_df)

time.sleep(3)
up = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/main/section[5]')))
driver.execute_script("arguments[0].scrollIntoView();", up)
time.sleep(3)
button_xpath = '//*[@id="desktop-store-filter-panel--0"]/ul/li[2]'  # Replace with your button's XPath
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))

# Click the button
button.click()
time.sleep(5)
scot = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/main/section[5]')))
driver.execute_script("arguments[0].scrollIntoView();", scot)
time.sleep(3)

cat_xpath = '//*[@id="desktop-store-filter-panel--0"]/ul/li[3]'  # Replace with your button's XPath
wait = WebDriverWait(driver, 10)
catbutton = wait.until(EC.element_to_be_clickable((By.XPATH, cat_xpath)))

# Click the button
catbutton.click()
time.sleep(3)
filter = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[6]/div/div[1]/div[2]/button')
filter.click()
time.sleep(5)
urls = [
    "https://www.exito.com/vinos-y-licores?category-2=cerveza&category-1=vinos-y-licores&facets=category-2%2Ccategory-1&sort=score_desc&page=0",
    "https://www.exito.com/vinos-y-licores?category-2=cerveza&category-1=vinos-y-licores&facets=category-2%2Ccategory-1&sort=score_desc&page=1",
    "https://www.exito.com/vinos-y-licores?category-2=cerveza&category-1=vinos-y-licores&facets=category-2%2Ccategory-1&sort=score_desc&page=2"
]


product3_data = []  # Changed variable name to product2_data
for url in urls:
    # Navigate to the page
    driver.get(url)

    # Find all elements containing product name, price, and quantity
    product_elements = driver.find_elements(By.XPATH, '//*[@id="__next"]/main/section[6]/div/div[2]/div[2]/div[2]')

    print("Number of product elements found:", len(product_elements))

    # Iterate over the found elements and collect data
    for element in product_elements:
        # Find the product name, price, and quantity elements within the product element
        name_elements = element.find_elements(By.XPATH, '//div[@data-fs-product-card-heading="true"]')
        price_elements = element.find_elements(By.XPATH, "//div[contains(@class,'ProductPrice_container__CkWjL')]")

        print("Number of name elements found:", len(name_elements))
        print("Number of price elements found:", len(price_elements))

        # Extract text from the name, price, and quantity elements
        for name_element, price_element in zip(name_elements, price_elements):
            product_name = name_element.text.strip()
            product_price = price_element.text.strip()


            # Add the name, price, and quantity to the product_data list as a dictionary
            product3_data.append({
                "name": product_name,
                "price": product_price,
                "Category": "beer"

            })
    time.sleep(5)

# Convert product3_data list to DataFrame and print
product3_data_df = pd.DataFrame(product3_data)
print("product3_data DataFrame:")
print(product3_data_df)
time.sleep(5)
time.sleep(3)
up = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/main/section[5]')))
driver.execute_script("arguments[0].scrollIntoView();", up)
time.sleep(3)
button_xpath = '//*[@id="desktop-store-filter-panel--0"]/ul/li[3]'  # Replace with your button's XPath
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))

# Click the button
button.click()
time.sleep(5)
scot = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/main/section[5]')))
driver.execute_script("arguments[0].scrollIntoView();", scot)
time.sleep(3)

cat_xpath = '//*[@id="desktop-store-filter-panel--0"]/ul/li[4]'  # Replace with your button's XPath
wait = WebDriverWait(driver, 10)
catbutton = wait.until(EC.element_to_be_clickable((By.XPATH, cat_xpath)))

# Click the button
catbutton.click()
time.sleep(3)
filter = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[6]/div/div[1]/div[2]/button')
filter.click()
time.sleep(5)
urls = [ "https://www.exito.com/vinos-y-licores?category-2=cigarrillos-y-vapeadores&category-1=vinos-y-licores&facets=category-2%2Ccategory-1&sort=score_desc&page=0",
         "https://www.exito.com/vinos-y-licores?category-2=cigarrillos-y-vapeadores&category-1=vinos-y-licores&facets=category-2%2Ccategory-1&sort=score_desc&page=1",
         "https://www.exito.com/vinos-y-licores?category-2=cigarrillos-y-vapeadores&category-1=vinos-y-licores&facets=category-2%2Ccategory-1&sort=score_desc&page=2"
         ]



product4_data = []  # Changed variable name to product2_data
for url in urls:
    # Navigate to the page
    driver.get(url)

    # Find all elements containing product name, price, and quantity
    product_elements = driver.find_elements(By.XPATH, '//*[@id="__next"]/main/section[6]/div/div[2]/div[2]/div[2]')

    print("Number of product elements found:", len(product_elements))

    # Iterate over the found elements and collect data
    for element in product_elements:
        # Find the product name, price, and quantity elements within the product element
        name_elements = element.find_elements(By.XPATH, '//div[@data-fs-product-card-heading="true"]')
        price_elements = element.find_elements(By.XPATH, "//div[contains(@class,'ProductPrice_container__CkWjL')]")

        print("Number of name elements found:", len(name_elements))
        print("Number of price elements found:", len(price_elements))

        # Extract text from the name, price, and quantity elements
        for name_element, price_element in zip(name_elements, price_elements):
            product_name = name_element.text.strip()
            product_price = price_element.text.strip()


            # Add the name, price, and quantity to the product_data list as a dictionary
            product4_data.append({
                "name": product_name,
                "price": product_price,
                "Category": "vape"

            })
    product4_data_df = pd.DataFrame(product4_data)
    print("product4_data DataFrame:")
    print(product4_data_df)
    time.sleep(5)
all_product_data = product_data + product3_data + product4_data

# Convert the combined product data list to a DataFrame
all_product_data_df = pd.DataFrame(all_product_data)

# Select only the 'name' and 'price' columns
all_product_data_df = all_product_data_df[['name', 'price', 'Category']]

# Rename the columns to match the desired names
all_product_data_df.rename(columns={'name': 'Product Name', 'price': 'Regular Price'}, inplace=True)

# Save the DataFrame to a CSV file
all_product_data_df.to_csv("all_product_data2.csv", index=False)
df = pd.read_csv("all_product_data2.csv")

# Display the DataFrame
print(df)