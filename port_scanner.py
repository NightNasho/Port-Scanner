"""
PORT SCANNER : DEVELOPED BY NIGHTNASHO
USAGE : python port_scanner.py --ho <host> -p <port_number> :: Additional Features For -p Option : --pl <port_list>     --pr <port_range>

Developed : 2020/05/01 : 6.40pm
Version : 1.0

"""

import socket
import optparse

socket.setdefaulttimeout(1)

def connectAddr(host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((host, port))
        receive = client.recv(4096)
        print '[+] Port '+ str(port) +' is open.'
        print '[+] Received: '+str(receive)
        client.close()
    except Exception, e:
        print '[-] Error on checking port: '+str(port)+' : ' + str(e)

def main():
    parser = optparse.OptionParser("Usage: python port_scanner.py "+\
    "(--ho <host> [-p <port> --pl <port_list EG:22,23,45,80> --pr <port_range EG:22,23>])")
    
    parser.add_option('--ho', dest='host', type='string',\
    help='Specify host address')
    parser.add_option('-p', dest='port', type='int',\
    help='Specify port number')
    parser.add_option('--pl', dest='port_list', type='string',\
    help='Specify port list(type-tuple)')
    parser.add_option('--pr', dest='port_range', type='string',\
    help='Specify port range')
    
    (options, args) = parser.parse_args()
    if (options.host == None) |\
       ((options.port == None) &\
        (options.port_list == None) &\
        (options.port_range == None)):
        print parser.usage
        exit(0)
    else:
        host = options.host
        port = options.port
        port_list = options.port_list
        port_range = options.port_range
        
        if (port):
            connectAddr(host, port)
        elif (port_list):
            port_list = port_list.split(',')
            for prt in port_list:
                connectAddr(host, int(prt))
        elif (port_range):
            port_range = port_range.split(',')
            if len(port_range) > 2 & len(port_range) < 1:
                print '[-] Error: Please give Minimum,Maximum range values.'
                exit(0)
            for prt in range(int(port_range[0]), int(port_range[1])):
                connectAddr(host, prt)
        
        
        
        
if __name__ == '__main__':
    main()