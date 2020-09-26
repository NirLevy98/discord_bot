import argparse
import os
from dotenv import load_dotenv
from bot import Bot


def is_command_prefix_validate(command_prefix):
    if type(command_prefix) == str and len(command_prefix) > 3:
        return argparse.ArgumentTypeError(
            f'{command_prefix} is not a valid prefix. Prefix need to be less than 3 characters')
    return command_prefix


def parse_args():
    load_dotenv()
    parser = argparse.ArgumentParser(description='Discord Bot')
    parser.add_argument('--token', type=str, dest="token", default=os.getenv('DISCORD_TOKEN'),
                        help='TOKEN for connecting the  bot')
    parser.add_argument('--guid', type=str, dest='guid', default=os.getenv('DISCORD_GUILD'),
                        help='GUID for connect to specific server')
    parser.add_argument('--command_prefix', dest='command_prefix',
                        help='Command Prefix for the bot(For example: ! or $', default="!",
                        type=is_command_prefix_validate)
    args = parser.parse_args()
    return args


def load_extensions(bot: Bot):
    bot.load_extension("cogs.error_handler")
    bot.load_extension("cogs.greetings")


def main():
    args = parse_args()
    bot = Bot(command_prefix=args.command_prefix)
    load_extensions(bot)
    print("Starting bot...")
    print(f'The bot token is:{args.token}')
    print(f'The bot prefix is:{args.command_prefix}')
    bot.run(args.token)


if __name__ == '__main__':
    main()
