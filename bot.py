import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh: int = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def atik(ctx):
    message = ("Geri dönüşüm, doğaya atık bırakmayı önlemenin en iyi yollarından biridir. "
               "Plastik, kağıt, cam ve metal gibi malzemeleri geri dönüşüm kutularına atarak "
               "doğal kaynakları korumaya yardımcı olabilirsiniz. "
               "Atıkları azaltmak ve doğaya katkı sağlamak için geri dönüşüm kutularını kullanın!")
    await ctx.send(message)

@bot.command()
async def su(ctx):
    message = ("Su hayati bir kaynaktır ve onu boşa harcamamak gerekir. "
               "Daha kısa duşlar alın, dişlerinizi fırçalarken musluğu kapatın ve gereksiz yere su kullanmayın. "
               "Bahçenizi sularken sabah erken veya akşam geç saatlerde sulayın. Bu şekilde su israfını önlersiniz!")
    await ctx.send(message)

@bot.command()
async def enerji(ctx):
    message = ("Enerji tasarrufu yapmak hem çevreyi korur hem de faturalarınızı azaltır. "
               "Gereksiz ışıkları kapatın, enerji verimli ampuller kullanın ve elektronik cihazları kullanmadığınızda kapatın. "
               "Daha az enerji tüketerek karbon ayak izinizi azaltabilirsiniz.")
    await ctx.send(message)

@bot.command()
async def agacekme(ctx):
    message = ("Ağaç dikmek, atmosferdeki karbondioksiti azaltmanın ve doğayı korumanın en etkili yollarından biridir. "
               "Yerel organizasyonlara katılarak ağaç dikme etkinliklerine katılabilirsiniz. "
               "Ağaçlar, temiz hava sağlamaya yardımcı olur ve erozyonu önler.")
    await ctx.send(message)
@bot.command()
async def kompost(ctx):
    message = ("Kompost yapma, organik atıkları değerlendirmenin mükemmel bir yoludur. "
               "Yemek atıkları, sebze kabukları ve bahçe atıkları gibi biyolojik olarak ayrışabilir maddeleri kompostlayarak "
               "toprağınıza doğal gübre sağlayabilirsiniz. Bu hem atıkları azaltır hem de toprağı besler!")
    await ctx.send(message)

@bot.command()
async def plastik(ctx):
    message = ("Plastik kullanımını azaltarak doğaya olan zararları en aza indirebilirsiniz. "
               "Tek kullanımlık plastik ürünler yerine yeniden kullanılabilir çantalar, şişeler ve kaplar tercih edin. "
               "Bu, plastik kirliliğini azaltmanın ve çevreyi korumanın etkili bir yoludur!")
    await ctx.send(message)
@bot.command()
async def ulasim(ctx):
    message = ("Daha az araba kullanarak karbon ayak izinizi küçültebilirsiniz. "
               "Kısa mesafelerde yürümek, bisiklet kullanmak veya toplu taşıma araçlarını tercih etmek, "
               "hem çevreyi korur hem de sağlığınızı iyileştirir!")
    await ctx.send(message)
@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command()
async def roll(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    await ctx.send(random.choice(choices))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def test(ctx):
    await ctx.send("Bot çalışıyor!")
