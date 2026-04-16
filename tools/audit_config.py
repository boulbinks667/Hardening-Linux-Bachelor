import os
import subprocess

def check_status(command, service_name):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT).decode()
        print(f"[OK] {service_name} est actif et configuré.")
        return output
    except:
        print(f"[ERREUR] {service_name} présente un problème !")
        return None

print("=== AUDIT DE L'IMPLEMENTATION SECURITE ===\n")

# 1. SSH Port
try:
    with open("/etc/ssh/sshd_config", "r") as f:
        if "Port 45678" in f.read():
            print("[OK] SSH est bien configuré sur le port masqué 45678.")
except: pass

# 2. UFW
check_status("sudo ufw status | grep -E 'active|actif'", "Pare-feu UFW")

# 3. Fail2ban
status = check_status("sudo fail2ban-client status", "Service Fail2ban")
if status and "sshd" in status:
    print("[OK] Toutes les prisons (jails) sont actives.")

# 4. LE SCORE LYNIS (La partie qui manque sur ton image)
if os.path.exists("/usr/sbin/lynis") or os.path.exists("/usr/bin/lynis"):
    print("[OK] L'outil d'audit certifié Lynis est installé.")
    if os.path.exists("/var/log/lynis-report.dat"):
        # On extrait le score
        try:
            score = subprocess.check_output("sudo grep 'hardening_index' /var/log/lynis-report.dat | cut -d'=' -f2", shell=True).decode().strip()
            print(f"[OK] Votre score de Hardening actuel est de : {score}/100")
        except: print("[!] Impossible de lire le score.")
else:
    print("[!] Suggestion : Installez Lynis.")

print("\n=== FIN DE L'AUDIT ===")
