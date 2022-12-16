#include <TimerOne.h>

//int led4 = 4;
//#define led4 4
#define JoyStick_X A5 //x
#define JoyStick_Y A6 //x
//#define JoyStick_Z A3 //Boutton
#define Relay A4

//int xpos, ypos;
//bool mooved;
int buzzInt = 0;
bool buzzBool = false;
String data = "";

void setup() {
  //pinMode(led4, OUTPUT);
  pinMode(JoyStick_X, INPUT);
  pinMode(JoyStick_Y, INPUT);
  //pinMode(JoyStick_Z, INPUT);
  pinMode(Relay, OUTPUT);
  Serial.begin(57600); // 9600 bps
  //tRelay = 0;
  //xpos = 0;
  //ypos = 0;
  //mooved = false;
}

void loop() {
  
  // put your main code here, to run repeatedly:
  /*digitalWrite(led4, HIGH);
  delay(1000);
  digitalWrite(led4, LOW);
  delay(1000);*/

  
  //z=digitalRead(JoyStick_Z);
  
  /*int xmap,ymap;
  xmap = map(x, 0, 1023, -100, 100);
  ymap = map(y, 0, 1023, -100, 100);
  Serial.print("x:");
  Serial.print(x ,DEC);
  Serial.print(",");
  Serial.print("y:");
  Serial.println(y ,DEC);
  delay(100);*/

  

  //if(xpos < 0) xpos = 12;
  //if(xpos > 12) xpos = 0;
  //if(ypos < 0) ypos = 12;
  //if(ypos > 12) ypos = 0;

  /*
  String data = "";
  while(Serial.available()) {
    data += Serial.readString();
  }

  if(data == "on") {
    buzzBool = true;
  }
  */

  

  /*
  if(mooved){
    //displayMap();
    mooved = false;
  }
  */

  int x,y;
  x=analogRead(JoyStick_X);
  y=analogRead(JoyStick_Y);

  int displayX = 0;
  int displayY = 0;

  if(x > 1000){
    displayX = 1;
    //xpos = xpos + 1;
    //mooved = true;
  } else if (x < 100) {
    displayX = -1;
    //xpos = xpos - 1;
    //mooved = true;
  }

  if(y > 1000){

    displayY = -1;
    //ypos = ypos - 1;
    //mooved = true;
  } else if (y < 100) {
    displayY = 1;
    //ypos = ypos + 1;
    //mooved = true;    
  }
  
  
  Serial.print(displayX);
  Serial.print(",");  
  Serial.println(displayY);
  
  /*
  while(Serial.available()) {
    data += Serial.readString();
  }

  if(data == "on") {
    buzzBool = true;
  }
  data="";

  if(buzzBool == true)
  {
    buzzInt = 50;
    digitalWrite(Relay, HIGH);
    buzzBool = false;    
  }
  if(buzzInt <= 0)
  {
    digitalWrite(Relay, LOW);
    buzzInt = 0;
  }
  buzzInt--;
  */
  
  delay(250);  
}



/*
void OnBuzzer(){
  digitalWrite(Relay, HIGH);
  buzzBool = true;
  buzzInt = 0;
}


void buzzer(){
  if(buzzBool == true){
    if(buzzInt == 4){
      digitalWrite(Relay, LOW);
      buzzInt = 0;
      buzzBool = false;
    }
    buzzInt++;
  }
}
*/

/*
void displayMap(){

  clearMap();
  Serial.print("xpos: ");
  Serial.print(xpos);
  Serial.print(",");  
  Serial.print("ypos: ");
  Serial.println(ypos);
  for(int i = 0; i < 13; i++){
    for(int j = 0; j < 13; j++){
      if(xpos == j && ypos == i){
        Serial.print("1 ");           
      }
      else
        Serial.print("0 ");
    }
    Serial.println();
  }
}

void clearMap(){
  for(int i = 0; i < 4; i++){
      Serial.println("");
  }
}
*/