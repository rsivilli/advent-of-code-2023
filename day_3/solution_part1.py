import re
from string import punctuation
punctuation = punctuation.replace(".","")
SEARCH_PATTERN = r'\d+'
test = ["467..114..",
        "...*......",
        "..35..633."
]

     
def safe_2d_access(i:int,j:int,_2d_list:list[list[str]], default="."):
    max_height = len(_2d_list)
    max_width =len(_2d_list[0])
    if j > max_height or j < 0 or i>max_width or i<0:
        return default
    return _2d_list[i][j]   
def convert_1d_to_2d(val:int,max_width:int)->tuple[int,int]:
    height = int(val/max_width)
    width = val%max_width
    return width,height

print()