import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GithubTestCase(unittest.TestCase):
    def setUp(self):
        # self.browser = webdriver.Chrome()
        self.browser = webdriver.Remote(
            command_executor='http://localhost:4444',
            options=webdriver.ChromeOptions()
        )
        self.addCleanup(self.browser.quit)

    def test_search(self):
        # 打开 GitHub 首页
        self.browser.get('https://www.baidu.com/')
        time.sleep(10)

        # 在搜索框键入关键字 Selenium，并回车
        search_box_elem = self.browser.find_element(By.XPATH, '//input[@name="q"]')
        search_box_elem.send_keys('Selenium' + Keys.RETURN)

        # 点击第一个搜索结果
        first_result_elem = self.browser.find_element(By.XPATH, '//ul[@class="repo-list"]/li//div[@class="d-flex"]//a')
        first_result_elem.click()

        # 等待 Code Tab 页出现，即仓库首页打开
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, 'code-tab')))

        # 断言仓库首页标题包含 Selenium
        self.assertIn('Selenium', self.browser.title)


if '__main__' == __name__:
    unittest.main(verbosity=2)