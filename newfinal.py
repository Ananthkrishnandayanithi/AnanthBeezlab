import csv
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
driver.get("https://www.aeliadutyfree.co.nz/auckland/")
time.sleep(3)

# Maximize the window
driver.maximize_window()
time.sleep(3)

# Handling cookies
cookie = driver.find_element(By.XPATH, '//*[@id="html-body"]/div[4]/aside/div[2]/div[1]/i')
cookie.click()
time.sleep(3)

cookie = driver.find_element(By.XPATH, '//*[@id="btn-cookie-allow"]')
cookie.click()
time.sleep(3)

# Navigate to the spirits section
spirit = driver.find_element(By.XPATH, '//*[@id="html-body"]/div[3]/nav/ul/li[2]/a')
spirit.click()
time.sleep(3)

# Scroll to the toolbar amount
wait = WebDriverWait(driver, 10)
sco = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="toolbar-amount"]')))
driver.execute_script("arguments[0].scrollIntoView();", sco)
time.sleep(5)

# List to store product data
product_data = []

# XPath for the quantity of each product
quantity_xpath = ".//span[@class='product-item-quantity']"

# XPath for the next button
next_button_xpath = '(//*[@class="item pages-item-next"])[2]'

# Loop to scrape data from multiple pages
while True:
    # Find all elements containing product name, price, and quantity
    product_elements = driver.find_elements(By.XPATH, '//*[@id="maincontent"]/div/div[1]/div[5]/ol/li')
    print("Number of product elements found:", len(product_elements))

    # Iterate over the found elements and collect data
    for element in product_elements:
        # Find the product name, price, and quantity elements within the product element
        name_elements = element.find_elements(By.XPATH, ".//div[@class='product-item-brand']")
        price_elements = element.find_elements(By.XPATH, ".//span[@class='price']")
        quantity_element = element.find_element(By.XPATH, "//a[@class='product-item-link']")

        # Extract text from the name, price, and quantity elements
        for name_element, price_element in zip(name_elements, price_elements):
            product_name = name_element.text.strip()
            product_price = price_element.text.strip()
            product_quantity = re.search(r'(\d+\s*[a-zA-Z]+)', quantity_element.text.strip()).group(0)

            # Add the name, price, and quantity to the product_data list as a dictionary
            product_data.append({
                "Product": product_name,  # Changed column name to "Product"
                "Regular Price": product_price,  # Changed column name to "Regular Price"
                "Quantity": product_quantity  # No change in column name for quantity
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

# Close the WebDriver
driver.quit()

# Print the collected product data
for product in product_data:
    print("Name:", product["Product"], "Price:", product["Regular Price"], "Quantity:", product["Quantity"])

# Write the collected product data to a CSV file
csv_filename = "product_data.csv"
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Product", "Regular Price", "Quantity"])  # Changed column names here
    writer.writeheader()
    for product in product_data:
        writer.writerow(product)

print("Product data has been successfully saved to", csv_filename)

# Read the CSV file into a pandas DataFrame
data_df = pd.read_csv(csv_filename)
print(data_df)
