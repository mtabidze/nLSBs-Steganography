# Performance Measurement and Optimization

---

## Baseline measurement
This section presents the baseline measurement results obtained from benchmarking and profiling.

### Benchmarking
Benchmarking results for the functions were measured using the **timeit** library.

| Function   | Repetitions | Baseline Time (seconds) |
|------------|-------------|-------------------------|
| insertion  | 1000        | 2.61                    |
| extraction | 1000        | 1.23                    |

### Profiling
Profiling results for the functions were obtained using the **line_profiler** library.

<details>
    <summary><b>insertion</b> function stats</summary>

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
</details>

<details>
    <summary><b>extraction</b> function stats</summary>

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
</details>


## Optimization #1
This section presents the optimization results achieved by replacing string manipulations with bitwise operations.

### Benchmarking
Benchmarking results for the optimized functions are provided in this section.

| Function   | Repetitions | Baseline Time (seconds) | Execution Time (seconds) | Optimization Gain (%) |
|------------|-------------|-------------------------|--------------------------|-----------------------|
| insertion  | 1000        | 2.61                    | 1.99                     | 23.75                 |
| extraction | 1000        | 1.23                    | 0.96                     | 21.95                 |

### Profiling
Profiling results for the optimized functions are provided in this section.

<details>
    <summary><b>insertion</b> function stats</summary>

  ```log
Timer unit: 1e-09 s

Total time: 0.008801 s
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
    22         1       1000.0   1000.0      0.0      if not 1 <= bits_to_use <= 8:
    23                                                   raise InvalidBitsToUseError("Bits to use must be between 1 and 8.")
    24                                           
    25         1          0.0      0.0      0.0      binary_message = (
    26         1      96000.0  96000.0      1.0          "".join([format(byte, "08b") for byte in message.encode()]) + DELIMITER
    27                                               )
    28         1          0.0      0.0      0.0      binary_message_length = len(binary_message)
    29         1       2000.0   2000.0      0.0      min_required_pixels = math.ceil(binary_message_length / bits_to_use)
    30         1       3000.0   3000.0      0.0      total_image_pixels = image.width * image.height
    31         1          0.0      0.0      0.0      if min_required_pixels > total_image_pixels:
    32                                                   raise InsufficientPixelsError("Message size exceeds image pixels capacity.")
    33                                           
    34         1          0.0      0.0      0.0      index = 0
    35        18       3000.0    166.7      0.0      for y in range(image.height):
    36      1801     138000.0     76.6      1.5          for x in range(image.width):
    37      1784    1619000.0    907.5     17.6              pixel = list(image.getpixel(xy=(x, y)))
    38      5351     611000.0    114.2      6.7              for bit_index in range(bits_to_use):
    39      3568     566000.0    158.6      6.2                  new_bit_value = int(binary_message[index], 2)
    40      3568     412000.0    115.5      4.5                  color_value = pixel[-1]
    41      3568     415000.0    116.3      4.5                  clear_bit_color = color_value & ~(1 << bit_index)
    42      3568     432000.0    121.1      4.7                  new_color_value = clear_bit_color | (new_bit_value << bit_index)
    43      3568     344000.0     96.4      3.7                  pixel[-1] = new_color_value
    44      3568    3688000.0   1033.6     40.2                  image.putpixel(xy=(x, y), value=tuple(pixel))
    45      3568     404000.0    113.2      4.4                  index += 1
    46      3568     444000.0    124.4      4.8                  if index >= binary_message_length:
    47         1          0.0      0.0      0.0                      return image
    48                                               return image
  ```
</details>

