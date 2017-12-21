#!/usr/bin/env python
# -*- coding:utf-8 -*-

from collections import Counter

print 'Test1'

str_list = ('a', 'a', 'a', 'a', 'b', 'c', 'c')
c = Counter(str_list)

print(c)        # Counter({'a': 4, 'c': 2, 'b': 1})
print(type(c))  # <class 'collections.Counter'>

print(c['a'])   # 4
print(c['b'])   # 1
print(c['c'])   # 2
print(c['d'])   # 0


print 'Test2'
gettysburg = "government of the people, by the people, for the people."

gettysburg = gettysburg.replace(',', '')    # カンマ削除
gettysburg = gettysburg.replace('.', '')    # ピリオド削除
words = gettysburg.split()                  # スペースで分割してリスト化
print(Counter(words)['people'])                          # 3


print 'Test3'
word = 'supercalifragilisticexpialidocious'
print(Counter(word).most_common(5))  # [('i', 7), ('a', 3), ('c', 3), ('l', 3), ('s', 3)]
