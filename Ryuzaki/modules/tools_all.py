import datetime
import math
import random
import time
import uuid
from random import randint

from pyrogram.types import Message, User
from pyrogram import Client, enums

async def get_ub_chats(
    client: Client,
    chat_types: list = [
        enums.ChatType.GROUP,
        enums.ChatType.SUPERGROUP,
        enums.ChatType.CHANNEL,
    ],
    is_id_only=True,
):
    ub_chats = []
    async for dialog in client.get_dialogs():
        if dialog.chat.type not in chat_types:
            continue
        if is_id_only:
            ub_chats.append(dialog.chat.id)
        else:
            ub_chats.append(dialog.chat)
    return ub_chats

def ReplyCheck(message: Message):
    reply_id = None

    if message.reply_to_message:
        reply_id = message.reply_to_message.id

    elif not message.from_user.is_self:
        reply_id = message.id

    return reply_id


def SpeedConvert(size):
    power = 2 ** 10
    zero = 0
    units = {0: "", 1: "Kbit/s", 2: "Mbit/s", 3: "Gbit/s", 4: "Tbit/s"}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


def GetFromUserID(message: Message):
    return message.from_user.id


def GetChatID(message: Message):
    return message.chat.id


def GetUserMentionable(user: User):
    if user.username:
        username = f"@{user.username}"
    else:
        if user.last_name:
            name_string = f"{user.first_name} {user.last_name}"
        else:
            name_string = f"{user.first_name}"

        username = f"<a href='tg://user?id={user.id}'>{name_string}</a>"

    return username

def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    return "" if not " ".join(split[1:]).strip() else " ".join(split[1:])

def split_list(input_list, n):
    n = max(1, n)
    return [input_list[i: i + n] for i in range(0, len(input_list), n)]


def human_time(*args, **kwargs):
    secs = float(datetime.timedelta(*args, **kwargs).total_seconds())
    units = [("day", 86400), ("hour", 3600), ("minute", 60), ("second", 1)]
    parts = []
    for unit, mul in units:
        if secs / mul >= 1 or mul == 1:
            if mul > 1:
                n = int(math.floor(secs / mul))
                secs -= n * mul
            else:
                n = secs if secs != int(secs) else int(secs)
            parts.append(f'{n} {unit}{"" if n == 1 else "s"}')
    return ", ".join(parts)


def random_interval():
    rand_value = randint(14400, 43200)
    delta = (time.time() + rand_value) - time.time()
    return int(delta)


def get_random_hex(chars=4):
    return uuid.uuid4().hex[:chars]


def get_mock_text(sentence):
    new_sentence = ""
    for number, letter in enumerate(sentence.lower()):
        if len(new_sentence) < 2:
            random_number = random.randint(
                0, 1
            )
            new_sentence += letter.upper() if random_number == 0 else letter
        elif (
                    new_sentence[number - 2].isupper()
                    and new_sentence[number - 1].isupper()
                    or new_sentence[number - 2].islower()
                    and new_sentence[number - 1].islower()
            ):
            new_sentence += (
                letter.lower()
                if new_sentence[number - 1].isupper()
                else letter.upper()
            )
        else:
            random_number = random.randint(0, 1)
            new_sentence += letter.upper() if random_number == 0 else letter
    return new_sentence
