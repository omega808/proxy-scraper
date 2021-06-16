#!/usr/bin/python3 
#Author: New Wavex86 
#Date Created: Wed Jun 16 19:10:16
import os

#Checks if program has been run before
#Program never run before run startup instructions

if not os.path.exists('log.txt'):
    with open('log.txt','w') as f:
        f.write('0')
                   
with open('log.txt','r') as f:
    a = f.readlines()
    st = int(f.read() or 0)
    
    if ( st == 1 ): #Program has been run before
        os.system(" rm -r output.txt formatted.txt") #Reset txtdumps
        os.system(" sudo sed -i /etc/proxychains4.conf -e '115,125d' ") #Remove previous proxies


#Reset counters                                
with open('log.txt','w') as f:
    if ( st == 1 ):
        f.write('0')
    if ( st == 0 ):
        f.write('1')


#Run shell command

os.system(" sudo python3 proxyScraper.py -p socks5 ")
os.system("sudo python3 proxyChecker.py -t 20 -s google.com -l output.txt") #Remove dead proxies
os.system(" cat output.txt | head > formatted.txt ")

#Lists to store IP and Port Numbers
ip_list = []
port_list = []

Rfile = open('test.txt', 'r')
Wfile = open('/etc/proxychains4.conf', 'a')
for line in Rfile.readlines():
    IP = line.split(':')[0]
    PORT = line.split(':')[1].strip(' ')

    ip_list.append(IP)
    port_list.append(PORT)
Rfile.close()

list_len = len(ip_list)
for line in range(10):
    Wfile.write('socks5 ' + str(ip_list[line]) + ' ' + str(port_list[line]))

Wfile.close()

exit (0) 
