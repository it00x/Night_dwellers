from socket import *
from time import time
import csv
import os
from platform import system

def nory(usr_input):
    NORY=["Y","T","TAK","YES"]
    if usr_input in NORY:
        return True
    else: return False

def create_DB_by_scanning():
    My_hostname=gethostname()
    myIP=gethostbyname(My_hostname)
    New_DB ={myIP:"my device"}  
    mask_IP=(myIP.split('.')[1]+'.'+myIP.split('.')+'.')
    for i in range(0,255,1):
        test_IP=mask_IP+"{}".format(i)
        if test_IP!=myIP:
            out_test=os.command("ping -n {}".format(test_IP))
            if out_test[-1]!=".":
                New_DB.append(test_IP+" ; "+"Unknown type")



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