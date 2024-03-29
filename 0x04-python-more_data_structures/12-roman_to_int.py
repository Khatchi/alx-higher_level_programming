#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    last_rom = 0
    list_num = [0]

    for ch in roman_string:
        for r_num in rom_n:
            if r_num == ch:
                if rom_n[ch] <= last_rom:
                    list_num[-1] = rom_n[ch]
                else:
                    list_num.append(rom_n[ch])
                last_rom = rom_n[ch]

    num = sum(list_num)
    return num

