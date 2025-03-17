# TP3_EMSY_1
TP3_EMSY_BSH_HMT

--------------------

Réponse aux questions théoriques.

**Q1. Quel est le protocole de communication permettant de vous connecter à distance à la BBG ?**

Pour communiquer à notre BBG, on règle notre Putty en mode de communication SSH (The Secure Shell)

SSH uses cryptography to authenticate and encrypt connections between devices.

**Q2. Dans le modèle OSI, à quoi correspond ce protocole (numéro et nom de la couche) ?**

Le SSH prend la couche Application qui est le numéro 7.

**Q3. Sur cette couche spécifique, le protocole utilisé à la question Q1 fait référence à quel(s) autre(s)
protocole(s) et port(s) ?**

On pourais utilisé les protocoles FTP SFTP

**Q4. Lors de votre connexion, dans quel répertoire vous trouvez-vous ? quelle(s) commande(s)
utilisez-vous (complète) ?**

debian@BBG004:~$

le "~" nous indique que on fonctione actuellement sure le "working directory", ou simplement sure le Home.

**5. Créez un répertoire à cet emplacement que vous nommerez : TP3_XXX_YYY 
X et Y représentent vos initiales si vous êtes en binômes**

sudo nano TP3_BSH_HMT

Q5. Quelle(s) commande(s) utilisez-vous pour créer ce répertoire et qui a les droits d’écriture
dessus ?

sudo

Q6. Comment contrôlez-vous qu’un logiciel soit bien installé ? Quelle(s) est/sont les commandes 
pour installer un logiciel (prenez l’exemple de Nano) ?

nano --version

Q7. Réalisez un schéma de principe réseau montrant comment est câblé votre BBG au réseau bleu 
de l’école
