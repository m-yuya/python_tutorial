#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

def path_test():
    print("__file__                                  : %r" %  __file__)
    print("os.getcwd()                               : %r" % (os.getcwd()))
    print("os.path.dirname(__file__)                 : %r" % (os.path.dirname(__file__)))
    print("os.path.abspath(__file__)                 : %r" % (os.path.abspath(__file__)))
    print("os.path.dirname(os.path.abspath(__file__)): %r" % (os.path.dirname(os.path.abspath(__file__))))

if __name__ == '__main__':
    path_test()
