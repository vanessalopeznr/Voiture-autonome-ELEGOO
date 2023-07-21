// Define L298N module IO pin
#define ENA 5
#define ENB 6
#define IN1 7
#define IN2 8
#define IN3 9
#define IN4 11
int pause=70;

void stop() {
  digitalWrite(ENA,LOW);
  digitalWrite(ENB,LOW);
  Serial.println("Stop");
}

void width(String command){
  if (command=="right") {
    digitalWrite(ENA,HIGH);
    digitalWrite(ENB,HIGH);
    digitalWrite(IN1,HIGH);
    digitalWrite(IN2,LOW);
    digitalWrite(IN3,HIGH);
    digitalWrite(IN4,LOW);
    Serial.println("rotate right");
    delay(pause);
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
    delay(pause);
    stop();
  }
  else {
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
  if (Serial.available() > 0) { //The number of bytes that Arduino receive in buffer
    String message = Serial.readStringUntil('_');
    Serial.print(message);
    Serial.print('\n');
    int index = message.indexOf('/');
    int last = message.length();
    String cmd_width = message.substring(0,index);
    String cmd_height = message.substring(index+1,last);
    width(cmd_width);
  }

}
