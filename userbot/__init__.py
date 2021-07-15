# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot initialization. """

import logging
import os
import re
import time
from sys import version_info
from logging import basicConfig, getLogger, INFO, DEBUG
from distutils.util import strtobool as sb
from math import ceil

from pylast import LastFMNetwork, md5
from pySmartDL import SmartDL
from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
from requests import get
from telethon import TelegramClient, custom, events
from telethon.sessions import StringSession
from telethon import Button, events, functions, types
from telethon.utils import get_display_name

load_dotenv("config.env")

StartTime = time.time()

CMD_LIST = {}
# for later purposes
CMD_HELP = {}
INT_PLUG = ""
LOAD_PLUG = {}

# Bot Logs setup:
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get(
    "CONSOLE_LOGGER_VERBOSE") or "False")

if CONSOLE_LOGGER_VERBOSE:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=DEBUG,
    )
else:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=INFO)
LOGS = getLogger(__name__)

if version_info[0] < 3 or version_info[1] < 8:
    LOGS.info(
        "You MUST have a python version of at least 3.8."
        "Multiple features depend on this. Bot quitting."
    )
    quit(1)

# Check if the config was edited by using the already used variable.
# Basically, its the 'virginity check' for the config file ;)
CONFIG_CHECK = (os.environ.get(
    "___________PLOX_______REMOVE_____THIS_____LINE__________") or None)

if CONFIG_CHECK:
    LOGS.info(
        "Please remove the line mentioned in the first hashtag from the config.env file"
    )
    quit(1)

# Telegram App KEY and HASH
API_KEY = os.environ.get("API_KEY") or None
API_HASH = os.environ.get("API_HASH") or None


# Userbot Session String
STRING_SESSION = os.environ.get("STRING_SESSION") or None

# Deezloader
DEEZER_ARL_TOKEN = os.environ.get("DEEZER_ARL_TOKEN") or None

# Logging channel/group ID configuration.
BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID") or 0)

# Userbot logging feature switch.
BOTLOG = sb(os.environ.get("BOTLOG") or "False")
if BOTLOG:
    LOGSPAMMER = sb(os.environ.get("LOGSPAMMER") or "False")
else:
    LOGSPAMMER = False

# Bleep Blop, this is a bot ;)
PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN") or "False")

# Heroku Credentials for updater.
HEROKU_MEMEZ = sb(os.environ.get("HEROKU_MEMEZ") or "False")
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME") or None
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY") or None

# Github Credentials for updater and Gitupload.
GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME") or None
GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN") or None

# Custom (forked) repo URL and BRANCH for updater.
UPSTREAM_REPO_URL = (os.environ.get("UPSTREAM_REPO_URL")
                     or "https://github.com/levina-lab/AzumiUserbot.git")
UPSTREAM_REPO_BRANCH = os.environ.get("UPSTREAM_REPO_BRANCH") or "main"

# Console verbose logging
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get(
    "CONSOLE_LOGGER_VERBOSE") or "False")

# SQL Database URI
DB_URI = os.environ.get("DATABASE_URL") or None

# OCR API key
OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY") or None

# remove.bg API key
REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY") or None

# Chrome Driver and Headless Google Chrome Binaries
CHROME_DRIVER = os.environ.get("CHROME_DRIVER") or None
GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN") or None

# OpenWeatherMap API Key
OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID") or None
WEATHER_DEFCITY = os.environ.get("WEATHER_DEFCITY") or None
WEATHER_DEFLANG = os.environ.get("WEATHER_DEFLANG") or None

# Genius lyrics API
GENIUS = os.environ.get("GENIUS_ACCESS_TOKEN") or None

# Wolfram Alpha API
WOLFRAM_ID = os.environ.get("WOLFRAM_ID") or None

# Anti Spambot Config
ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT") or "False")
ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT") or "False")

# Default .alive name
ALIVE_NAME = os.environ.get("ALIVE_NAME") or "Azumi"

# Default .alive logo
ALIVE_LOGO = os.environ.get(
    "ALIVE_LOGO") or "https://telegra.ph/file/a95ae386a01cee3c0892e.png"

