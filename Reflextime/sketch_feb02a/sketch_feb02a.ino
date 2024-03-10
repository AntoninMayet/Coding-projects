/*
PUL+ >>> 3v & DIR+
PUL- >>> D7
DIR- >>> 6~
ENA+ >>> D5~

List of errors:
- Error 1: the motor was disable but the programm want it to move 
*/

// called it a day on line 176

#include <Wire.h> //I don't know what's its use but need to be here 😅
#include <LiquidCrystal_I2C.h>

#define upButton 1
#define rightButton 2
#define downButton 3
#define leftButton 4

#define homeButton 8

const int numberCarLCD = 16;
const int calcultatedNumberOfRotation; //Need to calculate how much rotation are needed to
//go from the home position to the other end. We'll then compare the calculatedNb and compare it
//to the reel one
int numberOfRotations = 0;


float dlais = 250; //is used to control the speed of the motor
int steps = 1600; //is used to know how many steps are in a full rotation of the rotor

char ans;
char stateOfTheMotor = 'D'; // will always be E or D (enable/disable)

int PUL=7; //those three lines are used to tell how to communicate with the driver
int DIR=6; //when the code will work, change this to #define and move it to the #define block
int ENA=5;

LiquidCrystal_I2C lcd(0x27, 20, 4); //set the LCD adress for a 16/2

byte upPoitingArrow[8] = {
  0b00100,
  0b01110,
  0b11111,
  0b00100,
  0b00100,
  0b00100,
  0b00100,
  0b00100
};

byte rightPointingArrow[8] = {
  0b00000,
  0b00100,
  0b00110,
  0b11111,
  0b11111,
  0b00110,
  0b00100,
  0b00000
};

byte downPointingArrow[8] = {
  0b00100,
  0b00100,
  0b00100,
  0b00100,
  0b00100,
  0b11111,
  0b01110,
  0b00100
};

byte leftPointingArrow[8] = {
  0b00000,
  0b00100,
  0b01100,
  0b11111,
  0b11111,
  0b01100,
  0b00100,
  0b00000
};

void setup()
{
  lcd.createChar(0, "upPoitingArrow"); //not sure if that will work over I2C
  lcd.createChar(1, "rightPoitingArrow");
  lcd.createChar(2, "downPointingArrow");
  lcd.createChar(3, "leftPointingArrow");
  lcd.init();
  lcd.backlight();
  lcd.rightToLeft(); //change to leftToRight if the text scrolls in the wrong direction
  lcd.setCursor(0,0);
  lcd.print("<void setup>");

  pinMode (PUL, OUTPUT);
  pinMode (DIR, OUTPUT);
  pinMode (ENA, OUTPUT);
  pinMode(13, OUTPUT); //I think this pin isn't plug to anything. If it's true I can remove this line and the one after
  digitalWrite(13, LOW);

  lcd.clear();
  lcd.print("</void setup>");
  lcd.clear();
}

void turnClockwise(int nbTurn)
{
  for (int i=0; i<nbTurn*steps; i++)
  {
    digitalWrite(DIR,HIGH);
    digitalWrite(ENA,HIGH);
    digitalWrite(PUL,HIGH);
    delayMicroseconds(dlais);
    digitalWrite(PUL,LOW);
    delayMicroseconds(dlais);
    numberOfRotations ++;
  }
}

void turnCounterClockwise(int nbTurn)
{
  for (int i=0; i<(nbTurn*steps); i++)
  {
    digitalWrite(DIR,LOW);
    digitalWrite(ENA,HIGH);
    digitalWrite(PUL,HIGH);
    delayMicroseconds(dlais);
    digitalWrite(PUL,LOW);
    delayMicroseconds(dlais);
    numberOfRotations --;
  } 
}

void clearLCDLine(int lineToErase)
{

  lcd.setCursor(lineToErase, 0);

  for(int n = 0; n < numberCarLCD; n++)
  {
    lcd.print(" ");
  }
}

Char askYesOrNoQuestion(char phrase) //returns 'y' or 'n'
{
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print(phrase)
  lcd.setCursor(0, 1);
  lcd.print((byte)4);//This is just a test, I'm not sure it will work
  lcd.setCursor(2, 1);
  lcd.print("Yes");
  lcd.setCursor(16, 1);
  lcd.print((byte),2);
  lcd.setCursor(12, 1);
  lcd.print("No");

  if (leftButton == HIGH)
  {
    char ans = y;
  }
  else if (rightButton == HIGH)
  {
    char ans = n;
  }
  return ans;
}

void homingSequence()
{
  if askYesOrNo("You have entered the homing sequence") == 'y'
  {
    lcd.print("The motor will be disable while you presse the ""up"" button");
    motorToggler("disable");
  }
}

String motorChecker() //returns "can move" or "Error 1"
{
  if stateOfTheMotor == 'E'
  {
    return "can move";
  }
  else if stateOfTheMotor == 'D'
  {
    return "Error 1";
  }
}

void motorToggler(string state) //takes "disbale" or "enable"
{
  if state == "disable"
  {
    digitalWrite(PUL, LOW);
    digitalWrite(DIR, LOW);
    digitalWrite(ENA, LOW);
    stateOfTheMotor == 'D';
  }
  else if state == "enable"
  {
    digitalWrite(PUL, HIGH);
    digitalWrite(DIR, HIGH);
    digitalWrite(ENA, HIGH);
    stateOfTheMotor == 'E'; 
  }
}

void loop()
{
  //need to make a function that catch errors

  turnClockwise(1); //those 4 lines are just to test two functions
  delay(1000);
  turnCounterClockwise(1);
  delay(1000);
}