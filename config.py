import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("AgAmOrYfH-3Spao4z9RQ97DNH_2RkAkUSKdhSMsTzf4CJcaye0SUFyCoJuvfyKDcY9_U0wfHB1JA_w3jDB5QJM7wO7IeSzSEMWh_keE-JWDn4b7hAYiVW9_b043IvH72BBoiFwLYpNeV50b__3gMAndJgjQuVocNVNfludcx6T6ctJKUZOwN8XzgcCGfR9Mbw-QDg6mgZbFt4TTBgBVIp_YfRM2y_WY3I38-MbIJ0DTIHqToxYGxQkNONtR0YDs2YDJS6pm4GGE7jWLypXztLfzwUAebkkAlUKNhKbmwVN-YdI7syTkEqbiC02CVs9CqshCZNu3lqFwFjyLGg7EpYjZDAAAAAUfeVr8A", "AgAmOrYfH-")
BOT_TOKEN = getenv("5720406158:AAFo1Iyb7beAZnPM8vGvxWzKywGUmkyGjVw")
BOT_NAME = getenv("BOT_NAME", ". 𝖬𝗎𝗌𝗂𝖼 𝖱𝗂𝗈 . ")
API_ID = int(getenv("9186219"))
API_HASH = getenv("219c6122db6da9511abe1fee87a43e01")
OWNER_NAME = getenv("OWNER_NAME", "vv5nv")
ALIVE_NAME = getenv("ALIVE_NAME", "سورس فولتر ميوزك")
BOT_USERNAME = getenv("BOT_USERNAME", "vvr4bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "VVKK8")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "TI9TI9")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "TI9TI9")
SUDO_USERS = list(map(int, getenv("5340127979").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/b3582257ed6036ca095fa.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://telegra.ph/file/b3582257ed6036ca095fa.jpg")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/b3582257ed6036ca095fa.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/b3582257ed6036ca095fa.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/b3582257ed6036ca095fa.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/b3582257ed6036ca095fa.jpg")
