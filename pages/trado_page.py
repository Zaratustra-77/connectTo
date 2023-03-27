from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TradoPage:

    def __init__(self, driver):
        self.driver = driver

        # Replace this with the path to your web driver (e.g., ChromeDriver, FirefoxDriver, etc.)

        # Initialize the browser (e.g., Chrome, Firefox)
    def click_Off(self):
        xp = '//*[@id="root"]/div/div[4]/div/div/div/button'
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xp))).click()


    def get_item_list(self):
        listOf = []
        # Locate the list container using the XPath
        list_container_xpath = '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]'
        list_container = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, list_container_xpath))
        )
        print(type(list_container))
        # # Find all the list items in the container using the <a> tag
        # list_items = list_container.find_elements_by_tag_name("a")
        #
        # # Loop through the list items and access their attributes or text
        # for item in list_items:
        #     listOf.append(item.get_attribute("href"))
        #     # print(item.text)  # Access the text content of the list item
        #     # print(item.get_attribute("href"))  # Access the href attribute of the list item
        # return listOf
        # Close the browser
