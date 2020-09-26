from discord.ext import commands


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        self.token = kwargs.get("token", None)
        super().__init__(*args, **kwargs)

    def run(self, *args, **kwargs):
        super(Bot, self).run(*args, **kwargs)
