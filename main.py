from pypresence import Presence  # The simple rich presence client in pypresence
import time

RPC = Presence(838237077602566166)
RPC.connect()
start_time = int(time.time())
while True:
    RPC.update(start=start_time, large_image="youtube", join="abc")
    time.sleep(60)
