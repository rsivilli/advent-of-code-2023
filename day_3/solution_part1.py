from re import finditer, Match
from string import punctuation
from pathlib import Path
MODEL_SEARCH_PATTERN = r'(?P<model_number>\d+)'
INDICATOR_SEARCH_PATTERN = r'(?P<model_indicator>[!"#\$%&\'\(\)\*\+,\-\/:\;<=>?@\[\]\^_`{\|}~])'

test = ["467..114..",
        "...*......",
        "..35..633."
]

class LineObject:

    def __init__(self,str_in:str,model_search_pattern=MODEL_SEARCH_PATTERN,indicator_search_patter=INDICATOR_SEARCH_PATTERN) -> None:
        self.model_number_matches:list[Match] = []
        self.verifier_locations:list[int] = []
        for m in finditer(model_search_pattern,str_in):
            self.model_number_matches.append(m)
        for m in finditer(indicator_search_patter,str_in):
            self.verifier_locations.append(m.span()[0])
    def find_verifier_collision(self,lower_bound:int, upper_bound:int, arr=None)->int|None:
        """Simple binary search for fast lookup"""
        
        if arr is None:
            arr = self.verifier_locations
        if len(arr) == 0:
            return None
        pos = int(len(arr)/2)
        if arr[pos] >= lower_bound and arr[pos] <= upper_bound:
            return arr[pos]
        elif arr[pos] < lower_bound:
            return self.find_verifier_collision(lower_bound,upper_bound,arr[pos+1:])
        elif arr[pos] > upper_bound:
            return self.find_verifier_collision(lower_bound,upper_bound,arr[:pos])
            
        

            
def get_match_bounding_box(m:Match,max_length):
    start, end = m.span()
    return max(0,start-1), min(end,max_length)

def find_verified_models(model_line:LineObject,verifier_lines:list[LineObject],max_length:int):
    verified_models = []
    for model in model_line.model_number_matches:
        for line in verifier_lines: 
            tmp = line.find_verifier_collision(*get_match_bounding_box(model,max_length))
            if tmp:
                verified_models.append(model)
                break
    return verified_models



if __name__ == "__main__":
    file = Path("./day_3/puzzle_input.txt")
    if not file.exists():
        raise FileNotFoundError(f"Could not find puzzle input file at {file.as_posix()}")
    line_buffer:list[str] = []
    with open(file) as f:
        verified_models:list[Match] = []
        for line_number,line in enumerate(f):
            max_line_length = len(line)
            line_buffer.append(LineObject(line))
            #Ensures we're only maintaining at most 3 lines in memory            
            if len(line_buffer)>3:
                line_buffer.pop(0)
            if len(line_buffer) ==3:
                verified_models.extend(find_verified_models(line_buffer[1],line_buffer,max_line_length))
            elif len(line_buffer)==2:
                verified_models.extend(find_verified_models(line_buffer[0],line_buffer,max_line_length))
                
                #evaluate first line
        verified_models.extend(find_verified_models(line_buffer[2],[line_buffer[1]],max_line_length))
    verified_model_numbers = [int(m.group()) for m in verified_models]
    print(sum(verified_model_numbers))
        


    
