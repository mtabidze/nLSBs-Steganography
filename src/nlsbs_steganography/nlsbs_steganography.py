# Copyright (c) 2023 Mikheil Tabidze
import math

import numpy as np
from PIL import Image

DELIMITER = "00000000"


def insertion(image: Image, message: str, bits_to_use: int = 1) -> Image:
    """
    Least Significant Bit (LSB) insertion of a message into an image.

    Parameters:
    - image (Image): The input image to which message will be inserted.
    - message (str): The message to be inserted into the image.
    - bits_to_use (int, optional): The number of least significant bits
        to use for insertion. Default is 1.

    Returns:
    - image (Image): The resulting image with the message inserted.
    """
    if not 1 <= bits_to_use <= 8:
        raise InvalidBitsToUseError("Bits to use must be between 1 and 8.")

    binary_message = (
        "".join([format(byte, "08b") for byte in message.encode()]) + DELIMITER
    )
    binary_message_length = len(binary_message)
    min_required_pixels = math.ceil(binary_message_length / bits_to_use)
    total_image_pixels = image.width * image.height
    if min_required_pixels > total_image_pixels:
        raise InsufficientPixelsError("Message size exceeds image pixels capacity.")

    image_array = np.array(image, dtype=np.uint8)
    image_mode = image.mode

    index = 0
    for y in range(image.height):
        for x in range(image.width):
            pixel = image_array[y, x].tolist()
            color_value = pixel[-1]
            for bit_index in range(bits_to_use):
                new_bit_value = int(binary_message[index], 2)
                extracted_bit = (color_value >> bit_index) & 1
                if new_bit_value != extracted_bit:
                    clear_bit_color = color_value & ~(1 << bit_index)
                    color_value = clear_bit_color | (new_bit_value << bit_index)
                    pixel[-1] = color_value
                    image_array[y, x] = pixel
                index += 1
                if index >= binary_message_length:
                    new_image = Image.fromarray(obj=image_array, mode=image_mode)
                    return new_image
    raise MessageInsertionError(f"Error insertion message at index {index}")


def extraction(image: Image, bits_to_use: int = 1) -> str:
    """
    Least Significant Bit (LSB) extraction of a message from the image.

    Parameters:
    - image (Image): The image from which message will be extracted.
    - bits_to_use (int, optional): The number of least significant bits
        used for insertion. Default is 1.

    Returns:
    - message (str): The extracted message from the image.
    """
    if not 1 <= bits_to_use <= 8:
        raise InvalidBitsToUseError("Bits to use must be between 1 and 8.")

    image_array = np.asarray(a=image, dtype=int)

    message_characters = []
    index = 0
    character_buffer = []
    for y in range(image.height):
        for x in range(image.width):
            color_value = image_array[y, x, -1]
            for bit_index in range(bits_to_use):
                extracted_bit = (color_value >> bit_index) & 1
                character_buffer.append(str(extracted_bit))
                index += 1
                if index % 8 == 0:
                    if "1" not in character_buffer:
                        message = "".join(message_characters)
                        return message
                    try:
                        character_code = int("".join(character_buffer), 2)
                        message_characters.append(chr(character_code))
                    except ValueError:
                        raise MessageExtractionError(
                            f"Error extracting message at index {index}"
                        ) from None
                    character_buffer.clear()
    raise MessageNotFoundError("Hidden message not found in the image.")


class InvalidBitsToUseError(Exception):
    """Raised when the specified number of bits to use is invalid."""

    pass


class MessageInsertionError(Exception):
    """Raised when the message insertion fails."""

    pass


class InsufficientPixelsError(Exception):
    """Raised when the message size exceeds image pixels capacity."""

    pass


class MessageExtractionError(Exception):
    """Raised when the message extraction fails."""

    pass


class MessageNotFoundError(Exception):
    """Raised when the hidden message is not found in the image."""

    pass
