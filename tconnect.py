import socket
import sys
import time
import argparse

# Define params
def get_parser():
    parser = argparse.ArgumentParser(description="TConnect : test for a TCP connection.")
    parser.add_argument("-m","--mode", help="Server or client mode", choices=['client','server'], required=True)
    parser.add_argument("-H","--host", help="Server: listening interface (ip); Client: Host server to reach", required=True)
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-i", "--inp", help="Port list from a text file (one port per line). Override --port option")
    group.add_argument("-p", "--port", type=int, nargs='*',help="Port list (separated by a space)")
    return parser

# Extract network ports from a text file
def get_port(filename):
    with open(filename) as file_in:
        ports = []
        for port in file_in:
            ports.append(int(port))
    return ports

# Create a client socket
def create_client_socket(ip, port):
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((ip, port))
        print("TCP " + str(port) + ": OK")
    except Exception as e:
        print("TCP " + str(port) + ": NOK => ", e)
    finally:
        s.close()
    return 1

# Create a server socket
def create_server_socket(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try: 
        s.bind((ip, port))
        s.listen()
        print('listening on TCP ', port)
        conn, addr = s.accept()
    except Exception as e:
        print("TCP " + str(port) + ": error => ", e)
    finally:
        s.close()
        print('connection closed : TCP', port)
    

# main function for client side
def main_client():
    host = args.host
    if args.inp:
        port_list = get_port(args.inp)
    else:
        port_list = args.port
    print("Testing port(s) : " , port_list, "\n on ", host)

    for port in port_list:
        time.sleep(0.2)
        create_client_socket(host, port)

# main function for server side
def main_server():
    host = args.host
    if args.inp:
        port_list = get_port(args.inp)
    else:
        port_list = args.port
    print("Testing ports : " , port_list)
    for port in port_list:
        create_server_socket(host, port)

if __name__ == "__main__":
    p = get_parser()
    args = p.parse_args()
    match args.mode:
        case 'server':
            main_server()
        case 'client':
            main_client()
        case _:
            exit()