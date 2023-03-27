import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.trado_page import TradoPage


class WebDriverSetup(unittest.TestCase):
    def setUp(self) -> None:
        try:
            chromedriver_path = "C:/Webdriver/chromedriver.exe"
            service = Service(executable_path=chromedriver_path)
            options = Options()
            options.headless = False
            # options = webdriver.ChromeOptions()
            options.add_argument("--disable-extensions")
            self.driver = webdriver.Chrome(service=service, options=options)
            self.driver.maximize_window()
            self.driver.set_page_load_timeout(30)
            self.driver.get("https://qa.trado.co.il/?&sort={%22price%22:1}")
            self.trado_page = TradoPage(self.driver)
            self.trado_page.click_Off()
            time.sleep(5)


        except AssertionError:
            self.driver.quit()

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='C:/Users/Elik/PycharmProjects/seleniumProjects/POM_Orange/reports'))
