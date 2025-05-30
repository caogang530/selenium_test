import time

from pages.admin_page.admin_login_page import AdminLoginPage
from pages.admin_page.admin_home_page import AdminHomePage
from utils.config_reader import ConfigReader
config = ConfigReader().get_config()



class AdminEngine:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        email = config["admin"]["email"]
        password = config["admin"]["password"]
        admin_login_page = AdminLoginPage(self.driver)
        admin_login_page.login(email, password)

    def delete_customer(self, email):
        admin_home_page = AdminHomePage(self.driver)
        admin_home_page.click_customer()
        admin_home_page.click_customer_list()
        admin_home_page.delete_customer_in_customer_list(email)
        time.sleep(1)
        admin_home_page.click_recycle_bin()
        admin_home_page.delete_customer_in_recycle_bin(email)



