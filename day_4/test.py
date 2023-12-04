from solution_part1 import count_winners, parse_line

TEST_CASE = [([41, 48, 83, 86, 17], [83, 86,  6, 31, 17,  9, 48, 53],4),
([13, 32, 20, 16, 61], [61, 30, 68, 82, 17, 32, 24, 19],2),
([1, 21, 53, 59, 44], [69, 82, 63, 72, 16, 21, 14,  1],2)
]


for your_numbers,winning_numbers,expected in TEST_CASE:
    assert count_winners(your_numbers,winning_numbers) == expected



TEST_CASE = [
    ('Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',[41, 48, 83, 86, 17], [83, 86,  6, 31, 17,  9, 48, 53]),
    ('Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',[13, 32, 20, 16, 61], [61, 30, 68, 82, 17, 32, 24, 19])
]

for test_string, expected_numbers, expected_winners in TEST_CASE:
    try:
        num,win = parse_line(test_string)
        assert num == expected_numbers
        assert win == expected_winners
    except AssertionError as e:
        print(f"expected numbers:{expected_numbers}")
        print(f"parsed numbers:{num}")
        print(f"expected winners:{expected_winners}")
        print(f"parsed winners:{win}")
