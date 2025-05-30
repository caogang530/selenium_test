import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    element_dict = {
    }
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5, 0.3)


    def switch_to_cn(self):
        time.sleep(2)
        language = self.driver.find_element(By.ID, 'language-dropdown')
        print(f"Visible: {language.is_displayed()}, Enabled: {language.is_enabled()}")
        ActionChains(self.driver).move_to_element(language).perform()
        # self.driver.find_element(By.LINK_TEXT, "中文").click()
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "中文"))).click()
        # 验证窗口大小
        print(f"当前窗口尺寸: {self.driver.get_window_size()}")

        # 保存截图验证
        self.driver.save_screenshot("headless_screenshot.png")
        print("截图已保存为 headless_screenshot.png")

    def input_text(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def click(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator)).click()


if __name__ == '__main__':
    pass
