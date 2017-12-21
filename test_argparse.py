#!/usr/bin/env python
# -*- coding:utf-8 -*-

import argparse
 
def argparse_test():
    parser = argparse.ArgumentParser(description='argparse sample.')

    #bool オプション
    parser.add_argument('-s','--show', action='store_true', default=False, help='show your name (default: false)')
    #数値 オプション
    parser.add_argument('-g','--generation', type=int, default=0, choices=range(1, 18), help='birth generation')
    #文字列オプション
    parser.add_argument('-n', '--name', dest='name', type=str, metavar='first name', help='your first name', required=True)
    parser.add_argument('-l', '--last-name', dest='last_name', type=str, default='Potter', help='your last name', required=False)
    #文字列引数
    parser.add_argument('middle_name', nargs='?', default='D', type=str, help='middle name')
    parser.add_argument('friend', nargs=2, type=str, help='Your two friends')

    args = parser.parse_args()
    print args

    if args.show == True:
        print("Are you \"%s %s %s %d\" ?" % (args.name, args.middle_name, args.last_name, args.generation))

    if args.show == True:
        print("Your Friends are %s and %s." % (args.friend[0], args.friend[1]))

if __name__ == '__main__':
    argparse_test()
