#Libraries
import RPi.GPIO as GPIO
import time
 
# Sensors pins setting
# ===== tilt sensor pin setting ==================
tiltPin = 29
# tilt sensor connect the grn pin to GROUND (for example: pin 6)
# tilt sensor connect the VCC pin to 5v pin#2
 
 
def cleanBoard():
    print("Cleaning up!")
    # Release resources - clean up the board setting
    GPIO.cleanup()
 
 
def setup():
    # Disable warnings (optional)
    GPIO.setwarnings(False)
    # set the GPIO to the BOARD mode
    GPIO.setmode(GPIO.BOARD)
    #Sensors Setting
    # ===== tilt sensor pin setting ==================
    # Bottom pin mode is input, and pull up to high level (3.3 v)
    GPIO.setup(tiltPin , GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(tiltPin, GPIO.FALLING, callback=detectTilt, bouncetime=200)

 
def detectTilt(null):
    print('Tilt Detected')
    
    '''
    if(GPIO.input(tiltPin)):
        #print("tilted")
        print("True")
    else:
        #print("Horizontal")
        print("False")
    '''
 
# main part
if __name__ == "__main__":
    print("Tilt sensor-test [press ctrl+c to end]")
    setup()
    try:
        while True:
            print('pause 1 sec')
            time.sleep(1.0)
    except KeyboardInterrupt:  # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program
        cleanBoard()
