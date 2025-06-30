import discord
from dotenv import load_dotenv
import os
from bubble import edit_image
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))
bot = discord.Bot()

@bot.command(description="Sends the bot's latency", guild_ids=[GUILD_ID])
async def ping(ctx):
    await ctx.respond(f"Pong! the ping is {bot.latency}")
@bot.command(description="Add a speech bubble to an image", guild_ids=[GUILD_ID])
async def process_image(
    ctx,
    image: discord.Option(discord.Attachment, description="Upload the image you want to add a speech bubble to"),
    option: discord.Option(str, description="Choose an option", choices=["left", "right"])
):
    await ctx.defer()

    # Download the image bytes
    img_bytes = await image.read()

    # Call your external function to get edited image bytes
    edited_bytes = edit_image(img_bytes, option)

    # Send back the edited image as a Discord file
    edited_file = discord.File(fp=edited_bytes, filename=f"edited_{image.filename}")

    await ctx.respond("Here is your edited image:", file=edited_file)

bot.run(DISCORD_TOKEN)