<details>
    <summary><b>extraction</b> function stats</summary>

  ```log
Timer unit: 1e-09 s

Total time: 0.004595 s
File: nlsbs_steganography.py
Function: extraction at line 51

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    51                                           def extraction(image: Image, bits_to_use: int = 1) -> str:
    52                                               """
    53                                               Least Significant Bit (LSB) extraction of a message from the image.
    54                                           
    55                                               Parameters:
    56                                               - image (Image): The image from which message will be extracted.
    57                                               - bits_to_use (int, optional): The number of least significant bits
    58                                                   used for insertion. Default is 1.
    59                                           
    60                                               Returns:
    61                                               - message (str): The extracted message from the image.
    62                                               """
    63         1          0.0      0.0      0.0      if not 1 <= bits_to_use <= 8:
    64                                                   raise InvalidBitsToUseError("Bits to use must be between 1 and 8.")
    65                                           
    66         1          0.0      0.0      0.0      message = ""
    67         1          0.0      0.0      0.0      index = 0
    68         1          0.0      0.0      0.0      character_buffer = ""
    69        18       3000.0    166.7      0.1      for y in range(image.height):
    70      1801     153000.0     85.0      3.3          for x in range(image.width):
    71      1784    1506000.0    844.2     32.8              pixel = list(image.getpixel(xy=(x, y)))
    72      5351     619000.0    115.7     13.5              for bit_index in range(bits_to_use):
    73      3568     299000.0     83.8      6.5                  color_value = pixel[-1]
    74      3568     431000.0    120.8      9.4                  extracted_bit = (color_value >> bit_index) & 1
    75      3568     634000.0    177.7     13.8                  character_buffer += str(extracted_bit)
    76      3568     355000.0     99.5      7.7                  index += 1
    77      3568     351000.0     98.4      7.6                  if index % 8 == 0:
    78       446      43000.0     96.4      0.9                      if character_buffer == DELIMITER:
    79         1          0.0      0.0      0.0                          return message
    80       445      31000.0     69.7      0.7                      try:
    81       445      68000.0    152.8      1.5                          character_code = int(character_buffer, 2)
    82       445      74000.0    166.3      1.6                          message += chr(character_code)
    83                                                               except ValueError:
    84                                                                   raise MessageExtractionError(
    85                                                                       f"Error extracting message at index {index}"
    86                                                                   ) from None
    87       445      28000.0     62.9      0.6                      character_buffer = ""
    88                                               raise MessageNotFoundError("Hidden message not found in the image.")
  ```
</details>

## Optimization #2
This section presents the optimization results achieved by using the **NumPy** library.

### Benchmarking
Benchmarking results for the optimized functions are provided in this section.

| Function   | Repetitions | Baseline Time (seconds) | Execution Time (seconds) | Optimization Gain (%) |
|------------|-------------|-------------------------|--------------------------|-----------------------|
| insertion  | 1000        | 2.61                    | 1.68                     | 35.63                 |
| extraction | 1000        | 1.23                    | 0.79                     | 35.77                 |

### Profiling
Profiling results for the optimized functions are provided in this section.

<details>
    <summary><b>insertion</b> function stats</summary>

  ```log
Timer unit: 1e-09 s

Total time: 0.017477 s
File: nlsbs_steganography.py
Function: insertion at line 10

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    10                                           def insertion(image: Image, message: str, bits_to_use: int = 1) -> Image:
    11                                               """
    12                                               Least Significant Bit (LSB) insertion of a message into an image.
    13                                           
    14                                               Parameters:
    15                                               - image (Image): The input image to which message will be inserted.
    16                                               - message (str): The message to be inserted into the image.
    17                                               - bits_to_use (int, optional): The number of least significant bits
    18                                                   to use for insertion. Default is 1.
    19                                           
    20                                               Returns:
    21                                               - image (Image): The resulting image with the message inserted.
    22                                               """
    23         1       1000.0   1000.0      0.0      if not 1 <= bits_to_use <= 8:
    24                                                   raise InvalidBitsToUseError("Bits to use must be between 1 and 8.")
    25                                           
    26         1          0.0      0.0      0.0      binary_message = (
    27         1     245000.0 245000.0      1.4          "".join([format(byte, "08b") for byte in message.encode()]) + DELIMITER
    28                                               )
    29         1       1000.0   1000.0      0.0      binary_message_length = len(binary_message)
    30         1       2000.0   2000.0      0.0      min_required_pixels = math.ceil(binary_message_length / bits_to_use)
    31         1       5000.0   5000.0      0.0      total_image_pixels = image.width * image.height
    32         1       1000.0   1000.0      0.0      if min_required_pixels > total_image_pixels:
    33                                                   raise InsufficientPixelsError("Message size exceeds image pixels capacity.")
    34                                           
    35         1     818000.0 818000.0      4.7      image_array = np.array(image, dtype=np.uint8)
    36         1       2000.0   2000.0      0.0      image_mode = image.mode
    37                                           
    38         1          0.0      0.0      0.0      index = 0
    39        18      11000.0    611.1      0.1      for y in range(image.height):
    40      1801     669000.0    371.5      3.8          for x in range(image.width):
    41      1784    1265000.0    709.1      7.2              pixel = image_array[y, x, :].tolist()
    42      5351    2063000.0    385.5     11.8              for bit_index in range(bits_to_use):
    43      3568    1737000.0    486.8      9.9                  new_bit_value = int(binary_message[index], 2)
    44      3568    1230000.0    344.7      7.0                  color_value = pixel[-1]
    45      3568    1453000.0    407.2      8.3                  clear_bit_color = color_value & ~(1 << bit_index)
    46      3568    1448000.0    405.8      8.3                  new_color_value = clear_bit_color | (new_bit_value << bit_index)
    47      3568    1127000.0    315.9      6.4                  pixel[-1] = new_color_value
    48      3568    2403000.0    673.5     13.7                  image_array[y, x, :] = pixel
    49      3568    1395000.0    391.0      8.0                  index += 1
    50      3568    1218000.0    341.4      7.0                  if index >= binary_message_length:
    51         1     383000.0 383000.0      2.2                      new_image = Image.fromarray(obj=image_array, mode=image_mode)
    52         1          0.0      0.0      0.0                      return new_image
    53                                               new_image = Image.fromarray(obj=image_array, mode=image_mode)
    54                                               return new_image
  ```
