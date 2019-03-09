/*
  The circuit:
  - Attached button pin to 2,3,4,5,7,8,9,10
  - 

  created 2019
  by Nicholas Choo
  modified 04 Feb 2019
  by Nicholas Choo
*/

// constants won't change. They're used here to set pin numbers:
const int buttonPin1 = 2;     // the number of the pushbutton pin
const int buttonPin2 = 3;     // the number of the pushbutton pin
const int buttonPin3 = 4;     // the number of the pushbutton pin
const int buttonPin4 = 5;     // the number of the pushbutton pin
const int buttonPin5 = 6;     // the number of the pushbutton pin
const int buttonPin6 = 7;     // the number of the pushbutton pin
const int buttonPin7 = 8;     // the number of the pushbutton pin
const int buttonPin8 = 9;     // the number of the pushbutton pin
const int outPin1 = 10;
const int outPin2 = 11;
const int outPin3 = 12;
const int outPin4 = 13;


char serialData;

// variables will change:
int buttonState1 = 0;         // variable for reading the pushbutton status
int buttonState2 = 0;         // variable for reading the pushbutton status
int buttonState3 = 0;         // variable for reading the pushbutton status
int buttonState4 = 0;         // variable for reading the pushbutton status
int buttonState5 = 0;         // variable for reading the pushbutton status
int buttonState6 = 0;         // variable for reading the pushbutton status
int buttonState7 = 0;         // variable for reading the pushbutton status
int buttonState8 = 0;         // variable for reading the pushbutton status

void setup() {
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin1, INPUT);
  pinMode(buttonPin2, INPUT);
  pinMode(buttonPin3, INPUT);
  pinMode(buttonPin4, INPUT);
  pinMode(buttonPin5, INPUT);
  pinMode(buttonPin6, INPUT);
  pinMode(buttonPin7, INPUT);
  pinMode(buttonPin8, INPUT);
  pinMode(outPin1, OUTPUT);
  pinMode(outPin2, OUTPUT);
  pinMode(outPin3, OUTPUT);
  pinMode(outPin4, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // read the state of the pushbutton value:
  buttonState1 = digitalRead(buttonPin1);
  buttonState2 = digitalRead(buttonPin2);
  buttonState3 = digitalRead(buttonPin3);
  buttonState4 = digitalRead(buttonPin4);
  buttonState5 = digitalRead(buttonPin5);
  buttonState6 = digitalRead(buttonPin6);
  buttonState7 = digitalRead(buttonPin7);
  buttonState8 = digitalRead(buttonPin8);

  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if (buttonState1 == HIGH) {
    Serial.println("1");
  }
  else if(buttonState2 == HIGH) {
    Serial.println("2");
  }
  else if(buttonState3 == HIGH) {
    Serial.println("3");
  }
  else if(buttonState4 == HIGH) {
    Serial.println("4");
  }
  else if(buttonState5 == HIGH) {
    Serial.println("5");
  }
  else if(buttonState6 == HIGH) {
    Serial.println("6");
  }
  else if(buttonState7 == HIGH) {
    Serial.println("7");
  }
  else if(buttonState8 == HIGH) {
    Serial.println("8");
  }else{
    Serial.println("");
  }
  if (Serial.available() > 0) //Waiting for request   
  {
    serialData = Serial.read();
    switch(serialData){
      case 'a':
        digitalWrite(outPin1, LOW);
        digitalWrite(outPin2, LOW);
        digitalWrite(outPin3, LOW);
        digitalWrite(outPin4, HIGH);
      case 'b':
        digitalWrite(outPin1, LOW);
        digitalWrite(outPin2, LOW);
        digitalWrite(outPin3, HIGH);
        digitalWrite(outPin4, HIGH);
      case 'c':
        digitalWrite(outPin1, LOW);
        digitalWrite(outPin2, HIGH);
        digitalWrite(outPin3, LOW);
        digitalWrite(outPin4, HIGH);
      case 'd':
        digitalWrite(outPin1, LOW);
        digitalWrite(outPin2, HIGH);
        digitalWrite(outPin3, HIGH);
        digitalWrite(outPin4, HIGH);
      case 'e':
        digitalWrite(outPin1, HIGH);
        digitalWrite(outPin2, LOW);
        digitalWrite(outPin3, LOW);
        digitalWrite(outPin4, HIGH);
      case 'f':
        digitalWrite(outPin1, HIGH);
        digitalWrite(outPin2, LOW);
        digitalWrite(outPin3, HIGH);
        digitalWrite(outPin4, HIGH);
      case 'g':
        digitalWrite(outPin1, HIGH);
        digitalWrite(outPin2, HIGH);
        digitalWrite(outPin3, LOW);
        digitalWrite(outPin4, HIGH);
      case 'h':
        digitalWrite(outPin1, HIGH);
        digitalWrite(outPin2, HIGH);
        digitalWrite(outPin3, HIGH);
        digitalWrite(outPin4, HIGH);
      case 'i':
        digitalWrite(outPin4, LOW);
    }
  }
}
