#!/usr/bin/python3

"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Prototype: def validUTF8(data)
    Return: True if data is a valid UTF-8 encoding, else return False
    A character in UTF-8 can be 1 to 4 bytes long
    The data will be represented by a list of integers
    Each integer represents 1 byte of data
    Return: True if data is a valid UTF-8 encoding,
    therefore you only need to handle the 8 least significant
    bits of each integer
    """
    number_of_bytes = 0
    n1 = 1 << 7
    b2 = 1 << 6

    for i in data:
        j = 1 << 7
        if number_of_bytes == 0:
            while j & i:
                number_of_bytes += 1
                j = j >> 1
            if number_of_bytes == 0:
                continue
            if number_of_bytes == 1 or number_of_bytes > 4:
                return False
        else:
            if not (i & n1 and not (i & b2)):
                return False
        number_of_bytes -= 1
    return number_of_bytes == 0
    # num_bytes = 0
    # for byte in data:
    #     # Check if current byte is a start byte
    #     if num_bytes == 0:
    #         if (byte >> 5) == 0b110:
    #             num_bytes = 1
    #         elif (byte >> 4) == 0b1110:
    #             num_bytes = 2
    #         elif (byte >> 3) == 0b11110:
    #             num_bytes = 3
    #         elif (byte >> 7):
    #             return False
    #     else:
    #         # Check if current byte is a continuation byte
    #         if (byte >> 6) != 0b10:
    #             return False
    #         num_bytes -= 1
    # return num_bytes == 0