</details>

<details>
    <summary><b>extraction</b> function stats</summary>

  ```log
Timer unit: 1e-09 s

Total time: 0.010928 s
File: nlsbs_steganography.py
Function: extraction at line 57

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    57                                           def extraction(image: Image, bits_to_use: int = 1) -> str:
    58                                               """
    59                                               Least Significant Bit (LSB) extraction of a message from the image.
    60                                           
    61                                               Parameters:
    62                                               - image (Image): The image from which message will be extracted.
    63                                               - bits_to_use (int, optional): The number of least significant bits
    64                                                   used for insertion. Default is 1.
    65                                           
    66                                               Returns:
    67                                               - message (str): The extracted message from the image.
    68                                               """
    69         1       3000.0   3000.0      0.0      if not 1 <= bits_to_use <= 8:
    70                                                   raise InvalidBitsToUseError("Bits to use must be between 1 and 8.")
    71                                           
    72         1     236000.0 236000.0      2.2      image_array = np.asarray(a=image, dtype=int)
    73                                           
    74         1       3000.0   3000.0      0.0      message_characters = []
    75         1       1000.0   1000.0      0.0      index = 0
    76         1          0.0      0.0      0.0      character_buffer = []
    77        18      10000.0    555.6      0.1      for y in range(image.height):
    78      1801     619000.0    343.7      5.7          for x in range(image.width):
    79      1784     861000.0    482.6      7.9              color_value = image_array[y, x, -1]
    80      5351    2043000.0    381.8     18.7              for bit_index in range(bits_to_use):
    81      3568    1632000.0    457.4     14.9                  extracted_bit = (color_value >> bit_index) & 1
    82      3568    1859000.0    521.0     17.0                  character_buffer.append(str(extracted_bit))
    83      3568    1400000.0    392.4     12.8                  index += 1
    84      3568    1333000.0    373.6     12.2                  if index % 8 == 0:
    85       446     144000.0    322.9      1.3                      if "1" not in character_buffer:
    86         1       4000.0   4000.0      0.0                          message = "".join(message_characters)
    87         1          0.0      0.0      0.0                          return message
    88       445     124000.0    278.7      1.1                      try:
    89       445     254000.0    570.8      2.3                          character_code = int("".join(character_buffer), 2)
    90       445     213000.0    478.7      1.9                          message_characters.append(chr(character_code))
    91                                                               except ValueError:
    92                                                                   raise MessageExtractionError(
    93                                                                       f"Error extracting message at index {index}"
    94                                                                   ) from None
    95       445     189000.0    424.7      1.7                      character_buffer.clear()
    96                                               raise MessageNotFoundError("Hidden message not found in the image.")
  ```
</details>

## Optimization #3
This section presents the optimization results achieved by using the stable pixel updating.

### Benchmarking
Benchmarking results for the optimized functions are provided in this section.

| Function   | Repetitions | Baseline Time (seconds) | Execution Time (seconds) | Optimization Gain (%) |
|------------|-------------|-------------------------|--------------------------|-----------------------|
| insertion  | 1000        | 2.61                    | 1.29                     | 50.57                 |
| extraction | 1000        | 1.23                    | 0.79                     | 35.77                 |

