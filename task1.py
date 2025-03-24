from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://nexign.com/ru")

products_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//li[contains(@class, 'menu-item--expanded') and .//span[text()='Продукты и решения']]")
    )
)
products_menu.click()

products_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//li[contains(@class, 'menu-item menu-item--expanded menu-double-column') and .//span[text()='Инструменты для ИТ-команд']]")
    )
)
products_menu.click()

nord_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//li[contains(@class, 'menu-item')]//a[normalize-space()='Nexign Nord']")
    )
)
nord_link.click()