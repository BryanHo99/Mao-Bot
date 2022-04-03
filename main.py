from os.path import isfile

import config
from mao_bot import MaoBot


def main():
    if not isfile(".env"):
        print("No '.env' file found.\nPlease make sure it is there.")

    else:
        bot = MaoBot(command_prefix=config.PREFIX)
        bot.run(config.BOT_TOKEN)


if __name__ == "__main__":
    main()
