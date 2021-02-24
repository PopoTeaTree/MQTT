from socket import *
from threading import Thread
import sys,os,time

dicttop = {}    #Set dicttop to null first
flag = {}

SERV_PORT = 50000

def handle_client(s):
    while True:
        try:    
            msg = s.recv(1024)
            msg2 = (msg).decode('utf-8')
            #Publisher role    
            (role, topic, data) = msg2.split(" ")
            (clnt, role) = role.split('^')

            if(role != 'publish'): 
                txtout = "\n......COMMAND ERROR......\n"
                s.send((txtout).encode('utf-8'))            
            
            elif(clnt != 'publ'):
                txtout = "\n......WRONG ROLE......\n"
                s.send((txtout).encode('utf-8'))             
                        
            else:
                if topic not in dicttop.keys() :
                    flag[topic] = 0
                dicttop[topic] = data
                flag[topic] += 1
                txtout = "\n......Data published......\n"
                s.send((txtout).encode('utf-8'))
        
        
        except ValueError:  
            #Subscriber role
            try:
                (role, topic) = msg2.split(" ")
                (clnt, role) = role.split('^')
                if topic not in flag.keys():
                    flag[topic] = 0
                if(topic == 'quit'):
                    print('\n......Client disconnected......\n')
                    s.send(('\n......You are disconnected......\n').encode('utf-8'))
                    break
                if(role != 'subscribe'):    
                    txtout = "\n......COMMAND ERROR......\n"
                    s.send((txtout).encode('utf-8'))
                elif(clnt != 'subs'):
                    txtout = "\n......WRONG ROLE......\n"
                    s.send((txtout).encode('utf-8')) 
                else:
                    tflag = flag[topic] # initial to the current flag
                    while True:
                        # try:
                        while True:
                            if flag[topic] != tflag:
                                break
                        txtout = topic + ' -> ' + dicttop[topic]
                        s.send((txtout).encode('utf-8'))
                        tflag = flag[topic] # update tflag
            except ValueError:
                    txtout = "\n......FORMAT ERROR......\n"
                    s.send((txtout).encode('utf-8'))

        print("All topics--------------------")
        for t,d in dicttop.items():
            print("|   "+ t + ": ",d)    
        print("------------------------------\n")
 
    s.close()
    return

addr = ('127.0.0.1', SERV_PORT)
s = socket(AF_INET, SOCK_STREAM)

s.bind(addr)
s.listen(5)

print('\n......Broker initiated......\n')
while True:    
    sckt, addr = s.accept()
    ip, port = str(addr[0]), str(addr[1])
    if(ip == '127.0.0.1'):
        print ('\n          New connection was made from .. ' + ip + ': ' + port + '\n')
    try:
        Thread(target=handle_client, args=(sckt,)).start()
    except:
        print("Cannot start thread..")
        import traceback
        traceback.print_exc()
