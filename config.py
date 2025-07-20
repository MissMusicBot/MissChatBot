from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "26504251"
# -------------------------------------------------------------
API_HASH = "a50070614b2e87e3a0f2cd3ae08034c9"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", "8134992251:AAG1UJA-5d9Ts6_PzJnK7zaXWWgWxM6DW0I")
STRING1 = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Sweettoxic:Sweettoxic@sweettoxic.mg57v4c.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = int(getenv("OWNER_ID", "8130271170"))
SUPPORT_GRP = "muzic7888"
UPDATE_CHNL = "muzic7888"
OWNER_USERNAME = "System0999"
