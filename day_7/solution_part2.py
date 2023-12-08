from solution_part1 import CARD_RANK_LOOKUP, parse_input, Hand, Hand_Type, get_hand_type


CARD_RANK_LOOKUP_OVERRIDE = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}


def find_max(lookup: dict[str, int]) -> list[str]:
    out = sorted(lookup.keys(), key=lambda item: lookup[item])
    return out


ORDERED_CARD_RANK = find_max(CARD_RANK_LOOKUP_OVERRIDE)


class JokerWild(Hand):
    def __init__(
        self,
        str_in: str,
        card_rank_lookup: dict[str, int] = CARD_RANK_LOOKUP_OVERRIDE,
        wild_card="J",
        ordered_card_rank=ORDERED_CARD_RANK,
    ) -> None:
        super().__init__(str_in, card_rank_lookup)
        self.original_hand = self.hand_string
        if ordered_card_rank is None:
            ordered_card_rank = find_max(card_rank_lookup)

        card_count = {}
        for c in self.hand_string:
            card_count[c] = card_count.get(c, 0) + 1
        ordered_count = find_max(card_count)[::-1]
        if self.hand_rank == Hand_Type.FIVE_OF_A_KIND and ordered_count[0] == wild_card:
            self.update_hand(self.hand_string.replace(wild_card, ordered_card_rank[-1]))
        elif self.hand_rank == Hand_Type.FOUR_OF_A_KIND:
            if ordered_count[0] == wild_card:
                self.update_hand(self.hand_string.replace(wild_card, ordered_count[-2]))
            else:
                self.update_hand(self.hand_string.replace(wild_card, ordered_count[0]))
        elif self.hand_rank == Hand_Type.FULL_HOUSE:
            if ordered_count[0] == wild_card:
                self.update_hand(self.hand_string.replace(wild_card, ordered_count[1]))
            else:
                self.update_hand(self.hand_string.replace(wild_card, ordered_count[0]))
        elif self.hand_rank == Hand_Type.THREE_OF_A_KIND:
            if ordered_count[0] == wild_card:
                if CARD_RANK_LOOKUP_OVERRIDE.get(
                    ordered_count[1]
                ) > CARD_RANK_LOOKUP_OVERRIDE.get(ordered_count[2]):
                    self.update_hand(
                        self.hand_string.replace(wild_card, ordered_count[1])
                    )
                else:
                    self.update_hand(
                        self.hand_string.replace(wild_card, ordered_count[2])
                    )
            else:
                self.update_hand(self.hand_string.replace(wild_card, ordered_count[0]))
        elif self.hand_rank == Hand_Type.TWO_PAIR:
            if card_rank_lookup.get(ordered_count[0]) > card_rank_lookup.get(
                ordered_count[1]
            ):
                self.update_hand(self.hand_string.replace(wild_card, ordered_count[0]))
            else:
                self.update_hand(self.hand_string.replace(wild_card, ordered_count[1]))
        elif self.hand_rank == Hand_Type.ONE_PAIR:
            if ordered_count[0] == wild_card:
                self.update_hand(
                    self.hand_string.replace(
                        wild_card,
                        sorted(
                            ordered_count[1:],
                            key=lambda item: card_rank_lookup.get(item),
                        )[-1],
                    )
                )
            else:
                self.update_hand(self.hand_string.replace(wild_card, ordered_count[0]))
        elif self.hand_rank == Hand_Type.HIGH_CARD:
            self.update_hand(
                self.hand_string.replace(
                    wild_card,
                    sorted(ordered_count, key=lambda item: card_rank_lookup.get(item))[
                        -1
                    ],
                )
            )

    def __lt__(self: "JokerWild", other: "JokerWild"):
        if self.hand_rank == other.hand_rank:
            # for i in range(5):
            #     if self.hand_string[i] != other.hand_string[i]:
            #         return self.card_rank_lookup.get(self.hand_string[i]) < self.card_rank_lookup.get(other.hand_string[i])

            # same string
            for i in range(5):
                if self.original_hand[i] != other.original_hand[i]:
                    return self.card_rank_lookup.get(
                        self.original_hand[i]
                    ) < self.card_rank_lookup.get(other.original_hand[i])

        else:
            return self.hand_rank.value < other.hand_rank.value


if __name__ == "__main__":
    tmp = "./day_7/puzzle_input.txt"
    hands = parse_input(tmp, hand_class=JokerWild)
    hands.sort()
    running_sum = 0

    for rank_number, hand in enumerate(hands):
        running_sum += (rank_number + 1) * hand.bet
    with open("debug.txt", "w") as f:
        f.writelines(
            [
                f"{hand.original_hand}->{hand.hand_string} {hand.hand_rank.name}\n"
                for hand in hands
            ]
        )
    print(running_sum)
