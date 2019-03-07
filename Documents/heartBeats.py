# Simple heart beat reader for Raspberry pi using ADS1x15 family of ADCs and a pulse sensor - http://pulsesensor.com/.
# The code borrows heavily from Tony DiCola's examples of using ADS1x15 with 
# Raspberry pi and WorldFamousElectronics's code for PulseSensor_Amped_Arduino

# Author: Udayan Kumar
# License: Public Domain

import time
# Import the ADS1x15 module.
import Adafruit_ADS1x15
import board
import busio
import adafruit_is31fl3731
from threading import Thread
i2c = busio.I2C(board.SCL, board.SDA)

display = adafruit_is31fl3731.Matrix(i2c)


display.pixel(5, 3, 127, blink=True)
display.pixel(6, 3, 127, blink=True)
display.pixel(5, 4, 127, blink=True)
display.pixel(4, 4, 127, blink=True)
display.pixel(3, 4, 127, blink=True)
display.pixel(2, 3, 127, blink=True)
display.pixel(3, 3, 127, blink=True)
display.pixel(4, 5, 127, blink=True)
display.pixel(4, 3, 127, blink=True)
display.pixel(5, 2, 127, blink=True)
display.pixel(6, 2, 127, blink=True)
display.pixel(7, 3, 127, blink=True)
display.pixel(6, 4, 127, blink=True)
display.pixel(5, 5, 127, blink=True)
display.pixel(4, 6, 127, blink=True)
display.pixel(3, 5, 127, blink=True)
display.pixel(2, 4, 127, blink=True)
display.pixel(1, 3, 127, blink=True)
display.pixel(2, 2, 127, blink=True)
display.pixel(3, 2, 127, blink=True)

def zero_left():
    with busio.I2C(board.SCL, board.SDA) as i2c:
        display = adafruit_is31fl3731.Matrix(i2c)
        display.pixel(8, 2, 50)
        display.pixel(9, 2, 50)
        display.pixel(10, 2, 50)
        display.pixel(8, 3, 50)
        display.pixel(8, 4, 50)
        display.pixel(10, 3, 50)
        display.pixel(10, 4, 50)
        display.pixel(10, 5, 50)
        display.pixel(10, 6, 50)
        display.pixel(9, 6, 50)
        display.pixel(8, 6, 50)
        display.pixel(8, 5, 50)


def one_left():
    with busio.I2C(board.SCL, board.SDA) as i2c:
        display = adafruit_is31fl3731.Matrix(i2c)
        display.pixel(8, 3, 50)
        display.pixel(9, 2, 50)
        display.pixel(9, 3, 50)
        display.pixel(9, 4, 50)
        display.pixel(9, 5, 50)
        display.pixel(10, 6, 50)
        display.pixel(9, 6, 50)
        display.pixel(8, 6, 50)


def two_left():
    with busio.I2C(board.SCL, board.SDA) as i2c:
        display = adafruit_is31fl3731.Matrix(i2c)
        display.pixel(8, 2, 50)
        display.pixel(9, 2, 50)
        display.pixel(10, 2, 50)
        display.pixel(10, 3, 50)
        display.pixel(8, 4, 50)
        display.pixel(9, 4, 50)
        display.pixel(10, 4, 50)
        display.pixel(8, 5, 50)
        display.pixel(10, 6, 50)
        display.pixel(9, 6, 50)
        display.pixel(8, 6, 50)


def three_left():
    with busio.I2C(board.SCL, board.SDA) as i2c:
        display = adafruit_is31fl3731.Matrix(i2c)
        display.pixel(8, 2, 50)
        display.pixel(9, 2, 50)
        display.pixel(10, 2, 50)

            # display.pixel(8, 3, 50)

        display.pixel(8, 4, 50)
        display.pixel(9, 4, 50)
        display.pixel(10, 3, 50)
        display.pixel(10, 4, 50)
        display.pixel(10, 5, 50)
        display.pixel(10, 6, 50)
        display.pixel(9, 6, 50)
        display.pixel(8, 6, 50)


        # display.pixel(8, 5 , 50)

