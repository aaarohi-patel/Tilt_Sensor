#Libraries
import RPi.GPIO as GPIO
import time
 
# Sensors pins setting
# ===== tilt sensor pin setting ==================
rightTiltPin = 31
leftTiltPin = 29
# tilt sensor connect the grn pin to GROUND (for example: pin 6)
# tilt sensor connect the VCC pin to 5v pin#2
 
#==========LED pin=========
redLedPin = 12 #longer leg
#groundpin = 6 smaller leg

#==========5V Buzzer=======
buzzerPin = 22
#groundpin = 14

def setup():
    # Disable warnings (optional)
    GPIO.setwarnings(False)
    # set the GPIO to the BOARD mode
    GPIO.setmode(GPIO.BOARD)
    # ===== LED sensor pin setting ==================
    GPIO.setup(redLedPin, GPIO.OUT)
    # ===== buzzer pin setting ==================
    GPIO.setup(buzzerPin, GPIO.OUT)
    
    # ===== tilt sensor pin setting ==================
    # Bottom pin mode is input, and pull up to high level (3.3 v)
    GPIO.setup(tiltPin , GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(tiltPin, GPIO.FALLING, callback=detectTilt, bouncetime=200)

    
def cleanBoard():
    print("Cleaning up!")
    # Release resources - clean up the board setting
    GPIO.cleanup()
 
 def LEDOn():
    #turning the light on
    GPIO.output(redLedPin, GPIO.HIGH)

def LEDOff():
    #turning the light off
    GPIO.output(redLedPin, GPIO.LOW)
    
def BeepOn():
    GPIO.output(buzzerPin, GPIO.HIGH)
    
def BeepOff():
    GPIO.output(buzzerPin, GPIO.LOW)


 def AlertOn():
    BeepOn()
    LEDOn()
    time.sleep(0.5)


def clearAlert():
    BeepOff()
    LEDOff()
    
    
def detectTilt(null):
    if(GPIO.input(tiltPin)):
        print("tilt left")
    else:
        print("tilt right")
    time.sleep(0.10)  #sleep 5 seconds
    
    
    try:
        while True:
            
            if checkLeftTilt() or checkRightTilt()
                AlertOn()
                continue
            else:
                AlertClear()
                continue
          
            if checkLeftTilt():
                print("Left tilted\n")
                AlertOn()
            else:
                print("Horizontal\n")
                clearAlert() 
            if checkRightTilt():    
                print("Right tilted\n")
                AlertOn()
            else:
                print("Horizontal\n")
                clearAlert()
            time.sleep(1)
            
            
             
    except KeyboardInterrupt:  # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program
        clearAlert()
 
 
# main part
if __name__ == "__main__":
    print("Tilt sensor-test [press ctrl+c to end]")
    setup()
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:  # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program
        cleanBoard()