### Profiling
Profiling results for the optimized functions are provided in this section.

<details>
    <summary><b>insertion</b> function stats</summary>

  ```log
Timer unit: 1e-09 s

Total time: 0.017402 s
File: nlsbs_steganography.py
Function: insertion at line 10

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    10                                           def insertion(image: Image, message: str, bits_to_use: int = 1) -> Image:
    11                                               """
    12                                               Least Significant Bit (LSB) insertion of a message into an image.
    13                                           
    14                                               Parameters:
    15                                               - image (Image): The input image to which message will be inserted.
    16                                               - message (str): The message to be inserted into the image.
    17                                               - bits_to_use (int, optional): The number of least significant bits
    18                                                   to use for insertion. Default is 1.
    19                                           
    20                                               Returns:
    21                                               - image (Image): The resulting image with the message inserted.
    22                                               """
    23         1       1000.0   1000.0      0.0      if not 1 <= bits_to_use <= 8:
    24                                                   raise InvalidBitsToUseError("Bits to use must be between 1 and 8.")
    25                                           
    26         1          0.0      0.0      0.0      binary_message = (
    27         1     233000.0 233000.0      1.3          "".join([format(byte, "08b") for byte in message.encode()]) + DELIMITER
    28                                               )
    29         1          0.0      0.0      0.0      binary_message_length = len(binary_message)
    30         1       4000.0   4000.0      0.0      min_required_pixels = math.ceil(binary_message_length / bits_to_use)
    31         1       9000.0   9000.0      0.1      total_image_pixels = image.width * image.height
    32         1          0.0      0.0      0.0      if min_required_pixels > total_image_pixels:
    33                                                   raise InsufficientPixelsError("Message size exceeds image pixels capacity.")
    34                                           
    35         1    1152000.0    1e+06      6.6      image_array = np.array(image, dtype=np.uint8)
    36         1       2000.0   2000.0      0.0      image_mode = image.mode
    37                                           
    38         1          0.0      0.0      0.0      index = 0
    39        18       5000.0    277.8      0.0      for y in range(image.height):
    40      1801     512000.0    284.3      2.9          for x in range(image.width):
    41      1784    4730000.0   2651.3     27.2              pixel = image_array[y, x].tolist()
    42      1784     590000.0    330.7      3.4              color_value = pixel[-1]
    43      5351    1575000.0    294.3      9.1              for bit_index in range(bits_to_use):
    44      3568    1352000.0    378.9      7.8                  new_bit_value = int(binary_message[index], 2)
    45      3568    1059000.0    296.8      6.1                  extracted_bit = (color_value >> bit_index) & 1
    46      3568     897000.0    251.4      5.2                  if new_bit_value != extracted_bit:
    47      1911     552000.0    288.9      3.2                      clear_bit_color = color_value & ~(1 << bit_index)
    48      1911     553000.0    289.4      3.2                      color_value = clear_bit_color | (new_bit_value << bit_index)
    49      1911     515000.0    269.5      3.0                      pixel[-1] = color_value
    50      1911    1139000.0    596.0      6.5                      image_array[y, x] = pixel
    51      3568    1034000.0    289.8      5.9                  index += 1
    52      3568     971000.0    272.1      5.6                  if index >= binary_message_length:
    53         1     517000.0 517000.0      3.0                      new_image = Image.fromarray(obj=image_array, mode=image_mode)
    54         1          0.0      0.0      0.0                      return new_image
    55                                               raise MessageInsertionError(f"Error insertion message at index {index}")
  ```
</details>

