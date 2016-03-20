'''
Created on 2016年3月20日

@author: lyt1987
'''
import sys

import os
from imaplib import Commands
print("os.system")
os.system("pwd")
print("os.popen")
print(os.popen("whereis python").read())
print("Commands.get")
print(Commands.get("pwd"))

print(sys.platform)
print('%s in' % 'akhf3878hhf')
print('{0} and {1}' .format( 'akhf3878hhf','eee'))



print(os.popen("free -m").read())

print(os.popen("df -h").read())

print(os.popen("du ").read())
print(os.popen("du -hs").read())


print(os.popen("lspci -vv").read())
os.popen("hwbrowser")

print(os.popen("find /-mtime -l cpio -c").read())
print(os.popen("find /-newer /Users/lyt1987/Desktop/GitHub/python -print cpio -o").read())



print(os.popen("ps ax | grep emacs ").read())
print(os.popen("ps aux | less").read()) 
print(os.popen("ls").read())