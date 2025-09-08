# Don't Remove Credit @CodeFlix_Bots, @rohit_1888
# Ask Doubt on telegram @CodeflixSupport
#
# Copyright (C) 2025 by Codeflix-Bots@Github, < https://github.com/Codeflix-Bots >.
#
# This file is part of < https://github.com/Codeflix-Bots/FileStore > project,
# and is released under the MIT License.
# Please see < https://github.com/Codeflix-Bots/FileStore/blob/master/LICENSE >
#
# All rights reserved.
#

import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler

#rohit_1888 on Tg
#--------------------------------------------
#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", "")) #Your API ID from my.telegram.org
API_HASH = os.environ.get("API_HASH", "") #Your API Hash from my.telegram.org
#--------------------------------------------

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "")) #Your db channel Id
OWNER = os.environ.get("OWNER", "") # Owner username without @
OWNER_ID = int(os.environ.get("OWNER_ID", "")) # Owner id
#--------------------------------------------
PORT = os.environ.get("PORT", "8001")
#--------------------------------------------
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluooo")
#--------------------------------------------
FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "10"))  # 0 means no expiry
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "https://t.me/spk_links")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))
#--------------------------------------------
START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/ec17880d61180d3312d6a.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/e292b12890b8b4b9dcbd1.jpg")

#--------------------------------------------
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 21600)) # Add time in seconds
TUT_VID = os.environ.get("TUT_VID","")

#--------------------------------------------

#--------------------------------------------
HELP_TXT = "<b><blockquote>ᴛʜɪs ɪs ᴀɴ ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ ᴡᴏʀᴋ ғᴏʀ @spk_links\n\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n├/myplan : ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ sᴛᴀᴛᴜs\n└@Spk_links_1_bot : ᴄᴏɴᴛᴀᴄᴛ ʜᴇʀᴇ ᴛᴏ ɢᴇᴛ Membership\n\n sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!\n\n ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ <a href=https://t.me/spk_links>suvo</a></blockquote></b>"
ABOUT_TXT = "<b><blockquote>◈ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/spk_links>Suvo</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/spk_links>ᴏᴛᴀᴋᴜғʟɪx ɴᴇᴛᴡᴏʀᴋ</a>\n◈ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/+SInyGLpoVWw1Nzhl>ᴀɴɪᴍᴇ ᴄʀᴜɪsᴇ</a>\n◈ sᴇʀɪᴇs ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/spk_links>ᴡᴇʙsᴇʀɪᴇs ғʟɪx</a>\n◈ ᴀᴅᴜʟᴛ ᴍᴀɴʜᴡᴀ : <a href=https://t.me/spk_links>ᴘᴏʀɴʜᴡᴀs</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/spk_links>Suvo</a></blockquote></b>"
#--------------------------------------------
#--------------------------------------------
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ {mention}\n\n<blockquote> ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.</blockquote></b>")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {mention}\n\n<b><blockquote>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b></blockquote>")

CMD_TXT = """<blockquote><b>» ADMIN COMMANDS:</b></blockquote>

<blockquote><b>📊 Bot Statistics</b></blockquote>
<b>/users :</b> VIEW BOT STATISTICS (ADMIN ONLY)
<b>/stats :</b> CHECK YOUR BOT UPTIME (ADMIN ONLY)
<b>/count :</b> COUNT SHORTNER CLICKS (ADMIN ONLY)

<blockquote><b>📢 Broadcast Commands</b></blockquote>
<b>/broadcast :</b> BROADCAST ANY MESSAGES TO BOT USERS (ADMIN ONLY)
<b>/dbroadcast :</b> BROADCAST ANY MESSAGES WITH AUTO DELETE (ADMIN ONLY)
<b>/pbroadcast :</b> PIN A BROADCAST TO ALL USER'S CHAT (ADMIN ONLY)

<blockquote><b>⏳ Auto Delete</b></blockquote>
<b>/dlt_time :</b> SET AUTO DELETE TIME FOR FILES (ADMIN ONLY)
<b>/check_dlt_time :</b> CHECK CURRENT DELETE TIME SETTING (ADMIN ONLY)

<blockquote><b>🚫 User Management</b></blockquote>
<b>/ban :</b> BAN A USER FROM USING THE BOT (ADMIN ONLY)
<b>/unban :</b> UNBAN A PREVIOUSLY BANNED USER (ADMIN ONLY)
<b>/banlist :</b> GET LIST OF BANNED USERS (ADMIN ONLY)
<b>/delreq :</b> REMOVE USERS THAT LEFT CHANNEL AND NOT GETTING REQUEST FSUB (ADMIN ONLY)

<blockquote><b>📺 Force Subscribe</b></blockquote>
<b>/addchnl :</b> ADD A CHANNEL FOR FORCE SUBSCRIPTION (ADMIN ONLY)
<b>/delchnl :</b> REMOVE A FORCE SUBSCRIBE CHANNEL (ADMIN ONLY)
<b>/listchnl :</b> VIEW ALL ADDED FORCE SUBSCRIBE CHANNELS (ADMIN ONLY)
<b>/fsub_mode :</b> TOGGLE FORCE SUBSCRIBE ON OR OFF (ADMIN ONLY)

<blockquote><b>👮 Admin Management</b></blockquote>
<b>/add_admin :</b> ADD A NEW ADMIN (ADMIN ONLY)
<b>/deladmin :</b> REMOVE AN ADMIN (ADMIN ONLY)
<b>/admins :</b> LIST ALL CURRENT ADMINS (ADMIN ONLY)

<blockquote><b>⭐ Premium Management</b></blockquote>
<b>/addpremium :</b> GRANT PREMIUM ACCESS TO A USER (ADMIN ONLY)
<b>/premium_users :</b> LIST ALL PREMIUM USERS (ADMIN ONLY)
<b>/remove_premium :</b> REMOVE PREMIUM FROM A USER (ADMIN ONLY)
"""
#--------------------------------------------
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @spk_links</b>") #set your Custom Caption here, Keep None for Disable Custom Caption
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False #set True if you want to prevent users from forwarding files from bot
#--------------------------------------------
#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", "True") == 'True'
#--------------------------------------------
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"

#==========================(BUY PREMIUM)====================#

OWNER_TAG = os.environ.get("OWNER_TAG", "@Subho5995")
UPI_ID = os.environ.get("UPI_ID", "")
QR_PIC = os.environ.get("QR_PIC", "https://telegra.ph/file/3e83c69804826b3cba066-16cffa90cd682570da.jpg")
SCREENSHOT_URL = os.environ.get("SCREENSHOT_URL", f"t.me/spk_links")
#--------------------------------------------
#Time and its price
#3 Days
PRICE1 = os.environ.get("PRICE1", "29 rs")
#7 Days
PRICE2 = os.environ.get("PRICE2", "49 rs")
#1 Month
PRICE3 = os.environ.get("PRICE3", "99 rs")
#2 Month
PRICE4 = os.environ.get("PRICE4", "149 rs")
#3 Month
PRICE5 = os.environ.get("PRICE5", "199 rs")

#===================(END)========================#

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
