import python_weather


async def getWeather(city_name, unit):
    weatherObject = []
    currentWeatherObject = {}

    client = python_weather.Client(format=unit)
    weather = await client.find(city_name)

    # Add Items To Current Weather Dictionary
    currentWeatherObject["temperature"] = str(weather.current.temperature)
    currentWeatherObject["location"] = str(weather.current.observation_point).split(",")[0]
    currentWeatherObject["date"] = str(weather.current.date).split(" ")[0]
    currentWeatherObject["day"] = str(weather.current.day)
    currentWeatherObject["sky_text"] = str(weather.current.sky_text)
    currentWeatherObject["feels_like"] = str(weather.current.feels_like)
    currentWeatherObject["wind_speed"] = str(weather.current.wind_speed)
    currentWeatherObject["humidity"] = str(weather.current.wind_speed)

    for forecast in range(len(weather.forecasts)):
        if forecast > 0:
            if forecast == 1:
                currentWeatherObject["temp_low"] = str(weather.forecasts[forecast].low)
                currentWeatherObject["temp_high"] = str(weather.forecasts[forecast].high)
                currentWeatherObject["precip"] = str(weather.forecasts[forecast].precip)
            weatherObject.append(
                [str(weather.forecasts[forecast].short_day), str(weather.forecasts[forecast].temperature),
                 str(weather.forecasts[forecast].high), str(weather.forecasts[forecast].low),
                 str(weather.forecasts[forecast].sky_text)])

    await client.close()
    return currentWeatherObject, weatherObject
