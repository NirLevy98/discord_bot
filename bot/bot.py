from discord.ext import commands
from bot.config import BotConfig,  DiscordConfig


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        self.config = BotConfig(
            discord=DiscordConfig(token=kwargs.get("token", None), guid=kwargs.get("guid", None)),
            command_prefix=kwargs.get("command_prefix", None))
        super().__init__(*args, **kwargs)

    def run(self, *args, **kwargs):
        super(Bot, self).run(*args, **kwargs)
