from pypresence import Presence
import time

YOUTUBE = Presence(739528267039768647)
YOUTUBE.connect()
start_time = int(time.time())
while True:
    # noinspection PyArgumentList
    YOUTUBE.update(start=start_time, large_image="youtube", buttons=[{"label": "Aariy.NETに参加", "url": "https://discord.com/invite/jeghwmr"}, {"label": "ANEボット導入", "url": "https://discord.com/oauth2/authorize?client_id=482195859186909184&scope=bot+applications.commands&permissions=2147483647"}])  # YouTube
    time.sleep(30)
