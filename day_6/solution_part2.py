from math import floor, ceil
from solution_part1 import calc_distance, Race, exceeds_record
from pathlib import Path
import re

def local_max(race_time:int)->int:
    #Since we're working with ints, we need to check either side of the possible decimals
    tmp_1 = floor(race_time/2)
    tmp_1_distance = calc_distance(race_time,tmp_1)
    tmp_2 = ceil(race_time/2)
    tmp_2_distance = calc_distance(race_time,tmp_2)
    if tmp_1_distance>=tmp_2_distance:
        return tmp_1
    return tmp_2

def parse_input(file_path:str= "./day_6/small_input.txt")->Race:
    file = Path(file_path)
    if not file.exists():
        raise FileNotFoundError(f"Could not find puzzle input file at {file.as_posix()}")
    with open(file) as f:
        lines = f.readlines()
        times= re.findall(r"\d+",lines[0].replace(" ",""))
        distances = re.findall(r"\d+",lines[1].replace(" ",""))
        
    return Race(
                time = int(times[0]),
                distance=int(distances[0])
            )
def binary_search(min_val,max_val,record_distance, race_time)->int:
    # print(f"searching {min_val}-{max_val}")
    if min_val==max_val:
        return max_val
    if (max_val-min_val) == 1:
        if exceeds_record(record_distance=record_distance,race_time=race_time,charge_time=min_val):
            return min_val
        else:
            return max_val
    test_val = int((max_val-min_val)/2)+min_val
    if exceeds_record(record_distance=record_distance,race_time=race_time,charge_time=test_val):
        return binary_search(test_val,max_val,record_distance,race_time)
    else:
        return binary_search(min_val,test_val,record_distance,race_time)
if __name__ =="__main__":
    race = parse_input("./day_6/puzzle_input.txt")
    t_0 = local_max(race.time)
    print(t_0)
    t_max = binary_search(t_0,race.time,race.distance,race.time)
    print(f"Max time you could charge is {t_max}")
    t_delta = t_max-t_0
    t_min = t_0-t_delta
    print(f"Min time you could charge is {t_min}")
    print(2*(t_max-t_0)+1)