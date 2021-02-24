from socket import *
import sys

ce = "\n......COMMAND ERROR......\n"
wr = "\n......WRONG ROLE......\n"
fe = "\n......FORMAT ERROR......\n"
ip_list = []

MAX_BUF = 2048
SERV_PORT = 50000

print('\n\n/* The Publisher */\n')

while True:
    while True:
        print('Publisher says (\"publish \'broker\'s IP\' quit\" to disconnected or only \"quit\" to quit from software): ',end = '')
        sys.stdout.flush()
        txtout = sys.stdin.readline().strip()
        if txtout == 'quit':
            break
        try:        
            (str1,bkIP,str3,str4) = txtout.split(' ')  
            if(str1 != 'publish'):
                print(wr)
            else:
                txtout = str1 + ' ' + str3 + ' ' + str4
                break    
        except ValueError:
            try:
                (str1,bkIP,str3) = txtout.split(' ')
                if(str1 != 'publish'):
                    print(wr)
                else:
                    txtout = str1 + ' ' + str3
                    break    
            except ValueError:
                print(ce)

    if txtout == 'quit':
        break
    
    if(bkIP not in ip_list):
        
        ip_list.append(bkIP)

        addr = (bkIP, SERV_PORT)
        s = socket(AF_INET, SOCK_STREAM)

        print("\n  Waiting for connection...\n")
        while True:
            try:
                s.connect(addr)
                break
            except Exception:
                print("  Waiting...")
            
        print("  Connected...")  
        
    txtout = "publ" + '^' + txtout
    s.send(txtout.encode('utf-8'))
    (clnt,txtout) = txtout.split('^')
    if txtout == 'quit':
        break
    modifiedMsg = s.recv(2048)
    print (modifiedMsg.decode('utf-8'))