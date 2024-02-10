import urllib.request, os
from openai import OpenAI
from PIL import Image

client = OpenAI()


def img_creator(
    prompt,
    size=256,
):
    size = int(size)

    response = client.images.generate(
        model="dall-e-2",
        prompt=f"Make {size}x{size} pixel art, the prompt is a {prompt}.",
        size="256x256",
        quality="hd",
    )

    image_url = response.data[0].url
    urllib.request.urlretrieve(image_url, "image.png")

    image = Image.open("image.png")
    image = image.resize((size, size))

    algorithm = {}
    pixels = image.load()
    for i in range(size):
        for j in range(size):
            algorithm[f"{i}, {j}"] = pixels[i, j]

    image.save("image.png")
    os.remove("image.png")
    return algorithm
