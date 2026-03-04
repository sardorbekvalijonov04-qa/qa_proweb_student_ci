from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

class LessonsPage:
    def __init__(self, driver):
        self.driver = driver
        self.nav_lesson = (By.CSS_SELECTOR, "#tabbar > div > div.tab-header > div.tab-header__wrapper > div:nth-child(2)")
        self.last_lesson = (By.CSS_SELECTOR, "#app > div > div.container.container_mobile > div > div > div.new-lessons_content > div > div:nth-child(5) > div.flex.gap20 > div:nth-child(7) > div.lesson-card > div")
        self.last_video_play = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(3) > div.video-player-proweb > div > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-left > button")
        self.last_video_fullscreen = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(3) > div.video-player-proweb > div > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-right > button.baseicon.baseavatar_fullscreen")
        # self.last_video_stop = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(3) > div.video-player-proweb > div > video")
        # self.last_video_fullscreen_exit = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(3) > div.video-player-proweb > div > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-right > button.baseicon.baseavatar_fullscreen-exit")
        self.last_pause = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(3) > div.video-player-proweb > div > video")
        self.profile_icon = (By.CSS_SELECTOR, "#app > div > div.header > div > div.header__avatar > div")
        self.exit_btn = (By.CSS_SELECTOR, "#app > div > div.inforation > div > div > div:nth-child(5) > div")
        self.confirm_exit = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-actions > button:nth-child(2)")


    def click_nav_lesson(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.nav_lesson)).click()

    def click_last_lesson(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.last_lesson)).click()

    def click_last_video_play(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.last_video_play)).click()

    def click_last_video_fullscreen(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.last_video_fullscreen)).click()

    # def click_last_video_stop(self):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(EC.element_to_be_clickable(self.last_video_stop)).click()

    def click_last_pause(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.last_pause))
        ActionChains(self.driver).double_click(element).perform()
    # def click_last_video_fullscreen_exit(self):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(EC.element_to_be_clickable(self.last_video_fullscreen_exit))


    def click_profile_icon(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.profile_icon)).click()

    def click_exit_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.exit_btn)).click()

    def click_confirm_exit(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.confirm_exit)).click()

