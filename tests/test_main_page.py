import pytest
from Python_Selenium.Test.pages.main_page import MainPage


@pytest.mark.parametrize("link_text, expected_url", [
    ("О нас ", "https://effective-mobile.ru/#about"),
    ("Услуги ", "https://effective-mobile.ru/#moreinfo"),
    ("Проекты ", "https://effective-mobile.ru/#cases"),
    ("Отзывы ", "https://effective-mobile.ru/#Reviews"),
    ("Контакты ", "https://effective-mobile.ru/#contacts"),
])

# @pytest.fixture(scope="module")
# @pytest.fixture(scope="function")
# def browser():
#     # Инициализация драйвера
#     driver = webdriver.Chrome()
#     # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     yield driver
#     # Закрытие браузера после завершения тестов
#     driver.quit()


def test_navigation_links(browser, link_text, expected_url):
    # Открываем главную страницу
    main_page = MainPage(browser)
    main_page.open()

    # Кликаем по ссылке
    if link_text == "О нас ":
        main_page.click_about_us()
    elif link_text == "Услуги ":
        main_page.click_services()
    elif link_text == "Проекты ":
        main_page.click_projects()
    elif link_text == "Отзывы ":
        main_page.click_reviews()
    elif link_text == "Контакты ":
        main_page.click_contacts()

    # Проверяем URL после перехода
    assert main_page.get_current_url() == expected_url, f"Ожидаемый URL: {expected_url}, Фактический URL: {main_page.get_current_url()}"
