import numpy as np
import re

def get_first_last_digits_from_word(word:str) -> list:
    num_list = [x for x in list(word) if x.isnumeric()]
    return num_list[0] + num_list[-1] 

def convert_list_to_number(l:list) -> int:
    return int(''.join(l))

def replace_string_with_digit(word:str) -> str:
    digit_names = {
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9'
    }

    found_digits = {}
    temp_word = word

    for k in digit_names.keys():
        if k in word:
            i = [m.start() for m in re.finditer(f'(?={k})', word)]
            found_digits[digit_names[k]]= i

    for k,v in found_digits.items():
        for occur in v:
            temp_word = temp_word[:occur] + k + temp_word[occur+1:]

    return temp_word


def part1(data:np.array) -> None:
    result = []

    for word in data:
        digits = get_first_last_digits_from_word(word)
        result.append(convert_list_to_number(digits))
    print(sum(result))



def part2(data):
    result = []

    for word in data:
        new_word = replace_string_with_digit(word.lower())
        num = get_first_last_digits_from_word(new_word)
        result.append(convert_list_to_number(num))

    print(sum(result))

if __name__ == "__main__":
    data = np.loadtxt('day1/day1_input.txt',dtype=str)
    
    part1(data)
    part2(data)