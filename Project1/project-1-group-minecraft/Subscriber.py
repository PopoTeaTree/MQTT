from socket import *
import sys
import time

ce = "\n......COMMAND ERROR......\n"
wr = "\n......WRONG ROLE......\n"
fe = "\n......FORMAT ERROR......\n"

MAX_BUF = 2048
SERV_PORT = 50000

print('\n\n/* The Subscriber */\n')

while True:        
    try:
        print('Subscriber says (Only \"quit\" to quit from software): ',end = '')
        sys.stdout.flush()
        txtout = sys.stdin.readline().strip()
        
        if txtout == 'quit':
            break

        (str1,bkIP,str3) = txtout.split(' ')
        if(str1 != 'subscribe'):
            print(wr)
        else:
            txtout = str1 + ' ' + str3
            break          
    except ValueError:
        print(ce)

if txtout == 'quit':
    exit()

addr = (bkIP, SERV_PORT)
s = socket(AF_INET, SOCK_STREAM)

print("\n  Waiting for connection...\n")
while True:
    try:
        s.connect(addr)
        break
    except Exception:
        print("  Waiting...")
    
print("\n......Connected......\n") 

txtout = "subs" + '^' + txtout
s.send(txtout.encode('utf-8'))
while True:
    modifiedMsg = s.recv(2048)
    msgdc = modifiedMsg.decode('utf-8')
    print (modifiedMsg.decode('utf-8'))