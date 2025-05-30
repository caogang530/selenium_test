from ..base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ele_dict = {
    "订单": (By.LINK_TEXT, "订单"),
    "商品": (By.LINK_TEXT, "商品"),
    # 客户模块下的元素
    "客户": (By.LINK_TEXT, "客户"),
    "客户管理": (By.LINK_TEXT, "客户管理"),
    "客户组": (By.LINK_TEXT, "客户组"),
    "回收站": (By.LINK_TEXT, "回收站"),

    "确定": (By.XPATH, '//div[@class="el-message-box"]/div[@class="el-message-box__btns"]/button[@class="el-button el-button--default el-button--small el-button--primary "]'),
    "取消": (By.XPATH, '//div[@class="el-message-box"]/div[@class="el-message-box__btns"]/button[@class="el-button el-button--default el-button--small"]'),

    "文章": (By.LINK_TEXT, "文章"),
    "设计": (By.LINK_TEXT, "设计"),
    "插件": (By.LINK_TEXT, "插件"),
    "系统": (By.LINK_TEXT, "系统")
}


class AdminHomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5, 0.3)

    def click_customer(self):
        self.wait.until(EC.visibility_of_element_located(ele_dict['客户'])).click()

    def click_customer_list(self):
        self.wait.until(EC.visibility_of_element_located(ele_dict['客户管理'])).click()

    def click_recycle_bin(self):
        self.wait.until(EC.visibility_of_element_located(ele_dict['回收站'])).click()

    def delete_customer_in_customer_list(self, email):
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, f'//tbody/tr/td[text()="{email}"]/following-sibling::td[button]/button')
        )).click()
        self.wait.until(EC.visibility_of_element_located(ele_dict['确定'])).click()

    def delete_customer_in_recycle_bin(self, email):
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             f'//tr[td[text()="{email}"]]/td[last()]/button[@class="btn btn-outline-danger btn-sm ml-1"]')
        )).click()
        self.wait.until(EC.visibility_of_element_located(ele_dict['确定'])).click()


if __name__ == '__main__':
    pass
