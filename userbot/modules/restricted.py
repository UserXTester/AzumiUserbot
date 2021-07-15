# Copyright (C) 2021 By Veez Project
# Rewriten from Geez Userbot
# Inspirated from ultroid userbot

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import bot, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.limit(?: |$)(.*)")
async def _(event):
    await event.edit("__memeriksa status akun telegram anda...__")
    async with bot.conversation("@SpamBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=178220800)
            )
            await conv.send_message("/start")
            response = await response
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("__boss, mohon unblokir @SpamBot terlebih dahulu.__")
            return
        await event.edit(f"~ {response.message.message}")


CMD_HELP.update({"limits": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.limit`"
                 "\n•: untuk memeriksa apakah akun anda dibatasi telegram atau tidak."})
