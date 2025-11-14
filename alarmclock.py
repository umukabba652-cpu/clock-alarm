from datetime import datetime
import time
from playsound3 import playsound

alarm_hour = int(input("Enter the hour(0-23):"))
alarm_minute = int(input("Enter the minute(0-59):"))
print(f" Alarm set for{alarm_hour:02d}:{alarm_minute:02d}")

while True:
    now = datetime.now()
    current_hour = now.hour
    current_minute = now.minute
    if current_hour == alarm_hour and current_minute == alarm_minute:
        print("wake up!")
        playsound("C:\\Users\\Examination\\Music\\test.mp3")
        break
    time.sleep(10)

    
