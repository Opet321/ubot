# code by @xtdevs
# library RyuzakiLib

from pyrogram import Client, filters
from pyrogram.types import Message

from Ryuzaki.modules.help import *
from config import *

from RyuzakiLib.hackertools.github import GithubUsername

@Client.on_message(filters.command(["github", "git"], PREFIXES_CMD) & filters.me)
async def github_search(client: Client, message: Message):
    pro = await message.reply_text("`Processing.....`")
    username = message.text.split(" ", 1)[1] if len(message.command) > 1 else None
    if not username:
        await pro.edit_text("Give username from github")
        return
    try:
        hacking = await GithubUsername(username).get_github_data()
        await client.send_photo(
            message.chat.id,
            hacking[1],
            caption=hacking[0],
            reply_to_message_id=message.id
        )
        await pro.delete()
    except Exception as e:
        await pro.edit_text(str(e))
        return
    
add_command_help(
    "github",
    [
        ["github or git [username]", "To Search for a github user"],
    ],
)
