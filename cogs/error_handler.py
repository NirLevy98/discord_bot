from discord import Embed

from discord.ext.commands import Cog, context, errors


class ErrorHandler(Cog):
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    def get_error_embed(title: str, body: str) -> Embed:
        """Return an embed that contains the exception."""
        return Embed(
            title=title,
            description=body
        )

    @Cog.listener()
    async def on_command_error(self, ctx: context, e: errors.CommandError) -> None:
        command = ctx.command
        if isinstance(e, errors.BadArgument):
            error_embed = ErrorHandler.get_error_embed("BadArgument", str(e))
            await ctx.send(embed=error_embed)


def setup(bot):
    bot.add_cog(ErrorHandler(bot))