<details>
    <summary><b>extraction</b> function stats</summary>

  ```log
Timer unit: 1e-09 s

Total time: 0.013973 s
File: nlsbs_steganography.py
Function: extraction at line 58

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    58                                           def extraction(image: Image, bits_to_use: int = 1) -> str:
    59                                               """
    60                                               Least Significant Bit (LSB) extraction of a message from the image.
    61                                           
    62                                               Parameters:
    63                                               - image (Image): The image from which message will be extracted.
    64                                               - bits_to_use (int, optional): The number of least significant bits
    65                                                   used for insertion. Default is 1.
    66                                           
    67                                               Returns:
    68                                               - message (str): The extracted message from the image.
    69                                               """
    70         1          0.0      0.0      0.0      if not 1 <= bits_to_use <= 8:
    71                                                   raise InvalidBitsToUseError("Bits to use must be between 1 and 8.")
    72                                           
    73         1    1336000.0    1e+06      9.6      image_array = np.asarray(a=image, dtype=int)
    74                                           
    75         1       1000.0   1000.0      0.0      message_characters = []
    76         1          0.0      0.0      0.0      index = 0
    77         1          0.0      0.0      0.0      character_buffer = []
    78        18      13000.0    722.2      0.1      for y in range(image.height):
    79      1801     760000.0    422.0      5.4          for x in range(image.width):
    80      1784     958000.0    537.0      6.9              color_value = image_array[y, x, -1]
    81      5351    2463000.0    460.3     17.6              for bit_index in range(bits_to_use):
    82      3568    1917000.0    537.3     13.7                  extracted_bit = (color_value >> bit_index) & 1
    83      3568    2215000.0    620.8     15.9                  character_buffer.append(str(extracted_bit))
    84      3568    1518000.0    425.4     10.9                  index += 1
    85      3568    1700000.0    476.5     12.2                  if index % 8 == 0:
    86       446     174000.0    390.1      1.2                      if "1" not in character_buffer:
    87         1       2000.0   2000.0      0.0                          message = "".join(message_characters)
    88         1       1000.0   1000.0      0.0                          return message
    89       445     150000.0    337.1      1.1                      try:
    90       445     290000.0    651.7      2.1                          character_code = int("".join(character_buffer), 2)
    91       445     237000.0    532.6      1.7                          message_characters.append(chr(character_code))
    92                                                               except ValueError:
    93                                                                   raise MessageExtractionError(
    94                                                                       f"Error extracting message at index {index}"
    95                                                                   ) from None
    96       445     238000.0    534.8      1.7                      character_buffer.clear()
    97                                               raise MessageNotFoundError("Hidden message not found in the image.")
  ```
</details>

## Optimization #4
This section presents the optimization results achieved by using the C extension module.

### Benchmarking
Benchmarking results for the optimized functions are provided in this section.

| Function   | Repetitions | Baseline Time (seconds) | Execution Time (seconds) | Optimization Gain (%) |
|------------|-------------|-------------------------|--------------------------|-----------------------|
| insertion  | 1000        | 2.61                    | 1.78                     | 31.80                 |
| extraction | 1000        | 1.23                    | 0.82                     | 33.33                 |

### Profiling
Profiling results for the optimized functions are provided in this section.

<details>
    <summary><b>insertion</b> function stats</summary>

  ```log
Timer unit: 1e-09 s

Total time: 0.021088 s
File: nlsbs_steganography.py
Function: insertion at line 15

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    15                                           def insertion(image: Image, message: str, bits_to_use: int = 1) -> Image:
    16                                               """
    17                                               Least Significant Bit (LSB) insertion of a message into an image.
    18                                           
    19                                               Parameters:
    20                                               - image (Image): The input image to which message will be inserted.
    21                                               - message (str): The message to be inserted into the image.
    22                                               - bits_to_use (int, optional): The number of least significant bits
    23                                                   to use for insertion. Default is 1.
    24                                           
    25                                               Returns:
    26                                               - image (Image): The resulting image with the message inserted.
    27                                               """
    28         1       1000.0   1000.0      0.0      if not 1 <= bits_to_use <= 8:
    29                                                   raise InvalidBitsToUseError("Bits to use must be between 1 and 8.")
    30                                           
    31         1          0.0      0.0      0.0      binary_message = (
    32         1     230000.0 230000.0      1.1          "".join([format(byte, "08b") for byte in message.encode()]) + DELIMITER
    33                                               )
    34         1          0.0      0.0      0.0      binary_message_length = len(binary_message)
    35         1       4000.0   4000.0      0.0      min_required_pixels = math.ceil(binary_message_length / bits_to_use)
    36         1       6000.0   6000.0      0.0      total_image_pixels = image.width * image.height
    37         1       1000.0   1000.0      0.0      if min_required_pixels > total_image_pixels:
    38                                                   raise InsufficientPixelsError("Message size exceeds image pixels capacity.")
    39                                           
    40         1     428000.0 428000.0      2.0      image_array = np.array(image, dtype=np.uint8)
    41         1       1000.0   1000.0      0.0      image_mode = image.mode
    42                                           
    43         1          0.0      0.0      0.0      index = 0
    44        18      10000.0    555.6      0.0      for y in range(image.height):
    45      1801     855000.0    474.7      4.1          for x in range(image.width):
    46      1784    1339000.0    750.6      6.3              pixel = image_array[y, x].tolist()
    47      1784     803000.0    450.1      3.8              color_value = pixel[-1]
    48      5351    2698000.0    504.2     12.8              for bit_index in range(bits_to_use):
    49      7136    4265000.0    597.7     20.2                  color_value = c_functions.update_color_bit_value(
    50      3568    1938000.0    543.2      9.2                      color_value, bit_index, ord(binary_message[index])
    51                                                           )
    52      3568    1574000.0    441.1      7.5                  pixel[-1] = color_value
    53      3568    2663000.0    746.4     12.6                  image_array[y, x] = pixel
    54      3568    2438000.0    683.3     11.6                  index += 1
    55      3568    1754000.0    491.6      8.3                  if index >= binary_message_length:
    56         1      79000.0  79000.0      0.4                      new_image = Image.fromarray(obj=image_array, mode=image_mode)
    57         1       1000.0   1000.0      0.0                      return new_image
    58                                               raise MessageInsertionError(f"Error insertion message at index {index}")
  ```
