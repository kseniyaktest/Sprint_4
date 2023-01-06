import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def get_driver():
    driver = webdriver.Firefox(r"C:\Users\Aquafresh\WebDriver\bin")
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.close()




