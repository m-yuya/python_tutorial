#!/usr/bin/env python
# -*- coding:utf-8 -*-

import subprocess

def subprocess_test():
    
    cmd = 'ls yaml'
    print cmd
    retcode = subprocess.call(cmd.split())
    print retcode

    cmd = 'ls -l yaml'
    print cmd
    retcode  =  subprocess.check_output(cmd.split(" "))
    print retcode

if __name__ == '__main__':
    subprocess_test()
