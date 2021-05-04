from pypresence import Presence
import time

MC = Presence(833349474213691404)
MC.connect()
start_time = int(time.time())
while True:
    MC.update(start=start_time, large_image="minecraft", join="abc")  # Prime Video
    time.sleep(30)
