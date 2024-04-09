# 百度贴吧爬虫

    这是一个基于 Python 的百度贴吧爬虫，用于获取指定关键词的贴吧帖子信息并存储到 CSV 文件中。

## 项目结构

- 🚀 `tieba.py`：主要的爬虫脚本，用于爬取贴吧帖子信息。
- 🎂 `config.py`：配置文件，用于设置搜索关键词、爬取起始页数和终点页数。
- 🔗 `requirements.txt`：依赖的 Python 包列表。
- 📦 `data/{吧名}.csv`：存储爬取到的数据。
- 📩 `logs/{吧名}.log`：存储爬取过程中的日志信息。

## 使用方法

- 1.⚡安装依赖：

    ```bash
    pip install -r requirements.txt
    ```

- 2.🌊配置参数：

    在 config.py 中设置需要爬取的贴吧关键词 KW、爬取起始页数 ST 和终点页数 PN。
    
- 3.🚄运行脚本：

    ```bash
    python tieba.py
    ```

    脚本会开始爬取贴吧帖子信息，并将结果存储到 CSV 文件中。

- 4.🌈功能特点：

    * ✅ 使用了 fake_useragent 库生成随机 User-Agent，增加了爬虫的隐蔽性。
    * ✅ 使用了 rich 库提供的进度条功能，使爬取过程更加可视化。
    * ✅ 支持设置爬取的起始页数和终点页数，灵活控制爬取范围。
    * ✅ 使用了多个账号的cookie构建cookie池，提高反爬能力，增加数据获取的健壮性。
    
- 5.🚩注意事项：

    * 🚧爬取过程中请遵守网站的规则，不要过于频繁地进行请求，以免被封禁 IP。
    * 🚥请勿将爬取到的数据用于违法或商业用途，仅限个人学习和研究使用。