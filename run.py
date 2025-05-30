import os
import pytest
from datetime import datetime

# 获取当前时间
current_time = datetime.now()

# 将时间格式化为"年-月-日-时-分-秒"字符串
formatted_time = current_time.strftime("%Y-%m-%d_%H_%M_%S")

# 打印结果2024-01-07 16_36_24
print(formatted_time)

if __name__ == '__main__':
    pytest.main([
        '-sv',  # 执行过程的细节打印
        'tests/test_account.py::TestLogin',  # 执行的测试用力
        '-n 4',  # 多线程执行
        '-p pytest_ordering',
        '--alluredir=./allure-results/{}'.format(formatted_time),  # allure报告生成
        '--clean-alluredir',  # 如果allure报告的目录已存在则清除
        # '--base_url=http://baidu.com'
    ])
    # os.popen("allure serve ./allure-results/{}".format(formatted_time))
