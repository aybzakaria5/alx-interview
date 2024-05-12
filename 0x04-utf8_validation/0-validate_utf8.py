#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Method to determine if a given data set represents a valid UTF-8 encoding.

    Args:
        data: A list of integers representing bytes of data.

    Returns:
        True if data is a valid UTF-8 encoding, else return False.
    """
    # Initialize a count variable to track the number of leading ones
    count = 0

    # Iterate through each integer in the data
    for num in data:
        if count == 0:
            if (num >> 5) == 0b110:
                count = 1
            elif (num >> 4) == 0b1110:
                count = 2
            elif (num >> 3) == 0b11110:
                count = 3
            elif (num >> 7) != 0:
                return False
        else:
            # If the byte starts with 10, it's part of a multi-byte character
            if (num >> 6) != 0b10:
                return False
            count -= 1

    # If count is not 0 at the end, it means a character was not completed
    return count == 0
