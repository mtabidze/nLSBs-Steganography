# Copyright (c) 2023 Mikheil Tabidze
import timeit


def main():
    insertion_benchmarking()
    extraction_benchmarking()


def insertion_benchmarking():
    setup = """
from PIL import Image

from src.nlsbs_steganography.nlsbs_steganography import insertion

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
    """
    statement = "insertion(image=test_image, message=test_message, bits_to_use=2)"
    number = 1000
    execution_time = timeit.timeit(stmt=statement, setup=setup, number=number)

    print(f"Execution time the 'insertion' function in seconds: {execution_time}")


def extraction_benchmarking():
    setup = """
from PIL import Image

from src.nlsbs_steganography.nlsbs_steganography import extraction, insertion

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
    """
    statement = "extraction(image=image_with_message, bits_to_use=2)"
    number = 1000
    execution_time = timeit.timeit(stmt=statement, setup=setup, number=number)

    print(f"Execution time the insertion 'extraction' in seconds: {execution_time}")


if __name__ == "__main__":
    main()
