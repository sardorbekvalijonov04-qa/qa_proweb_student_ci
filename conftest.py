import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver_chrome():
    chrome_options = Options()

    # Если код запущен в GitHub Actions — включаем headless
    if os.environ.get("GITHUB_ACTIONS"):
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")
    else:
        # Локальный запуск (PyCharm) — браузер с окном
        chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)

    yield driver

    driver.quit()

# import pytest
# from selenium import webdriver

# @pytest.fixture
# def driver_chrome():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()
