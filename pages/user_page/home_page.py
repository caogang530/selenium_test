from ..base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element_dict = {
    "登录注册图标": (By.XPATH, '//*[@class="navbar-nav flex-row"]//*[@class="nav-item dropdown"]'),
    "登录注册链接": (By.LINK_TEXT, "登录/注册")
}


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.switch_to_cn()

    def go_to_login_register(self):
        user_icon = self.driver.find_element(*element_dict["登录注册图标"])
        # user_icon = self.wait.until(EC.visibility_of_element_located(element_dict["登录注册图标"]))
        ActionChains(self.driver).move_to_element(user_icon).perform()
        # self.driver.find_element(*element_dict["登录注册链接"]).click()
        self.wait.until(EC.visibility_of_element_located(element_dict["登录注册链接"])).click()


if __name__ == '__main__':
    pass
