# this file is rewriten by levina on github
# ported from ultroid
# Copyright (C) 2021 By Veez Project


import glob
import os
import random

from userbot import CMD_HELP
from userbot.events import register
from PIL import Image, ImageDraw, ImageFont
from telethon.tl.types import InputMessagesFilterPhotos


@register(pattern="^.logo(?: |$)(.*)")
async def logo_gen(event):
    xx = await eor(event, get_string("com_1"))
    name = event.pattern_match.group(1)
    if not name:
        await eod(xx, "`berikan teks untuk logo!`")
    bg_, font_ = "", ""
    if event.reply_to_msg_id:
        temp = await event.get_reply_message()
        if temp.media:
            if hasattr(temp.media, "document"):
                if "font" in temp.file.mime_type:
                    font_ = await temp.download_media()
                elif (".ttf" in temp.file.name) or (".otf" in temp.file.name):
                    font_ = await temp.download_media()
            elif "pic" in mediainfo(temp.media):
                bg_ = await temp.download_media()
    else:
        pics = []
        async for i in azumiuserbot.iter_messages(
            "@SakuraLogos", filter=InputMessagesFilterPhotos
        ):
            pics.append(i)
        id_ = random.choice(pics)
        bg_ = await id_.download_media()
        fpath_ = glob.glob("resources/fonts/*")
        font_ = random.choice(fpath_)
    if not bg_:
        pics = []
        async for i in azumiuserbot.iter_messages(
            "@SakuraLogos", filter=InputMessagesFilterPhotos
        ):
            pics.append(i)
        id_ = random.choice(pics)
        bg_ = await id_.download_media()
    if not font_:
        fpath_ = glob.glob("resources/fonts/*")
        font_ = random.choice(fpath_)
    if len(name) <= 8:
        fnt_size = 150
        strke = 10
    elif len(name) >= 9:
        fnt_size = 50
        strke = 5
    else:
        fnt_size = 130
        strke = 20
    img = Image.open(bg_)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_, fnt_size)
    w, h = draw.textsize(name, font=font)
    h += int(h * 0.21)
    image_width, image_height = img.size
    draw.text(
        ((image_width - w) / 2, (image_height - h) / 2),
        name,
        font=font,
        fill=(255, 255, 255),
    )
    x = (image_width - w) / 2
    y = (image_height - h) / 2
    draw.text(
        (x, y), name, font=font, fill="white", stroke_width=strke, stroke_fill="black"
    )
    flnme = f"azumi.png"
    img.save(flnme, "png")
    await xx.edit("`SELESAI !`")
    if os.path.exists(flnme):
        await event.client.send_file(
            event.chat_id,
            file=flnme,
            caption=f"logo by [{OWNER_NAME}](tg://user?id={OWNER_ID})",
            force_document=True,
        )
        os.remove(flnme)
        await xx.delete()
    if os.path.exists(bg_):
        os.remove(bg_)
    if os.path.exists(font_):
        if not font_.startswith("resources/fonts"):
            os.remove(font_)
            
            
CMD_HELP.update({
  "logo":
  "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.logo` <teks>\
 \nUsage : Untuk membuat logo dari teks"
})
