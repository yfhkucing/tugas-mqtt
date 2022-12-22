#include "MQ135.h"
#define RLOAD 1.0
#define RZERO 80.1
int MQ2pin = A0;
int sensorValueQ2;
#include <OneWire.h>
#include <DallasTemperature.h>

OneWire pin_DS18B20(8);
DallasTemperature DS18B20(&pin_DS18B20);
void setup() {
// put your setup code here, to run once:
Serial.begin(9600);
DS18B20.begin();
}
void loop() {
// put your main code here, to run repeatedly:
MQ135 gasSensor = MQ135(A0);
float rzero = gasSensor.getRZero();
//sensorValueQ2 = analogRead(MQ2pin);
//Serial.print(sensorValueQ2);
float ppm = gasSensor.getPPM();
Serial.print(ppm);
Serial.print(",");
DS18B20.requestTemperatures();
Serial.print(DS18B20.getTempCByIndex(0));
Serial.print(",");
float random_ph = random(50,100);
float ph = random_ph/10;
Serial.print(ph); //PH
Serial.print(",");
float random_amonia = random(0,25);
float amonia = random_amonia/100;
Serial.print(amonia); //Amonia
Serial.print(",");
float random_do = random(30,120);
float dis_oks = random_do/10;
Serial.print(dis_oks); //DO
Serial.print(",");
float random_nitrit = random(0,3);
float nitrit = random_nitrit/100;
Serial.println(nitrit); //Nitrit
delay(200);
}