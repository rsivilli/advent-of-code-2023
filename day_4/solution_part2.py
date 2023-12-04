from solution_part1 import count_winners, parse_line
from pathlib import Path

if __name__ == "__main__":
    file_path="./day_4/puzzle_input.txt"
    file = Path(file_path)
    if not file.exists():
        raise FileNotFoundError(f"Could not find puzzle input file at {file.as_posix()}")

    with open(file) as f:
       winner_lookup = {0:1}
       for line_number,line in enumerate(f):
            winner_lookup[line_number] = winner_lookup.get(line_number,1)
            for i in range(count_winners(*parse_line(line))):
                future_card = line_number+i+1
                winner_lookup[future_card] =winner_lookup.get(future_card,1) + winner_lookup.get(line_number,1)
                
    print(sum(winner_lookup.values()))