def four_left():
    with busio.I2C(board.SCL, board.SDA) as i2c:
        display = adafruit_is31fl3731.Matrix(i2c)
        display.pixel(8, 2, 50)

            # display.pixel(9, 2, 50)

        display.pixel(10, 2, 50)
        display.pixel(8, 3, 50)
        display.pixel(8, 4, 50)
        display.pixel(9, 4, 50)
        display.pixel(10, 3, 50)
        display.pixel(10, 4, 50)
        display.pixel(10, 5, 50)
        display.pixel(10, 6, 50)


            # display.pixel(9, 6, 50)
            # display.pixel(8, 6 , 50)
            # display.pixel(8, 5 , 50)

def five_left():
    with busio.I2C(board.SCL, board.SDA) as i2c:
        display = adafruit_is31fl3731.Matrix(i2c)
        display.pixel(8, 2, 50)
        display.pixel(9, 2, 50)
        display.pixel(10, 2, 50)
        display.pixel(8, 3, 50)
        display.pixel(8, 4, 50)
        display.pixel(9, 4, 50)
        display.pixel(10, 4, 50)
        display.pixel(10, 5, 50)
        display.pixel(10, 6, 50)
        display.pixel(9, 6, 50)
        display.pixel(8, 6, 50)


def six_left():
    with busio.I2C(board.SCL, board.SDA) as i2c:
        display = adafruit_is31fl3731.Matrix(i2c)

        # ....display.pixel(8, 2, 50)

        display.pixel(9, 2, 50)
        display.pixel(10, 2, 50)
        display.pixel(8, 3, 50)
        display.pixel(8, 4, 50)
        display.pixel(9, 4, 50)
        display.pixel(10, 4, 50)
        display.pixel(10, 5, 50)
        display.pixel(10, 6, 50)
        display.pixel(9, 6, 50)
        display.pixel(8, 6, 50)
        display.pixel(8, 5, 50)


def seven_left():
    with busio.I2C(board.SCL, board.SDA) as i2c:
        display = adafruit_is31fl3731.Matrix(i2c)
        display.pixel(8, 2, 50)
        display.pixel(9, 2, 50)
        display.pixel(10, 2, 50)

            # display.pixel(8, 3, 50)
            # display.pixel(8, 4, 50)
            # display.pixel(9, 4, 50)

        display.pixel(10, 3, 50)
        display.pixel(10, 4, 50)
        display.pixel(10, 5, 50)
        display.pixel(10, 6, 50)


        # display.pixel(9, 6, 50)
        # display.pixel(8, 6 , 50)
        # display.pixel(8, 5 , 50)

def eight_left():
    with busio.I2C(board.SCL, board.SDA) as i2c:
        display = adafruit_is31fl3731.Matrix(i2c)
        display.pixel(8, 2, 50)
        display.pixel(9, 2, 50)
        display.pixel(10, 2, 50)
        display.pixel(8, 3, 50)
        display.pixel(8, 4, 50)
        display.pixel(9, 4, 50)
        display.pixel(10, 3, 50)
        display.pixel(10, 4, 50)
        display.pixel(10, 5, 50)
        display.pixel(10, 6, 50)
        display.pixel(9, 6, 50)
        display.pixel(8, 6, 50)
        display.pixel(8, 5, 50)


def nine_left():
    with busio.I2C(board.SCL, board.SDA) as i2c:
        display = adafruit_is31fl3731.Matrix(i2c)
        display.pixel(8, 2, 50)
        display.pixel(9, 2, 50)
        display.pixel(10, 2, 50)
        display.pixel(8, 3, 50)
        display.pixel(8, 4, 50)
        display.pixel(9, 4, 50)
        display.pixel(10, 3, 50)
        display.pixel(10, 4, 50)
        display.pixel(10, 5, 50)

            # display.pixel(10, 6, 50)

        display.pixel(9, 6, 50)
        display.pixel(8, 6, 50)


        # display.pixel(8, 5 , 50)

