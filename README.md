#  EMSY02 – TP3: Linux Embarqué avec BeagleBone Green 
> Benjamin Schafroth et Henri Mott

## but du TP

Ce projet a pour but d’explorer l'utilisation d’un système Linux embarqué sur une BeagleBone Green (BBG), à travers diverses manipulations réseau, de configuration, de lecture de capteur, d’automatisation, et de traitement de données.

---

### Q1. Quel est le protocole de communication permettant de vous connecter à distance à la BBG ?
SSH (Secure Shell)

### Q2. Dans le modèle OSI, à quoi correspond ce protocole (numéro et nom de la couche) ?
Couche 7 – Application

### Q3. Sur cette couche spécifique, le protocole utilisé à la question Q1 fait référence à quel(s) autre(s) protocole(s) et port(s) ?
Protocole : TCP  
Port : 22

### Q4. Lors de votre connexion, dans quel répertoire vous trouvez-vous ? quelle(s) commande(s) utilisez-vous (complète) ?
Commande : `pwd`  
Répertoire : `/home/debian`

### Q5. Si vous n’arriviez pas à vous connecter à la BBG, quelle(s) commande(s), testeriez-vous depuis la machine hôte ?
- `ping <adresse_IP>`
- `telnet <adresse_IP> 22`
- `nmap <adresse_IP>`

### Q6. Sur la BBG, quelle(s) est/sont la/es commande(s) pour connaitre la configuration du réseau Ethernet ?
- `ip a`
- `ip r`
- `ip link`

a. Adresse IP : affichée par `ip a`  
b. Masque de sous-réseau : affiché par `ip a` ou avec `ifconfig`  
c. Adresse réseau : calculable avec `ipcalc`  
d. Passerelle par défaut : `ip r`  
e. MAC adresse : `ip link`

### Q7. Quelle(s) commande(s) utilisez-vous pour créer ce répertoire et qui a les droits d’écriture dessus ?
```bash
mkdir TP3_BSH_HMT
ls -ld TP3_BSH_HMT
