# Copyright (c) 2023 Mikheil Tabidze
from random import randint

from PIL import Image

from src.nlsbs_steganography.nlsbs_steganography import insertion


def main():
    test_message = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do "
        "eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut "
        "enim ad minim veniam, quis nostrud exercitation ullamco laboris "
        "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in"
        " reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla"
        " pariatur. Excepteur sint occaecat cupidatat non proident, sunt in "
        "culpa qui officia deserunt mollit anim id est laborum."
    )
    image = Image.new(mode="RGB", size=(25, 25), color=(0, 0, 0))
    for y in range(image.height):
        for x in range(image.width):
            pixel = list(image.getpixel(xy=(x, y)))
            pixel[0] = randint(a=0, b=255)
            pixel[1] = randint(a=0, b=255)
            pixel[2] = randint(a=0, b=255)
            image.putpixel(xy=(x, y), value=tuple(pixel))
    image.save("input_image.png")
    image_with_message = insertion(image=image, message=test_message, bits_to_use=8)
    image_with_message.save("resulting_image.png")


if __name__ == "__main__":
    main()
