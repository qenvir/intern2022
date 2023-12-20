/**
  * Copyright (c) 2022 and later Qenvi.
  * Developed by Qenvi and affiliates which hold all
  * intellectual property rights. Use of this software is subject
  * to a specific license granted by Qenvi.
  */

// On définit JoyStick_X à A5 qui est le port sur lequel il est branché
#define JoyStick_X A5
// On définit JoyStick_Y à A6 qui est le port sur lequel il est branché
#define JoyStick_Y A6
#define Relay A4 //(Non obligatoire)

void setup() {
  // On définit les joystick en input (c'est à dire qu'ils vont envoyer des informations vers l'arduino)
  pinMode(JoyStick_X, INPUT);
  pinMode(JoyStick_Y, INPUT);
  // Enlever le commentaire si l'on veut accèder au relai
  //pinMode(Relay, OUTPUT);

  // On définit la fréquence du serial à 57600
  Serial.begin(57600);
}

void loop() {
  // On définit x et y
  int x,y;

  // On lis les valeurs x et y du joystick et on les assigne aux valeurs précédentes
  x=analogRead(JoyStick_X);
  y=analogRead(JoyStick_Y);

  // On définit les valuers que l'on va print
  int displayX = 0;
  int displayY = 0;

  if(x > 1000){
    // Si x (qui est l'inclinaison du joystick) est supérieur à 1000 on met la valeur displayX à 1
    displayX = 1;
  } else if (x < 100) {
    // Si x (qui est l'inclinaison du joystick) est inférieur à 100 on met la valeur displayX à -1
    displayX = -1;
  }

  if(y > 1000){
    // Si y (qui est l'inclinaison du joystick) est supérieur à 1000 on met la valeur displayY à -1
    displayY = -1;
  } else if (y < 100) {
    // Si y (qui est l'inclinaison du joystick) est inférieur à 100 on met la valeur displayY à 1
    displayY = 1; 
  }
  
  // On print les deux valeurs x et y pour que Python puisse les lire
  Serial.print(displayX);
  Serial.print(",");  
  Serial.println(displayY);
  
  // Délai
  delay(250);  
}
