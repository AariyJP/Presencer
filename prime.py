from pypresence import Presence
import time

PRIME = Presence(838237077602566166)
PRIME.connect()
start_time = int(time.time())
while True:
    PRIME.update(details=None, start=start_time, large_image="prime_video", join="abc")  # Prime Video
    time.sleep(30)
