# coding=utf-8
"""
 r以读的方式打开文件，读取文件信息
 w 以写入当时打开文件，如果文件存在，清空文件重新写入
 a 以追加模式打开文件，可对文件进行读写操作
 w+ 消除文件内容，然后以读写方式打开
 a+ 以读写方式打开文件，并把文件指针移动到文件尾
 b 以二进制模式打开文件，不是文本模式
 测试报告加时间戳不利于持续集成，jenkins不能持续集成

"""

import unittest
from BSTestRunner import BSTestRunner
import time
import logging

test_dir = "../test_case"
report_dir = "../reports"
rule = "test*.py"

discover = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern=rule)  # 模糊匹配用例，使用test*.py即可执行全部用例

now = time.strftime("%Y-%m-%d %H_%M_%S")  # 加时间戳不利于持续集成，jenkins不能持续集成
report_name = report_dir + "/" + now + "_YouStar_test_report.html"

with open(report_name, "wb") as f:
    runner = BSTestRunner(stream=f,
                          title="YouStar test report",
                          description="YouStar Android app test report",
                          )
    logging.info("start run test case")
    runner.run(discover)

