import socket
import time
start_time = time.time()
def main():
    My_hostname=socket.gethostname()
    # gets host ip and assigns it to variable
    myIP=socket.gethostbyname(My_hostname)
    print(myIP)
    # writes code execution time
    print((time.time()-start_time))

if __name__=="__main__":
    main()