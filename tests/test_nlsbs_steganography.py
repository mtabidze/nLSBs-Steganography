# Copyright (c) 2023 Mikheil Tabidze
import numpy as np
import pytest
from PIL import Image

from src.nlsbs_steganography.nlsbs_steganography import (
    InsufficientPixelsError,
    InvalidBitsToUseError,
    MessageNotFoundError,
    extraction,
    insertion,
)


def test_insertion():
    test_message = "!"  # 0b00100001
    test_image = Image.new(mode="RGB", size=(2, 3), color=(255, 255, 255))
    expected_image_array = np.array(
        object=[
            [[255, 255, int("11111100", 2)], [255, 255, int("11111000", 2)]],
            [[255, 255, int("11111010", 2)], [255, 255, int("11111000", 2)]],
            [[255, 255, int("11111000", 2)], [255, 255, int("11111110", 2)]],
        ],
        dtype=np.uint8,
    )

    image_with_message = insertion(
        image=test_image, message=test_message, bits_to_use=3
    )
    image_array = np.asarray(a=image_with_message, dtype=np.uint8)
    assert np.array_equal(
        a1=image_array, a2=expected_image_array
    ), f"Expected: {expected_image_array}, Got: {image_array}"


def test_insertion_and_extraction_empty(sample_rgb_image):
    test_message = ""
    image_with_message = insertion(
        image=sample_rgb_image, message=test_message, bits_to_use=1
    )
    extracted_message = extraction(image=image_with_message, bits_to_use=1)

    assert (
        extracted_message == test_message
    ), f"Expected: {test_message}, Got: {extracted_message}"


def test_insertion_max_length():
    test_message = "!"  # 0b00100001
    test_image = Image.new(mode="RGB", size=(2, 2), color=(255, 255, 255))

    image_with_message = insertion(
        image=test_image, message=test_message, bits_to_use=4
    )
    extracted_message = extraction(image=image_with_message, bits_to_use=4)

    assert (
        extracted_message == test_message
    ), f"Expected: {test_message}, Got: {extracted_message}"


def test_insertion_and_extraction_rgb(sample_rgb_image):
    test_message = "Hello, n-Least Significant Bit(s) Steganography!"
    image_with_message = insertion(
        image=sample_rgb_image, message=test_message, bits_to_use=1
    )
    extracted_message = extraction(image=image_with_message, bits_to_use=1)

    assert (
        extracted_message == test_message
    ), f"Expected: {test_message}, Got: {extracted_message}"


def test_insertion_and_extraction_rgba(sample_rgba_image):
    test_message = "Hello, n-Least Significant Bit(s) Steganography!"
    image_with_message = insertion(
        image=sample_rgba_image, message=test_message, bits_to_use=1
    )
    extracted_message = extraction(image=image_with_message, bits_to_use=1)

    assert (
        extracted_message == test_message
    ), f"Expected: {test_message}, Got: {extracted_message}"


def test_insertion_invalid_bits_to_use(sample_rgb_image):
    with pytest.raises(InvalidBitsToUseError):
        insertion(image=sample_rgb_image, message="Test", bits_to_use=0)

    with pytest.raises(InvalidBitsToUseError):
        insertion(image=sample_rgb_image, message="Test", bits_to_use=9)


def test_insertion_insufficient_pixels(sample_rgb_image):
    test_message = "A" * 10000
    with pytest.raises(InsufficientPixelsError):
        insertion(image=sample_rgb_image, message=test_message, bits_to_use=1)


def test_extraction():
    expected_message = "!"  # 0b00100001
    test_image_array = np.array(
        object=[
            [[255, 255, int("11111100", 2)], [255, 255, int("11111000", 2)]],
            [[255, 255, int("11111010", 2)], [255, 255, int("11111000", 2)]],
            [[255, 255, int("11111000", 2)], [255, 255, int("11111110", 2)]],
        ],
        dtype=np.uint8,
    )
    image_with_message = Image.fromarray(obj=test_image_array, mode="RGB")

    extracted_message = extraction(image=image_with_message, bits_to_use=3)

    assert (
        extracted_message == expected_message
    ), f"Expected: {expected_message}, Got: {extracted_message}"


def test_extraction_invalid_bits_to_use(sample_rgb_image):
    with pytest.raises(InvalidBitsToUseError):
        extraction(image=sample_rgb_image, bits_to_use=0)

    with pytest.raises(InvalidBitsToUseError):
        extraction(image=sample_rgb_image, bits_to_use=9)


def test_extraction_message_not_found(sample_rgb_image):
    with pytest.raises(MessageNotFoundError):
        extraction(image=sample_rgb_image, bits_to_use=8)
