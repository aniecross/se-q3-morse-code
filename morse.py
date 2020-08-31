#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Morse Code Decoder

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
"""
__author__ = """Anie Cross with help from instructor demo recordings,
Group-B discussion topics, Google search, docs.python.org, stackoverflow.com,
assessment completed with help from Tutor HPost"""

from morse_dict import MORSE_2_ASCII


def decode_bits(bits):
    bits = bits.strip("0")
    unit = 0
    for bit in bits:
        if bit != "0":
            unit += 1
        else:
            break
    # unit now might be 1 unit or 3 units
    count = 1
    for i in range(1, len(bits)):
        if bits[i] == bits[i-1]:
            count += 1
        else:
            if count < unit:
                unit = count
                count = 1
            else:
                count = 1
    morse_code = ""
    words = bits.split("0"*7*unit)
    for word in words:
        characters = word.split("0"*3*unit)
        for character in characters:
            signs = character.split("0"*unit)
            for sign in signs:
                if sign != "":
                    sign.strip('0')
                    if sign == "1"*3*unit:
                        morse_code += "-"
                    else:
                        morse_code += "."
            morse_code += " "
        morse_code += "  "
    return morse_code.strip(" ")


def decode_morse(morse):
    results = ''
    for item in morse.split('  '):  # gives word
        for ltr in item.split(' '):     # gives characters
            if ltr != '':
                results += MORSE_2_ASCII[ltr]
        results += ' '  # this is for space in between words
    return results.strip(' ')   # strip ending space and beginning


if __name__ == '__main__':
    hey_jude_morse = ".... . -.--   .--- ..- -.. ."
    hey_jude_bits = "11001100110011000000110000001111110011001111110011111100000000000000000000011001111110011111100111111000000110011001111110000001111110011001100000011" # noqa

    # Be sure to run all included unit tests, not just this one.
    print("Morse Code decoder test")
    print("Part A:")
    print(f"'{hey_jude_morse}' -> {decode_morse(hey_jude_morse)}")
    print()
    print("Part B:")
    print(f"'{hey_jude_bits}' -> {decode_morse(decode_bits(hey_jude_bits))}")

    print("\nCompleted.")
