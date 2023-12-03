from string import digits
from pathlib import Path
import re

base_number_spelling = 'zero|one|two|three|four|five|six|seven|eight|nine'
reverse_number_spelling = base_number_spelling[::-1]
FORWARD_NUMBER_SEARCH = f'{base_number_spelling}|\d'
REVERSE_NUMBER_SEARCH = f'{reverse_number_spelling}|\d'

NUMBER_LOOKUP = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}



def find_digit(str_in:str,search_re)->int:
    """Returns the first digit within a string"""

    tmp = re.match(str_in,search_re)
    
def first_digit(str_in:str)->int:
    """Return the left most digit in a string"""
    
    tmp = re.search(FORWARD_NUMBER_SEARCH,str_in).group()
    if len(tmp)>1:
        tmp = NUMBER_LOOKUP.get(tmp)
    return int(tmp)
def last_digit(str_in:str)->int:
    """Return the right most digit in a string"""
    tmp = re.search(REVERSE_NUMBER_SEARCH,str_in[::-1]).group()
    if len(tmp)>1:
        tmp = NUMBER_LOOKUP.get(tmp[::-1])
    return int(tmp)
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
           