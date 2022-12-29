from common.myunit import startEnd
from youstar_page.room_page import Room
import unittest


class Test_Room(startEnd):
    """房间内功能测试"""

    def test_createroom(self):
        """创建房间成功"""
        room = Room(self.driver)
        room.vip_loin("chuiling950720@gmail.com", "9507201995")
        room.Createroom_Case()
        self.assertTrue(room.Check_Creatroom())


if __name__ == '__main__':
    unittest.main()
