# coding=utf-8
"""

yaml封装后读取config/capbilty.yaml文件已写入数据
 logging参数输出info 以上级别的日志,指定文件地址输出,asctime =当前时间，filename=模块名称，lineno=行号，
 levelname = 日志等级名称，message=日志信息

"""
from appium import webdriver
import yaml
import logging
import logging.config
import time
import os
from common.resd_yaml import readyml
from pathlib import Path

# 读取log.conf中的配置表
# file_path = Path.cwd()  # 获取当前文件路径
path = Path.cwd().parent  # 获取上一层路径
configpath = ["config", "log.conf"]
CON_LOG = path.joinpath(*configpath)  # 拼接路径
# print(CON_LOG)
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()
# yamlpath
a = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
capbilly_path = os.path.join(a, "config", "capbillty.yaml")

# print(capbilly_path)
# readyml(capbilly_path)


def youstar_desired_conf():
    data = readyml(capbilly_path)
    desired_caps = {'platformName': data['platformName'], 'platformVersion': data['platformVersion'],
                    'deviceName': data['deviceName'], 'udid': data['udid'], 'noReset': data['noReset'],
                    'unicodeKeyboard': data['unicodeKeyboard'], 'resetKeyboard': data['resetKeyboard'],
                    'appPackage': data['appPackage'], 'appActivity': data['appActivity']}
    # base_dir = os.path.dirname(os.path.dirname(__file__))
    # app_path = os.path.join(base_dir, "app", data['appPackage'])
    # desired_caps['app'] = app_path         电脑数据包安装需要读取APK路径本地安装了就不需要

    logging.info("....Start App.....")
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
    logging.info("自动化配置参数：{}".format(desired_caps))
    driver.implicitly_wait(8)
    # driver.find_element_by_id("")
    return driver


if __name__ == '__main__':
    youstar_desired_conf()
# 获取到当前APP模块的存放的APP路径，从电脑安装APP的路径时需要使用到的方法，手机本地已安装的不用使用到下面读取方法
# with open(r"D:\codetest\kyb_testproject\config\capbillty.yaml", 'r', encoding="UTF-8") as file:
#     data = yaml.load(file)
# base_dir = os.path.dirname(os.path.dirname(__file__))
# print(os.path.dirname(__file__))
# print(base_dir)
# app_path = os.path.join(base_dir,"app", data['appPackage'])
# print(app_path)
