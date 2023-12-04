# Copyright (c) 2023 Mikheil Tabidze
from line_profiler import LineProfiler
from PIL import Image

from src.nlsbs_steganography.nlsbs_steganography import extraction, insertion


def main():
    insertion_profiling()
    extraction_profiling()


def insertion_profiling():
    test_image = Image.new(mode="RGB", size=(100, 100), color=(255, 255, 255))
    test_message = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do "
        "eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut "
        "enim ad minim veniam, quis nostrud exercitation ullamco laboris "
        "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor "
        "in reprehenderit in voluptate velit esse cillum dolore eu fugiat"
        " nulla pariatur. Excepteur sint occaecat cupidatat non proident,"
        " sunt in culpa qui officia deserunt mollit anim id est laborum."
    )
    profiler = LineProfiler()
    insertion_wrapper = profiler(insertion)
    insertion_wrapper(image=test_image, message=test_message, bits_to_use=2)
    profiler.print_stats()


def extraction_profiling():
    test_image = Image.new(mode="RGB", size=(100, 100), color=(255, 255, 255))
    test_message = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do "
        "eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut "
        "enim ad minim veniam, quis nostrud exercitation ullamco laboris "
        "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor "
        "in reprehenderit in voluptate velit esse cillum dolore eu fugiat"
        " nulla pariatur. Excepteur sint occaecat cupidatat non proident,"
        " sunt in culpa qui officia deserunt mollit anim id est laborum."
    )
    image_with_message = insertion(
        image=test_image, message=test_message, bits_to_use=2
    )
    profiler = LineProfiler()
    insertion_wrapper = profiler(extraction)
    insertion_wrapper(image=image_with_message, bits_to_use=2)
    profiler.print_stats()


if __name__ == "__main__":
    main()
