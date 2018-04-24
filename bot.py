 #print login information

import discord
from discord.ext import commands
from discord.ext.commands import bot

bot = commands.Bot(command_prefix='$sudo ', description='speedy boi')

@bot.event
async def on_ready():
	print('Logged in as ')
	print(bot.user.name)
	print(bot.user.id)
	print('------')


#add functions

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def interject(ctx):
    await ctx.send('''I'd just like to interject for a moment. What you're referring to as Linux, is in 
    fact, GNU/Linux, or as I've recently taken to calling it, GNU plus Linux. Linux is not an operating
    system unto itself, but rather another free component of a fully functioning GNU system made useful
    by the GNU corelibs, shell utilites, and vital system-components comprising a full OS as defined by
    POSIX.''')

@bot.command()
async def gentoo(ctx):
    await ctx.send("https://thumbs.gfycat.com/BlaringEachBats-size_restricted.gif")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def userinfo(ctx, user: discord.Member):
    await ctx.send("The user's name is: {}".format(user.name))
    await ctx.send("The user's ID is: {}".format(user.id))
    await ctx.send("The user's status is: {}".format(user.status))
    await ctx.send("The user's highest role is: {}".format(user.top_role))
    await ctx.send("The user joined at: {}".format(user.joined_at))

def is_in_guild(guild_id):
    async def predicate(ctx):
        return ctx.guild.id == guild_id
    return commands.check(is_in_guild)

def accesstoguild.error
async def access(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('access denied')

@bot.command()
if is_in_guild(438466152318894080)
async def guild(ctx):
    await ctx.send('stuff')
else accesstoguild.error

#run bot with the functions
bot.run('NDM4NDQ5NDAzMjYzNzEzMjgw.DcEyIg.jIUy8gyHURsM6y7GIMdNIeewm08')
