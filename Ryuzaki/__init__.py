
import asyncio
import logging
import time
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import Message

from pymongo import MongoClient
from pyrogram import Client
from pyrogram.types import *
from pyrogram import filters
from pyrogram.raw.all import layer
from pyrogram.handlers import MessageHandler
from aiohttp import ClientSession

from config import *

logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.basicConfig(level=logging.INFO)

LOGS = logging.getLogger(__name__)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

if not SESSION_STRING:
    print("Warning no session String")

logger = logging.getLogger(__name__)

StartTime = time.time()
START_TIME = dt.now()
CMD_HELP = {}
clients = []
ids = []
act = []

aiohttpsession = ClientSession()

client = Client(
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING,
    plugins=dict(root="Ryuzaki.modules")
)
clients.append(client)
