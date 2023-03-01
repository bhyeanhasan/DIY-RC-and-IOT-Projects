
#include <LiquidCrystal_I2C.h>
#include <ESP8266WiFi.h>
#include <DHT.h>
#include <SFE_BMP180.h>

//Initialize the LCD display
LiquidCrystal_I2C lcd(0x27, 16, 2);

// Create an object for the BMP180 sensor
SFE_BMP180 bmp;
DHT dht(0, DHT11);//(DHT sensor pin,sensor type)


//Define Rain and LDR pins
#define rain A0
#define light 16

//Create three variables for pressure
double T, P;
char status;

void setup() {
  Serial.begin(9600);
  bmp.begin();
  lcd.init();
  lcd.backlight();
  pinMode(light, INPUT);
    pinMode(14, OUTPUT);

  dht.begin();

  lcd.setCursor(0, 0);
  lcd.print("Weather Monitor");
  lcd.setCursor(4, 1);
  lcd.print("System");
  digitalWrite(14,LOW);
  delay(4000);
  lcd.clear();
}

//Get the DHT11 sensor values
void DHT11sensor() {
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  if (isnan(h) || isnan(t)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }


  lcd.setCursor(0, 0);
  lcd.print("T:");
  lcd.print(t);

  lcd.setCursor(8, 0);
  lcd.print("H:");
  lcd.print(h);

}

//Get the rain sensor values
void rainSensor() {
  int value = analogRead(rain);
  value = map(value, 0, 1024, 0, 100);

  lcd.setCursor(0, 1);
  lcd.print("R:");
  lcd.print(value);
  lcd.print(" ");
}

//Get the pressure values
void pressure() {
  status =  bmp.startTemperature();
  if (status != 0) {
    delay(status);
    status = bmp.getTemperature(T);

    status = bmp.startPressure(3);// 0 to 3
    if (status != 0) {
      delay(status);
      status = bmp.getPressure(P, T);
      if (status != 0) {

      }
    }
  }


  lcd.setCursor(8, 1);
  lcd.print("P:");
  lcd.print(P);
}

//Get the LDR sensor values
void LDRsensor() {
  bool value = digitalRead(light);
  Serial.println(value);

  if(value>0)
  {
     digitalWrite(14,HIGH);
  }
  delay(100);

 

}

void loop() {

LDRsensor();
pressure();
DHT11sensor();
rainSensor();
digitalWrite(14,LOW);

}
