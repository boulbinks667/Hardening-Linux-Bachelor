
import os
import subprocess

def check_status(command, service_name):
    try:
        # On exécute la commande et on récupère le résultat
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT).decode()
        print(f"[OK] {service_name} est actif et configuré.")
        return output
    except:
        print(f"[ERREUR] {service_name} présente un problème !")
        return None

print("=== AUDIT DE L'IMPLEMENTATION SECURITE ===\n")

# 1. Vérification du Port SSH
try:
    with open("/etc/ssh/sshd_config", "r") as f:
        config = f.read()
        if "Port 45678" in config:
            print("[OK] SSH est bien configuré sur le port masqué 45678.")
        else:
            print("[!] ATTENTION : Le port SSH n'est pas le bon !")
except:
    print("[ERREUR] Impossible de lire la configuration SSH.")

# 2. Vérification UFW (Français et Anglais)
check_status("sudo ufw status | grep -E 'active|actif'", "Pare-feu UFW")

# 3. Vérification Fail2ban
status = check_status("sudo fail2ban-client status", "Service Fail2ban")
if status:
    if "sshd" in status and "ufw-scan" in status:
        print("[OK] Toutes les prisons (jails) sont actives.")

# 4. Vérification de Lynis et affichage du score
if os.path.exists("/usr/bin/lynis"):
    print("[OK] L'outil d'audit certifié Lynis est installé.")
    try:
        # On va chercher la ligne hardening_index dans le rapport
        score = subprocess.check_output("sudo grep 'hardening_index' /var/log/lynis-report.dat | cut -d'=' -f2", shell=True).decode().strip()
        print(f"[OK] Votre score de Hardening actuel est de : {score}/100")
    except:
        print("[!] Rapport Lynis introuvable. Lancez 'sudo lynis audit system'.")
else:
    print("[!] Suggestion : Installez Lynis.")

print("\n=== FIN DE L'AUDIT ===")
