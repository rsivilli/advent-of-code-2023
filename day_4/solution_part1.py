from pathlib import Path
def parse_numbers(str_in:str)->list[int]:
    return [int(val) for val in str_in.strip().split(" ") if val != ""]
def parse_line(str_in:str)->tuple[list[int],list[int]]:
    tmp = str_in.split(":")[1]
    tmp = tmp.split("|")
    return parse_numbers(tmp[0]), parse_numbers(tmp[1])
def count_winners(you_numbers:list[int],winning_numbers:list[int])->int:
    """Returns the number of winning numbers found in your numbers"""
    lookup = set(winning_numbers)
    winner_count = 0
    for val in you_numbers:
        if val in lookup:
            winner_count +=1
    return winner_count

if __name__ == "__main__":
    file_path="./day_4/puzzle_input.txt"
    file = Path(file_path)
    if not file.exists():
        raise FileNotFoundError(f"Could not find puzzle input file at {file.as_posix()}")

    running_sum = 0

    with open(file) as f:
       for line in f:
           total_winners = count_winners(*parse_line(line))
           if total_winners > 0:
            running_sum = running_sum + 2**(total_winners-1)
    print(running_sum)