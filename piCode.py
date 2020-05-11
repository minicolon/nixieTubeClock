import time
from datetime import datetime

# Obtain current time and set both minute and hour value
t = time.localtime()
currentHour = time.strftime("%H", t)
currentMin = time.strftime("%M", t)

# convert time into separate digits
leadHour = int(currentHour[0])
trailHour = int(currentHour[1])
leadMin = int(currentMin[0])
trailMin = int(currentMin[1])

# needs to alternate between anode 0 and 1
# initialize output to current time
# increment each minute
# output BCD value for every change
# reset after 12:59

dictBCD = {
    0: "0000",
    1: "0001",
    2: "0010",
    3: "0011",
    4: "0100",
    5: "0101",
    6: "0110",
    7: "0111",
    8: "1000",
    9: "1001"
}

cHour = 0
cMin = 0
Anode = 0
print(f"{leadHour}{trailHour}:{leadMin}{trailMin}")
print(dictBCD[trailHour])
