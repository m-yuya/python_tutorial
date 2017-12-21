# Python Tutorial

personal test codes to learn how to use basic python

## os
```shell
$ ./test_os.py
__file__                                  : './os_test.py'
os.getcwd()                               : '/mnt/c/cygwin64/home/Yuya/lesson_python/python_tutorial'
os.path.dirname(__file__)                 : '.'
os.path.abspath(__file__)                 : '/mnt/c/cygwin64/home/Yuya/lesson_python/python_tutorial/os_test.py'
os.path.dirname(os.path.abspath(__file__)): '/mnt/c/cygwin64/home/Yuya/lesson_python/python_tutorial'

$ cd yaml
$ ../test_os.py
__file__                                  : './os_test.py'
os.getcwd()                               : '/mnt/c/cygwin64/home/Yuya/lesson_python/python_tutorial'
os.path.dirname(__file__)                 : '.'
os.path.abspath(__file__)                 : '/mnt/c/cygwin64/home/Yuya/lesson_python/python_tutorial/os_test.py'
os.path.dirname(os.path.abspath(__file__)): '/mnt/c/cygwin64/home/Yuya/lesson_python/python_tutorial'
```


## yaml
```shell
$ ./test_yaml_set.py yaml/complex.yaml
raw data:
[{'cluster': 1, 'name': 'talker', 'publish': ['/chatter'], 'subscribe': ['/chatter6']}, {'cluster': 1, 'name': 'talker2', 'publish': ['/chatter2', '/chatter3'], 'subscribe': []}, {'cluster': 2, 'name':
'listener', 'publish': ['/chatter4'], 'subscribe': ['/chatter']}, {'cluster': 2, 'name': 'listener2', 'publish': ['/chatter5'], 'subscribe': ['/chatter', '/chatter2']}]
--
node name: talker
assinged cluster: 1
publish topic: /chatter
subscribe topic: /chatter6
--
node name: talker2
assinged cluster: 1
publish topic: /chatter2
publish topic: /chatter3
--
node name: listener
assinged cluster: 2
publish topic: /chatter4
subscribe topic: /chatter
--
node name: listener2
assinged cluster: 2
publish topic: /chatter5
subscribe topic: /chatter
subscribe topic: /chatter2
--
all topics:
['/chatter', '/chatter2', '/chatter3', '/chatter4', '/chatter5', '/chatter6']

---  Completed!! ---
```


## collections
```shell
$ ./test_collections.py
Test1
Counter({'a': 4, 'c': 2, 'b': 1})
<class 'collections.Counter'>
4
1
2
0
Test2
3
Test3
[('i', 7), ('a', 3), ('c', 3), ('l', 3), ('s', 3)]
```


## subprocess
``` shell

$ ./test_subprocess.py
ls yaml
arrays.yaml  complex.yaml  two_listenres.yaml
0
ls -l yaml
total 338
-rwxrwxrwx 1 root root 135 Dec 12 23:27 arrays.yaml
-rwxrwxrwx 1 root root 322 Dec 13 18:50 complex.yaml
-rwxrwxrwx 1 root root 205 Dec 13 18:07 two_listenres.yaml
```


## argparse

``` shell
$ ./test_argparse.py -n Taro John Mike
Namespace(friend=['John', 'Mike'], generation=0, last_name='Potter', middle_name='D', name='Taro', show=False)

$ ./test_argparse.py -s -n Taro John Mike
Namespace(friend=['John', 'Mike'], generation=0, last_name='Potter', middle_name='D', name='Taro', show=True)
Are you "Taro D Potter 0" ?
Your Friends are John and Mike.

$ ./test_argparse.py -s -n Taro -l Yamada -g 12 John Mike
Namespace(friend=['John', 'Mike'], generation=12, last_name='Yamada', middle_name='D', name='Taro', show=True)
Are you "Taro D Yamada 12" ?
Your Friends are John and Mike.

$ ./test_argparse.py -s -n Taro -l Yamada -g 12 Marx John Mike
Namespace(friend=['John', 'Mike'], generation=12, last_name='Yamada', middle_name='Marx', name='Taro', show=True)
Are you "Taro Marx Yamada 12" ?
Your Friends are John and Mike.

$ ./test_argparse.py --help
usage: test_argparse.py [-h] [-s]
                        [-g {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17}] -n
                        first name [-l LAST_NAME]
                        [middle_name] friend friend

argparse sample.

positional arguments:
  middle_name           middle name
  friend                Your two friends

optional arguments:
  -h, --help            show this help message and exit
  -s, --show            show your name (default: false)
  -g {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17}, --generation {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17}
                        birth generation
  -n first name, --name first name
                        your first name
  -l LAST_NAME, --last-name LAST_NAME
                        your last name

```


## sys, StringIO, datetime
``` shell
$ ./test_sys_StringIO_datetime.py hoge foo bar
Generate [./hoge.c]
-- end --
```
