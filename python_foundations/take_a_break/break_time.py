import time
import webbrowser

total_breaks = 3
break_count = 0
break_interval = 10 # in seconds

while (break_count < total_breaks):
    print("Break " + str(break_count) + " started at " + time.ctime())
    time.sleep(break_interval)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    break_count += 1
