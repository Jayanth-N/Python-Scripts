
import os
import time
import psutil
import platform
import json
import socket
import subprocess
import sys

info ={}
info['os']={}
info['os']['user id']=os.getuid()
info['os']['process id']=os.getpid()
info['os']['current Directory']=os.getcwd()
info['os']['system info']=os.uname()
info['os']['mode']=os.times()



info['platform']={}


info['platform']['Version']  = platform.python_version()
info['platform']['Version tuple']= platform.python_version_tuple()
info['platform']['Compiler']  = platform.python_compiler()
info['platform']['Build']     = platform.python_build()
info['platform']['system '] = platform.system()
info['platform']['node ']   = platform.node()
info['platform']['release']  = platform.release()
info['platform']['version']= platform.version()
info['platform']['machine'] = platform.machine()
info['platform']['processor'] = platform.processor()



info['usinfo']={}
us=psutil.users()
for u in us:
	info['usinfo']['host']=u.host
	info['usinfo']['usrname']=u.name
	info['usinfo']['teminal']=u.terminal
	

#info['open ports'] = {}


#for port in range(1,1024):  
      #  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       # result = sock.connect_ex((remoteServerIP, port))
        #if result == 0:
         #   ls = "Port {}: 	 Open".format(port)
        #sock.close()


filename ="pro.json"

with open(filename,"w") as properties:
				json.dump(info, properties,indent=4)
