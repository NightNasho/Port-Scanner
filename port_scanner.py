"""
PORT SCANNER : DEVELOPED BY NIGHTNASHO
USAGE : python port_scanner.py -H <host> -p <port> 

Developed : 2020/05/01 : 6.40pm

Updated : 2020/06/01 : 4.12pm : ( ChangeLog : [+] Style Improvement (New clean look)
                                              [+] Huge performance than v1.0.1 - only 1.32s to 20ports 
                                                  (v1.0.1 taken 16.33s) [Note: Performance may vary due 
                                                  to your internet connection.)

Feature Update : (ChangeLog : [+] Using argparse library instead of optparse (due to an out of date in optparse library).)

Version : 1.0.3

"""

import socket
import optparse
import threading

socket.setdefaulttimeout(1)
screenLock = threading.Semaphore(value=1)


def connectAddr(host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((host, port))
        client.send('Test\r\n')
        receive = client.recv(4096)
        screenLock.acquire()
        print '[+] %d/tcp open' % port
        print '[+] Responded: '+str(receive)
    except:
        screenLock.acquire()
        print '[-] %d/tcp closed\n ' % port
    finally:
        screenLock.release()
        client.close()
    
        
def main():
    print ('='*50) + '\n' + '     Port Scanner V_1.0.1\n' + '     Script by Nasho Nightmare (2020)'
    print ('='*50) + '\n'
    
    parser = optparse.OptionParser("Usage: python port_scanner.py "+\
    "(-H <host>   -p <port> )")
    
    parser.add_option('-H', dest='host', type='string',\
    help='Specify host address')
    parser.add_option('-p', dest='port', type='string',\
    help='Specify port number')
    
    (options, args) = parser.parse_args()
    if (options.host == None or options.port == None) :
        print parser.usage
        exit(0)
    else:
        host = options.host
        port = options.port
        print '[*] Scan Results for: '+ socket.gethostbyaddr(host)[0] 
        port = port.split(',')
        for prt in port:
                t = threading.Thread(target=connectAddr, args=(host, int(prt)))
                t.start()
        
        
        
        
if __name__ == '__main__':
    main()
