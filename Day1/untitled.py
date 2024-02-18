import os
import re

input_path = os.path.join(os.path.dirname(__file__), "Day1-input.txt")
input_file = open(input_path, "r")
file_lines = input_file.readlines()
result = 0

RE_PATTERN = r"\d|one|two|three|four|five|six|seven|eight|nine"
replace_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


for line in file_lines:
    digits = []
    matched_digit = re.search(RE_PATTERN, line)
    while matched_digit:
        digits.append(matched_digit.group())
        next_start = matched_digit.start() + 1
        line = line[next_start:]
        matched_digit = re.search(RE_PATTERN, line)
    digits = [
        replace_dict[digit] if digit in replace_dict else digit for digit in digits
    ]
    result = result + int(digits[0] + digits[-1])

print("result", result)