import time
from datetime import datetime
from gpiozero import LEDBoard

cathode1 = LEDBoard(23, 21, 20, 16, 12)
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
def BCD(AN, i):
    if i == 0:
        cathode1.value = (AN, 0, 0, 0, 0)
    elif i == 1:
        cathode1.value = (AN, 0, 0, 0, 1)
    elif i == 2:
        cathode1.value = (AN, 0, 0, 1, 0)
    elif i == 3:
        cathode1.value = (AN, 0, 0, 1, 1)
    elif i == 4:
        cathode1.value = (AN, 0, 1, 0, 0)
    elif i == 5:
        cathode1.value = (AN, 0, 1, 0, 1)
    elif i == 6:
        cathode1.value = (AN, 0, 1, 1, 0)
    elif i == 7:
        cathode1.value = (AN, 0, 1, 1, 1)
    elif i == 8:
        cathode1.value = (AN, 1, 0, 0, 0)
    elif i == 9:
        cathode1.value = (AN, 1, 0, 0, 1)
    else:
        cathode1.value = (AN, 0, 0, 0, 0)
# cHour = 0
# cMin = 0
try:
    while True:
        for i in range(10):
            BCD(1, i)
            time.sleep(.5)
except KeyboardInterrupt:
    cathode1.value = (0, 0, 0, 0, 0)

# print(f"{leadHour}{trailHour}:{leadMin}{trailMin}")
# print(dictBCD[trailHour])
