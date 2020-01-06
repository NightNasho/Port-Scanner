"""
PORT SCANNER : DEVELOPED BY NIGHTNASHO
USAGE : python port_scanner.py -H <host> -p <port> 

Developed : 2020/05/01 : 6.40pm
Updated : 2020/06/01 : 1.43pm : ( ChangeLog : [^] Used option -p <port> as a port list and optimized code while checking the arguments ,
                                              [^] Removed the --pl <port_list> option and --pr <port_range> option,
                                              [^] Use -H option instead of old --ho <host> option,
                                              [-] Port range feature removed,
                                              [+] Code optimised.)
                                              
Next Update : (ChangeLog : [+] Using argparse library instead of optparse (due to an out of date in optparse library),
                           [+] Improving performence using threading library.)

Version : 1.0.1

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
        
        port = port.split(',')
        for prt in port:
                connectAddr(host, int(prt))
        
        
        
        
if __name__ == '__main__':
    main()
