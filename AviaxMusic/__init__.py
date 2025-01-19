from AviaxMusic.core.bot import Aviax
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
CLONE_OWNERS = {}




cloneownerdb = mongodb.clone_owners

async def load_clone_owners():
    async for entry in cloneownerdb.find():
        bot_id = entry["bot_id"]
        user_id = entry["user_id"]
        CLONE_OWNERS[bot_id] = user_id

async def save_clonebot_owner(bot_id, user_id):
    await cloneownerdb.update_one(
        {"bot_id": bot_id},
        {"$set": {"user_id": user_id}},
        upsert=True
    )
async def get_clone_owner(bot_id):
    data = await cloneownerdb.find_one({"bot_id": bot_id})
    if data:
        return data["user_id"]
    return None

async def delete_clone_owner(bot_id):
    await cloneownerdb.delete_one({"bot_id": bot_id})
    CLONE_OWNERS.pop(bot_id, None)

async def save_idclonebot_owner(clone_id, user_id):
    await cloneownerdb.update_one(
        {"clone_id": clone_id},
        {"$set": {"user_id": user_id}},
        upsert=True
    )

async def get_idclone_owner(clone_id):
    data = await cloneownerdb.find_one({"clone_id": clone_id})
    if data:
        return data["user_id"]
    return None
