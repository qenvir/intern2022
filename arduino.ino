/**
  * Copyright (c) 2022 and later Qenvi.
  * Developed by Qenvi and affiliates which hold all
  * intellectual property rights. Use of this software is subject
  * to a specific license granted by Qenvi.
  */

#define JoyStick_X A5
#define JoyStick_Y A6
#define Relay A4 //(Non obligatoire)

void setup() {
  pinMode(JoyStick_X, INPUT);
  pinMode(JoyStick_Y, INPUT);
  // Enlever le commentaire si l'on veut accèder au relai
  //pinMode(Relay, OUTPUT);
  Serial.begin(57600);
}

void loop() {
  int x,y;
  x=analogRead(JoyStick_X);
  y=analogRead(JoyStick_Y);

  int displayX = 0;
  int displayY = 0;

  if(x > 1000){
    displayX = 1;
  } else if (x < 100) {
    displayX = -1;
  }

  if(y > 1000){

    displayY = -1;
  } else if (y < 100) {
    displayY = 1; 
  }
  
  Serial.print(displayX);
  Serial.print(",");  
  Serial.println(displayY);
  
  delay(250);  
}
