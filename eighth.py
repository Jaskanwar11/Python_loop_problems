import time

retries = 5
attempts = 0
stop_time = 1

while attempts < retries:
    print("attempt", attempts + 1, "\nwait time -", stop_time, "seconds")
    time.sleep(stop_time)
    stop_time *= 2
    attempts += 1