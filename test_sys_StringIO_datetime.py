#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import datetime

try:
    from cStringIO import StringIO #Python 2.x
except ImportError:
    from io import StringIO #Python 3.x

class pycolor:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    END = '\033[0m'
    BOLD = '\038[1m'
    UNDERLINE = '\033[4m'
    INVISIBLE = '\033[08m'
    REVERCE = '\033[07m'

def write_date(s):
    d = datetime.datetime.today()
    s.write('// [note] Auto-generated file\n')
    s.write('// [note] %s/%s/%s %sh %sm %ss\n' % (d.year, d.month, d.day, d.hour, d.minute, d.second))

def print_generated_file(print_name):
    print ('Generate [./%s%s%s]' %(pycolor.GREEN, print_name, pycolor.END))

def output_file(s, file):
    f = open('%s'%(file), 'w')
    f.write(s.getvalue() + "\n")
    s.close()

def write_arg(s, arg):
    s.write('// [note] %s\n' %(arg))

def write_args(s, argv):
    for arg in argv[1:]:
        write_arg(s, arg)

if __name__ == '__main__':
    file_name = 'generated_file1.c'
    s = StringIO()
    write_date(s)
    write_args(s, sys.argv)
    print_generated_file(file_name)
    output_file(s, file_name)
    print '-- end --'
