import time
from time import sleep

from pages.auth_page import AuthPage
from pages.home_page import HomePage
from pages.lessons_page import LessonsPage

def test_auth_chrome(driver_chrome):
    driver_chrome.get("https://my.proweb.uz/log-in?q=/home")
    auth_page = AuthPage(driver_chrome)
    auth_page.enter_login("998903084927")
    time.sleep(2)
    auth_page.click_btn_login()
    time.sleep(2)
    auth_page.enter_password("Mashaalah")
    time.sleep(2)
    auth_page.click_btn_password()
    time.sleep(2)
    try:
        auth_page.click_btn_session()
        time.sleep(2)
        auth_page.click_btn_finish()
        time.sleep(2)
    except:
        pass


    home_page = HomePage(driver_chrome)
    home_page.click_video_instruction()
    time.sleep(2)
    home_page.click_fullscreen_btn()
    time.sleep(10)
    home_page.click_pause()
    time.sleep(2)
    home_page.click_fullscreen_exit()
    time.sleep(2)
    home_page.click_main_btn()
    time.sleep(2)
    home_page.click_group_card()
    time.sleep(2)

    lessons_page = LessonsPage(driver_chrome)
    lessons_page.click_lessons_btn()
    time.sleep(2)
    lessons_page.click_last_card()
    time.sleep(2)
    lessons_page.click_fullscreen_btn()
    time.sleep(2)
    lessons_page.click_play_btn()
    time.sleep(10)
    lessons_page.click_pause()
    time.sleep(2)
    lessons_page.click_fullscreen_exit()
    time.sleep(2)


    home_page.click_profile_icon()
    time.sleep(2)
    home_page.click_exit_btn()
    time.sleep(2)
    home_page.click_confirm_exit()
    time.sleep(2)




