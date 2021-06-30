from pypresence import Presence
import time

STUDY = Presence(739528267039768647)
STUDY.connect()
print(f"[pypresence]: Successfully connected to Discord client.")
start_time = int(time.time())
while True:
    STUDY.update(start=start_time, join="abc")
    time.sleep(30)
