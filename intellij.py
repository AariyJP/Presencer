from pypresence import Presence
import time

INTELLIJ = Presence(626050213651677214)
INTELLIJ.connect()
start_time = int(time.time())
while True:
    INTELLIJ.update(start=start_time, large_image="java", join="abc")
    time.sleep(30)
