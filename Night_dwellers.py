from dataclasses import dataclass
from msvcrt import kbhit
from operator import truediv
from pickle import TRUE
from socket import *
from time import time
import csv
import os
from platform import system
import random

def nory(usr_input):
    #checks if user enters an affirmative answer
    NORY=["Y","T","TAK","YES"]
    if usr_input in NORY:
        return True
    else: return False
    

def sorting_of_DB(database, DB_TYPE):
    #checks datatype and acts accordingly
    if DB_TYPE==0: return database
    else:
        #iterates over types of databases and sorts IPs
        for iterable_ in range(DB_TYPE,0,-1):
            N_DB=sorted(database.items().split('.')[-iterable_],key=lambda x:x[1])
    return N_DB

def create_DB_by_scanning():
    #getting host name and assigning it to variable to get ip
    My_hostname=gethostname()
    myIP=gethostbyname(My_hostname)
    #creating database to store devices and their IP
    New_DB ={myIP:"my device"}  
    #getting internet mask of given IP
    mask_IP=(myIP.split('.')[1]+'.'+myIP.split('.')+'.')
    #Searching for devices in the network
    for i in range(0,255,1):
        test_IP=mask_IP+"{}".format(i)
        #if internet mask isn't equal to IP append device to database
        if test_IP!=myIP:
            out_test=os.command("ping -n {}".format(test_IP))
            if out_test[-1]!=".":
                New_DB.append(test_IP+" ; "+"Unknown type")
    return New_DB

def check_netmask(database):
    #database types:
    #0= DB consists of only 1 variable and can not be sorted
    #1= 255.255.255.0
    #2= 255.255.0.0
    #3= 255.0.0.0
    #4= 0.0.0.0
    #check database length before checking mask
    if len(database) == 1:
        return 0
    #gets a number of keys to check
    tempa = len(database)/10+2
    #create temporary lists for keys and their indexes that are randomly chosen
    tempList = []
    tempKeyList = []
    tempKeys = []
    gotmask=False
    #generate random indexes of keys
    for i in range(0,tempa):
        tempRandom = random.randrange(0,tempa)
        if tempRandom in tempList:
            i-=1
        else:
            tempList.append(tempRandom)
    #create a list with ips
    for j in tempList:
        tempKeyList.append(database[j])
    #split ips into iterable parts to check mask type
    for key in tempKeyList:
        tempKey = key.split(".")
        tempKeys.append(tempKey)
    #compare ip segments  to get mask type
    for k in range(3,0,-1):
        for l in range(0,len(tempKeys),1):
            if tempKeys[k][l]!=tempKeys[k][l+1]:
                break
            else:
                gotmask=True
                return 3-k
        if gotmask==True: break
    return 4

def delete_expandable(database):
    netmask_type=check_netmask(database)
    sorted_database=sorting_of_DB(database,netmask_type)
    for items in range(0,len(sorted_database)-1,1):
        if sorted_database[items]==sorted_database[items+1]:
            del sorted_database[items]
    return sorted_database

def find_file_locally(is_txt):
    #checking file type
    if is_txt==True:
        print("choosing a .txt file")
        #check if there is .txt at end of path and adds it if it's absent
        filepath=str(input("input file path/name if the path is in the project folder>>"))
        if filepath[-4:-1]!=".txt" or filepath[-1]=="/" or filepath[-1]=="\\" :
            filepath.append(".txt")
    else:
        print("choosing a .csv file")
                #check if there is .csv at end of path and adds it if it's absent
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
            #finds the file if it's not a local database
            filepath=find_file_locally(True)
            with open(filepath, "r") as f:
                my_DB=f.readlines()
        return(my_DB)
    else:
        #asks the user to migrate the database to the device using newly opened terminal window
        print("use an ftp or sftp connection to transfer the DataBase to this device")
        if system()=="Windows":
            os.command("start cmd.exe")
        else:
            os.command("gnome-terminal")
        download_existing_DB()

def main():
    start_time = time()
    if(nory(input("is there an existing dataBase of you IoT devices in this network (Y/n)>>"))==True):
        #there is an existing data base
        #download a new DB
        DB_of_IoT=download_existing_DB()
    else:
        #there is no DB
        # create new by scaning network
        DB_of_IoT=create_DB_by_scanning()
    DB_of_IoT=delete_expandable(DB_of_IoT)
    # writes code execution time
    print((time()-start_time))

if __name__=="__main__":
    main()