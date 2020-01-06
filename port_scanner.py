"""
PORT SCANNER : DEVELOPED BY NIGHTNASHO
USAGE : python port_scanner.py -H <host> -p <port> 

Developed : 2020/05/01 : 6.40pm

Updated : 2020/06/01 : 3.16pm : ( ChangeLog : [+] Style Improvement (New clean look))

Feature Update : (ChangeLog : [+] Using argparse library instead of optparse (due to an out of date in optparse library),
                           [+] Improving performence using threading library.)

Version : 1.0.2

"""

import socket
import optparse

socket.setdefaulttimeout(1)

def connectAddr(host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((host, port))
        client.send('Test\r\n')
        receive = client.recv(4096)
        print '[+] %d/tcp open' % port
        print '[+] Responded: '+str(receive)
        client.close()
    except:
        print '[-] %d/tcp closed\n ' % port
        
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
                connectAddr(host, int(prt))
        
        
        
        
if __name__ == '__main__':
    main()
