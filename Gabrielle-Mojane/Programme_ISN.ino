#define NOTE_DO 261,63
#define NOTE_RE 293,66
#define NOTE_MI 329,63
#define NOTE_FA 349,23
#define NOTE_SOL 392,00
#define NOTE_LA 440,00
#define NOTE_SI 493,88

#define ACTIVATED LOW 

const int PIEZO = 11;
const int LED = 13;

const int BUTTON_DO = 10;
const int BUTTON_RE = 9;
const int BUTTON_MI = 8;
const int BUTTON_FA = 7;
const int BUTTON_SOL = 6;
const int BUTTON_LA = 5;
const int BUTTON_SI = 4;



void setup()
{
  pinMode(LED, OUTPUT);
  pinMode(BUTTON_C, INPUT);
  digitalWrite(BUTTON_C,HIGH);
  pinMode(BUTTON_D, INPUT);
  digitalWrite(BUTTON_D,HIGH);
  pinMode(BUTTON_E, INPUT);
  digitalWrite(BUTTON_E,HIGH);
  pinMode(BUTTON_F, INPUT);
  digitalWrite(BUTTON_F,HIGH);
  pinMode(BUTTON_G, INPUT);
  digitalWrite(BUTTON_G,HIGH);
  pinMode(BUTTON_A, INPUT);
  digitalWrite(BUTTON_A,HIGH);
  pinMode(BUTTON_B, INPUT);
  digitalWrite(BUTTON_B,HIGH);
  
  digitalWrite(LED,LOW);
}

void loop()
{
  while(digitalRead(BUTTON_DO) == ACTIVATED)
  {
    tone(PIEZO,NOTE_DO);
    digitalWrite(LED,HIGH);
  }

  while(digitalRead(BUTTON_RE) == ACTIVATED)
  {
    tone(PIEZO,NOTE_RE);
    digitalWrite(LED,HIGH);
  }

  while(digitalRead(BUTTON_MI) == ACTIVATED)
  {
    tone(PIEZO,NOTE_MI);
    digitalWrite(LED,HIGH);
  }

  while(digitalRead(BUTTON_FA) == ACTIVATED)
  {
    tone(PIEZO,NOTE_FA);
    digitalWrite(LED,HIGH);
  }

  while(digitalRead(BUTTON_SOL) == ACTIVATED)
  {
    tone(PIEZO,NOTE_SOL);
    digitalWrite(LED,HIGH);
  }

  while(digitalRead(BUTTON_LA) == ACTIVATED)
  {
    tone(PIEZO,NOTE_LA);
    digitalWrite(LED,HIGH);
  }

  while(digitalRead(BUTTON_SI) == ACTIVATED)
  {
    tone(PIEZO,NOTE_SI);
    digitalWrite(LED,HIGH);
  }

  noTone(PIEZO);
  digitalWrite(LED,LOW);

}
