import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from utils.config_reader import ConfigReader
config = ConfigReader().get_config()



class DriverManager:
    driver = None

    @classmethod
    def get_driver(cls):
        if not cls.driver:
            browser = config["webdriver"]["browser"]  # 这里可以根据需要设置浏览器类型，也可以从配置文件读取
            cls.driver = cls.create_driver(browser)
        return cls.driver

    @classmethod
    def create_driver(cls, browser):
        if browser.lower() == "chrome":
            return cls.create_chrome_driver()
        elif browser.lower() == "firefox":
            return cls.create_firefox_driver()

    @classmethod
    def create_chrome_driver(cls):
        options = Options()
        is_headless = config["webdriver"]["headless"].lower() == "true"
        print('is_headless', is_headless)
        if is_headless:
            # 配置无头浏览器
            options = Options()
            options.add_argument("--headless=new")  # 新版 headless 模式
            options.add_argument("--window-size=1920,1080")  # 设置窗口大小
            options.add_argument("--disable-gpu")  # 禁用 GPU 加速（旧系统可能需要）
            options.add_argument(
                "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)

        # current_dir = os.path.dirname(os.path.abspath(__file__))
        # project_root = os.path.dirname(current_dir)  # utils的上级目录是项目根目录
        # config_file = os.path.join(project_root, 'resources', 'browser_drivers', 'chromedriver.exe')
        # service = Service(executable_path=config_file)
        return webdriver.Chrome(options=options)

    @classmethod
    def create_firefox_driver(cls):
        # 在这里添加创建 Firefox WebDriver 的逻辑
        pass

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None
