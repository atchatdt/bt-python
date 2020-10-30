# Định nghĩa một lớp gồm có tham số lớp và có cùng tham số instance

from module import clear
clear()

class Person:
    def __init__(self, name = "kuro"):
        self.name = name
    def printInfo(self):
        print('Hello {0}'.format(self.name))
student = Person("kazuto")
student.printInfo()
