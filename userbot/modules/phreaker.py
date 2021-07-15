# Copyright (C) 2021 By Veez Project
# All right reserved

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.nmap(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@scriptkiddies_bot"  # pylint:disable=E0602
    nmap = f"nmap"  # pylint:disable=E0602
    await event.edit("memproses...")
    async with bot.conversation("@scriptkiddies_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=510263282))
            await conv.send_message(f'/{nmap} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("boss, mohon unblock @scriptkiddies_bot terlebih dahulu!")
            return
        else:
            await event.edit(f"{response.message.message}")
            await event.client.delete_messages(response.message.message)


@register(outgoing=True, pattern=r"^\.subd(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@scriptkiddies_bot"  # pylint:disable=E0602
    subdomain = f"subdomain"  # pylint:disable=E0602
    await event.edit("memproses...")
    async with bot.conversation("@scriptkiddies_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=510263282))
            await conv.send_message(f'/{subdomain} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("boss, mohon unblock @scriptkiddies_bot terlebih dahulu!")
            return
        else:
            await event.edit(f"{response.message.message}")
            await event.client.delete_messages(response.message.message)


@register(outgoing=True, pattern=r"^\.cek(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@scriptkiddies_bot"  # pylint:disable=E0602
    httpheader = f"httpheader"  # pylint:disable=E0602
    await event.edit("memproses...")
    async with bot.conversation("@scriptkiddies_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=510263282))
            await conv.send_message(f'/{httpheader} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("boss, mohon unblock @scriptkiddies_bot terlebih dahulu!")
            return
        else:
            await event.edit(f"{response.message.message}")
            await event.client.delete_messages(httpheader, response.message.message)


@register(outgoing=True, pattern=r"^\.bin(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@Carol5_bot"  # pylint:disable=E0602
    bin = f"bin"  # pylint:disable=E0602
    await event.edit("memproses...")
    async with bot.conversation("@Carol5_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1247032902))
            await conv.send_message(f'/{bin} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("boss, mohon unblock @Carol5_bot terlebih dahulu!!")
            return
        else:
            await event.edit(f"{response.message.message}")
            await event.client.delete_messages(response.message.message)


@register(outgoing=True, pattern=r"^\.cc(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@Carol5_bot"  # pylint:disable=E0602
    ss = f"ss"  # pylint:disable=E0602
    await event.edit("memproses...")
    async with bot.conversation("@Carol5_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1247032902))
            await conv.send_message(f'/{ss} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("boss, mohon unblock @Carol5_bot terlebih dahulu!")
            return
        else:
            await event.edit(f"{response.message.message}")
            await event.client.delete_messages(response.message.message)


CMD_HELP.update({
    "phreaker":
    "`𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .nmap <bug hosts>`\
\nUsage: to get info bug/host.\
\n\n`𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .subd <bug hosts>`\
\nUsage: to get subdomain bug/host.\
\n\n`𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .cek <bug hosts>`\
\nUsage: to cek respons bug/host.\
    \n\n`𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .bin < bin number >`\
    \nUsage: to cek bin ip.\
\n\n`𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .cc <mm|yy|cvv`\
\nUsage: to cek Credits Card Stats."
})
