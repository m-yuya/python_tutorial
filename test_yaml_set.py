#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import yaml

# tests

def yaml_test(yaml_file):
    with open('%s' %(yaml_file)) as fp:
        data = yaml.safe_load(fp)
    print 'raw data: '
    print repr(data)
    print '--'

    for node in data:
        print('node name: ' + node['name'])
        print('assinged cluster: %d' %(node['cluster']))
        for topic in node['publish']:
            print('publish topic: ' + topic)
        for topic in node['subscribe']:
            print('subscribe topic: ' + topic)
        print '--'

def set_test(yaml_file):
    with open('%s' %(yaml_file)) as fp:
        data = yaml.safe_load(fp)
    s = set()
    
    print 'all topics:'
    for node in data:
        for topic in node['publish']:
            s.add(topic)
        for topic in node['subscribe']:
            s.add(topic)
    print sorted(s)
          
# main

def generate(yaml_file):
    # test area
    yaml_test(yaml_file)
    set_test(yaml_file)

def generate_files(argv):
    generate(argv[1])

# start from here
if __name__ == '__main__':
    generate_files(sys.argv)
    print('\n---  Completed!! ---')
