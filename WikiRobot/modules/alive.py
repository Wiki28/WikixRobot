import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from WikiRobot.events import register
from WikiRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/9b9a27cd02e65046d5515.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hai [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Wiki W.** \n\n"
  TEXT += "⚪ **Saya Bekerja Dengan Benar** \n\n"
  TEXT += f"⚪ **Tuanku : [Wiki W](terserah_wiki)** \n\n"
  TEXT += f"⚪ **Library Version :** `{telever}` \n\n"
  TEXT += f"⚪ **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"⚪ **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Terima Kasih Telah Menambahkan Saya Di Sini ❤️**"
  BUTTON = [[Button.url("Help", "https://t.me/WikiTapiBot?start=help"), Button.url("Support", "https://t.me/WikiTapiGroup")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
