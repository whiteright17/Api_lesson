from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class MySelenium:
    def __init__(self, browser_type="chrome"):
        self.browser_type = browser_type
        self.driver = self._get_driver()

    def _get_driver(self):
        if self.browser_type == "chrome":
            driver = webdriver.Chrome()
        elif self.browser_type == "firefox":
            driver = webdriver.Firefox()
        else:
            raise ValueError(f"Unsupported browser type: {self.browser_type}")
        return driver

    def get_page(self, url):
        self.driver.get(url)

    def search_box(self, my_text):
        wait_name = WebDriverWait(self.driver, 20)
        element = self.driver.find_element(By.ID, 'APjFqb')
        element.clear()
        element.send_keys(my_text)
        return element.clear

    def click_all_links_and_return(self):
        base_url = self.driver.current_url

        links = self.driver.find_elements(By.TAG_NAME, 'a')

        for link in links:
            ActionChains(self.driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
            WebDriverWait(self.driver, 5).until(EC.url_changes(base_url))
            self.driver.get(base_url)
        self.driver.get(base_url)

    def follow_links_and_return(self):
        base_url = self.driver.current_url
        base_window = self.driver.current_window_handle
        links = self.driver.find_elements(By.TAG_NAME, 'a')[:2]
        for link in links:
            ActionChains(self.driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
            WebDriverWait(self.driver, 10).until(lambda driver: len(driver.window_handles) >= 2)
            for window_handle in self.driver.window_handles:
                if window_handle != base_window:
                    self.driver.switch_to.window(window_handle)
                    WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
                    print(f"Current URL: {self.driver.current_url}")
                    self.driver.close()
                    break
            self.driver.switch_to.window(base_window)
        self.driver.get(base_url)
