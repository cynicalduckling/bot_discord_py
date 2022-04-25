from discord.ext import commands


def main():
    bot = commands.Bot(command_prefix = ".") 

    @bot.event
    async def on_ready():
        print("Connected to Discord")

    bot.run("OTY4MDc1MjM0MjExMTU1OTk5.YmZkUQ.yj0vgERZCDfMoqfEnFo-AMVqxDE")

if __name__ == '__main__':
    main()