# For default inline pic
INLINE_PIC = os.environ.get(
    "INLINE_PIC") or "https://telegra.ph/file/787aeeae0398c8b46c5a5.png"

# Time & Date - Country and Time Zone
COUNTRY = str(os.environ.get("COUNTRY") or "")
TZ_NUMBER = int(os.environ.get("TZ_NUMBER") or 1)

# Version of One4uBot
USERBOT_VERSION = os.environ.get("USERBOT_VERSION") or "4.0"

# User Terminal alias
USER_TERM_ALIAS = os.environ.get("USER_TERM_ALIAS") or "AzumiUserbot"

# Updater alias
UPDATER_ALIAS = os.environ.get("UPDATER_ALIAS") or "AzumiUserbot"

# Zipfile module
ZIP_DOWNLOAD_DIRECTORY = os.environ.get("ZIP_DOWNLOAD_DIRECTORY") or "./zips"

# Clean Welcome
CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME") or "True")

# Last.fm Module
BIO_PREFIX = os.environ.get("BIO_PREFIX") or None
DEFAULT_BIO = os.environ.get("DEFAULT_BIO") or None

LASTFM_API = os.environ.get("LASTFM_API") or None
LASTFM_SECRET = os.environ.get("LASTFM_SECRET") or None
LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME") or None
LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD") or None
LASTFM_PASS = md5(LASTFM_PASSWORD_PLAIN)
if LASTFM_API is not None:
    lastfm = LastFMNetwork(
        api_key=LASTFM_API,
        api_secret=LASTFM_SECRET,
        username=LASTFM_USERNAME,
        password_hash=LASTFM_PASS,
    )
else:
    lastfm = None

# Google Drive Module
G_DRIVE_DATA = os.environ.get("G_DRIVE_DATA") or None
G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID") or None
G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET") or None
G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA") or None
G_DRIVE_FOLDER_ID = os.environ.get("G_DRIVE_FOLDER_ID") or None
TEMP_DOWNLOAD_DIRECTORY = os.environ.get(
    "TMP_DOWNLOAD_DIRECTORY") or "./downloads"

# Uptobox
USR_TOKEN = os.environ.get("USR_TOKEN_UPTOBOX", None)

# Inline bot helper
BOT_TOKEN = os.environ.get("BOT_TOKEN") or None
BOT_USERNAME = os.environ.get("BOT_USERNAME") or None

# For MONGO based DataBase
MONGO_URI = os.environ.get("MONGO_URI", None)

# Init Mongo
MONGOCLIENT = MongoClient(MONGO_URI, 27017, serverSelectionTimeoutMS=1)
MONGO = MONGOCLIENT.userbot


def is_mongo_alive():
    try:
        MONGOCLIENT.server_info()
    except BaseException:
        return False
    return True


# Setting Up CloudMail.ru and MEGA.nz extractor binaries,
# and giving them correct perms to work properly.
if not os.path.exists("bin"):
    os.mkdir("bin")

binaries = {
    "https://raw.githubusercontent.com/adekmaulana/megadown/master/megadown": "bin/megadown",
    "https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py": "bin/cmrudl",
}

for binary, path in binaries.items():
    downloader = SmartDL(binary, path, progress_bar=False)
    downloader.start()
    os.chmod(path, 0o755)

# 'bot' variable
if STRING_SESSION:
    # pylint: disable=invalid-name
    bot = TelegramClient(StringSession(STRING_SESSION), API_KEY, API_HASH)
else:
    # pylint: disable=invalid-name
    bot = TelegramClient("userbot", API_KEY, API_HASH)


async def check_botlog_chatid():
    if not BOTLOG:
        return

    entity = await bot.get_entity(BOTLOG_CHATID)
    if entity.default_banned_rights.send_messages:
        LOGS.info(
            "Your account doesn't have rights to send messages to BOTLOG_CHATID "
            "group. Check if you typed the Chat ID correctly.")
        quit(1)


with bot:
    try:
        bot.loop.run_until_complete(check_botlog_chatid())
    except BaseException:
        LOGS.info(
            "BOTLOG_CHATID environment variable isn't a "
            "valid entity. Check your environment variables/config.env file.")
        quit(1)


