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
OWNER_ID= getenv("OWNER_ID", "1782402849")
ALIVE_NAME = getenv("ALIVE_NAME", "Suryaa")
BOT_USERNAME = getenv("BOT_USERNAME", "Zaynmalik_gc_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Cristiano Ronaldo x Robot assistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "mafia_kings_tg")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "mafiaking_fed")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1782402849").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/bbbd9b011a11544d321d8.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/40f7da0c6f0dd5915de99.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "180"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/skizzyyir/tamil-music")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/152a3def02458d6617306.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/ed69743673752c8380957.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/3e695f45ae66c74ad702a.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/367e6a2a23939de4f4499.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/fa1334bf64a31e0072b93.jpg")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/800c697809b45f91f7cf5.jpg")
