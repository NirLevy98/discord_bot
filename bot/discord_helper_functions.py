import discord


async def send_photo(ctx, photo_path, file_name):
    with open(photo_path, "rb") as file:
        photo = discord.file.File(file, f"{file_name}.jpg")
        await ctx.send(file=photo)
