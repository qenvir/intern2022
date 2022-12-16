**Python Snake Arduino Game**

_Jeu de serpent en python avec l'implémentation de arduino pour le déplacement sur la carte avec un joystick_

# Informations:

## Arduino (arduino.ino) :

* L'axe X du joystick doit être situé sur le port A5
* L'axe Y du joystick doit être situé sur le port A6
* Le relais doit être placé sur le port A4. (Non obligatoire, il ne sers à rien dans le code du snake mais peut servir pour l'implémentation de divers modules pour rendre le jeu meilleur ou plus comprehensible avec des bruits lors de déclanchements d'objets dans le jeu, libres à vous de rajouter ce que vous voulez)

(Le tout reste quand même modifiable à tout moment dans le fichier `arduino.ino`)

## Python (main.py) :

* Le nom du port dans le fichier par défaut est "COM5". Ce paramètre est à modifier.
* Pour quitter la fenêtre, il surffit d'appuyer sur échap.

# Installation :

## Arduino (arduino.ino) :

* Téléchargez le fichier `arduino.ino` et mettez le dans un dossier présent sur le bureau.

* Ouvrez ce dossier et ouvrez le fichier `arduino.ino`

* Branchez le joystick sur les bonnes cases
    1. Brancher le G du joystick sur le GND de la carte Arduino
    2. Brancher le V du joystick sur le 5V de la carte Arduino
    1. Brancher le X et le Y du joysyick (à voir dans les `informations`)

* Dans l'Arduino IDE, vérifiez que ce sois le bon code puis téléversez le code sur la carte Arduino avec le bouton présent en haut à gauche représenté par une flèche

C'est fini du côté de Arduino, le code est prêt pour être lu par Python

Si vous souhaitez savoir si votre code est correctement en route:

* Ouvrez votre serial monitor dans l'onglet "Tools". Le débit du serial du code est de 57600 bps, Vous devez donc calibrer votre console à 57600 baud pour pouvoir lire le contenu du Serial. Il suffit de cliquer sur les paramètres des baud en haut à droite de la console est sélectionner 57600 baud.
  1. `Tools>SerialMonitor`
  2. `Sélectionner le bps`
  3. `9600 baud>57600 baud`


* Le console doit afficher l'une de ces cinq varientes:

  ```
  0,0
  1,0
  -1,0
  0,1
  0,-1
  ```

## Python (main.py) :

* Téléchargez le fichier `main.py` et mettez le dans un dossier présent sur le bureau.

* Ouvrez le fichier `main.py` avec PyCharm disponible sur le bureau de l'ordinateur.

* Changez le port "COM5" sur la ligne 14 et le baudrate si vous l'aviez changé auparavant dans le code de l'Arduino

* Débranchez l'arduino de l'odinateur et fermez l'Arduino IDE

* Rebreanchez l'arduino dans l'odinateur en vous assurant que l'arduino IDE n'est plus lancé

* Lancez le code en appuyant sur le triangle vert en haut à droite

(En cas d'erreur avec le port, vérifiez bien toutes les étapes et si le problème persiste appelez votre tuteur)

# Jouer ?

* Principe


Le principe du jeu est le même que celui du très connu, snake

* Comment jouer

Pour jouer il suffit de prendre le joystick avec les câbles vers le bas et de simplement tourner dans le sens que l'on veut pour se déplacer. Attention, lors de la mort de votre serpent le programme va automatiquement se fermer et vous devez le rouvrir pour recommencer le jeu.

# Idées

* Facile: Ecran de mort

Lorsque le serpent meurt, un écran de mort s'affiche et permet de relancer le jeu à zero lorsqu'on appui sur une touche prédéfinie

* Intermédiaire: Menu de démarrage

Lorqu'on lance le programme, on peut choisir quelques paramètres (couleur du serpent, vitesse, mode de jeu, nombre de pommes, couleure de la pomme...) dans un menu puis lancer la partie avec ces différents paramètres

* Expert: Super-pouvoirs

En partie, il y a une petite chance que un super-pouvoir d'une couleur qui défile apparaisse et donne un pouvoir d'invicibilité ou de vitesse au serpent pendant un temps donné

# Fin / Ajout de votre code:

Vous souhaitez ajouter votre code pour que le prochain ne repart pas de ce code mais bien du votre ?
C'est bien simple, suivez le petit tutoriel présent si-dessous

## Comment ?

* **Première façon**

Demandez à votre tuteur d'ajouter une branche à cette repository et déposez-y votre code, les prochains pourront changer de branche et aller voir toutes les choses qui ont été résalisés à partir ce code de base

* **Deuxième façon**

La deuxième façon est de créer votre repository sur le gitlab de Qenvi ou sur le site officiel de Github en écrivant une rapide documentation sur votre code, vous pouvez biensûr vous baser sur ce tutoriel et ajouter ce que vous avez fait au code à partir du moment ou vous l'avez téléchargé.
