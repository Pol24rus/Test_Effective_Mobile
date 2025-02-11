from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://effective-mobile.ru/"

    def open(self):
        self.driver.get(self.url)

    def click_about_us(self):
        # self.driver.find_element(By.XPATH, "//a[contains(text(), 'О нас ')]").click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(text(), 'О нас ')]"))).click()

    def click_services(self):
        # self.driver.find_element(By.XPATH, "//a[contains(text(), 'Услуги ')]").click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(text(), 'Услуги ')]"))).click()

    def click_projects(self):
        # self.driver.find_element(By.XPATH, "//a[contains(text(), 'Проекты ')]").click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(text(), 'Проекты ')]"))).click()

    def click_reviews(self):
        # self.driver.find_element(By.XPATH, "//a[contains(text(), 'Отзывы ')]").click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(text(), 'Отзывы ')]"))).click()

    def click_contacts(self):
        # self.driver.find_element(By.XPATH, "//a[contains(text(), 'Контакты ')] ").click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(text(), 'Контакты ')]"))).click()

    def get_current_url(self):
        return self.driver.current_url
