from pathlib import Path
import re
from dataclasses import dataclass
from math import floor, ceil

@dataclass
class Race:
    time:int
    distance:int

def calc_distance(race_time:int, charge_time:int)->int:
    return charge_time*race_time-charge_time**2
def exceeds_record(race_time:int,charge_time:int,record_distance:int):
    return calc_distance(race_time,charge_time)>record_distance
def parse_input(file_path:str= "./day_6/small_input.txt")->list[Race]:
    file = Path(file_path)
    if not file.exists():
        raise FileNotFoundError(f"Could not find puzzle input file at {file.as_posix()}")
    with open(file) as f:
        lines = f.readlines()
        times= re.findall(r"\d+",lines[0])
        distances = re.findall(r"\d+",lines[1])
        out = []
        for i in range(len(times)):
            out.append(Race(
                time = int(times[i]),
                distance=int(distances[i])
            ))
    return out




if __name__ == "__main__":
    races = parse_input("./day_6/puzzle_input.txt")
    win_count = []
    for race in races:
        win_count.append(sum([1 for t in range(race.time) if exceeds_record(race.time,t,race.distance)]))
    product = 1
    for win in win_count:
        product = product*win
    print(product)

        