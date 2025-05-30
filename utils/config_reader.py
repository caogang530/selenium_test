import configparser
import os

class ConfigReader:
    def __init__(self, config_file=None):
        self.config_reader = configparser.ConfigParser()
        # 修复路径：基于项目根目录定位配置文件
        if not config_file:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            project_root = os.path.dirname(current_dir)  # utils的上级目录是项目根目录
            config_file = os.path.join(project_root, 'config', 'config.ini')

        self.config_file = config_file
        self.config = {}
        self.parser_config()

    def parser_config(self):
        try:
            self.config_reader.read(self.config_file)
            # 遍历配置信息
            for section in self.config_reader.sections():  # 获取所有节
                print(f"Section: {section}")
                for option in self.config_reader.options(section):  # 获取每个节中的选项
                    value = self.config_reader.get(section, option)  # 获取选项的值
                    if section not in self.config:
                        self.config[section] = {}
                    self.config[section][option] = value
            print("全部配置：", self.config)
        except Exception as e:
            raise Exception(f"Error reading config file '{self.config_file}': {e}")

    def get_config(self):
        return self.config