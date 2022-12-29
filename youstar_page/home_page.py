import os
import random

from common.desired_cadps import desired_conf
from selenium.common.exceptions import TimeoutException
import logging
import time
from selenium.webdriver.common.by import By
from youstar_page.login_page import LoginPage


class HomePage(LoginPage):
    # 顶部的入口
    Related_button = (By.XPATH, "//*[@text='Related']")
    hot_button = (By.XPATH, "//*[@text='Hot']")
    Discover_button = (By.XPATH, "//*[@text='Discover']")
    search_button = (By.ID, "in.dradhanus.liveher:id/iv_home_search")
    createroom_button = (By.ID, "in.dradhanus.liveher:id/txt_room_create")

    # 页面房间入口
    roomlist_button = (By.ID, "in.dradhanus.liveher:id/iv_head")

    def click_Hot(self):
        """点击Hot列表"""
        self.click(self.hot_button)

    def click_Related(self):
        """点击Related列表"""
        self.click(self.Related_button)

    def click_Discover(self):
        """点击Discover列表"""
        self.click(self.Discover_button)

    def click_createroom(self):
        """点击创建房间"""
        self.click(self.createroom_button)

    def click_search(self):
        """点击搜索按钮"""
        self.click(self.search_button)

    def Click_Room(self):
        self.findElements(self.roomlist_button)

    # 底部入口id都是一致需要使用list集合处理每个入口
    bottomen_button = (By.ID, "in.dradhanus.liveher:id/img_main_tab_icon")

    def click_room(self):
        """点击进入room页面"""
        self.findElements(self.bottomen_button)[0].click()

    def click_Momen(self):
        """点击进入Moment房间页面"""
        self.findElements(self.bottomen_button)[1].click()

    def click_chat(self):
        """点击进入chat房间页面"""
        self.findElements(self.bottomen_button)[2].click()

    def click_Me(self):
        """点击进入ME房间页面"""
        self.findElements(self.bottomen_button)[3].click()

    def click_listroom(self):
        """点击进入页面任意房间"""
        self.findElements(self.roomlist_button)[3].click()

    # 房间关闭按钮
    roomquit_button = (By.ID, "in.dradhanus.liveher:id/img_room_quit")
    roomquitone_button = (By.ID, "in.dradhanus.liveher:id/img_exit")

    def clickroom_quit_button(self):
        """点击房间关闭按钮"""
        self.click(self.roomquit_button)

    def clickroomone_quit_room(self):
        """点击房间内关闭按钮"""
        self.click(self.roomquitone_button)

    def room_testcase(self):
        """进入房间测试"""
        try:
            self.findElements(self.roomlist_button)
            self.getScreenShot("进入房间")
        except Exception as e:
            print("未在当前页面找到房间，报错信息：{}".format(e))
            self.getScreenShot("进入房间失败")
        else:
            self.findElements(self.roomlist_button)[0].click()
            logging.info("hot页面存在房间,点击第{}个房间".format(0 + 1))
            time.sleep(2)
            self.getScreenShot("进入房间")


if __name__ == '__main__':
    driver = youstar_desired_conf()
    home = HomePage(driver)
    home.vip_loin("chuiling950720@gmail.com", "9507201995")
    time.sleep(1)
    home.check_search()
    home.click_Hot()
    for i in range(0, 500):
        i += 1
        home.room_testcase()
        time.sleep(2)
        home.clickroom_quit_button()
        time.sleep(3)
        home.clickroomone_quit_room()
        time.sleep(3)
        print("进出房间测试完成:%s次" % i)
