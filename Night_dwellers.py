import socket

def main():
    My_hostname=socket.gethostname()
    myIP=socket.gethostbyname(My_hostname)
    print(myIP)

if __name__=="__main__":
    main()