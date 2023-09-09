import asyncio
import importlib
from pyrogram import Client, idle
from Ryuzaki.modules import ALL_MODULES
from Ryuzaki import clients

async def start_bot():
    for all_module in ALL_MODULES:
        importlib.import_module(f"Ryuzaki.modules{all_module}")
        print(f"Successfully Imported {all_module}")
    for pro in clients:
        try:
            await pro.start()
            ur = await pro.get_me()
            print(f"Started {ur.first_name}")
        except Exception as e:
            print(f"{e}")
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
