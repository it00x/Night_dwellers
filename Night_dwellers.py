import nmap
nmScan = nmap.PortScanner()

def main():
    myIP = nmScan.all_hosts()
    print(myIP)

if __name__=="__main__":
    main()