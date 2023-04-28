from PIL import Image, ImageDraw, ImageFont
from typing import Dict, Any

# Create a new image with the dimensions you want


def create_grapic(data: Dict[str, Dict[str, Any]], width: int = 800, height: int = 800):
    image = Image.new("RGB", (width, height), "white")

    # Define the font and font size you want to use for the text
    # font = ImageFont.truetype("arial.ttf", 20)
    # linux no likey
    font = ImageFont.load_default()

    # Define the regions where you want to display the weather information
    offset = 50
    num_regions = len(data)
    regions = [
        (
            int(offset + _ * (width / num_regions)),
            offset,
            int((_ + 1) * (width / num_regions)),
            550,
        )
        for _ in range(num_regions)
    ]

    # Draw the weather information as text in each region
    draw = ImageDraw.Draw(image)

    for _ in range(num_regions):
        region = regions[_]
        region_info = data[_]

        draw.text(
            (region[0] + 5, region[1] + 5), f"Region {_ + 1}", font=font, fill="black"
        )
        for i, (key, value) in enumerate(region_info.items()):
            draw.text(
                (region[0] + 5, region[1] + 30 + i * 25),
                f"{key}: {value}",
                font=font,
                fill="black",
            )

    # Save the image
    image.save("weather.png")


if __name__ == "__main__":
    data = [
        {
            "Min Temp": 10,
            "Max Temp": 20,
            "Wind Speed": 5,
            "Wind Gust": 10,
            "Wind Direction": "N",
        },
        {
            "Min Temp": 15,
            "Max Temp": 25,
            "Wind Speed": 7,
            "Wind Gust": 12,
            "Wind Direction": "NE",
        },
        {
            "Min Temp": 12,
            "Max Temp": 22,
            "Wind Speed": 6,
            "Wind Gust": 11,
            "Wind Direction": "E",
        },
        {
            "Min Temp": 18,
            "Max Temp": 28,
            "Wind Speed": 8,
            "Wind Gust": 14,
            "Wind Direction": "SE",
        },
    ]

    create_grapic(data)
