import argparse
from tulipService import TulipService
import csv
import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import pandas as pd

class BotLogic:
    def __init__(self):
        parser = argparse.ArgumentParser(description='Get working dir.')
        parser.add_argument('--working_dir', type=str, help='Enter working dir path')
        args = parser.parse_args()
        self.bot_input = TulipService.BotInputs(working_dir=args.working_dir)
        self.bot_output = TulipService.BotOutputs(working_dir=args.working_dir)
        self.log = TulipService.Log(logger_name=self.__class__.__name__,
                                    log_dir="C:\\Users\\ASUS\\PycharmProjects\\py_bot\\py-bot\\pylog",
                                    archive_dir="C:\\Users\\ASUS\\PycharmProjects\\py_bot\\py-bot\\pylog\\archives"
                                    )
        self.log.message(f"\"{self.__class__.__name__}\" Bot started")

    def crawler(self):
        driver1 = self.bot_input.get_inputs(key="WebsiteURL")

        def scrap_product_details(product_list, price_list):
            # self.bot_input.get_value(key="WebsiteURL")

            product_elements = driver.find_elements(By.XPATH, "//span[@class='R6Z9B _4YY8f MUapD yY7uJ _8VJGH YVomU']")
            for element in product_elements:
                product_name = element.text.strip()
                product_list.append(product_name)
                print(element.text)

            price_ele = driver.find_elements(By.XPATH, "//div[@class='-OX0o']")
            # regex= "[€\d+.\d+]"
            pattern = r'Current price:\n(.*)'
            for price in price_ele:
                # print(price.text)
                match = re.search(pattern, price.text)
                # print(match)
                if match:
                    current_price = match.group(1)
                    print(current_price)
                    # price_val = match.text.replace("Current price:\n","")
                    # price_val1 = price_val.replace("Price from:\n[€\d+.\d+]","")
                    price_list.append(current_price)

        driver = webdriver.Chrome()  # WebsiteURL
        driver.get(driver1)
        time.sleep(1)
        driver.maximize_window()
        time.sleep(2)
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(3)
        actions = ActionChains(driver)
        button = driver.find_element(By.XPATH, "/html/body/header/div[2]/div[2]/div/div/div[2]/div/button")

        button.click()
        actions.double_click(button).perform()
        time.sleep(3)
        cookies = driver.find_element(By.XPATH, "//span[contains(text(),'Yes, I accept all cookies')]")
        cookies.click()
        time.sleep(2)

        # button_text = button.text
        drinks_food = driver.find_element(By.XPATH, "(//div[@class='wpU6u'])[6]")
        drinks_food.click()
        time.sleep(3)
        # drinks_food1 =[]
        drinks = driver.find_element(By.XPATH, "//button[text()='Drinks']")
        drinks.click()
        time.sleep(2)

        product_list = []
        price_list = []
        scrap_product_details(product_list, price_list)

        self.log.message(price_list)
        # print(product_list)
        # print(len(price_list))
        # print(len(product_list))

        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(3)
        drink_food_page2 = driver.find_element(By.XPATH, "//button[@class='BaRFD']")
        drink_food_page2.click()
        time.sleep(4)
        scrap_product_details(product_list, price_list)
        df = pd.DataFrame({"Product Titles": product_list, "Price": price_list})
        csv_file_path = "product_details.csv"
        df.to_csv(csv_file_path, index=False)
        self.bot_output.add_input(key="file", value=csv_file_path)
        self.bot_output.add_input(key="name", value="jeeva")

def main(self):
    try:
        self.crawler()
        self.log.success(message="huraa")
    except Exception as e:
        self.log.error(message=str(e))

if __name__ == "__main__":
    _BotLogic = BotLogic()
    _BotLogic.main()