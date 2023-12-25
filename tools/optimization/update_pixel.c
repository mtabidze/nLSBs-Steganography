// Copyright (c) 2023 Mikheil Tabidze
#include <stdio.h>

int update_color_bit_value(int color_value, int bit_index, char bit_value) {
    return (color_value & ~(1 << bit_index)) | ((bit_value - '0') << bit_index);
}

void run_unit_test(int test_number, int input_color, int bit_index, char bit_value, int expected_result) {
    int result = update_color_bit_value(input_color, bit_index, bit_value);
    if (result == expected_result) {
        printf("Test %d Passed\n", test_number);
    } else {
        printf("Test %d Failed. Expected %d but got %d\n", test_number, expected_result, result);
    }
}

int main() {
    run_unit_test(1, 0b11111111, 0, '1', 0b11111111);
    run_unit_test(2, 0b11111111, 0, '0', 0b11111110);
    run_unit_test(3, 0b11111111, 4, '0', 0b11101111);
    run_unit_test(4, 0b11111111, 7, '1', 0b11111111);
    run_unit_test(5, 0b11111111, 7, '0', 0b01111111);

    return 0;
}