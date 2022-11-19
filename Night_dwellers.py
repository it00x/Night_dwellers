from socket import *
from time import time
import csv
import os
from platform import system
#test parsing
import json
import pingparsing

def nory(usr_input):
    NORY=["Y","T","TAK","YES"]
    if usr_input in NORY:
        return True
    else: return False

def test_parsing(My_IP):
    splitIP = myIP.split(".")
    fixedIP = splitIP[0]+"."+splitIP[1]+"."+splitIP[2]+"."
    ping_parser = pingparsing.PingParsing()
    transmitter = pingparsing.PingTransmitter()
    for ip in range(0,255):
        transmitter.destination = fixedIP+":"+ip
        transmitter.count = 10
        result = transmitter.ping()
        print(json.dumps(ping_parser.parse(result).as_dict(), indent=4))

def create_DB_by_scanning():
    #find my Hostname
    My_hostname=gethostname()
    # gets host ip and assigns it to variable
    myIP=gethostbyname(My_hostname)
    #create a DataBase to be filled with connected IoT Devices
    New_DB ={myIP:"my device"}  
    #assign_Devices(myIP)
    test_parsing(My_IP)
    return New_DB

def assign_Devices(myIP):
    #convert ip to ip for iteration
    splitIP = myIP.split(".")
    fixedIP = splitIP[0]+"."+splitIP[1]+"."+splitIP[2]+"."
    scan_IP(fixedIP)
    #check os
    if system() == "Windows":
        ping1 = "ping -n 1"
    else:
        ping1 = "ping -c 1"
    #pings ip in range xxx.xxx.xxx.0-255
    for ip in range (0,255):
        addr = fixedIP + str(ip)
        comm = ping1 + addr
        response = os.popen(comm)
        for line in response.readlines():
            if(line.count("TTL")):
                break
            if (line.count("TTL")):
                print (addr, "--> Live")

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
            filepath.append(".csv")

def download_existing_DB():
    if(nory(input("is the DataBase located locally on this device (Y/n)>>"))==True):
        # import DB from local file
        if nory(input("is your file .csv (Y/n)>>"))==True:
            #open a .csv DB_file
            filepath=find_file_locally(False)
            with open(filepath,newline='') as csvfile:
                my_DB = csv.reader(csvfile, delimiter=' ', quotechar='|')
        else:
            filepath=find_file_locally(True)
            with open(filepath, "r") as f:
                my_DB=f.readlines()
            print(my_DB)
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