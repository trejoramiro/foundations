import time
import webbrowser

two_hours = 15
present = time.time()
future = present + two_hours

breaks = 0

print("This program started on " + time.ctime())

while breaks < 4:
    if time.time() >= future:
        webbrowser.open("https://www.youtube.com/watch?v=VLAdKCyD_IA")
        time.sleep(4*65)
        breaks += 1
        future = time.time() + two_hours
