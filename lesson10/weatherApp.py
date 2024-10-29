import aiohttp
import asyncio
import datetime


async def get_location_info(location):
    long_lat_finder_api = f'https://geocode.maps.co/search?q={location}'

    async with aiohttp.ClientSession() as session:
        async with session.get(long_lat_finder_api) as response:
            data = await response.json()
            # pretty print data json
            lat = data[0]["lat"]
            lon = data[0]["lon"]

            await get_wether(lat, lon, location)


async def get_wether(lat, lon, location):
    weather_finder_api = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m'
    async with aiohttp.ClientSession() as session:
        async with session.get(weather_finder_api) as response:
            data = await response.json()
            print(
                f'Weather at {location}: {data["current"]["temperature_2m"]}°C', f'Time at {location}: {data["current"]["time"]} UTC')


async def main():
    location = input("Enter a location: ")
    await get_location_info(location)
asyncio.run(main())
