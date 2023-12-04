# Performance Measurement and Optimization

---

## Baseline measurement
This section presents the baseline measurement results obtained from benchmarking and profiling.

### Benchmarking
The execution times of the functions were measured using the **timeit** library.

| Function   | Repetitions | Execution Time (seconds)  |
|------------|-------------|---------------------------|
| insertion  | 1000        | 2.608868667000934         |
| extraction | 1000        | 1.2318516250015819        |

### Profiling
Profiling results for the functions were obtained using the **line_profiler** library.

1. **insertion** function stats
```log
Timer unit: 1e-09 s

Total time: 0.010802 s
File: nlsbs_steganography.py
Function: insertion at line 9

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     9                                           def insertion(image: Image, message: str, bits_to_use: int = 1) -> Image:
    10                                               """
    11                                               Least Significant Bit (LSB) insertion of a message into an image.
    12                                           
    13                                               Parameters:
    14                                               - image (Image): The input image to which message will be inserted.
    15                                               - message (str): The message to be inserted into the image.
    16                                               - bits_to_use (int, optional): The number of least significant bits
    17                                                   to use for insertion. Default is 1.
    18                                           
    19                                               Returns:
    20                                               - image (Image): The resulting image with the message inserted.
    21                                               """
    22         1          0.0      0.0      0.0      if not 1 <= bits_to_use <= 8:
    23                                                   raise InvalidBitsToUseError("Bits to use must be between 1 and 8.")
    24                                           
    25         1          0.0      0.0      0.0      binary_message = (
    26         1      93000.0  93000.0      0.9          "".join([format(byte, "08b") for byte in message.encode()]) + DELIMITER
    27                                               )
    28         1          0.0      0.0      0.0      binary_message_length = len(binary_message)
    29         1       1000.0   1000.0      0.0      min_required_pixels = math.ceil(binary_message_length / bits_to_use)
    30         1       1000.0   1000.0      0.0      total_image_pixels = image.width * image.height
    31         1          0.0      0.0      0.0      if min_required_pixels > total_image_pixels:
    32                                                   raise InsufficientPixelsError("Message size exceeds image pixels capacity.")
    33                                           
    34         1          0.0      0.0      0.0      index = 0
    35        18       1000.0     55.6      0.0      for y in range(image.height):
    36      1801     165000.0     91.6      1.5          for x in range(image.width):
    37      1784    1464000.0    820.6     13.6              pixel = list(image.getpixel(xy=(x, y)))
    38      5351     606000.0    113.2      5.6              for i in range(bits_to_use):
    39      3568     860000.0    241.0      8.0                  pixel_value = format(pixel[-1], "08b")
    40      3568     351000.0     98.4      3.2                  left_end = 8 - i - 1
    41      3568     301000.0     84.4      2.8                  right_start = 8 - i
    42      3568     226000.0     63.3      2.1                  update_value = (
    43     10704    1235000.0    115.4     11.4                      pixel_value[:left_end]
    44      3568     321000.0     90.0      3.0                      + binary_message[index]
    45      3568     404000.0    113.2      3.7                      + pixel_value[right_start:8]
    46                                                           )
    47      3568     575000.0    161.2      5.3                  pixel[-1] = int(update_value, 2)
    48      3568    3492000.0    978.7     32.3                  image.putpixel(xy=(x, y), value=tuple(pixel))
    49      3568     322000.0     90.2      3.0                  index += 1
    50      3568     384000.0    107.6      3.6                  if index >= binary_message_length:
    51         1          0.0      0.0      0.0                      return image
    52                                               return image
```

**extraction** function stats
```log
Timer unit: 1e-09 s

Total time: 0.004826 s
File: nlsbs_steganography.py
Function: extraction at line 55

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    55                                           def extraction(image: Image, bits_to_use: int = 1) -> str:
    56                                               """
    57                                               Least Significant Bit (LSB) extraction of a message from the image.
    58                                           
    59                                               Parameters:
    60                                               - image (Image): The image from which message will be extracted.
    61                                               - bits_to_use (int, optional): The number of least significant bits
    62                                                   used for insertion. Default is 1.
    63                                           
    64                                               Returns:
    65                                               - message (str): The extracted message from the image.
    66                                               """
    67         1          0.0      0.0      0.0      if not 1 <= bits_to_use <= 8:
    68                                                   raise InvalidBitsToUseError("Bits to use must be between 1 and 8.")
    69                                           
    70         1          0.0      0.0      0.0      message = ""
    71         1          0.0      0.0      0.0      index = 0
    72         1          0.0      0.0      0.0      character_buffer = ""
    73        18       2000.0    111.1      0.0      for y in range(image.height):
    74      1801     157000.0     87.2      3.3          for x in range(image.width):
    75      1784    1493000.0    836.9     30.9              pixel = list(image.getpixel(xy=(x, y)))
    76      5351     649000.0    121.3     13.4              for i in range(bits_to_use):
    77      3568     771000.0    216.1     16.0                  pixel_value = format(pixel[-1], "08b")
    78      3568     426000.0    119.4      8.8                  extracted_bit = pixel_value[8 - i - 1]
    79      3568     376000.0    105.4      7.8                  character_buffer += extracted_bit
    80      3568     311000.0     87.2      6.4                  index += 1
    81      3568     376000.0    105.4      7.8                  if index % 8 == 0:
    82       446      42000.0     94.2      0.9                      if character_buffer == DELIMITER:
    83         1          0.0      0.0      0.0                          return message
    84       445      30000.0     67.4      0.6                      try:
    85       445      61000.0    137.1      1.3                          character_code = int(character_buffer, 2)
    86       445      97000.0    218.0      2.0                          message += chr(character_code)
    87                                                               except ValueError:
    88                                                                   raise MessageExtractionError(
    89                                                                       f"Error extracting message at index {index}"
    90                                                                   ) from None
    91       445      35000.0     78.7      0.7                      character_buffer = ""
    92                                               raise MessageNotFoundError("Hidden message not found in the image.")
```
