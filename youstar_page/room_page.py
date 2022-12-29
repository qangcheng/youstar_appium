import random

from common.Youstar_cadps import youstar_desired_conf
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import logging
import time
from selenium.webdriver.common.by import By
from youstar_page.home_page import HomePage


class RoomPage(HomePage):
    # 创建房间入口
    createroom_button = HomePage.createroom_button

    # 创建房间房间输入typle&标签
    input_room = (By.ID, "in.dradhanus.liveher:id/edt_name")
    tag_button = (By.ID, "in.dradhanus.liveher:id/txt_tag")
    voicechat_button = (By.XPATH, "//*[@text='Voice Chat']")
    livesteam_button = (By.XPATH, "//*[@text='Live Stream'")
    createroomvvoice_button = (By.XPATH, "//*[@text='Create a voice room']")

    # 房间内顶部按钮相关控件
    header_button = (By.ID, "in.dradhanus.liveher:id/img_publish_header")
    quitroom_button = (By.ID, "in.dradhanus.liveher:id/img_room_quit")
    share_button = (By.ID, "in.dradhanus.liveher:id/img_room_share1")
    keep_button = (By.ID, "in.dradhanus.liveher:id/img_icon_2")
    Quit_button = (By.ID, "in.dradhanus.liveher:id/img_icon_1")
    Settings_button = (By.ID, "in.dradhanus.liveher:id/img_icon_1")

    # 排行榜行相关控件
    totalcontribution_button = (By.ID, "in.dradhanus.liveher:id/txt_total_contribution")
    annouce_button = (By.ID, "in.dradhanus.liveher:id/txt_room_annouce")
    usernumber_button = (By.ID, "in.dradhanus.liveher:id/txt_room_user_num")

    # 底部功能空间入口
    sound_button = (By.ID, "in.dradhanus.liveher:id/room_sound")
    mic_button = (By.ID, "in.dradhanus.liveher:id/room_mic")
    layoutinput_button = (By.ID, "in.dradhanus.liveher:id/layout_input")
    face_button = (By.ID, "in.dradhanus.liveher:id/room_face")
    msg_button = (By.ID, "in.dradhanus.liveher:id/room_msg")
    gameroom_button = (By.ID, "in.dradhanus.liveher:id/room_game")
    giftroom_button = (By.ID, "in.dradhanus.liveher:id/room_gift")

    def Createroom_Case(self):
        """创建房间"""
        self.click(self.createroom_button)
        try:
            self.findElement(self.input_room)
        except NoSuchElementException:
            logging.info("未调起创建房间页面")
        else:
            a = random.randint(0, 9)
            c = self.findElements(self.tag_button)[a]
            print("选中的标签是:{}".format(c.text))  # 打印标签文案
            logging.info("选中的标签是:{}".format(c.text))
            c.click()
            self.sendKeys(self.input_room, "Test_Room" + str(int(time.time())))
            time.sleep(1)
            self.getScreenShot("房间创建页面")
            self.click(self.createroomvvoice_button)
            time.sleep(1)
            self.getScreenShot("创建房间")

    def Check_Creatroom(self):
        """检查是否创建成功"""
        try:
            self.findElement(self.quitroom_button)
            logging.info("创建房间成功")
            self.getScreenShot("创建房间成功")
            return True
        except TimeoutException:
            logging.info("创建房间失败")
            return False


if __name__ == '__main__':
    driver = youstar_desired_conf()
    room = RoomPage(driver)
    room.vip_loin("chuiling950720@gmail.com", "9507201995")
    room.Createroom_Case()
    room.Check_Creatroom()
