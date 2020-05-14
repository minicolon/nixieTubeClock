import time
from datetime import datetime
from gpiozero import LEDBoard

AN = LEDBoard(23, 24)
cathode1 = LEDBoard(21, 20, 16, 12)
cathode2 = LEDBoard(26, 19, 13, 6)
# Obtain current time and set both minute and hour value
# t = time.localtime()
# currentHour = time.strftime("%H", t)
# currentMin = time.strftime("%M", t)
# 
# # convert time into separate digits
# leadHour = int(currentHour[0])
# trailHour = int(currentHour[1])
# leadMin = int(currentMin[0])
# trailMin = int(currentMin[1])

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
# cHour = 0
# cMin = 0
try:
    while True:
        AN.value = (1, 0)
        for i in range(10):
            cathode2.value = BCD.get(i)
            cathode1.value = BCD.get(i)
            time.sleep(.5)
except KeyboardInterrupt:
    AN.value = (0, 0)

# print(f"{leadHour}{trailHour}:{leadMin}{trailMin}")
# print(dictBCD[trailHour])
