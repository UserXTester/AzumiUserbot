# Copyright (C) 2021 By Veez Project
# Ported From Ultroid
# This file is part of Geez Userbot and Ultroid Userbot
# bug not fixed !!

from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from telethon.tl.types import ChatAdminRights
from userbot import CMD_HELP
from userbot.events import register

NO_ADMIN = "`maaf, anda bukan admin!`"


async def get_call(event):
    geez = await event.client(getchat(event.chat_id))
    vcky = await event.client(getvc(geez.full_chat.call))
    return vcky.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i: i + n]


@register(outgoing=True, pattern=r"^\.startvc$", groups_only=True)
async def _(e):
    chat = await e.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        return await e.edit(NO_ADMIN)
    new_rights = ChatAdminRights(invite_users=True)
    try:
        await e.client(startvc(e.chat_id))
        await e.edit("`voice chat dimulai...`")
    except Exception as ex:
        await e.edit(f"`{str(ex)}`")


@register(outgoing=True, pattern=r"^\.stopvc$", groups_only=True)
async def _(e):
    chat = await e.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        return await e.edit(NO_ADMIN)
    new_rights = ChatAdminRights(invite_users=True)
    try:
        await e.client(stopvc(await get_call(e)))
        await e.edit("`voice chat dimatikan...`")
    except Exception as ex:
        await e.edit(f"`{str(ex)}`")


@register(outgoing=True, pattern=r"^\.vcinvite", groups_only=True)
async def _(e):
    await e.edit("`mengundang member ke voice chat...`")
    users = []
    z = 0
    async for x in e.client.iter_participants(e.chat_id):
        if not x.bot:
            users.append(x.id)
    hmm = list(user_list(users, 6))
    for p in hmm:
        try:
            await e.client(invitetovc(call=await get_call(e), users=p))
            z += 6
        except BaseException:
            pass
    await e.edit(f"`invited {z} users`")


CMD_HELP.update(
    {
        "calls": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.startvc`\
         \n↳ : Start Group Call in a group.\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.stopvc`\
         \n↳ : `Stop Group Call in a group.`\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.vcinvite`\
         \n↳ : Invite all members of group in Group Call. (You must be joined)."
    }
)
