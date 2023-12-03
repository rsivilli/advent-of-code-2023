from solution_part2 import find_two_digit

tests =[
("two1nine",29),
("eightwothree",83),
("abcone2threexyz",13),
("xtwone3four",24),
("4nineeightseven2",42),
("zoneight234",14),
("7pqrstsixteen",76)
]


for test_input,expected in tests:
    assert find_two_digit(test_input) == expected