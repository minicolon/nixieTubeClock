import time
from datetime import datetime
from gpiozero import LEDBoard

AN = LEDBoard(23, 24)
cathode1 = LEDBoard(21, 20, 16, 12)
cathode2 = LEDBoard(26, 19, 13, 6)



# needs to alternate between anode 0 and 1
# initialize output to current time
# increment each minute
# reset after 12:59
    
# output BCD value for every value change    
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

tMin = time.time() + 60
try:
    while True:
        # Obtain current time and set both minute and hour value
        currentTime = time.strftime("%H%M", time.localtime())
        # separate time into individual digits
        leadHour = int(currentTime[0])
        trailHour = int(currentTime[1])
        leadMin = int(currentTime[2])
        trailMin = int(currentTime[3])
        getBCD(leadHour, trailHour, leadMin, trailMin)
        while time.time() < tMin:
            getBCD(leadHour, trailHour, leadMin, trailMin)
except KeyboardInterrupt:
    AN.value = (0, 0)

# print(f"{leadHour}{trailHour}:{leadMin}{trailMin}")
# print(dictBCD[trailHour])
