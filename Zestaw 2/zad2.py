import datetime
import time

while True:
    now = datetime.datetime.now().strftime("%H:%M:%S")
    print(chr(16), '\t', now, '\t', chr(17), end='\r')
    time.sleep(0.5)