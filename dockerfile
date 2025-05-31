# 使用带浏览器的基础镜像
FROM selenium/standalone-chrome:4.11.0

# 切换到 root 用户安装依赖
USER root

# 安装 Python 和 Git
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    && rm -rf /var/lib/apt/lists/*

# 设置工作目录
WORKDIR /app

# 克隆项目
RUN git clone https://github.com/caogang530/selenium_test.git . \
    && git checkout 48b8c5ebd78ba50eda6f09012e40c36b2ad35336

# 安装 Python 依赖
RUN pip3 install --no-cache-dir -r requirements.txt

# 切换回非 root 用户
USER 1200

# 设置执行命令
CMD ["python3", "run.py"]