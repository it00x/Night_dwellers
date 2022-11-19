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

def find_file_locally(is_txt):
    if is_txt==True:
        print("choosing a .txt file")
        filepath=str(input("input file path/name if the path is in the project folder>>"))
        if filepath[-4:-1]!=".txt" or filepath[-1]=="/" or filepath[-1]=="\\" :
            filepath.append(".txt")
    else:
        print("choosing a .csv file")
        filepath=str(input("input file path/name if the path is in the project folder>>"))
        if filepath[-4:-1]!=".csv" or filepath[-1]=="/" or filepath[-1]=="\\" :
            ilepath.append(".csv")

def download_existing_DB():
    if(nory(input("is the DataBase located locally on this device (Y/n)>>"))==True):
        # import DB from local file
        if nory(input("is your file .csv (Y/n)>>"))==True:
            #open a .csv DB_file
            filepath=find_file_locally(False)

        else:
            filepath=find_file_locally(True)

    else:
        #import DB from a server
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