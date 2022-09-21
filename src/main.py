from discord.ext import commands
from discord.utils import get
import discord
from random import randrange


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id =  430441557615706133 # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')


@bot.command()
async def name(message):
    await message.channel.send(message.author)

@bot.command()
async def d6(message):
    random_number = randrange(1,7)
    await message.channel.send('🎲Alea jacta est 🎲: ' + str(random_number))

@bot.event
async def on_message(message):
    if message.content == 'Salut tout le monde':
        await message.channel.send('Salut tout seul' + message.author.mention)
    else:
        await bot.process_commands(message)

@bot.command()
async def admin(ctx,nickname : discord.Member):
    admin_role = get(ctx.guild.roles,name="Admin")
    if not admin_role:
        permissions = discord.Permissions()
        permissions.update(kick_members = True, ban_members=True,manage_channels=True)
        admin_role = await ctx.guild.create_role(permissions=permissions,name="Admin")
    await nickname.add_roles(admin_role)

@bot.command()
async def ban(ctx,nickname : discord.Member):
    return await ctx.guild.ban(nickname)

@bot.command()
async def xkcd(ctx):
    random_number = randrange(1,2675)
    return await ctx.send('https://xkcd.com/' + str(random_number))

@bot.command()
async def count(ctx):
    offline = 0
    online = 0
    idle = 0
    not_disturb = 0
    for member in ctx.guild.members :
        if member.status == discord.Status.offline:
            offline += 1
        elif member.status == discord.Status.online:
            online += 1
        elif member.status == discord.Status.idle:
            idle += 1
        elif member.status == discord.Status.dnd:
            not_disturb += 1
    return await ctx.send ('Online : ' + str(online) + ' \nOffline :' + str (offline) + ' \nIdle :' + str(idle) + '\nDo not disturb :' + str(not_disturb))


token = ""
bot.run(token)  # Starts the bot