# code by @xtdevs
# library RyuzakiLib

from pyrogram import Client, filters
from pyrogram.types import Message

from Ryuzaki.modules.help import *

from RyuzakiLib.hackertools.chatgpt import RendyDevChat

@Client.on_message(filters.command(["ai", "ask"]) & filters.me)
async def chatgpt_support(client: Client, message: Message):
    pro = await message.reply_text("`Processing.....`")
    deny_ask_hehe = message.text.split(" ", 1)[1] if len(message.command) > 1 else None
    if not deny_ask_hehe:
        await pro.edit_text("Give ask from chatgpt")
        return
    try:
        hacking = RendyDevChat(deny_ask_hehe).get_response(message)
        await client.send_message(
            message.chat.id,
            hacking,
            reply_to_message_id=message.id
        )
        await pro.delete()
    except Exception as e:
        await pro.edit_text(str(e))
        return
    
add_command_help(
    "openai",
    [
        ["ai or ask [question]", "To ask questions using the assistant bot"],
    ],
)
