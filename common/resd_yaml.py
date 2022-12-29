import yaml
import os


def readyml(ymlpath):
    """读取yaml文件内容"""
    if not os.path.isfile(ymlpath):
        raise FileNotFoundError("文件不存在")
    f = open(ymlpath, "r", encoding="utf-8")
    c = f.read()
    # yaml文件转字典格式
    d = yaml.safe_load(c)
    print("读取出来的yaml文件内容是：", d)
    return d


if __name__ == '__main__':
    a = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    capbilly_path = os.path.join(a, "config", "capbillty.yaml")
    # print(capbilly_path)
    readyml(capbilly_path)
