import os
import time
os.system("apt update && apt install -y nmap")
os.system("apt update && apt install -y git")
os.system("apt update && apt install -y wget")
os.system("apt update && apt install -y python")
os.system("apt update && apt install -y python3")
while True:    
    os.system("clear")
    print("███████╗██████╗░███████╗░█████╗░██╗░░██╗")
    print("██╔════╝██╔══██╗██╔════╝██╔══██╗██║░██╔╝")
    print("█████╗░░██████╔╝█████╗░░███████║█████═╝░")
    print("██╔══╝░░██╔══██╗██╔══╝░░██╔══██║██╔═██╗░")
    print("██║░░░░░██║░░██║███████╗██║░░██║██║░╚██╗")
    print("╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝")
    print("                      TOOL MADE BY apexvr_ ON TIKTOK")
    print("")
    print("1. Nmap Scan")
    print("2. Update")
    freakchoice = int(input(">>> "))
    if freakchoice == 2:
        os.system("apt update && apt install -y nmap")
        os.system("clear")
        os.system("apt update && apt install -y git")
        os.system("clear")
        os.system("apt update && apt install -y wget")
        os.system("clear")
        os.system("apt update && sudo apt install -y python")
        os.system("clear")
        os.system("apt update && apt install -y python3")
        while True:
            os.system("clear")
        break
    elif freakchoice == 1:
        IP = input("TARGET IP: ")
        METHOD = input("SCAN METHOD (sT, sS, Pn...): ")
        os.system(f"sudo nmap -{METHOD} {IP}")
        time.sleep(5)
