from pypresence import Presence  # The simple rich presence client in pypresence
import time

RPC = Presence(739528267039768647)
RPC.connect()
start_time = int(time.time())
while True:
    # RPC.update(start=start_time, large_image="youtube", join="abc")  # YouTube
    RPC.update(start=start_time, large_image="prime_video", join="abc")  # Prime Video
    time.sleep(60)