</details>

<details>
    <summary><b>extraction</b> function stats</summary>

  ```log
Timer unit: 1e-09 s

Total time: 0.014976 s
File: nlsbs_steganography.py
Function: extraction at line 61

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    61                                           def extraction(image: Image, bits_to_use: int = 1) -> str:
    62                                               """
    63                                               Least Significant Bit (LSB) extraction of a message from the image.
    64                                           
    65                                               Parameters:
    66                                               - image (Image): The image from which message will be extracted.
    67                                               - bits_to_use (int, optional): The number of least significant bits
    68                                                   used for insertion. Default is 1.
    69                                           
    70                                               Returns:
    71                                               - message (str): The extracted message from the image.
    72                                               """
    73         1          0.0      0.0      0.0      if not 1 <= bits_to_use <= 8:
    74                                                   raise InvalidBitsToUseError("Bits to use must be between 1 and 8.")
    75                                           
    76         1     232000.0 232000.0      1.5      image_array = np.asarray(a=image, dtype=int)
    77                                           
    78         1       3000.0   3000.0      0.0      message_characters = []
    79         1       3000.0   3000.0      0.0      index = 0
    80         1          0.0      0.0      0.0      character_buffer = []
    81        18       9000.0    500.0      0.1      for y in range(image.height):
    82      1801    1023000.0    568.0      6.8          for x in range(image.width):
    83      1784    1109000.0    621.6      7.4              color_value = image_array[y, x, -1]
    84      5351    2957000.0    552.6     19.7              for bit_index in range(bits_to_use):
    85      3568    2082000.0    583.5     13.9                  extracted_bit = (color_value >> bit_index) & 1
    86      3568    2544000.0    713.0     17.0                  character_buffer.append(str(extracted_bit))
    87      3568    1855000.0    519.9     12.4                  index += 1
    88      3568    1835000.0    514.3     12.3                  if index % 8 == 0:
    89       446     193000.0    432.7      1.3                      if "1" not in character_buffer:
    90         1       2000.0   2000.0      0.0                          message = "".join(message_characters)
    91         1       1000.0   1000.0      0.0                          return message
    92       445     188000.0    422.5      1.3                      try:
    93       445     411000.0    923.6      2.7                          character_code = int("".join(character_buffer), 2)
    94       445     281000.0    631.5      1.9                          message_characters.append(chr(character_code))
    95                                                               except ValueError:
    96                                                                   raise MessageExtractionError(
    97                                                                       f"Error extracting message at index {index}"
    98                                                                   ) from None
    99       445     248000.0    557.3      1.7                      character_buffer.clear()
   100                                               raise MessageNotFoundError("Hidden message not found in the image.")

  ```
</details>

## Optimization #5
This section presents the optimization results achieved by using the **PyPy** (alternative implementation of Python).

### Benchmarking
Benchmarking results for the optimized functions are provided in this section.

| Function   | Repetitions | Baseline Time (seconds) | Execution Time (seconds) | Optimization Gain (%) |
|------------|-------------|-------------------------|--------------------------|-----------------------|
| insertion  | 1000        | 2.61                    | 4.86                     | -86.21                |
| extraction | 1000        | 1.23                    | 2.90                     | -136.59               |

