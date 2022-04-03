from os import getenv
from dotenv.main import load_dotenv


load_dotenv()

# Bot setup.
PREFIX = "!"
BOT_NAME = "Mao Bot"
BOT_TOKEN = getenv("BOT_TOKEN", "")

# Discord guild ID.
GUILD_ID = int(getenv("GUILD_ID"))

# Discord channel IDs.
WELCOME_CHANNEL_ID = int(getenv("WELCOME_CHANNEL_ID", ""))
REACT_ROLES_CHANNEL_ID = int(getenv("REACT_ROLES_CHANNEL_ID", ""))
GENERAL_CHANNEL_ID = int(getenv("GENERAL_CHANNEL_ID", ""))
DOTA_CHANNEL_ID = int(getenv("DOTA_CHANNEL_ID", ""))
GENSHIN_CHANNEL_ID = int(getenv("GENSHIN_CHANNEL_ID", ""))
DEV_CHANNEL_ID = int(getenv("DEV_CHANNEL_ID", ""))
MUSIC_CHANNEL_ID = int(getenv("MUSIC_CHANNEL_ID", ""))
BOT_SPAM_CHANNEL_ID = int(getenv("BOT_SPAM_CHANNEL_ID", ""))

# Discord role IDs.
MAO_ROLE_ID = int(getenv("MAO_ROLE_ID", ""))
BOT_DEV_ROLE_ID = int(getenv("BOT_DEV_ROLE_ID", ""))
GENSHIN_ROLE_ID = int(getenv("GENSHIN_ROLE_ID", ""))
DOTA_ROLE_ID = int(getenv("DOTA_ROLE_ID", ""))

# Discord message IDs.
REACT_ROLES_MESSAGE_ID = int(getenv("REACT_ROLES_MESSAGE_ID", ""))

# Discord member IDs.
MAO_BOT_ID = int(getenv("MAO_BOT_ID", ""))
SCARLET_SPARK_ID = int(getenv("SCARLET_SPARK_ID", ""))
