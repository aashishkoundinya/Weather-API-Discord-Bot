import nextcord
from nextcord.ext import commands
from config import TOKEN, API_KEY
import aiohttp

bot = commands.Bot(command_prefix = "!", intents = nextcord.Intents.all())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    weather_status = "Cool bot, even hotter (or cooler) weather"

@bot.command()
async def weather(ctx: commands.Context, *, city):
    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": API_KEY,
        "q": city
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as responses:
            if responses.status == 200:
                data = await responses.json()
                print(data)
                
                location = data["location"]["name"]
                localtime = data["location"]["localtime"]
                temp_c = data["current"]["temp_c"]
                humidity = data["current"]["humidity"]
                wind_kph = data["current"]["wind_kph"]
                feelslike_c = data["current"]["feelslike_c"]
                condition = data["current"]["condition"]["text"]
                image_url = "http:" + data["current"]["condition"]["icon"]

                embed = nextcord.Embed(title=f"Weather for {location}", description=f"The condition in {location} is {condition}")
                embed.add_field(name="Temperature", value=f"{temp_c} °C\n")
                embed.add_field(name="Humidity", value=f"{humidity}\n")
                embed.add_field(name="Wind Speed", value=f"{wind_kph} KPH\n")
                embed.add_field(name="Feels Like", value=f"{feelslike_c} °C\n")
                embed.add_field(name=f"Time in {location}", value=f"{localtime}\n")
                embed.set_thumbnail(url=image_url)

                await ctx.send(embed=embed)

            else:
                await ctx.send(f"Error getting weather for {city}, Status code: {responses.status}")

bot.run(TOKEN)