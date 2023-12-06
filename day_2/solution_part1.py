import re
from dataclasses import dataclass
from pathlib import Path

TRUTH = {"red": 12, "green": 13, "blue": 14}
RE_DICE_COUNT = r"(?P<draw>(?P<dice_count>\d+) (?P<dice_type>[a-zA-Z]+))"


@dataclass
class DiceCount:
    dice_type: str
    dice_count: int


def parse_game(str_in: str, truth: dict[str, int] = TRUTH) -> tuple[int, bool]:
    game_split = str_in.split(":")
    game_id = int(game_split[0].split(" ")[1])
    for draw_str, dice_count, dice_type in re.findall(RE_DICE_COUNT, game_split[1]):
        truth_count = truth.get(dice_type)
        if truth_count is None:
            return game_id, False
        elif int(dice_count) > truth_count:
            return game_id, False

    return game_id, True


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
            game_id, valid = parse_game(line)
            if valid:
                running_sum += game_id

    print(running_sum)
