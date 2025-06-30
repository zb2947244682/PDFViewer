# 基于官方Python镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 安装系统依赖
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libglib2.0-0 \
        libnss3 \
        libgdk-pixbuf2.0-0 \
        libgtk-3-0 \
        libx11-xcb1 \
        libxcomposite1 \
        libxdamage1 \
        libxrandr2 \
        libasound2 \
        libatk1.0-0 \
        libcups2 \
        libdbus-1-3 \
        libdrm2 \
        libgbm1 \
        libnspr4 \
        libpango-1.0-0 \
        libxshmfence1 \
        fonts-wqy-zenhei \
        wget \
        && rm -rf /var/lib/apt/lists/*

# 复制依赖文件并安装Python依赖
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 安装playwright浏览器
RUN python -m playwright install --with-deps chromium

# 复制项目文件
COPY . .

# 暴露端口
EXPOSE 5000

# 启动服务
CMD ["python", "app.py"] 