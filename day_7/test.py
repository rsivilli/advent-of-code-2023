from solution_part2 import JokerWild, Hand_Type, get_hand_type


HAND_TEST_CASES = [
    ("32T3K", Hand_Type.ONE_PAIR),
    ("T55J5", Hand_Type.THREE_OF_A_KIND),
    ("KK677", Hand_Type.TWO_PAIR),
    ("KTJJT", Hand_Type.TWO_PAIR),
    ("QQQJA", Hand_Type.THREE_OF_A_KIND),
    ("QQQQQ", Hand_Type.FIVE_OF_A_KIND),
    ("AQJT8", Hand_Type.HIGH_CARD),
    ("AAAQQ", Hand_Type.FULL_HOUSE),
    ("AAAAQ", Hand_Type.FOUR_OF_A_KIND),
]


for test_in, expected_out in HAND_TEST_CASES:
    tmp = get_hand_type(test_in)
    try:
        assert tmp == expected_out
    except AssertionError as e:
        print(test_in)
        print(tmp)
        raise e


TEST_CASES = [
    ("32T3K 765", "32T3K"),
    ("T55J5 684", "T5555"),
    ("KK677 28", "KK677"),
    ("KTJJT 220", "KTTTT"),
    ("QQQJA 483", "QQQQA"),
    ("JJJJJ 10", "AAAAA"),
    ("AAAAA 15", "AAAAA"),
    ("JJAAA 15", "AAAAA"),
    ("JJJKK 15", "KKKKK"),
    ("KK2JJ 15", "KK2KK"),
    ("JJ2KK 15", "KK2KK"),
    ("J2KK5 15", "K2KK5"),
    ("A2JK5 15", "A2AK5"),
    ("AAAAA 15", "AAAAA"),
    ("JJJJJ 15", "AAAAA"),
    ("KKKKK 15", "KKKKK"),
    ("AAAAK 15", "AAAAK"),
    ("AAAAJ 15", "AAAAA"),
    ("TTTTJ 15", "TTTTT"),
    ("TTTAA 15", "TTTAA"),
    ("TTTJJ 15", "TTTTT"),
    ("TTTAJ 15", "TTTAT"),
    ("TTTAA 15", "TTTAA"),
    ("TTTJJ 15", "TTTTT"),
    ("JJJAA 15", "AAAAA"),
    ("TTTAA 15", "TTTAA"),
    ("JJTAA 15", "AATAA"),
    ("JJT99 15", "99T99"),
    ("JJA98 15", "AAA98"),
    ("AAJ98 15", "AAA98"),
    ("TJ9T5 15", "TT9T5"),
    ("4267J 15", "42677"),
    ("4267A 15", "4267A"),
    ("JA267 15", "AA267"),
]


for test_in, expected_out in TEST_CASES:
    tmp = JokerWild(test_in)
    try:
        assert tmp.original_hand == test_in.split()[0]
        assert tmp.hand_string == expected_out
    except AssertionError as e:
        print(tmp.original_hand)
        print(tmp.hand_string)
        raise e

SORTING_CASE = [
    (
        [
            "3J4KT 513",
            "Q3K42 147",
        ],
        ["Q3K42", "3K4KT"],
    ),
    (["JJ32A 513", "J332A 147"], ["AA32A", "3332A"]),
    (["QJJQ2 513", "JKKK2 147", "QQQQ2 23"], ["KKKK2", "QQQQ2", "QQQQ2"]),
]

for test_in, expected_out in SORTING_CASE:
    hands = [JokerWild(str_in) for str_in in test_in]
    hands.sort()
    for count, hand in enumerate(hands):
        try:
            assert hand.hand_string == expected_out[count]
        except AssertionError as e:
            print(f"{hand}!={expected_out[count]}")
