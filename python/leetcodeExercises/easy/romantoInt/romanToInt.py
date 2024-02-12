# TODO create a passing and failing test for this in test.py
def roman_to_int(s: str) -> int:
    """
    Converts a roman numeral into it's integer representation.
    
    Args:
        s (str): A roman numeral as a string 

    Returns:
        int: An integer value of the roman numeral
    """
    roman_dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    previous_value = 0
    for c in s:
        current_value = roman_dictionary[c]
        result += current_value
        if current_value > previous_value:
            result -= 2 * previous_value
        previous_value = current_value
    return result
