from ..base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminLoginPage(BasePage):
    element_dict = {
        "邮箱": (By.ID, "email-input"),
        "密码": (By.ID, "password-input"),
        "登录": (By.XPATH, '//button[@type="submit"]')
    }

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.get("http://beikeshop.test/admin")
        self.wait = WebDriverWait(self.driver, 5, 0.3)

    def login(self, email, password):
        self.input_text(self.element_dict["邮箱"], email)
        self.input_text(self.element_dict["密码"], password)
        self.click(self.element_dict["登录"])



if __name__ == '__main__':
    pass
