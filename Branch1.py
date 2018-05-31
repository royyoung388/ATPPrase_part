# -*- coding: utf-8 -*-

"branch1类，转门存放branch1的结点"

__author__ = "Roy"


class Branch1(object):

    def __init__(self, line):
        print("parse branch1: %s" % (line))
        self.c = line[0:2].strip()
        self.n1 = line[2:8].strip()
        self.n2 = line[8:14].strip()
        self.ref1 = line[14:20].strip()
        self.ref2 = line[20:26].strip()
        print("r:" + line[26:32].strip())
        self.r = float(line[26:32].strip() if line[26:32].strip() != "" else "0")
        self.l = float(line[32:38].strip() if line[32:38].strip() != "" else "0")
        self.c = float(line[38:44].strip() if line[38:44].strip() != "" else "0")

    # 输出
    def print(self):
        print("branch1: n1 = %s, n2 = %s, ref1 = %s, ref2 = %s, r = %f, l = %f, c = %f" % (
            self.n1, self.n2, self.ref1, self.ref2, self.r, self.l, self.c))
