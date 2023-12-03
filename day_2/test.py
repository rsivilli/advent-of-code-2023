from solution_part1 import parse_game
from solution_part2 import parse_game as parse_game2

TEST_CASES = [
("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",True,1),
("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",True,2),
("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",False,3),
("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",False,4),
("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",True,5)
]


for test_input,expected_valid, expected_id in TEST_CASES:

    game_id, valid = parse_game(test_input)
    assert game_id == expected_id
    assert valid == expected_valid

TEST_CASES_2 = [
("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",48),
("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",12),
("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",1560),
("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",630),
("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",36)
]

for test_input, expected_sum in TEST_CASES_2:

    val= parse_game2(test_input)
    try:
        assert val == expected_sum
    except AssertionError as e:
        print(f"Expected {expected_sum}")
        print(f"Calculated {val}")
