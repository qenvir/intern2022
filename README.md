**Python Snake Arduino Game**

_Jeu de serpent en python avec l'implémentation de arduino pour le déplacement sur la carte avec un joystick_

## Instructions:

### Arduino (arduino.ino) :

* L'axe X du joystick doit être situé sur le port A5
* L'axe Y du joystick doit être situé sur le port A6
* Le relay doit être placé sur le port A4

* Le débit sur Serial est de 57600 bps
* Vous devez donc calibrer votre console à 57600 bps pour pouvoir lire le contenu du Serial

(Cela reste quand même à tout moment modifiable dans le code arduino.ino)

### Python (main.py) :

* Le nom du port qui est lu est le port "COM5"
  Ceci est à modifier sur la ligne 5 par le port qu'on a

Il suffit de lancer le code via PyCharm et l'interface Tkinter avec le jeu apparaitera
