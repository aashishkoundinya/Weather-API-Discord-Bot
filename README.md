# Weather API Discord Bot

This Discord bot acts as your personal weather concierge. Simply use the `!weather [city name]`
command, and it retrieves real-time temperature, humidity, wind speed, feels like, and current time for any location. It uses the [nextcord](https://docs.nextcord.dev/) API wrapper for Discord. Presented in a visually appealing embed with a weather icon, it empowers you and your server members to stay informed about conditions across the globe.

## Features

* Easy to use with the `!weather [city name]` command.
* Provides detailed weather information, including:
    * Temperature (°C)
    * Humidity (%)
    * Wind Speed (KPH)
    * Feels Like (°C)
    * Current time in the location
    * Weather condition description
    * Image icon representing the weather condition
* Uses a visually appealing Discord embed to present the weather data.

## Installation

**Prerequisites:**

* A Discord server
* A Bot created in Discord Developer Portal (https://discord.com/developers/applications)
* A WeatherAPI account and API key (https://www.weatherapi.com)

##Inviting the Bot##

* Go to the Discord Developer Portal and create a new application.
* In the "Bot" section, create a bot user and copy the bot token.
* Visit the "OAuth2" section and click "Add a Scopes". Under "Bot Permissions", grant the following permissions:
    * Send Messages
    * Embed Links
* Click "Copy" next to the "bot token" field. This is the token you'll use in the config.py file.
* Navigate to the "Authorization" URL and invite the bot to your Discord server.

## Run

* `config.py` - Place the `Discord Bot TOKEN` and the `Weather API_KEY` in the mentioned location.
* Make sure the bot is present in the desired server.
* `weather.py` - Simply run the file. The bot should come online.

**NOTE** - Enable `PRESENSE INTENT` `SERVER MEMBERS INTENT` `MESSAGE CONTENT INTENT` under the **BOT** section in [Discord Developer Portal](https://discord.com/developers/applications).

**Clone the repository:**

   ```bash
   git clone [https://github.com/](https://github.com/)<your-username>/weather-api-discord-bot.git
