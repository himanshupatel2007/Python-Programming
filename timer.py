import time
timer = int(input("Enter the Time in Seconds : "))
for x in range(timer,0,-1):
     seconds = x %60
     mins = int((x/60)%60)
     hours = int(x/3600)
     print(f"{hours:02}:{mins:02}:{seconds:02}")
     time.sleep(1)
print("Time's Up")