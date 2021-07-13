# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(event):
    """ untuk perintah .help,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("mohon berikan nama modul yang benar.")
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t\t\t🔸\t\t\t "
        await event.edit(
            f"{string}"
            "\n\n💡 Untuk melihat detail & penjelasan setiap modul gunakan perintah help.\
                        \n\n**Contoh:** `.help` <nama modul>"
        )
