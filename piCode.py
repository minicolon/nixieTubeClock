import time
from gpiozero import LEDBoard, Button
from subprocess import call

offSwitch = Button(25) # 25=pin to turn off raspberry pi
tubesOn = LEDBoard(22) # 22=pin to activate switch that turns on nixie tubes
AN = LEDBoard(23, 24) # 23=hours, 24=minutes 
cathode1 = LEDBoard(21, 20, 16, 12) # (MSB, Bit, Bit, LSB)
cathode2 = LEDBoard(26, 19, 13, 6) # (MSB, Bit, Bit, LSB)



# needs to alternate between anode 0 and 1
# initialize output to current time
# increment each minute
# reset after 12:59
    
# output BCD value for every decimal change    
BCD = {
    0: (0, 0, 0, 0),
    1: (0, 0, 0, 1),
    2: (0, 0, 1, 0),
    3: (0, 0, 1, 1),
    4: (0, 1, 0, 0),
    5: (0, 1, 0, 1),
    6: (0, 1, 1, 0),
    7: (0, 1, 1, 1),
    8: (1, 0, 0, 0),
    9: (1, 0, 0, 1)
}

def getBCD(lHour, tHour, lMin, tMin):
    AN.value = (1, 0)
    cathode1.value = BCD.get(lHour)
    cathode2.value = BCD.get(tHour)
    time.sleep(.015)
        
    AN.value = (0, 1)
    cathode1.value = BCD.get(lMin)
    cathode2.value = BCD.get(tMin)
    time.sleep(.015)

# Obtain current time and set both minute and hour value
currentTime = time.strftime("%H%M", time.localtime())
# separate time into individual digits
leadHour = int(currentTime[0])
trailHour = int(currentTime[1])
leadMin = int(currentTime[2])
trailMin = int(currentTime[3])
getBCD(leadHour, trailHour, leadMin, trailMin)

#activates the nixie tubes
tubesOn.on()

while True:
    # used so the clock can run independently of the internet after first initialization
    tMin = time.time() + 60
        
    # run this loop for 1 minute before breaking out into the logical checks
    while time.time() < tMin:
        getBCD(leadHour, trailHour, leadMin, trailMin)
        if offSwitch.is_pressed:
            break
                
    if offSwitch.is_pressed == False:        
        # logic to determine how to increment time for each minute
        # check if the time is at 11pm or 23:00
        if leadHour == 2 and trailHour == 3:
            # if at 23:59 set to 00:00 (midnight)
            if leadMin == 5 and trailMin == 9:
                leadHour, trailHour, leadMin, trailMin = 0, 0, 0, 0
            
            # increment by one minute until reaching 59 minutes
            else:
                if trailMin == 9:
                    trailMin = 0
                    leadMin = leadMin + 1
                else:
                    trailMin = trailMin + 1
        
        # if not at 11pm, carry this out
        # increment hour by 1 if at 59 minutes
        else:
            if leadMin == 5 and trailMin == 9:
                leadMin, trailMin = 0, 0
                # determine whether to increment leading hour or not
                if trailHour == 9:
                    trailHour = 0
                    leadHour = leadHour + 1
                else:
                    trailHour = trailHour + 1
 
            # increment minute by 1 if not at 59
            # determine whether to increment leading Minute or not
            else:
                if trailMin == 9:
                    trailMin = 0
                    leadMin = leadMin + 1
                else:
                    trailMin = trailMin + 1
    else:
        AN.value = (0,0)
        tubesOn.off()
        break

call("sudo shutdown -h now", shell=True)     
    
