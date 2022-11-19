from socket import *
from time import time

def nory(usr_input):
    NORY=["Y","T","TAK","YES"]
    if usr_input in NORY:
        return True
    else: return False


def create_DB_by_scanning():
    #find my Hostname
    My_hostname=gethostname()
    # gets host ip and assigns it to variable
    myIP=gethostbyname(My_hostname)
    #create a DataBase to be filled with connected IoT Devices
    New_DB ={myIP:"my device"}
    return New_DB

def assign_Devices(My_hostname):
    #socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #socket.bind((host, port))
    #socket.listen(max_connections)
    #try:
    #while True:
    #    connected_socket, addr = socket.accept()
    #    New_DB.update({addr,connected_socket})
    pass
    pass

def download_existing_DB():
    pass
    pass

def main():
    start_time = time()
    if(nory(input("is there an existing dataBase of you IoT devices in this network (Y/n)>>"))==True):
        pass #there is an existing data base
        #download a new DB
        DB_of_IoT=download_existing_DB()
    else:
        #there is no DB
        # create new by scaning network
        DB_of_IoT=create_DB_by_scanning()
    print(DB_of_IoT)
    
    # writes code execution time
    print((time()-start_time))

if __name__=="__main__":
    main()