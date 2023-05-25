import random

import settings
import discord
from discord.ext import commands


class Tod(discord.ui.View):
    def __init__(self) -> object:
        super().__init__(timeout=None)

        @discord.ui.button(label="Verita'", custom_id="truth1", style=discord.ButtonStyle.green)
        async def button1(self, interaction, button):
            role = "1094286827499815003"
            user = interaction.user
            if role in [y.id for y in user.roles]:
                await interaction.response.send_message("You already verified your account", ephemeral=True)
            else:
                await user.add_roles(user.guild.get_role(role))
                await interaction.response.send_message("Account verified", ephemeral=True)


def run():
    intents = discord.Intents.default()

    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print(f"{bot.user} is currently online")

    @bot.command(
        aliases=['p'],
        help="this is help",
        description="This is description",
        brief="Brief"
    )
    async def ping(ctx):
        """Answers with pong"""
        await ctx.send("pong")

    @bot.command()
    async def say(ctx, what="WHAT?!", why="why?", emoji="🥰"):
        await ctx.send(what)
        await ctx.send(why)
        await ctx.send(emoji)

    @bot.command()
    async def tod(ctx, truth, dare, Tod):
        await ctx.send(Tod())

    @bot.command()
    async def say2(ctx, *what):
        await ctx.send(" ".join(what))

    @bot.command()
    async def choises(ctx, *options):
        await ctx.send(random.choice(options))

    @bot.command()
    async def add(ctx, one: int, two: int):
        await ctx.send(one + two)

    @bot.command()
    async def about(ctx, who: discord.Member):
        await ctx.send(f"Ecco le info su {who.mention} ")
        await ctx.send(f"** {who.name} ** joined at {who.joined_at}")
        await ctx.send(f"{who.avatar}")

    bot.run(settings.DISCORD_API_SECRET)


if __name__ == "__main__":
    run()
