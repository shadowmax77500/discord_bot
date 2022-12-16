import discord
from discord.ext import commands

bot = commands.Bot(command_prefix= "!",description="le bon vieux 49.3",intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Ready !")

@bot.command()
async def server_info(ctx):
    await ctx.channel.purge(limit = 1)
    server = ctx.guild
    number_of_text_channels = len(server.text_channels)
    number_of_voice_channels = len(server.voice_channels)
    server_description = server.description
    number_of_person = server.member_count
    server_name = server.name
    message = f"Le serveur **{server_name}** à {number_of_person} membre.\nLa descrition du serveur est : {server_description}\nCe Serveur posede {number_of_text_channels} de salon textuelle et {number_of_voice_channels} de salon vocaux"
    await ctx.send(message)

@bot.command()
async def say(ctx, *text):
    await ctx.channel.purge(limit = 1)
    await ctx.send(" ".join(text))

@bot.command()
async def clear(ctx, nbr : int):
  await ctx.channel.purge(limit = nbr + 1)#deletes all messages

@bot.command()
async def kick(ctx, user : discord.User, *reason):
    await ctx.channel.purge(limit = 1)
    reason = " ".join(reason)
    await ctx.guild.kick(user, reason = reason)
    await ctx.send(f"{user} a été kick pour la raison : {reason}")

@bot.command()
async def ban(ctx, user : discord.User, *reason):
    await ctx.channel.purge(limit = 1)
    reason = " ".join(reason)
    await ctx.guild.ban(user, reason = reason)
    await ctx.send(f"{user} a été ban pour la raison : {reason}")

@bot.command()
async def unban(ctx, user, *reason):
    await ctx.channel.purge(limit = 1)
    reason = " ".join(reason)
    user_name, user_id = user.split("#")
    banned_user = ctx.guild.bans()
    async for i in banned_user:
        if i.user.name == user_name and i.user.discriminator == user_id:
            await ctx.guild.unban(i.user, reason = reason)
            await ctx.send(f"{user} a été déban du serveur.")
            return
    await ctx.send(f"{user} n'est pas dans la liste des bans")

@bot.command()
async def ban_user(ctx):
    await ctx.channel.purge(limit = 1)
    ban_list = []
    banned_user = ctx.guild.bans()
    async for i in banned_user:
        await ctx.send(f"{i.user.name}#{i.user.discriminator}")




bot.run("MTA1Mjg2NTI3MTQwMjA3NDEzMg.GH5wZ0.FfWXpbDZOl6295s_w5NwQuYmY__QkVFKn5ARas")