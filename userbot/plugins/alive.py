import asyncio
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "avengers User"
PM_IMG = "https://telegra.ph/file/fac7e043502927f46cc04.jpg"
pm_caption = "🔱 **ELIZA Is Online** 🔱\n\n"

pm_caption += f"🔸🔹 **ɱყ ცơʂʂ**           :   {DEFAULTUSER}\n"

pm_caption += "🔹🔸 тєℓєтнσи νєяѕισи   :   1.15.0 \n"

pm_caption += "🔸🔹 σffι¢ιαℓ ¢нαииєℓ   :   [ᴊᴏɪɴ](https://t.me/pyfilesforbot)\n"

pm_caption += "🔹🔸 σffι¢ιαℓ gяσυρ     :   [ᴊᴏɪɴ](https://t.me/eliza_support)\n"

pm_caption += "🔸🔹 ℓι¢єиѕє            :   [ӀíϲҽղՏҽ](https://github.com/lakshya-man05/eliza)\n"

pm_caption += "🔹🔸 ¢σρуяιgнт          :   [ELIZA](https://github.com/lakshya-man05)\n"

pm_caption += " [...▄███▄███▄\n....█████████\n.......▀█████▀\n............▀█▀\n](https://t.me/eliza_suport)\n"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
