from ..base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginRegisterPage(BasePage):
    element_dict = {
        '注册-邮箱': (By.XPATH, '//*[@class="card"][2]//*[@placeholder="邮箱地址"]'),
        '注册-密码': (By.XPATH, '//*[@class="card"][2]//*[@placeholder="密码"]'),
        '注册-确认密码': (By.XPATH, '//*[@class="card"][2]//*[@placeholder="确认密码"]'),
        '注册': (By.XPATH, '(//*[@class="btn btn-dark btn-lg w-100 fw-bold"])[2]'),
    }

    def __init__(self, driver):
        super().__init__(driver)

    def register(self, email, password):
        self.input_text(self.element_dict["注册-邮箱"], email)
        self.input_text(self.element_dict["注册-密码"], password)
        # self.input_text(element_dict["注册-确认密码"], password)
        self.click(self.element_dict["注册"])


if __name__ == '__main__':
    pass