# all right digit fucntions

def zero_right():
    with busio.I2C(board.SCL, board.SDA) as i2c:
        display = adafruit_is31fl3731.Matrix(i2c)
        display.pixel(12, 2, 50)
        display.pixel(13, 2, 50)
        display.pixel(14, 2, 50)
        display.pixel(12, 3, 50)
        display.pixel(12, 4, 50)

            # display.pixel(9, 4, 50)

        display.pixel(14, 3, 50)
        display.pixel(14, 4, 50)
        display.pixel(14, 5, 50)
        display.pixel(14, 6, 50)
        display.pixel(13, 6, 50)
        display.pixel(12, 6, 50)
        display.pixel(12, 5, 50)


def one_right():
    with busio.I2C(board.SCL, board.SDA) as i2c:
        display = adafruit_is31fl3731.Matrix(i2c)
        display.pixel(13, 3, 50)
        display.pixel(14, 2, 50)
        display.pixel(14, 3, 50)
        display.pixel(14, 4, 50)
        display.pixel(14, 5, 50)
        display.pixel(15, 6, 50)
        display.pixel(14, 6, 50)
        display.pixel(13, 6, 50)


def two_right():
    with busio.I2C(board.SCL, board.SDA) as i2c:
        display = adafruit_is31fl3731.Matrix(i2c)
        display.pixel(12, 2, 50)
        display.pixel(13, 2, 50)
        display.pixel(14, 2, 50)
        display.pixel(14, 3, 50)
        display.pixel(12, 4, 50)
        display.pixel(13, 4, 50)
        display.pixel(14, 4, 50)
        display.pixel(12, 5, 50)
        display.pixel(14, 6, 50)
        display.pixel(13, 6, 50)
        display.pixel(12, 6, 50)


def three_right():
    with busio.I2C(board.SCL, board.SDA) as i2c:
        display = adafruit_is31fl3731.Matrix(i2c)
        display.pixel(12, 2, 50)
        display.pixel(13, 2, 50)
        display.pixel(14, 2, 50)

            # display.pixel(8, 3, 50)

        display.pixel(12, 4, 50)
        display.pixel(13, 4, 50)
        display.pixel(14, 3, 50)
        display.pixel(14, 4, 50)
        display.pixel(14, 5, 50)
        display.pixel(14, 6, 50)
        display.pixel(13, 6, 50)
        display.pixel(12, 6, 50)


        # display.pixel(8, 5 , 50)

def four_right():
    with busio.I2C(board.SCL, board.SDA) as i2c:
        display = adafruit_is31fl3731.Matrix(i2c)
        display.pixel(12, 2, 50)

            # display.pixel(9, 2, 50)

        display.pixel(14, 2, 50)
        display.pixel(12, 3, 50)
        display.pixel(12, 4, 50)
        display.pixel(13, 4, 50)
        display.pixel(14, 3, 50)
        display.pixel(14, 4, 50)
        display.pixel(14, 5, 50)
        display.pixel(14, 6, 50)


            # display.pixel(9, 6, 50)
            # display.pixel(8, 6 , 50)
            # display.pixel(8, 5 , 50)

def five_right():
    with busio.I2C(board.SCL, board.SDA) as i2c:
        display = adafruit_is31fl3731.Matrix(i2c)
        display.pixel(12, 2, 50)
        display.pixel(13, 2, 50)
        display.pixel(14, 2, 50)
        display.pixel(12, 3, 50)
        display.pixel(12, 4, 50)
        display.pixel(13, 4, 50)
        display.pixel(14, 4, 50)
        display.pixel(14, 5, 50)
        display.pixel(14, 6, 50)
        display.pixel(13, 6, 50)
        display.pixel(12, 6, 50)


