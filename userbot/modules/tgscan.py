# Copyright (C) 2021 By Veez Project
# All Right Reserved


from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, pattern=r"^\.tscan(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply_message = await event.get_reply_message()
    if not event.reply_to_msg_id:
        await event.edit("```mohon balas ke pesan si pengguna, atau ketik .tscan (id/username) nya untuk mendeteksi.```")
        return
    if input_str:
        try:
            uid = int(input_str)
        except ValueError:
            try:
                u = await event.client.get_entity(input_str)
            except ValueError:
                await edit.event("`mohon berikan id/username si pengguna untuk mendeteksi.`"
                                 )
            uid = u.id
    else:
        uid = reply_message.sender_id
    chat = "@tgscanrobot"
    event = await event.edit("`mendeteksi...`")
    async with bot.conversation(chat) as conv:
        try:
            await conv.send_message(f"{uid}")
        except YouBlockedUserError:
            await steal.reply(
                "```boss, mohon unblock @tgscanrobot lalu coba lagi.```"
            )
        response = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.edit(response.text)


def inline_mention(user):
    full_name = user_full_name(user) or "no name"
    return f"[{full_name}](tg://user?id={user.id})"


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    return " ".join(names)


# Alvin Ganteng
CMD_HELP.update({
    "scanner":
        "`𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .tscan`\
          \nUsage: Mendeteksi riwayat grup dari seseorang."
})
