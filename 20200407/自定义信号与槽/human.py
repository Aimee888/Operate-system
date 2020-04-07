# # 自定义信号与槽的演示
import sys
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal


class Human(QObject):
    # # 定义一个带str类型参数的信号
    nameChanged = pyqtSignal(str)
    # # overload型信号有两种参数，一种是Int，一种是str
    ageChanged = pyqtSignal([int], [str])

    def __init__(self, name="Mike", age=10, parent=None):
        super().__init__(parent)
        self.setAge(age)
        self.setName(name)

    def setAge(self, age):
        self.__age = age
        self.ageChanged.emit(self.__age)  # 发射int参数信号
        if age <= 18:
            age_info = "你是 少年"
        elif 18 < age <= 35:
            age_info = "你是 年轻人"
        elif 35 < age <= 55:
            age_info = "你是 中年人"
        elif 55 < age <= 80:
            age_info = "您是 老人"
        else:
            age_info = "您是 寿星啊"
        self.ageChanged[str].emit(age_info)  # 发射str参数信号

    def setName(self, name):
        self.__name = name
        self.nameChanged.emit(self.__name)


class Responsor(QObject):
    # @pyqtSlot(int)
    def do_ageChanged_int(self, age):
        print("您的年龄是：" + str(age))

    # @pyqtSlot(str)
    def do_ageChanged_str(self, ageInfo):
        print(ageInfo)

    def do_nameChanged(self, name):
        print("Hello, " + name)


if __name__ == "__main__":  # 测试程序
    print("**创建对象时**")
    boy = Human("Boy", 16)
    resp = Responsor()
    boy.nameChanged.connect(resp.do_nameChanged)

    # # overload的信号，两个槽函数不能同名，关联时需要给信号加参数区分
    boy.ageChanged.connect(resp.do_ageChanged_int)
    boy.ageChanged[str].connect(resp.do_ageChanged_str)

    print("\n **建立关联后**")
    boy.setAge(35)
    boy.setName("Jack")

    boy.ageChanged[str].disconnect(resp.do_ageChanged_str)
    print("\n **断开ageChanged[str]的关联后**")
    boy.setAge(10)
