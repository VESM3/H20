// Byggt á tutorial: https://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-an-arduino/
// Náðu í DHTLib library (zip skrá) í tutorial
#include <dht.h>

//DHT11 is connected to pin 8
dht DHT;

#define sensorPin 8

//Raspberry Pi is connected to Serial 0
#define serialPi Serial

void setup() {
  serialPi.begin(9600);  //Arduino to serial monitor
}

void loop() {
  
  //Read sensor data
  int sensorData = DHT.read11(sensorPin);
  float temperature = DHT.temperature;
  
  //Send temperature float data to Raspberry Pi
  serialPi.println(temperature);
  
  //Wait for 1 seconds
  delay(1000);
}
