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

## 📁 Structure du Projet

- **[configs/](./configs)** : Fichiers de configuration de référence (Fail2ban, UFW).
- **[scripts/](./scripts)** : Scripts Bash d'automatisation de l'installation.
- **[tools/](./tools)** : Outils Python pour l'audit et l'analyse de sécurité.
- **README.md** : Documentation et rapport de projet.

## 🚀 Utilisation des outils

Pour lancer l'audit de conformité :
`sudo python3 tools/audit_config.py`

Pour lancer l'analyseur de logs :
`sudo python3 tools/security_analyzer.py`
