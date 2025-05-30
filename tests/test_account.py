import pytest
import time
import allure
from _pytest.config import Config
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.user_engine import UserEngine
from pages.admin_engine import AdminEngine
from check.check import Check


@allure.feature("登录功能")
@pytest.mark.usefixtures("get_driver")
class TestLogin:

    @pytest.mark.parametrize("email, password",[
        ("test1@mail.com", 123456),
        # ("test2@mail.com", 123456),
        # ("test3@mail.com", 123456)
    ])
    @allure.story("用户登录成功")
    def test_register_acount1(self, get_driver, email, password):
        # 注册账号
        user = UserEngine(get_driver)
        user.register_account(email, password)

        # 断言 注册成功
        Check(get_driver).check_element_exists((By.LINK_TEXT, "退出登录"), True)

        # 清理注册的账号
        admin = AdminEngine(get_driver)
        admin.login()
        admin.delete_customer(email)
        time.sleep(1)

        # 断言后台清理注册账号成功
        Check(get_driver).check_element_exists((By.XPATH, f'//td[text()="{email}"]'), False)

    # @pytest.mark.parametrize("email, password",[
    #     ("test4@mail.com", 123456),
    #     ("test5@mail.com", 123456),
    #     ("test6@mail.com", 123456)
    # ])
    # @allure.story("用户登录成功")
    # def test_register_acount2(self, get_driver, email, password):
    #     # 注册账号
    #     user = UserEngine(get_driver)
    #     user.register_account(email, password)
    #
    #     # 断言 注册成功
    #     Check(get_driver).check_element_exists((By.LINK_TEXT, "退出登录"), True)
    #
    #     # 清理注册的账号
    #     admin = AdminEngine(get_driver)
    #     admin.login()
    #     admin.delete_customer(email)
    #     time.sleep(1)
    #
    #     # 断言后台清理注册账号成功
    #     Check(get_driver).check_element_exists((By.XPATH, f'//td[text()="{email}"]'), False)
    #
    # @pytest.mark.run(order=1)
    # @pytest.mark.parametrize("email, password",[
    #     ("test7@mail.com", 123456),
    #     ("test8@mail.com", 123456),
    #     ("test9@mail.com", 123456)
    # ])
    # @allure.story("用户登录成功")
    # def test_register_acount3(self, get_driver, email, password):
    #     # 注册账号
    #     user = UserEngine(get_driver)
    #     user.register_account(email, password)
    #
    #     # 断言 注册成功
    #     Check(get_driver).check_element_exists((By.LINK_TEXT, "退出登录"), True)
    #
    #     # 清理注册的账号
    #     admin = AdminEngine(get_driver)
    #     admin.login()
    #     admin.delete_customer(email)
    #     time.sleep(1)
    #
    #     # 断言后台清理注册账号成功
    #     Check(get_driver).check_element_exists((By.XPATH, f'//td[text()="{email}"]'), False)
    #
    # @pytest.mark.parametrize("email, password",[
    #     ("test10@mail.com", 123456),
    #     ("test11@mail.com", 123456),
    #     ("test12@mail.com", 123456)
    # ])
    # @allure.story("用户登录成功")
    # def test_register_acount4(self, get_driver, email, password):
    #     # 注册账号
    #     user = UserEngine(get_driver)
    #     user.register_account(email, password)
    #
    #     # 断言 注册成功
    #     Check(get_driver).check_element_exists((By.LINK_TEXT, "退出登录"), True)
    #
    #     # 清理注册的账号
    #     admin = AdminEngine(get_driver)
    #     admin.login()
    #     admin.delete_customer(email)
    #     time.sleep(1)
    #
    #     # 断言后台清理注册账号成功
    #     Check(get_driver).check_element_exists((By.XPATH, f'//td[text()="{email}"]'), False)

if __name__ == '__main__':
    pytest.main(['-sv', __file__, '-n', '4'])