def six_right():
    with busio.I2C(board.SCL, board.SDA) as i2c:
        display = adafruit_is31fl3731.Matrix(i2c)

        # ....display.pixel(8, 2, 50)

        display.pixel(13, 2, 50)
        display.pixel(14, 2, 50)
        display.pixel(12, 3, 50)
        display.pixel(12, 4, 50)
        display.pixel(13, 4, 50)
        display.pixel(14, 4, 50)
        display.pixel(14, 5, 50)
        display.pixel(14, 6, 50)
        display.pixel(13, 6, 50)
        display.pixel(12, 6, 50)
        display.pixel(12, 5, 50)


def seven_right():
    with busio.I2C(board.SCL, board.SDA) as i2c:
        display = adafruit_is31fl3731.Matrix(i2c)
        display.pixel(12, 2, 50)
        display.pixel(13, 2, 50)
        display.pixel(14, 2, 50)

            # display.pixel(8, 3, 50)
            # display.pixel(8, 4, 50)
            # display.pixel(9, 4, 50)

        display.pixel(14, 3, 50)
        display.pixel(14, 4, 50)
        display.pixel(14, 5, 50)
        display.pixel(14, 6, 50)


            # display.pixel(9, 6, 50)
            # display.pixel(8, 6 , 50)
            # display.pixel(8, 5 , 50)

def eight_right():
    with busio.I2C(board.SCL, board.SDA) as i2c:
        display = adafruit_is31fl3731.Matrix(i2c)
        display.pixel(12, 2, 50)
        display.pixel(13, 2, 50)
        display.pixel(14, 2, 50)
        display.pixel(12, 3, 50)
        display.pixel(12, 4, 50)
        display.pixel(13, 4, 50)
        display.pixel(14, 3, 50)
        display.pixel(14, 4, 50)
        display.pixel(14, 5, 50)
        display.pixel(14, 6, 50)
        display.pixel(13, 6, 50)
        display.pixel(12, 6, 50)
        display.pixel(12, 5, 50)


def nine_right():
    with busio.I2C(board.SCL, board.SDA) as i2c:
        display = adafruit_is31fl3731.Matrix(i2c)
        display.pixel(12, 2, 50)
        display.pixel(13, 2, 50)
        display.pixel(14, 2, 50)
        display.pixel(12, 3, 50)
        display.pixel(12, 4, 50)
        display.pixel(13, 4, 50)
        display.pixel(14, 3, 50)
        display.pixel(14, 4, 50)
        display.pixel(14, 5, 50)

            # display.pixel(10, 6, 50)

        display.pixel(13, 6, 50)
        display.pixel(12, 6, 50)


            # display.pixel(8, 5 , 50)

            
def left_digit(digit2):
    switcher = {
        0: zero_left,
        1: one_left,
        2: two_left,
        3: three_left,
        4: four_left,
        5: five_left,
        6: six_left,
        7: seven_left,
        8: eight_left,
        9: nine_left
    }
    # Get the function from switcher dictionary
    display = switcher.get(digit2,lambda: "invalid month")
    # Execute the function
    display()
    



def right_digit(digit):
    switcher = {
        0: zero_right,
        1: one_right,
        2: two_right,
        3: three_right,
        4: four_right,
        5: five_right,
        6: six_right,
        7: seven_right,
        8: eight_right,
        9: nine_right
    }
    # Get the function from switcher dictionary
    display2 = switcher.get(digit,lambda: "invalid month")
    # Execute the function
    display2()



