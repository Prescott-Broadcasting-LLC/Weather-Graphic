def kelvin_to_fahrenheit(K: float) -> int:
    return int((K - 273.15) * 9 / 5) + 32

def degrees_to_direction(deg: float) -> str:
    if deg is None:
        return None
    directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    index = int(deg / 360 * 8 + .5) % 8
    return directions[index]

def mps_to_mph (speed: float) -> int:
    return int(2.24 * speed)