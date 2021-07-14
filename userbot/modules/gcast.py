# this file is part of Geez Userbot
# Copyright (C) 2021 Veez Project

from userbot.events import register
from userbot import CMD_HELP, bot


@register(outgoing=True, pattern="^.gcast (.*)")
async def gcast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return await event.edit("`berikan sebuah pesan untuk siaran global !!`")
    tt = event.text
    msg = tt[6:]
    kk = await event.edit("`📣 mengirim pesan secara global...`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"**berhasil mengirim pesan ke** `{done}` **grup, gagal mengirim pesan ke** `{er}` **grup**")


@register(outgoing=True, pattern=r"^\.gucast(?: |$)(.*)")
async def gucast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return await event.edit("`berikan pesan untuk dikirimkan secara global !!`")
    tt = event.text
    msg = tt[7:]
    kk = await event.edit("`mengirim pesan secara global...`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"berhasil mengirim pesan ke `{done}` obrolan, gagal dalam `{er}` obrolan(s)")


CMD_HELP.update(
    {
        "broadcast": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.gcast`\
         \n↳ : Mengirim pesan ke semua grup kamu.\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.gucast`\
         \n↳ : Mengirim pesan ke semua personal chat kamu."
    }
)
