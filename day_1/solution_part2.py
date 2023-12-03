from string import digits
from pathlib import Path

def find_digit(str_in:str)->int:
    """Returns the first digit within a string"""
    for letter in str_in:
        if letter in digits:
            return int(letter)
    raise ValueError(f"Could not find a digit in the provided string {str_in}")

def first_digit(str_in:str)->int:
    """Return the left most digit in a string"""
    return find_digit(str_in)
def last_digit(str_in:str)->int:
    """Return the right most digit in a string"""
    return find_digit(str_in[::-1])
def find_two_digit(str_in:str)->int:
    return 10*first_digit(str_in)+last_digit(str_in)


if __name__ == "__main__":
    file_path="./day_1/puzzle_input.txt"
    file = Path(file_path)
    if not file.exists():
        raise FileNotFoundError(f"Could not find puzzle input file at {file.as_posix()}")
    
    running_sum = 0

    with open(file) as f:
       for line in f:
           running_sum = running_sum + find_two_digit(line)
    print(running_sum)
           