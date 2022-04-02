# Dependencies
from os.path import isfile
from dotenv import dotenv_values


# Local imports
from mao_bot import MaoBot


def main():
    if not isfile(".env"):
        print("No '.env' file found.\nPlease make sure it is there.")

    else:
        config = dotenv_values(".env")
        bot_token = config.get("BOT_TOKEN")

        bot = MaoBot()
        bot.run(bot_token)


if __name__ == "__main__":
    main()
