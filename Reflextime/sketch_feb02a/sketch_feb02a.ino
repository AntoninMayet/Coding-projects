/*
PUL+ >>> 3v & DIR+
PUL- >>> D7
DIR- >>> 6~
ENA+ >>> D5~

List of errors:
- Error 1: the motor was disable but the programm want it to move 
*/

// question to ask @ line 109

#include <Wire.h> //I don't know what's its use but need to be here 😅
#include <LiquidCrystal_I2C.h>

#define upButton 1
#define rightButton 2
#define downButton 3
#define leftButton 4
#define ENA=5 //these three lines might cause issues
#define DIR=6
#define PUL=7
#define homeButton 8

const int numberCarLCD = 16; //is to change if the LCD display is changed
const int calcultatedNumberOfRotation; //Need to calculate how much rotation are needed to
//go from the home position to the other end. We'll then compare the calculatedNb and compare it to the reel one

int savedNumberOfRotations = 0;//is used to save the number of rotation the motor has done

float dlais = 250; //is used to control the speed of the motor
int steps = 1600; //is used to know how many steps are in a full rotation of the rotor

bool isTheMotorEnable = false; // will always be E or D (enable/disable)
bool answerYesOrNo;

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

string waitForButtonPresse(str defaultButton, str lookButton, int millisBeforeDefault)//lookButton = button that we want the user to press
//take the names of the buttons and the time before... and return the one who is press
{
  for (int i=0; i<millisBeforeDefault; i++)
  {
    break;//temporary
    //needs to break when a button is pressed and return the according string
  }
}

void turnClockwise(int nbTurn)// takes the number of rotations wanted. Does it need to take the dlais at wich it turns?
{
  for (int i=0; i<nbTurn*steps; i++)
  {
    digitalWrite(DIR,HIGH);
    digitalWrite(ENA,HIGH);
    digitalWrite(PUL,HIGH);
    delayMicroseconds(dlais);
    digitalWrite(PUL,LOW);
    delayMicroseconds(dlais);
    savedNumberOfRotations ++;
  }
}

void turnCounterClockwise(int nbTurn)//same as turnClockwise()
{
  for (int i=0; i<(nbTurn*steps); i++)
  {
    digitalWrite(DIR,LOW);
    digitalWrite(ENA,HIGH);
    digitalWrite(PUL,HIGH);
    delayMicroseconds(dlais);
    digitalWrite(PUL,LOW);
    delayMicroseconds(dlais);
    savedNumberOfRotations --;
  } 
}

void clearLCDLine(int lineToErase)//takes the index of the line it needs to erase and erase it
{
  lcd.setCursor(lineToErase, 0);
  for(int n = 0; n < numberCarLCD; n++)
  {
    lcd.print(" ");
  }
}

bool askYesOrNo(string phrase) //takes the the question ask and returns 1 for "yes" and 0 for "no"
{
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print(phrase);
  lcd.setCursor(0, 1);
  lcd.print((byte)4);//This is just a test, I'm not sure it will work
  lcd.setCursor(2, 1);
  lcd.print("Yes");
  lcd.setCursor(16, 1);
  //lcd.print((byte),2);//this line is problematic
  lcd.setCursor(12, 1);
  lcd.print("No");

  millis(2500);

  if (leftButton == HIGH)
  {
    answerYesOrNo = true;
    clearLCDLine(1);
    lcd.setCursor(0,1);
    lcd.print("You have selected yes");
  }
  else if (rightButton == HIGH)
  {
    answerYesOrNo = false;
    clearLCDLine(1);
    lcd.setCursor(0,1);
    lcd.print("You have selected no");
  }
  return ans;
}

void homingSequence()
{
  askYesOrNo("You have entered the homing sequence");
  if ( answerYesOrNo == true )
  {
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("The motor will be disabled in 2.5s, take it and move it to the bottom right hand corner");
    lcd.setCursor(0,1);
    lcd.print("Hold the motor");
    millis(2500);
    motorToggler("disable");
    clearLCDLine(1);
    lcd.print("Slowly move the motor to the bottom right hand corner");
    while(digitalRead(homeButton) == HIGH) //le problème c'est que cette line n'est exécuter qu'une seule fois
    {
      motorToggler("enable");
      lcd.clear();
      lcd.setCursor(0,0);
      lcd.print("The motor is in the home position, let it go")
      lcd.setCursor(0,1);
      millis(500);
      lcd.print("Let go of the motor");
      millis(2500);
      lcd.clear();
      lcd.setCursor(0,0);
      lcd.print("Exiting homing sequence");
      millis(500);
      lcd.clear();
    }
  }
  else if ( answerYesOrNo == false )
  {
    lcd.clear();
    lcd.print("You have decided to aborted the homing sequence");
    lcd.setCursor(0,1);
    lcd.print("Aborting home seqence");
    millis(500);
    lcd.clear();
  }
}

void motorToggler(String state) //takes "disbale" or "enable", changes the state of the motor and changes isTheMotorEnable to 'D' or 'E'
{
  if (state == "disable")
  {
    digitalWrite(PUL, LOW);
    digitalWrite(DIR, LOW);
    digitalWrite(ENA, LOW);
    isTheMotorEnable = false;
  }
  else if (state == "enable")
  {
    digitalWrite(PUL, HIGH);
    digitalWrite(DIR, HIGH);
    digitalWrite(ENA, HIGH);
    isTheMotorEnable = true; 
  }
}

void loop()
{
  //need to make a function that catchs errors

  turnClockwise(1); //those 4 lines are just to test two functions
  delay(1000);
  turnCounterClockwise(1);
  delay(1000);
}