from pyrogram import Client, filters
from pyrogram.types import Message

from config import *
from Ryuzaki.modules.help import *
from RyuzakiLib.extreme.userinfo import TelegramUserInfo

async def extract_userid(message, text: str):
    def is_int(text: str):
        try:
            int(text)
        except ValueError:
            return False
        return True

    text = text.strip()

    if is_int(text):
        return int(text)

    entities = message.entities
    app = message._client
    if len(entities) < 2:
        return (await app.get_users(text)).id
    entity = entities[1]
    if entity.type == "mention":
        return (await app.get_users(text)).id
    return entity.user.id if entity.type == "text_mention" else None


async def extract_user_and_reason(message, sender_chat=False):
    args = message.text.strip().split()
    text = message.text
    user = None
    reason = None
    if message.reply_to_message:
        reply = message.reply_to_message
        if reply.from_user:
            id_ = reply.from_user.id

        elif (
                reply.sender_chat
                and reply.sender_chat != message.chat.id
                and sender_chat
            ):
            id_ = reply.sender_chat.id
        else:
            return None, None
        reason = None if len(args) < 2 else text.split(None, 1)[1]
        return id_, reason

    if len(args) == 2:
        user = text.split(None, 1)[1]
        return await extract_userid(message, user), None

    if len(args) > 2:
        user, reason = text.split(None, 2)[1:]
        return await extract_userid(message, user), reason

    return user, reason


async def extract_user(message):
    return (await extract_user_and_reason(message))[0]


@Client.on_message(filters.command(["info"], PREFIXES_CMD) & filters.me)
async def userinfoc(client: Client, message: Message):
    pro = await message.reply_text("`Processing....`")
    user_id = await extract_user(message)
    if not user_id:
        await pro.edit_text("Give user id from userinfo")
        return
    hacking = await TelegramUserInfo(user_id).who_is(client)
    if hacking[0]:
        await client.send_photo(
            message.chat.id,
            hacking[0],
            caption=hacking[1]
        )
        await pro.delete()
    else:
        await pro.edit_text(hacking[1])
