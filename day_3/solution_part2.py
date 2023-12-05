from pathlib import Path
from re import Match
from solution_part1 import INDICATOR_SEARCH_PATTERN, MODEL_SEARCH_PATTERN, LineObject, get_match_bounding_box


def merge_tracker(primary_tracker:dict[int,dict[int,list[int]]],update_to_tracker:dict[int,dict[int,list[int]]],focus_lines:set[int]=None):
    out:dict[int,dict[int,list[int]]] = primary_tracker
    if focus_lines is None:
        focus_lines = (primary_tracker.keys() | update_to_tracker.keys())
    for line in focus_lines:
        out[line] = out.get(line,{})
        for gear_pos in (primary_tracker.get(line,{}).keys() | update_to_tracker.get(line,{}).keys()):
            out[line][gear_pos] = primary_tracker.get(line,{}).get(gear_pos,[])
            out[line][gear_pos].extend(update_to_tracker.get(line,{}).get(gear_pos,[]))
    return out
            


    


def find_gearing_sums(model_line:LineObject,verifier_lines:list[LineObject],max_length:int,offset:int=0):
    gearing:dict[int,dict[int,list[int]]] = {}
    for model in model_line.model_number_matches:
        for line_number,line in enumerate(verifier_lines): 
            tmp = line.find_verifier_collision(*get_match_bounding_box(model,max_length))
            if tmp:
                gearing[line_number+offset] = gearing.get(line_number+offset,{})
                gearing[line_number+offset][tmp] = gearing[line_number+offset].get(tmp,[])
                gearing[line_number+offset][tmp].append(int(model.group()))
    return gearing

if __name__ == "__main__":
    file = Path("./day_3/puzzle_input.txt")
    if not file.exists():
        raise FileNotFoundError(f"Could not find puzzle input file at {file.as_posix()}")
    line_buffer:list[str] = []
    gear_tracker = {}
    with open(file) as f:
        verified_models:list[Match] = []
        for line_number,line in enumerate(f):
            max_line_length = len(line)
            line_buffer.append(LineObject(line,indicator_search_patter=r'\*'))
            #Ensures we're only maintaining at most 3 lines in memory            
            if len(line_buffer)>3:
                line_buffer.pop(0)
            if len(line_buffer) ==3:
                tmp = find_gearing_sums(line_buffer[1],line_buffer,max_line_length,line_number-2)
                gear_tracker = merge_tracker(gear_tracker,tmp)
            #First line
            elif len(line_buffer)==2:
                tmp = find_gearing_sums(line_buffer[0],line_buffer,max_line_length)
                gear_tracker = tmp

        #last line
        tmp = find_gearing_sums(line_buffer[2],[line_buffer[1]],max_line_length,line_number-1)
        gear_tracker = merge_tracker(gear_tracker,tmp)
        print(gear_tracker)
        #  multiply and sum gearing
        running_sum = 0
        for line in gear_tracker.keys():
            for gear in gear_tracker[line].keys():
                if len(gear_tracker[line][gear]) == 2:
                    running_sum += gear_tracker[line][gear][0]*gear_tracker[line][gear][1]
        print(running_sum)        
