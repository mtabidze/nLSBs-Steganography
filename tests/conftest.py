# Copyright (c) 2023 Mikheil Tabidze
import pytest
from PIL import Image


@pytest.fixture(scope="function")
def sample_rgb_image():
    white_rgb_image = Image.new(mode="RGB", size=(100, 100), color=(255, 255, 255))
    return white_rgb_image


@pytest.fixture(scope="function")
def sample_rgba_image():
    white_rgba_image = Image.new(
        mode="RGB", size=(100, 100), color=(255, 255, 255, 255)
    )
    return white_rgba_image
