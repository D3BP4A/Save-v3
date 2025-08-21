# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv

load_dotenv()

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = os.getenv("API_ID", "14228286")
API_HASH = os.getenv("API_HASH", "76f5902a82ffcdc75dcf4777a320e3e1")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8261328890:AAHbUzf4FSi2QK4eocM0zjVD3WDh4tN0MAM")
MONGO_URI = os.getenv("MONGO_DB", "mongodb+srv://DE3PM:DE3PM@de3pm.vkghl.mongodb.net/?retryWrites=true&w=majority&appName=DE3PM")
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "8436530420").split())) # list seperated via space
DB_NAME = os.getenv("DB_NAME", "telegram_downloader")
STRING = os.getenv("STRING", None) # optional
LOG_GROUP = int(os.getenv("LOG_GROUP", "-1002178975255")) # optional with -100
FORCE_SUB = int(os.getenv("FORCE_SUB", "-1002178975255")) # optional with -100
YT_COOKIES = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)
