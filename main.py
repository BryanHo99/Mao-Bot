import config
from mao_bot import MaoBot


def main():
    bot = MaoBot(command_prefix=config.PREFIX)
    bot.run(config.BOT_TOKEN)


if __name__ == "__main__":
    main()
