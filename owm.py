"""
TODO:

Graphics - Almost done, just need tweaking and images. Can probably pull from a database online!

Need error handling for when 'gusts' etc is not in the weather data 
    - Currently use None values but it should omit during image creation

temp_min does not seem to correspond to the night. Is this necessary? What other info should there be?
"""

import pyowm
from utils import kelvin_to_fahrenheit, degrees_to_direction, mps_to_mph
from image import create_grapic
from typing import List

owm_api_key = "b0a26aa4b33ca220920e6f016c2661d5"
owm = pyowm.OWM(api_key=owm_api_key)

def get_weather_data_for_locations(locations: List["str"]):
    data = []

    for location in locations:
        manager = owm.weather_manager()
        obs = manager.weather_at_place(location)
        weather = obs.weather

        temp_max: int = (
            kelvin_to_fahrenheit(weather.temp["temp_max"])
            if "temp_max" in weather.temp
            else None
        )
        temp_min: int = (
            kelvin_to_fahrenheit(weather.temp["temp_min"])
            if "temp_min" in weather.temp
            else None
        )
        temp_feels_like: int = (
            kelvin_to_fahrenheit(weather.temp["feels_like"])
            if "feels_like" in weather.temp
            else None
        )
        chance_of_rain: int = (
            int(weather.precipitation_probability * 100)
            if weather.precipitation_probability is not None
            else 0
        )

        wind_speed: int = (
            mps_to_mph(weather.wnd["speed"]) if "speed" in weather.wnd else None
        )
        wind_gust: int = (
            mps_to_mph(weather.wnd["gust"]) if "gust" in weather.wnd else None
        )
        wind_deg: float = (
            mps_to_mph(weather.wnd["deg"]) if "deg" in weather.wnd else None
        )
        wind_direction: str = degrees_to_direction(wind_deg)

        description: str = weather.status

        print(
            f"""
        {location}:
        Temp: max {temp_max}, min {temp_min}
        Chance of Rain/Snow: {chance_of_rain}
        Wind: {wind_speed} mph {wind_direction}, gusts of {wind_gust} mph
        {description}
        """
        )

        location_data = {
            "max": temp_max,
            "min": temp_min,
            "feels like": temp_feels_like,
            "chance of rain": chance_of_rain,
            "wind speed": wind_speed,
            "gust": wind_gust,
            "direction": wind_direction,
            "desc": description,
        }
        data.append(location_data)
    return data

if __name__ == '__main__' :
    locations = ["Prescott", "Chino Valley", "Dewey", "Prescott Valley"]
    data = get_weather_data_for_locations(locations)
    create_grapic(data)