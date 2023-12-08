from pathlib import Path
from enum import Enum

# Types of hands
# Five of a kind set = 1, occur 5
# Four of a kind set = 2, occur 4 or  1
# Full house set = 2, occur 2 or 3
# Three of a Kind set = 3, occur 3 or 1
# Two pair set = 3, occur 2 or 1
# One Pair set = 4
# High Card set = 5

# Card types A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2,
# No suites

# hypothesis - we can still use Cactuskev approach, just with one suit 0b0100
# card rank is still 0 to 12 for 2 to A respectively
# Since everything can be repeated and is of the same suite, this may not work
# Card order matters
# If cards are initially sorted by hand_type and then order based on individual card "value"
# There are 13^5 (371,293) possible hands
# Simple approach might be use card rank and a multiplier for hand type so AAAAA as a sum of
# Maybe overly obvious - create a lookup table of values as this is now a sufficiently small lookup table


class Hand_Type(str, Enum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1


CARD_RANK_LOOKUP = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
}
rank_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]

suits = [1]
rank_names = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]


deck = []
for rank_count, rank in enumerate(range(13)):
    for suit in suits:
        deck.append(
            rank_primes[rank_count] | rank << 8 | suit << 12 | (1 << rank) << 16
        )


def get_hand_type(str_in: str) -> Hand_Type:
    unique_count = len(set(str_in))
    if unique_count == 1:
        return Hand_Type.FIVE_OF_A_KIND
    if unique_count == 2:
        occurrence_count = str_in.count(str_in[0])
        if occurrence_count == 1 or occurrence_count == 4:
            return Hand_Type.FOUR_OF_A_KIND
        return Hand_Type.FULL_HOUSE
    if unique_count == 3:
        occurrence_count = str_in.count(str_in[0])
        if occurrence_count == 3:
            return Hand_Type.THREE_OF_A_KIND
        elif occurrence_count == 2:
            return Hand_Type.TWO_PAIR
        else:
            occurrence_count = str_in.count(str_in[1])
            if occurrence_count == 3 or occurrence_count == 1:
                return Hand_Type.THREE_OF_A_KIND
            elif occurrence_count == 2:
                return Hand_Type.TWO_PAIR
    if unique_count == 4:
        return Hand_Type.ONE_PAIR
    if unique_count == 5:
        return Hand_Type.HIGH_CARD


class Hand:
    def update_hand(self, str_in: str):

        self.hand_string = str_in  # removing trailing newlines

        self.hand_rank: Hand_Type = get_hand_type(str_in)

    def __init__(
        self, str_in: str, card_rank_lookup: dict[str, int] = CARD_RANK_LOOKUP
    ) -> None:
        self.card_rank_lookup = card_rank_lookup
        tmp = str_in.split()
        self.bet: int = int(tmp[1])
        self.update_hand(tmp[0])

    def __lt__(self, other: "Hand"):
        if self.hand_rank == other.hand_rank:
            for i in range(5):
                if self.hand_string[i] != other.hand_string[i]:
                    return self.card_rank_lookup.get(
                        self.hand_string[i]
                    ) < self.card_rank_lookup.get(other.hand_string[i])

            # same string
            return False

        else:
            return self.hand_rank.value < other.hand_rank.value

    def __str__(self) -> str:
        return self.hand_string


def parse_input(file_path="./day_7/small_input.txt", hand_class=Hand):
    file = Path(file_path)
    if not file.exists():
        raise FileNotFoundError(
            f"Could not find puzzle input file at {file.as_posix()}"
        )
    hands: list[Hand] = []
    with open(file) as f:

        for line_number, line in enumerate(f):
            try:
                hands.append(hand_class(line))
            except Exception as e:
                print(f"Error on line number {line_number}")
                print(line)
                raise (e)

    return hands


if __name__ == "__main__":

    hands = parse_input("./day_7/puzzle_input.txt")
    hands.sort()
    running_sum = 0
    for rank_number, hand in enumerate(hands):
        running_sum += (rank_number + 1) * hand.bet
    print(running_sum)
    assert running_sum == 250453939
