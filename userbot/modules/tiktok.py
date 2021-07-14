# Copyright (C) 2021 By Veez Project
# rewriten by @levina-lab on github
# functions - tiktok downloader without watermark

from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.tiktok(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    if ".com" not in d_link:
        await event.edit("`mohon berikan link video tiktok yang ingin didownload.`")
    else:
        await event.edit("```memproses video anda...```")
    chat = "@ttsavebot"
    async with bot.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            r = await conv.get_response()
            msg = await conv.send_message(d_link)
            details = await conv.get_response()
            video = await conv.get_response()
            """ - don't spam notif - """
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("**kesalahan:** `mohon unblokir` @ttsavebot `dan coba lagi.`")
            return
        await bot.send_file(event.chat_id, video)
        await event.client.delete_messages(conv.chat_id,
                                           [msg_start.id, r.id, msg.id, details.id, video.id])
        await event.delete()


CMD_HELP.update(
    {
        "tiktok": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.tiktok <Link tiktok>`"
        "\n• : Download Video Tiktok Tanpa Watermark"
    }
)
