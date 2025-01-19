from AviaxMusic.core.bot import Aviax, nobita
from AviaxMusic.core.dir import dirr
from AviaxMusic.core.git import git
from AviaxMusic.core.userbot import Userbot
from AviaxMusic.core.mongo import mongodb 
from AviaxMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

iapp = nobita()
app = Aviax()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

HELPABLE = {}