async def check_alive():
    await bot.send_message(BOTLOG_CHATID, "```𝘊𝘰𝘯𝘨𝘳𝘢𝘵𝘴𝘴... 🦊𝘼𝙯𝙪𝙢𝙞 𝙐𝙨𝙚𝙧𝙗𝙤𝙩🦊 Has Been Active!!```")
    return

with bot:
    try:
        bot.loop.run_until_complete(check_botlog_chatid())
    except BaseException:
        LOGS.info(
            "BOTLOG_CHATID environment variable isn't a "
            "valid entity. Check your environment variables/config.env file."
        )
        quit(1)

# Global Variables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
ZALG_LIST = {}
ISAFK = False
AFKREASON = None


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


def paginate_help(page_number, loaded_modules, prefix):
    number_of_rows = 5
    number_of_cols = 2
    helpable_modules = [p for p in loaded_modules if not p.startswith("_")]
    helpable_modules = sorted(helpable_modules)
    modules = [
        custom.Button.inline(
            "{} {} 🔸".format(
                "🔸", x), data="ub_modul_{}".format(x))
        for x in helpable_modules
    ]
    pairs = list(zip(modules[::number_of_cols],
                     modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows: number_of_rows * (modulo_page + 1)
        ] + [
            (
                custom.Button.inline(
                    "⇍", data="{}_prev({})".format(prefix, modulo_page)
                ),
                custom.Button.inline(
                    "TUTUP", data="{}_close({})".format(prefix, modulo_page)
                ),
                custom.Button.inline(
                    "⇏", data="{}_next({})".format(prefix, modulo_page)
                ),
            )
        ]
    return pairs


with bot:
    try:
        tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=API_KEY,
            api_hash=API_HASH).start(
            bot_token=BOT_TOKEN)

        dugmeler = CMD_HELP
        me = bot.get_me()
        uid = me.id

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile("open")
            )
        )
        async def opeen(event):
            try:
                tgbotusername = BOT_USERNAME
                if tgbotusername is not None:
                    results = await event.client.inline_query(tgbotusername, "@AzumiUserbot")
                    await results[0].click(
                        event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
                    )
                    await event.delete()
                else:
                    await event.edit(
                        "`The bot doesn't work! Please set the Bot Token and Username correctly. The module has been stopped.`"
                    )
            except Exception:
                return await event.edit(
                    "`You cannot send inline results in this chat (caused by SendInlineBotResultRequest)`"
                )

        azumilogo = INLINE_PIC
        plugins = CMD_HELP
        vr = BOT_VER

        @tgbot.on(events.NewMessage(pattern="/start"))
        async def handler(event):
            if event.message.from_id != uid:
                u = await event.client.get_entity(event.chat_id)
                await event.reply(
                    f"Hallo [{get_display_name(u)}](tg://user?id={u.id}) Selamat Datang Di\n**Azumi Userbot Project**\nKalo mau tau lebih lanjut silahkan Join Ke \n**𝗚𝗥𝗢𝗨𝗣 𝗦𝗨𝗣𝗣𝗢𝗥𝗧** Dibawah Ini.\n",
                    buttons=[
                        [
                            Button.url("📢 Channel Support",
                                       "t.me/levinachannel"),
                            Button.url("🚨 Group support",
                                       "t.me/gcsupportbots")],
                        [Button.url("👤 Development",
                                    "t.me/dlwrml")],
                    ]
                )

        @tgbot.on(events.NewMessage(pattern="/ping"))
        async def handler(event):
            if event.message.from_id != uid:
                start = datetime.now()
                end = datetime.now()
                ms = (end - start).microseconds / 1000
                await tgbot.send_message(
                    event.chat_id,
                    f"**PONG!!**\n `{ms}ms`",
                )

        @tgbot.on(events.InlineQuery)  # pylint:disable=E0602
        async def inline_handler(event):
            builder = event.builder
            result = None
            query = event.text
            if event.query.user_id == uid and query.startswith(
                    "@AzumiUserbot"):
                buttons = paginate_help(0, dugmeler, "helpme")
                result = builder.photo(
                    file=azumilogo,
                    link_preview=False,
                    text=f"🦊𝘼𝙯𝙪𝙢𝙞 𝙐𝙨𝙚𝙧𝙗𝙤𝙩🦊\n\n🦊**Owner : {DEFAULTUSER}**\n\n🦊 **Bot Ver :** `4.0`\n🦊 **𝗠odules :** `{len(plugins)}`\n\n🦊 **Dev : LEVINA **".format(
                        len(dugmeler),
                    ),
                    buttons=buttons,
                )
            elif query.startswith("tb_btn"):
                result = builder.article(
                    "Bantuan Dari 🦊𝘼𝙯𝙪𝙢𝙞 𝙐𝙨𝙚𝙧𝙗𝙤𝙩🦊 ",
                    text="Daftar Plugins",
                    buttons=[],
                    link_preview=True)
            else:
                result = builder.article(
                    " 🦊𝘼𝙯𝙪𝙢𝙞 𝙐𝙨𝙚𝙧𝙗𝙤𝙩🦊 ",
                    text="""**🦊𝘼𝙯𝙪𝙢𝙞 𝙐𝙨𝙚𝙧𝙗𝙤𝙩🦊\n\n Anda Bisa Membuat Geez Userbot Anda Sendiri Dengan Cara:** __TEKAN DIBAWAH INI!__ 👇""",
                    buttons=[
                        [
                            custom.Button.url(
                                "🦊𝘼𝙯𝙪𝙢𝙞 𝙐𝙨𝙚𝙧𝙗𝙤𝙩🦊",
                                "https://github.com/levina-lab/AzumiUserbot"),
                            custom.Button.url(
                                "OWNER",
                                "t.me/dlwrml")]],
                    link_preview=False,
                )
            await event.answer([result] if result else None)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"helpme_next\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # pylint:disable=E0602
                current_page_number = int(
                    event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(
                    current_page_number + 1, dugmeler, "helpme")
                # https://t.me/TelethonChat/115200
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = f"🚫!WARNING!🚫 Jangan Menggunakan Milik {DEFAULTUSER}."
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"helpme_close\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # @AzumiUserbot
                # https://t.me/TelethonChat/115200
                await event.edit(
                    file=azumilogo,
                    link_preview=True,
                    buttons=[
                        [
                            Button.url("📢 Channel Support",
                                       "t.me/levinachannel"),
                            Button.url("🚨 Group support",
                                       "t.me/gcsupportbots")],
                        [custom.Button.inline(
                            "Close", b"close")],
                    ]
                )

        @ tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"helpme_prev\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # pylint:disable=E0602
                current_page_number = int(
                    event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(
                    current_page_number - 1, dugmeler, "helpme"  # pylint:disable=E0602
                )
                # https://t.me/TelethonChat/115200
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = f"🚫!WARNING!🚫 Jangan Menggunakan Milik {DEFAULTUSER}."
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"ub_modul_(.*)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # pylint:disable=E0602
                modul_name = event.data_match.group(1).decode("UTF-8")

                cmdhel = str(CMD_HELP[modul_name])
                if len(cmdhel) > 180:
                    help_string = (
                        str(CMD_HELP[modul_name]).replace(
                            '`', '')[:180] + "..."
                        + "\n\nBaca Text Berikutnya Ketik .help "
                        + modul_name
                        + " "
                    )
                else:
                    help_string = str(CMD_HELP[modul_name]).replace('`', '')

                reply_pop_up_alert = (
                    help_string
                    if help_string is not None
                    else "{} No document has been written for module.".format(
                        modul_name
                    )
                )
            else:
                reply_pop_up_alert = f"🚫!WARNING!🚫 Jangan Menggunakan Milik {DEFAULTUSER}."

            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(events.CallbackQuery(data=b"close"))
        async def close(event):
            await event.edit("Menu Ditutup!", buttons=Button.clear())

    except BaseException:
        LOGS.info(
            "Mode Inline Bot Mu Nonaktif. "
            "Untuk Mengaktifkannya, Silahkan Pergi Ke @BotFather Lalu, Settings Bot > Pilih Mode Inline > Turn On. ")
    try:
        bot.loop.run_until_complete(check_botlog_chatid())
    except BaseException:
        LOGS.info(
            "BOTLOG_CHATID Environment Variable Isn't a "
            "Valid Entity. Please Check Your Environment variables/config.env File.")
        quit(1)
