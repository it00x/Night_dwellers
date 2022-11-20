from socket import *
from time import time
import csv
import os
from platform import system
import random

#Device Classes
#test 10 device classes with their respective configuration options allowing for later expansion
class AC_UNIT:
    def __init__(self,FanSpeed,OnOff,TemperatureSetting):
        #fan speed is responsible for fan blades rotation
        self.FanSpeed = FanSpeed
        #onoff boolean taking care of state of device
        self.OnOff = OnOff
        #parameter allowing controlling whether user wants colder or warmer temps in their room
        self.TempereatureSetting = TemperatureSetting

class COFFEE_MAKER:
    def __init__(self,Cook,TemperatureControl,OnOff):
        #adjusting cooking modes
        self.Cook = Cook
        #adjusting target temperature
        self.TemperatureControl = TemperatureControl
        #controls power state of the device
        self.OnOff = OnOff

class DISHWASHER:
    def __init__(self,OnOff,RunCycle,StartStop):
        #controls power state of the device
        self.OnOff = OnOff
        #controls various modes that can be chosen
        self.RunCycly = RunCycle
        #controls starting and stopping dishwasher
        self.StartStop = StartStop

class DOOR:
    def __init__(self,LockUnlock,OpenClose):
        #controls lock state of the door
        self.LockUnlock = LockUnlock
        #controls opening and closing of the doors
        self.OpenClose = OpenClose

class GARAGE:
    def __init__(self,LockUnlock,OpenClose):
        #controls lock state of the door
        self.LockUnlock = LockUnlock
        #controls opening and closing of the door
        self.OpenClose = OpenClose

class HOOD:
    def __init__(self,Brightness,FanSpeed,OnOff):
        #controls brightness of the light in the hood
        self.Brightness = Brightness
        #controls fan speed of the hood
        self.FanSpeed = FanSpeed
        #controls power state of the device
        self.OnOff = OnOff

class LIGHT:
    def __init__(self,ColorSetting,Brightness,OnOff):
        #ColorSetting sets colour of the lights if possible
        self.ColorSetting = ColorSetting
        #controls the brightness of the lights
        self.Brightness = Brightness
        #Controls power state of the device
        self.OnOff = OnOff

class MICROWAVE:
    def __init__(self,Cook,Timer,StartStop):
        #controls cooking mode
        self.Cook = Cook
        #controls timer of the microwave
        self.Timer = Timer
        #controls starting and stopping of the device
        self.StartStop = StartStop

class MOWER:
    def __init__(self,Dock,EnergyStorage,Locator,OnOff,RunCycle,StartStop):
        #checks if device is docked
        self.Dock = Dock
        #defines remaining battery power
        self.EnergyStorage = EnergyStorage
        #responsible for handling location of the device
        self.Locator = Locator
        #controls power state of the device
        self.OnOff = OnOff
        #controls modes of the mower
        self.RunCycle = RunCycle
        #control starting and stopping the mower
        self.StartStop = StartStop

class SPEAKER:
    def __init__(self,AppSelector,InputSelector,MediaState,OnOff,TransportControl,Volume):
        #select applications
        self.AppSelector = AppSelector
        #select input settings
        self.InputSelector = InputSelector
        #handling currently playing stuff, portability
        self.MediaState = MediaState
        #handling device power state
        self.OnOff = OnOff
        #controls media playback
        self.TransportControl = TransportControl
        #responsible for handling volume setting
        self.Volume = Volume



def nory(usr_input):
    #checks if user enters an affirmative answer
    NORY=["Y","T","TAK","YES","YE","TA"]
    if usr_input.upper() in NORY:
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
    #checks starting time to measure execution time
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