"""
登录初始化操作，获取权限，跳过引导页等流程
"""
import logging
import os
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from youstar_baseview.youstar_baseview import BaseView
from common.Youstar_cadps import youstar_desired_conf
import csv


class Common(BaseView):
    aggregatebutton = (By.ID, "in.dradhanus.liveher:id/img_login_other")
    viplogin_button = (By.ID, "in.dradhanus.liveher:id/view_premium")
    checkin_button = (By.ID, "in.dradhanus.liveher:id/btn_check_in")
    checkinclose_button = (By.ID, "in.dradhanus.liveher:id/iv_close_old")

    # 应用初始化登录进入登录界面
    def __init__(self, driver):
        super().__init__(driver)
        self.new = time.strftime("%Y-%m-%d %H_%M_%S")

    def click_Collection(self):
        """点击集合入口"""
        self.click(self.aggregatebutton)

    def exception_error(self, element):
        """判断报错封装，作if判断"""
        try:
            self.findElement(element)
            return True
        except Exception as e:
            logging.exception(e)
            return False

    def click_checkbutton(self):
        """点击签到按钮"""
        self.click(self.checkin_button)

    def click_closecheckbutton(self):
        """点击关闭签到按钮"""
        self.click(self.checkinclose_button)

    def check_process(self):
        """签到流程"""
        try:
            self.findElement(self.checkin_button)
        except NoSuchElementException:
            logging.info("未找到签到弹窗")
        else:
            self.getScreenShot("签到弹窗")
            self.click(self.checkin_button)
            logging.info("完成签到奖励")
            time.sleep(1)
            self.getScreenShot("已完成签到")
            time.sleep(1)
            self.click(self.checkinclose_button)

    # 获取屏幕尺寸
    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    # 向左滑动
    def Swipe_left(self):
        logging.info("SwipeLeft")
        L = self.get_size()
        print(L)
        x1 = int(L[0] * 0.9)
        y1 = int(L[1] * 0.5)
        x2 = int(L[0] * 0.1)
        self.driver.swipe(x1, y1, x2, y1, 1000)

    # 向右滑动
    def Swipe_right(self):
        logging.info("SwipeRight")
        L = self.get_size()
        print(L)
        x1 = int(L[0] * 0.9)
        y1 = int(L[1] * 0.5)
        x2 = int(L[0] * 0.1)
        self.driver.swipe(x2, y1, x1, y1, 1000)

    # 向上滑动
    def Swipe_Up(self):
        logging.info(" SwipeUp")
        L = self.get_size()
        print(L)
        x1 = int(L[0] * 0.5)
        y1 = int(L[1] * 0.5)
        y2 = int(L[1] * 0.2)
        self.driver.swipe(x1, y1, x1, y2, 1000)

    # 向下滑动
    def Swipe_Down(self):
        logging.info(" SwipeDown")
        L = self.get_size()
        print(L)
        x1 = int(L[0] * 0.5)
        y1 = int(L[1] * 0.5)
        y2 = int(L[1] * 0.8)
        self.driver.swipe(x1, y1, x1, y2, 1000)

    # 左下角向上滑动
    def Swipe_Left_Up(self):
        logging.info(" LeapLefTup")
        L = self.get_size()
        x1 = int(L[0] * 0.3)
        y1 = int(L[1] * 0.9)
        y2 = int(L[1] * 0.7)
        self.driver.swipe(x1, y1, x1, y2, 1000)

    # 左下角向下滑动
    def Swipe_Left_Down(self):
        logging.info(" SwipeLeftDown")
        L = self.get_size()
        x1 = int(L[0] * 0.3)
        y1 = int(L[1] * 0.9)
        y2 = int(L[1] * 0.7)
        self.driver.swipe(x1, y2, x1, y1, 1000)

    # 获取当前时间
    def getTime(self):
        return self.new

    # 截取当前页面图片
    def getScreenShot(self, module):
        Time = self.getTime()
        image_ile = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s_%s.png' % (module, Time)
        logging.info("get %s screenshot" % module)
        self.driver.get_screenshot_as_file(image_ile)
        # 打印当前页面平台选择
        # print(self.driver.contexts)

    # 端内切换测试平台 CS/BS
    def Switch_platform(self, platform):
        self.Switch_To_Default_Content(platform)

    # 读取csv文件
    def Get_Scv_Data(self, csv_file, line):
        logging.info("=====get_scv_data======")
        with open(csv_file, "r", encoding="utf-8-sig") as file:  # 防止出现非法字符使用sig方法
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):  # 需要获取到第几行的参数数据就改为几行
                if index == line:
                    return row


if __name__ == '__main__':
    driver = youstar_desired_conf()
    com = Common(driver)
