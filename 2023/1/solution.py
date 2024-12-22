from lib.adventlib import parse_digits, input

print(f'1: {sum(ints[0]*10 + ints[-1] for ints in map(parse_digits, input()))}')

digit_words = {
    'one'  : '1',
    'two'  : '2',
    'three': '3',
    'four' : '4',
    'five' : '5',
    'six'  : '6',
    'seven': '7',
    'eight': '8',
    'nine' : '9'
}

def words_to_digits(l):
    result = ""
    skip_chars = 0

    for i in range(0, len(l)):
        fk = next((k for k in digit_words.keys() if l.startswith(k, i)), None)
        if fk:
            result += digit_words[fk]
            skip_chars = len(fk) 

        if skip_chars:
            skip_chars -= 1  
        else:
            result += l[i]            

    return result

assert words_to_digits("zoneight234") == 'z18234'
assert words_to_digits("one12two") == '1122'

print(f'2: {sum(ints[0]*10 + ints[-1] for ints in map(parse_digits, map(words_to_digits, input())))}')