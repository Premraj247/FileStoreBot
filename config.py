import os

API_ID = int(os.environ.get("API_ID", "26304894"))
API_HASH = os.environ.get("API_HASH", "ef1fb151bca2c1fa2544f67e3067ace7"
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5789677373:AAGVJ8ov8mWivbdaMdH6hxN7Z_nYER75qD8")
DB_CHANNEL_ID = os.environ.get("DB_CHANNEL_ID", "-1001967862801")
IS_PRIVATE = os.environ.get("IS_PRIVATE",False) # any input is ok But True preferable
OWNER_ID = int(os.environ.get("OWNER_ID", "5115252245"))
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', "NEWMOVIEUPDATE247")
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "5115252245").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)
