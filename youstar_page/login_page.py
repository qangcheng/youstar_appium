from selenium.common.exceptions import TimeoutException
import logging
import time
from selenium.webdriver.common.by import By
from common.Youstar_conmmon import Common
from common.Youstar_cadps import youstar_desired_conf


class LoginPage(Common):
    # 各个登录入口
    fb_button = (By.ID, "in.dradhanus.liveher:id/freme_login_fb")
    gp_button = (By.ID, "in.dradhanus.liveher:id/frame_login_gp")
    phone_button = (By.ID, "in.dradhanus.liveher:id/img_login_phone")
    email_button = (By.ID, "in.dradhanus.liveher:id/img_login_email")
    viplogin_button = (By.ID, "in.dradhanus.liveher:id/view_premium")

    # VIP登录页面元素
    Alias_button = (By.XPATH, "//*[@text='Alias name']")
    password_button = (By.XPATH, "//*[@text='Password']")
    login_button = (By.XPATH, "//*[@text='Login']")
    Plaintext_button = (By.ID, "in.dradhanus.liveher:id/text_input_end_icon")

    # 手机登录切换元素
    flag_codebutton = (By.ID, "in.dradhanus.liveher:id/ftv_flag_code")
    phone_seach_button = (By.ID, "in.dradhanus.liveher:id/edt_search")
    input_phonebutton = (By.ID, "in.dradhanus.liveher:id/edt_phonelogin_number")
    phone_loginbutton = (By.ID, "in.dradhanus.liveher:id/txt_phonelogin_login")
    china_button = (By.XPATH, "//*[@text='China']")
    phonepassword_button = (By.ID, "in.dradhanus.liveher:id/edt_password")
    confirm_button = (By.ID, "in.dradhanus.liveher:id/txt_confirm")

    # 搜索校验按钮
    createroom_button = (By.ID, "in.dradhanus.liveher:id/txt_room_create")

    def click_viplogin(self):
        """VIP登录入口"""
        self.click(self.viplogin_button)

    def input_account(self, number):
        """输入账号"""
        self.sendKeys(self.Alias_button, number)

    def input_password(self, pas):
        """输入密码"""
        self.sendKeys(self.password_button, pas)

    def click_login(self):
        """点击登录"""
        self.click(self.login_button)

    def vip_loin(self, user, psr, Plaintext_button=True):
        """
        vip 登录
        :param Plaintext_button: 登录密码是否明文显示开关
        :param user:  登录账号
        :param psr:   登录密码
        :return: None
        """
        self.click_Collection()
        logging.info("进入VIP登录集合列表")
        time.sleep(2)
        self.getScreenShot("登录集合入口")
        self.click_viplogin()
        try:
            self.Alias_button
        except Exception as e:
            logging.info("元素查找失败，报错如下：".format(e))
            raise e
        else:
            time.sleep(1)
            logging.info("进入vip登录页面，输入账号密码登录")
            self.input_account(user)
            logging.info("输入账号：{}".format(user))
            self.input_password(psr)
            logging.info("输入密码:{}".format(psr))
            if Plaintext_button: self.click(self.Plaintext_button)
            time.sleep(1)
            self.getScreenShot("进入vip登录页面，已输入账号密码登录")
            self.click_login()
            time.sleep(4)

    def click_phonelogin(self):
        """点击手机号登录"""
        self.click(self.phone_button)

    def click_flag_code(self):
        """进入国家选择页面"""
        self.click(self.flag_codebutton)

    def seach_countries(self, number):
        """选择国家并输入登录手机号"""
        self.click(self.phone_seach_button)
        self.clear(self.phone_seach_button)
        self.sendKeys(self.phone_seach_button, number)
        self.click(self.china_button)

    def input_phonenumber(self, phone_number):
        """输入手机号码"""
        self.sendKeys(self.input_phonebutton, phone_number)
        self.click(self.phone_loginbutton)

    def input_phonepassword(self, passwordnumber):
        """输入密码"""
        self.sendKeys(self.phonepassword_button, passwordnumber)
        self.click(self.confirm_button)

    def phone_login(self, number, phone_number, passwordnumber):
        """手机号登录流程"""
        self.click_phonelogin()
        logging.info("已进入手机登录页面")
        time.sleep(1)
        self.getScreenShot("手机登录页面")
        self.click_flag_code()
        self.seach_countries(number)
        try:
            self.phone_loginbutton
        except Exception as e:
            logging.info("未进入到登录页面报错：{}".format(e))
            self.getScreenShot("登录页面进入失败")
        else:
            self.input_phonenumber(phone_number)
            time.sleep(1)
            self.input_phonepassword(passwordnumber)

    # 校验是否进入主页面，做unittest需要校验是否成功
    def check_search(self):
        try:
            self.findElement(self.createroom_button)
            logging.info("校验元素成功，登录成功,找到校验元素:{%s}" % str(self.createroom_button))
            self.getScreenShot("登录成功")
            return True
        except Exception as e:
            logging.info("没有找到校验元素,登录失败报错,未找到首页元素:{%s}" % str(e))
            self.getScreenShot("登录失败")
            return False


if __name__ == '__main__':
    drriver = youstar_desired_conf()
    login = LoginPage(drriver)
    # login.vip_loin("chuiling950720@gmail.com", "9507201995")  # 测试环境
    # # login.vip_loin("yz@gmail.com", "123456")  # 正式环境
    login.phone_login(number=86, phone_number="013632721415", passwordnumber="950720")
    login.check_process()
    login.check_search()
