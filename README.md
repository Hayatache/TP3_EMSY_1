#  EMSY02 – TP3: Linux Embarqué avec BeagleBone Green 
> Benjamin Schafroth et Henri Mott

## but du TP

Ce projet a pour but d’explorer l'utilisation d’un système Linux embarqué sur une BeagleBone Green (BBG), à travers diverses manipulations réseau, de configuration, de lecture de capteur, d’automatisation, et de traitement de données.

---

### Q1. Protocole de communication permettant de vous connecter à distance à la BBG ?
SSH (Secure Shell)

### Q2. À quoi correspond ce protocole dans le modèle OSI (numéro et nom de la couche) ?
Couche 7 – Application

### Q3. Le protocole utilisé à la question 1 fait référence à quel autre protocole et port ?
Protocole : TCP  
Port : 22

### Q4. Lors de votre connexion, dans quel répertoire vous trouvez-vous ? quelle(s) commande(s) utilisez-vous (complète) ?
Commande : `pwd`  
Répertoire : `/home/debian`

### Q5. Si vous n’arriviez pas à vous connecter à la BBG, quelle commande, testeriez-vous depuis la machine hôte ?
- `ping <adresse_IP>`
- `telnet <adresse_IP> 22`
- `nmap <adresse_IP>`

### Q6. Sur la BBG, quelles sont les commandes pour connaitre la configuration du réseau Ethernet ?
- `ip a`
- `ip r`
- `ip link`

a. Adresse IP : affichée par `ip a`  
b. Masque de sous-réseau : affiché par `ip a` ou avec `ifconfig`  
c. Adresse réseau : calculable avec `ipcalc`  
d. Passerelle par défaut : `ip r`  
e. MAC adresse : `ip link`

### Q7. Quelles commandes utilisez-vous pour créer ce répertoire et qui a les droits d’écriture dessus ?
```bash
mkdir TP3_BSH_HMT
ls -ld TP3_BSH_HMT
```
### Q8. Vérification et installation d’un logiciel (exemple : `nano`)
#### verification si un logiciel est installé ?

Utilisez la commande suivante pour vérifier si le logiciel `nano` est présent :
```bash
Nano --version
```
#### installation si un logiciel n'est pas installer (exemple : `nano`)
```bash
sudo apt-get update
```
```bash
sudo apt-get install nano
```

#### lecture d'un fichier sans utiliser nano
```bash
cat mon_fichier.txt
```
### Q9. schéma de principe réseau
![Image non disponible pour jsp quel raison](docs/schema_de_principe.png)
