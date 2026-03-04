from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.video_instruction = (By.CSS_SELECTOR, "#app > div > div.home-content > div > div > div > div > div.home__education > div.home__education-page > div > div.home-card.pointer")
        self.pause = (By.CSS_SELECTOR, "#app > div > div.home-instruction > div > div.home-instruction__content-main > div > div > video")
        self.main_btn = (By.CSS_SELECTOR, "#app > div > div.layout > div > div.material-dialog__window > div > ul > li:nth-child(1) > div")
        self.group_card = (By.CSS_SELECTOR, "#app > div > div.home-content > div > div > div > div > div.home__education > div.home__education-page > div > div:nth-child(2)")



    def click_video_instruction(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.video_instruction)).click()

    def click_pause(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.pause))
        ActionChains(self.driver).double_click(element).perform()

    def click_pause_exit(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.pause))
        ActionChains(self.driver).double_click(element).perform()

    def click_main_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.main_btn)).click()

    def click_group_card(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.group_card)).click()


