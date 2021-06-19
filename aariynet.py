from pypresence import Presence
import time

AARIYNET = Presence(740833703277887491)  # Official App Id 356875570916753438
AARIYNET.connect()
start_time = int(time.time())
while True:
    AARIYNET.update(start=start_time, large_image="aariyjp", buttons=[{"label": "Aariy.NETに参加", "url": "https://discord.com/invite/jeghwmr"}, {"label": "ANEボット導入", "url": "https://discord.com/oauth2/authorize?client_id=482195859186909184&scope=bot+applications.commands&permissions=2147483647"}])  # Prime Video
    time.sleep(30)
