from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    login_link = (By.LINK_TEXT, "Signup / Login")
    username = (By.NAME, "email")
    password = (By.NAME, "password")
    login_btn = (By.XPATH, "//button[text()='Login']")
    logout_btn = (By.LINK_TEXT, "Logout")

    def __init__(self, driver):
        self.driver = driver

    def open_login(self):
        self.driver.find_element(*self.login_link).click()

    def enter_email(self):
        self.driver.find_element(*self.username).send_keys("jagatest1@gmail.com")

    def enter_password(self):
        self.driver.find_element(*self.password).send_keys("Password123")

    def click_login(self):
        self.driver.find_element(*self.login_btn).click()

    def verify_login(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(self.verify_login_name))
        return element.is_displayed()