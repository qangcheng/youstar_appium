import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction
import logging


class BaseView(object):
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 20
        self.t = 0.5

    #  单个元素定位方法
    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    # 多个元素list定位方法
    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    # 新的定位方法,与findElement方法返回一致
    def findElementNew(self, locator, ignored_exceptions=NoSuchElementException):
        if not isinstance(locator, tuple):
            logging.info('locator参数类型错误，必须传元组类型：loc=("id","value1")')
            raise ignored_exceptions
        else:
            logging.info("正在点各位元素信息：定位方式-》%s,value值-》%s" % (locator[0], locator[1]))
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
            return ele

    # 单个元素等待方法封装，调用这个方法可以返回定位元素，比sleep和隐示等待更加稳定
    def findElement(self, locator):
        if not isinstance(locator, tuple):
            logging.info('locator参数类型错误，必须传元组类型：loc=("id","value1")')

        else:
            logging.info("正在定位元素信息：定位方式-》%s,value值-》%s" % (locator[0], locator[1]))
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
            return ele

    # 一组元素等待方法封装，调用这个方法可以返回定位元素，比sleep和隐示等待更加稳定
    def findElements(self, locator):
        if not isinstance(locator, tuple):
            logging.info('locator参数类型错误，必须传元组类型：loc=("id","value1")')
        else:
            logging.info("正在定位元素信息：定位方式-》%s,value值-》%s" % (locator[0], locator[1]))
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_elements(*locator))
            return ele

    # 获取测试APP
    def get_pakgame(self):
        pass

    # 应用置后台操作
    def background(self, seconds):
        self.driver.background_app(seconds)

    # 手指按压操作
    def press_action(self, locator):
        TouchAction(self.driver).press(locator).release().perform()

    # 手指长按压操作
    def long_press_action(self, locator, time):
        TouchAction(self.driver).long_press(locator, duration=time).release().perform()

    # 封装input方法
    def sendKeys(self, locator, text):
        ele = self.findElement(locator)
        return ele.send_keys(text)

    # 封装点击方法
    def click(self, locator):
        ele = self.findElement(locator)
        return ele.click()

    # 封装清除内容方法
    def clear(self, locator):
        ele = self.findElement(locator)
        return ele.clear()

    # 获取屏幕大小方法
    def get_window_size(self):
        return self.driver.get_window_size()

    # 滑动方法
    def swipe(self, start_x, start_y, end_x, end_y, duration):
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    # 端内切换测试平台 web&Android
    def Switch_To_Default_Content(self, platform):
        return self.driver.switch_to_default_content(platform)

    # 结束当前服务,避免端口号占用报错
    def close_service(self):
        return self.driver.quit()

    # 获取应用当前页面涉及平台
    def get_contexts(self):
        return print(self.driver.contexts)

    # Schamea跳转
    def schamea_Jump(self, link):
        os.popen("adb -d shell am start -a android.intent.action.VIEW -d" + link)

    def a(self, element):
        """封装多个场景需要判断的条件，已true和False来判断"""
        try:
            self.findElement(element)
            return True
        except Exception as e:
            logging.exception(e)
            return False
    #
    # def check_login_succeus(self):
    #     """判断是否登录成功"""
    #     if self.a(self.live_button):
    #         logging.info("主播登录")
    #         self.getScreenShot("主播live页")
    #         return True
    #     elif self.a(self.data_card):
    #         logging.info("非live主播登录")
    #         self.getScreenShot("首页列表")
    #         return True
    #     else:
    #         logging.info("登录失败")
    #         self.getScreenShot("登录失败截图")
    #         return False


if __name__ == '__main__':
    pass
