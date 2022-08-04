import Adafruit_DHT
import time
import RPi.GPIO as GPIO
import RPi.GPIO as ultra
import socket
import requests# coming soon

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11 , GPIO.OUT)    #Tempreture  LED RED  GPIO 17
GPIO.setup(13 , GPIO.OUT)    #Tempreture  LED GREEN GPIO 27
GPIO.setup(37 , GPIO.OUT)   #humidity    LED  GPIO 26
GPIO.setup(32 , GPIO.OUT)   #distance    LED  GPIO 12

dht11_sensor = Adafruit_DHT.DHT11
dht11_pin = 23  #GPIO 23         #DHT11 input
trig = 18   #GPIO 24
echo = 22   #GPIO 25
GPIO.setup(trig , GPIO.OUT)
GPIO.setup(echo , GPIO.IN)

while True:
    humidity , tempreture = Adafruit_DHT.read_retry(dht11_sensor , dht11_pin)
    if humidity is None and tempreture is None :
        print ("Error : Can't read dht11_sensor!!!")
    elif tempreture <= 31 :
        GPIO.output(11 , False)
        GPIO.output(13 , True)
    else :
        GPIO.output(13 , False)
        GPIO.output(11 , True)
    if humidity >= 55 :
        GPIO.output(37 , True)
    else :
        GPIO.output(37 , False)   
    try :
        GPIO.output(trig , True)
        time.sleep(0.00001)
        GPIO.output(trig , False)
        while GPIO.input(echo) == 0:
            start_pulse = time.time()
        while GPIO.input(echo) == 1:
            end_pulse = time.time()
        pluse_duration = end_pulse - start_pulse
        distance = round((pluse_duration * 34300)/2)
        #during = round(distance , 2)
        print (f"temp = {tempreture}*C hum = {humidity}% Distance : {distance} cm ")
        if distance <50 :
            GPIO.output(32 , True)
        else :
            GPIO.output(32 , False)
    except:
        print ("Can't detect distance!!!")
    time.sleep(0.5)
