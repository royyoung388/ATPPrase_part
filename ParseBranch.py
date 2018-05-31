# -*- coding: utf-8 -*-
from Branch1 import Branch1
from Branch2 import Branch2

__author__ = "Roy"


class ATP(object):

    def __init__(self):
        self.__branch1_list = []
        self.__branch2_list = []

    # 解析branch信息
    def __parse_branch(self):
        pass

    # 解析头部1的定义信息
    def __parse_header1(self, header1):
        self.__c = header1[0:2]
        self.__n1 = header1[2:8]
        self.__n2 = header1[8:14]
        self.__ref1 = header1[14:20]
        self.__ref2 = header1[20:26]
        self.__r = header1[26:32]
        self.__l = header1[32:38]
        self.__c = header1[38:44]

    # 解析头部2的定义信息
    def __parse_header2(self, header2):
        # 前半部分和header1相同
        self.__a = header2[32:38]
        self.__b = header2[38:44]
        self.__b = header2[44:50]
        self.__empty1 = header2[50:52]
        self.__empty2 = header2[52:54]

    # 解析branch1基本信息并添加到列表中
    def parse_branch1(self, line):
        branch1 = Branch1(line)
        self.__branch1_list.append(branch1)

    # 解析branch2基本信息并添加到列表中
    def parse_branch2(self, line):
        branch2 = Branch2(line)
        self.__branch2_list.append(branch2)

    def print(self):
        for b in self.__branch1_list:
            b.print()

        for b in self.__branch2_list:
            b.print()


if __name__ == '__main__':
    atp_file = open(r"C:\Users\Administrator\Desktop\atp\test.atp")
    # print(atp_file.read())
    atp = ATP()

    s = atp_file.readline()
    while s.strip() != r"/BRANCH":
        print(s)
        s = atp_file.readline()

    # 跳过前两行头部
    atp_file.readline()
    atp_file.readline()

    s = atp_file.readline()
    while s.strip()[0] != r"/":
        atp.parse_branch1(s.strip())
        s = atp_file.readline()

    atp.print()
    atp_file.close()
    print("end")
