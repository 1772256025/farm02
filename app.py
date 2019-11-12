"""
    框架搭建:
        核心: api + case + data
            |-- api: 封装请求业务(requests)
            |-- case: 集成 unittest 实现, 调用 api 以及参数化解析 data
            |-- data: 封装测试数据
        报告: report + tools + run_suite.py
            |-- report: 保存测试报告
            |-- tools: 封装工具文件
            |-- run_suite.py: 组织测试套件
        配置: app.py
            |-- app.py：封装程序常量以及配置信息
        日志: log
            |-- log: 保存日志文件
"""

import os
import logging
import logging.handlers

# 封装接口的 URL 前缀


BASE_URL = "http://182.92.81.159"

# 封装项目路径
FILE_PATH = os.path.abspath(__file__)
PRO_PATH = os.path.dirname(FILE_PATH)

# 代码简化 -- 变体
# PRO_PATH1 = os.path.dirname(os.path.abspath(__file__))
# PRO_PATH2 = os.getcwd()
# print("动态获取的项目绝对路径:",PRO_PATH)
# print("动态获取的项目绝对路径:",PRO_PATH1)
# print("动态获取的项目绝对路径:",PRO_PATH2)

# 定义一个变量
TOKEN = None
USER_ID = None
# 日志模块实现
def my_log_config():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    to_1 = logging.StreamHandler()
    to_2 = logging.handlers.TimedRotatingFileHandler(PRO_PATH+"log/mylog.log",
                                                     when="h",
                                                     interval=12,
                                                     backupCount=14,
                                                     encoding="utf_8")
    formatter = logging.Formatter("%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%funcName)s:%(lineno)d]-")
    to_1.setFormatter(formatter)
    to_2.setFormatter(formatter)
    logger.addHandler(to_1)
    logger.addHandler(to_2)


