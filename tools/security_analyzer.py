import re
from collections import Counter

def analyze_logs():
    print("=== RAPPORT D'ANALYSE DES MENACES ===")
    
    # 1. Analyse des Brute Force SSH
    try:
        with open("/var/log/auth.log", "r") as f:
            log = f.read()
            ips = re.findall(r"Failed password for .* from ([0-9.]+)", log)
            print(f"\n[!] Tentatives Brute Force SSH détectées : {len(ips)}")
            for ip, count in Counter(ips).items():
                print(f" -> IP: {ip} | Essais: {count}")
    except: print("[-] Impossible de lire auth.log")

    # 2. Analyse des Scans de ports (UFW)
    try:
        with open("/var/log/syslog", "r") as f:
            log = f.read()
            scans = re.findall(r"\[UFW BLOCK\].*SRC=([0-9.]+)", log)
            print(f"\n[!] Scans de ports bloqués : {len(scans)}")
            for ip, count in Counter(scans).items():
                print(f" -> IP: {ip} | Paquets bloqués: {count}")
    except: print("[-] Impossible de lire syslog")

if __name__ == "__main__":
    analyze_logs()
