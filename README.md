# 🛡️ Hardening d'un Serveur Linux (Défense en Profondeur)

Ce projet illustre la mise en place d'une architecture de sécurité multicouche sur un serveur Ubuntu 24.04 LTS.

## 🏗️ Architecture de Sécurité
1. **Dissimulation :** Port SSH déplacé sur le port **45678**.
2. **Authentification :** Désactivation des mots de passe, usage exclusif de clés SSH.
3. **Pare-feu (UFW) :** Politique "Deny All" avec journalisation active.
4. **Défense Active (Fail2ban) :** - Protection SSH (Mode agressif).
   - Protection Anti-scan de ports (Détection via logs UFW).

## 🛠️ Validation
- ✅ Scan Nmap détecté et banni après 5 tentatives.
- ✅ Tentatives SSH non-autorisées bannies définitivement.
### 📜 Journal des commandes de sécurisation

**Pare-feu UFW :**
- `sudo ufw default deny incoming`
- `sudo ufw allow 45678/tcp`

**Fail2ban :**
- `sudo fail2ban-client status sshd`
- `sudo fail2ban-client status ufw-scan`
