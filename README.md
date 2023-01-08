# smarthouse
this project detect the tempreture &amp; humidity move detection
for normal weather the green LED will be on
when the tempreture will be hieght the red LED on
and orange one for hieght humidity , purple for a move detection when  


-  Rquirments  
      - raspberry pi 3B+  
       
-  Sensor  
    - Ultra sonic  
    - DHT11  
-  LED  
    - red green yellow and purple  

# setup raspberry
  you must already have a SD-card with the [raspberry pi](https://www.raspberrypi.com/software/). os  
  and if you want to useing into your computer, do this simple step  
  - first you need an ethirnet cable connect to raspbbery and your computer together  
  - then you must looking for rasbperry IP 
    - **Windows** you can find raspberry IP with [angryip](https://angryip.org/). or any ip scanning tool
    - **Linux** useing nmap so simple to find the ip sudo nmap -sn 192.168.1.1-254 
  - after find the IP you must try to enable SSH and VNC Viewer on the raspberry 
    - you must download [putty](https://www.putty.org/). and use SSH to conect with  the raspberry pi defualt **login:** pi **passowrd:** raspberry
    - after that you need to type  sudo raspi-config  and go ***Interfacing Option***  and enable the **SSH** and **VNC**
   - if you already enable ssh and vnc you shuld good to go 
     - we need a [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/) to display the raspberry screen on our computer

# raspberry pi 3b+
-pin stracture
![rp2_pinout](https://user-images.githubusercontent.com/92225352/179687331-94c14ac3-fad1-423b-a775-70f0dfac6d48.png)


# Usage 
```
pip install Adafruit_DHT
git clone https://github.com/rawezh97/smarthouse.git
cd smarthouse
python3 smarthouse.py
```



# diagram 
![Screenshot at 2022-07-18 22-46-53](https://user-images.githubusercontent.com/92225352/179686109-ca3d37f9-fb05-4681-892d-0982539c4755.png)
