# Copyright (c) 2023 Mikheil Tabidze
import pytest

from src.nlsbs_steganography.nlsbs_steganography import (
    InsufficientPixelsError,
    InvalidBitsToUseError,
    MessageNotFoundError,
    extraction,
    insertion,
)


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


def test_extraction_invalid_bits_to_use(sample_rgb_image):
    with pytest.raises(InvalidBitsToUseError):
        extraction(image=sample_rgb_image, bits_to_use=0)

    with pytest.raises(InvalidBitsToUseError):
        extraction(image=sample_rgb_image, bits_to_use=9)


def test_extraction_message_not_found(sample_rgb_image):
    with pytest.raises(MessageNotFoundError):
        extraction(image=sample_rgb_image, bits_to_use=8)
