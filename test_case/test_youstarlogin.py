from common.myunit import startEnd
from youstar_page.login_page import LoginPage
import unittest
import logging


class Test_loign(startEnd):
    """youstar登录测试"""

    def test_login_success(self):
        """vip登录成功"""
        logging.info("-----test_login_success------")
        login = LoginPage(self.driver)
        login.vip_loin("chuiling950720@gmail.com", "9507201995")
        login.check_process()
        self.assertTrue(login.check_search())

    def test_login_fail(self):
        """vip登录失败"""
        logging.info("-----test_login_fail------")
        login = LoginPage(self.driver)
        login.vip_loin("chuiling950720@gmail.com", "9507205")
        self.assertFalse(login.check_search())


if __name__ == '__main__':
    unittest.main()
