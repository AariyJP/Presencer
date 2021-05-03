from pypresence import Presence
import time

YOUTUBE = Presence(739528267039768647)
YOUTUBE.connect()
start_time = int(time.time())
while True:
    YOUTUBE.update(start=start_time, large_image="youtube", join="abc")  # YouTube
    time.sleep(30)
