import pytest
from selenium import webdriver


# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
# @pytest.fixture(scope="function")
def browser():
    # Инициализация драйвера
    driver = webdriver.Chrome()
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    # Закрытие браузера после завершения тестов
    driver.quit()
