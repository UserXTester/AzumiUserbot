# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot start point """

from importlib import import_module
from sys import argv

from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from userbot import LOGS, bot
from userbot.modules import ALL_MODULES


INVALID_PH = '\nERROR: Phone Number INVALID' \
             '\n Tips: Gunakan kode negara didepan nomor.' \
             '\n atau periksa nomor hp anda lalu coba lagi !'

try:
    bot.start()
except PhoneNumberInvalidError:
    print(INVALID_PH)
    exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

LOGS.info("Running On Azumi Userbot [v4.0]")

LOGS.info(
    "🦊 AZUMI USERBOT SUDAH AKTIF 🦊"
    "ketik ping atau alive untuk mengetes userbot anda.")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