if __name__ == '__main__':

    adc = Adafruit_ADS1x15.ADS1015()
    # initialization 
    GAIN = 2/3  
    curState = 0
    thresh = 525  # mid point in the waveform
    P = 512
    T = 512
    stateChanged = 0
    sampleCounter = 0
    lastBeatTime = 0
    firstBeat = True
    secondBeat = False
    Pulse = False
    IBI = 600
    rate = [0]*10
    amp = 100

    lastTime = int(time.time()*1000)

    # Main loop. use Ctrl-c to stop the code
    while True:
        # read from the ADC
        Signal = adc.read_adc(0, gain=GAIN)   #TODO: Select the correct ADC channel. I have selected A0 here
        curTime = int(time.time()*1000)

        sampleCounter += curTime - lastTime;      #                   # keep track of the time in mS with this variable
        lastTime = curTime
        N = sampleCounter - lastBeatTime;     #  # monitor the time since the last beat to avoid noise
        #print N, Signal, curTime, sampleCounter, lastBeatTime

        ##  find the peak and trough of the pulse wave
        if Signal < thresh and N > (IBI/5.0)*3.0 :  #       # avoid dichrotic noise by waiting 3/5 of last IBI
            if Signal < T :                        # T is the trough
              T = Signal;                         # keep track of lowest point in pulse wave 

        if Signal > thresh and  Signal > P:           # thresh condition helps avoid noise
            P = Signal;                             # P is the peak
                                                # keep track of highest point in pulse wave

          #  NOW IT'S TIME TO LOOK FOR THE HEART BEAT
          # signal surges up in value every time there is a pulse
        if N > 250 :                                   # avoid high frequency noise
            if  (Signal > thresh) and  (Pulse == False) and  (N > (IBI/5.0)*3.0)  :       
              Pulse = True;                               # set the Pulse flag when we think there is a pulse
              IBI = sampleCounter - lastBeatTime;         # measure time between beats in mS
              lastBeatTime = sampleCounter;               # keep track of time for next pulse

              if secondBeat :                        # if this is the second beat, if secondBeat == TRUE
                secondBeat = False;                  # clear secondBeat flag
                for i in range(0,10):             # seed the running total to get a realisitic BPM at startup
                  rate[i] = IBI;                      

              if firstBeat :                        # if it's the first time we found a beat, if firstBeat == TRUE
                firstBeat = False;                   # clear firstBeat flag
                secondBeat = True;                   # set the second beat flag
                continue                              # IBI value is unreliable so discard it


              # keep a running total of the last 10 IBI values
              runningTotal = 0;                  # clear the runningTotal variable    

              for i in range(0,9):                # shift data in the rate array
                rate[i] = rate[i+1];                  # and drop the oldest IBI value 
                runningTotal += rate[i];              # add up the 9 oldest IBI values

              rate[9] = IBI;                          # add the latest IBI to the rate array
              runningTotal += rate[9];                # add the latest IBI to runningTotal
              runningTotal /= 10;                     # average the last 10 IBI values 
              BPM = 60000/runningTotal;               # how many beats can fit into a minute? that's BPM!
              #print 'BPM: {}'.format(BPM)
              print("BPM: %d" %BPM)
              digit = int(BPM % 10)
              BPM = BPM - digit 
              digit2 = int(BPM / 10)
              print ("right Number is ",digit)
              print ("left Number is ",digit2) 
              #create a list of threads
              threads = []
              # In this case 'urls' is a list of urls to be crawled.
                  # We start one thread per url present.
              process = Thread(target=left_digit, args=[digit2])
              process.start()
              threads.append(process)

              process = Thread(target=right_digit, args=[digit])
              process.start()
              threads.append(process)
              # We now pause execution on the main thread by 'joining' all of our started threads.
              # This ensures that each has finished processing the urls.
              for process in threads:
                  process.join()

        if Signal < thresh and Pulse == True :   # when the values are going down, the beat is over
            Pulse = False;                         # reset the Pulse flag so we can do it again
            amp = P - T;                           # get amplitude of the pulse wave
            thresh = amp/2 + T;                    # set thresh at 50% of the amplitude
            P = thresh;                            # reset these for next time
            T = thresh;

        if N > 2500 :                          # if 2.5 seconds go by without a beat
            thresh = 512;                          # set thresh default
            P = 512;                               # set P default
            T = 512;                               # set T default
            lastBeatTime = sampleCounter;          # bring the lastBeatTime up to date        
            firstBeat = True;                      # set these to avoid noise
            secondBeat = False;                    # when we get the heartbeat back
            print ("no beats found");

        time.sleep(0.025)




