// Define L298N module IO pin
#define ENA 5
#define ENB 6
#define IN1 7
#define IN2 8
#define IN3 9
#define IN4 11
String cmd_width="None";
String cmd_height="None";
String buscar="None";

void stop() {
  digitalWrite(ENA,LOW);
  digitalWrite(ENB,LOW);
  Serial.println("Stop");
}

void rotate(String command){
  if (command=="right") {
    digitalWrite(ENA,HIGH);
    digitalWrite(ENB,HIGH);
    digitalWrite(IN1,HIGH);
    digitalWrite(IN2,LOW);
    digitalWrite(IN3,HIGH);
    digitalWrite(IN4,LOW);
    Serial.println("rotate right");
    delay(65);
    stop();
  }
  else if (command=="left"){
    digitalWrite(ENA,HIGH);
    digitalWrite(ENB,HIGH);
    digitalWrite(IN1,LOW);
    digitalWrite(IN2,HIGH);
    digitalWrite(IN3,LOW);
    digitalWrite(IN4,HIGH);
    Serial.println("rotate left");
    delay(65);
    stop();
  }
  else if (command=="nada") {
    digitalWrite(ENA,HIGH);
    digitalWrite(ENB,HIGH);
    digitalWrite(IN1,HIGH);
    digitalWrite(IN2,LOW);
    digitalWrite(IN3,HIGH);
    digitalWrite(IN4,LOW);
    Serial.println("rotate right");
    delay(200);
    stop();
  }
  else {
    stop();
  }
}

void advance(String command){
  if (command=="fast") {
    analogWrite(ENA,255);
    analogWrite(ENB,255);
    digitalWrite(IN1,HIGH);
    digitalWrite(IN2,LOW);
    digitalWrite(IN3,LOW);
    digitalWrite(IN4,HIGH);
    Serial.println("fast");
    delay(250);
    stop();
  }
  else if (command=="normal") {
    analogWrite(ENA,200);
    analogWrite(ENB,200);
    digitalWrite(IN1,HIGH);
    digitalWrite(IN2,LOW);
    digitalWrite(IN3,LOW);
    digitalWrite(IN4,HIGH);
    Serial.println("normal");
    delay(250);
    stop();
  }
  else {
    analogWrite(ENA,150);
    analogWrite(ENB,150);
    digitalWrite(IN1,HIGH);
    digitalWrite(IN2,LOW);
    digitalWrite(IN3,LOW);
    digitalWrite(IN4,HIGH);
    Serial.println("slow");
    delay(250);
    stop();
  }
}

void setup() {
  Serial.begin(115200);
  while(!Serial){}
  pinMode(IN1,OUTPUT); 
  pinMode(IN2,OUTPUT);
  pinMode(IN3,OUTPUT);
  pinMode(IN4,OUTPUT);
  pinMode(ENA,OUTPUT);
  pinMode(ENB,OUTPUT);
  stop();

}

void loop() {
  //Verify message by serial communication
  if (Serial.available() > 0) { //The number of bytes that Arduino receive in buffer
    String message = Serial.readStringUntil('_');
    int index = message.indexOf('/');
    int index2 = message.indexOf(':');
    int last = message.length();
    cmd_width = message.substring(0,index);
    cmd_height = message.substring(index+1,index2);
    buscar = message.substring(index2+1,last);

    if (buscar=="nada"){
      rotate("nada");
    }
    else {
      if (cmd_width=="None"){
        advance(cmd_height);
      }
      else {
        rotate(cmd_width);
      }
    }
   
  }
}
