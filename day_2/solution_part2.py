import re
from dataclasses import dataclass
from pathlib import Path

TRUTH = {"red": 12, "green": 13, "blue": 14}
RE_DICE_COUNT = r"(?P<draw>(?P<dice_count>\d+) (?P<dice_type>[a-zA-Z]+))"


@dataclass
class DiceCount:
    dice_type: str
    dice_count: int


def parse_game(str_in: str) -> int:
    game_split = str_in.split(":")
    game_id = int(game_split[0].split(" ")[1])
    max_dice_pull = {}
    for draw_str, dice_count, dice_type in re.findall(RE_DICE_COUNT, game_split[1]):
        max_dice_pull[dice_type] = max(max_dice_pull.get(dice_type, 0), int(dice_count))
    out = 1
    for val in max_dice_pull.values():
        out *= val
    return out


if __name__ == "__main__":
    file_path = "./day_2/puzzle_input.txt"
    file = Path(file_path)
    if not file.exists():
        raise FileNotFoundError(
            f"Could not find puzzle input file at {file.as_posix()}"
        )

    running_sum = 0

    with open(file) as f:
        for line in f:
            val = parse_game(line)
            running_sum += val

    print(running_sum)
