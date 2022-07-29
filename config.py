## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCnHo6AOzcU3qSZXCmzOFB8AUH0NWHgQaFDY9Bd5DTGEYlODL8J2zuA_sGNxkMJoKEd17xVPnGPT8Zq79U1KxD5Ph5WNOtSCA1gGPsJ9E9HucI1jnklKjOshivGbzP4Pi-x2xx41u-hpu99dKpyr0PHcExFHMkPJZQYAaG2DfnIKomYFLN2bgIGs5nYoUdC6_sOsP5BBCDSIHBvwGYNIrFS1iRmhE_9RfnkV2UVX7AVvW1Kiu3_4-asXblY7rq1Y2QqU3-nl9o8p0NB2wBVq7wg--CTlSSa4wIsL1FNZNDMY_JefORxw9ULTkaN88ctg37ddAEze5cSkCicMF8zjITMcoIBZgA")
BOT_TOKEN = getenv("BOT_TOKEN", "2081393992:AAGsApcFR0_FX9Y-RGlyct3UIBEn3UnUgjY")
BOT_NAME = getenv("BOT_NAME", "Cristiano Ronaldo x Robot")
API_ID = int(getenv("API_ID", "6439635"))
API_HASH = getenv("API_HASH", "cff5ae354fffc28e97739586d10c70a7")
OWNER_NAME = getenv("OWNER_NAME", "Suryaakumar")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Suryaakumar")
ALIVE_NAME = getenv("ALIVE_NAME", "Suryaa")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME")
GROUP_SUPPORT = getenv("GROUP_SUPPORT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1669178360").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
