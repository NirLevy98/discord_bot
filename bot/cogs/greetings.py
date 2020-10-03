import random
import logging
import discord

from discord.ext import commands
from discord.ext.commands import Cog

from bot.cogs.error_handler import ErrorHandler
from pathlib import Path
from bot.config import LoggerConfig
from bot.discord_helper_functions import send_photo


class Greetings(Cog):
    def __init__(self, bot):
        self.logger = logging.getLogger(__name__)
        self.init_logger()
        self.bot = bot
        self._last_member = None
        self.resources_path = Greetings.get_resources_path()

    def init_logger(self):
        # Create handlers
        c_handler = logging.StreamHandler()
        c_handler.setLevel(LoggerConfig.level)

        # Create formatters and add it to handlers
        c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        c_handler.setFormatter(c_format)

        # Add handlers to the logger
        self.logger.addHandler(c_handler)

    @staticmethod
    def get_resources_path():
        path = Path(__file__).parent.parent.parent
        rel_path = r"resources"
        return Path.joinpath(path, rel_path)

    @Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'Welcome {member.display_name}')
            self.logger.info(f'{member.display_name} joined the channel')

    @commands.command()
    async def hello(self, ctx, *, member: discord.member.Member = None):
        member = member or ctx.author
        if self._last_member is None or self._last_member.id == member.id:
            await ctx.send(f'Hello {member.display_name}')
        else:
            await ctx.send(f'Hello {member.display_name}... sound familiar.')
        self._last_member = member

    @commands.command()
    async def gonen(self, ctx):
        message_embed = ErrorHandler.get_error_embed('Gonen is the king!.', 'Always!!!')
        await ctx.send(embed=message_embed)

    @commands.command()
    async def tedi(self, ctx):
        random_tedi_photo_number = random.randint(0, 6)
        tedi_photo_path = Path.joinpath(self.resources_path, rf"tedi_0{random_tedi_photo_number}.jpeg")
        await send_photo(ctx, tedi_photo_path, "tedi")

    @commands.command()
    async def idan(self, ctx):
        idan_photo_path = Path.joinpath(self.resources_path, rf"idan.png")
        await send_photo(ctx, idan_photo_path, "idan")

    @commands.command()
    async def family(self, ctx):
        family_photo_path = Path.joinpath(self.resources_path, rf"family.jpeg")
        await send_photo(ctx, family_photo_path, "family")

    @commands.command()
    async def vatil(self, ctx):
        vatil_photo_path = Path.joinpath(self.resources_path, rf"vatil.png")
        await send_photo(ctx, vatil_photo_path, "vatil")

    @commands.command()
    async def rebar(self, ctx):
        rebar_photo_path = Path.joinpath(self.resources_path, rf"rear.jpeg")
        await send_photo(ctx, rebar_photo_path, "rebar")

    @commands.command()
    async def spam(self, ctx, member: discord.member.Member, number_of_messages: int):
        for message_counter in range(number_of_messages):
            await member.send(f"SPAM NUMBER #{message_counter}")


def setup(bot):
    bot.add_cog(Greetings(bot))
