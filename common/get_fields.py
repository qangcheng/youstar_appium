from resd_yaml import readyml
import os


def get_filed(yml: str, *args):
    """读取yml文件内的参数方法 """
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(path, "config", yml)
    temp = readyml(config_path)
    for i in args:
        temp = temp[i]
    return temp


if __name__ == '__main__':
    print(get_filed("capbillty.yaml", "platformVersion"))
