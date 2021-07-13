# Modules fake action by levina ( rewriten )
# Copyright (C) 2021 by Veez Project


from userbot.events import register
from userbot import CMD_HELP
import asyncio


@register(outgoing=True, pattern="^.ftyping(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`incorrect format`")
    await event.edit(f"`memulai fake typing dalam {t} detik.`")
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.faudio(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`incorrect format`")
    await event.edit(f"`memulai fake audio recording dalam {t} detik.`")
    async with event.client.action(event.chat_id, "record-audio"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.fvideo(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`incorrect format`")
    await event.edit(f"`memulai fake video recording dalam {t} detik.`")
    async with event.client.action(event.chat_id, "record-video"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.fgame(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Incorrect Format`")
    await event.edit(f"`memulai fake game playing dalam {t} detik.`")
    async with event.client.action(event.chat_id, "game"):
        await asyncio.sleep(t)

CMD_HELP.update({
    "fakeaction":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ftyping` <waktu>\
   \nUsage : Fake action mengetik teks\
   \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.faudio` <waktu>\
   \nUsage : Fake action merekam audio\
   \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.fgame` <waktu>\
   \nUsage : Fake action bermain game\
   \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.fvideo` <waktu>\
   \nUsage : Fake action merekam video"
})
