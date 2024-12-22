import sys
import re

I = list(map(str.strip, sys.stdin.readlines()))

def has_three_wovels(s):
    return len(re.findall("[aeiou]", s)) >= 3

def has_repeating_letter(s):
    for i in range(len(s)-1):
        if s[i+1] == s[i]:
            return True

    return False

def does_not_have_special_two(s):
    return not re.search("ab|cd|pq|xy", s)

def is_nice(s):
    return has_three_wovels(s) and has_repeating_letter(s) and does_not_have_special_two(s)

print("part1", len([i for i in I if is_nice(i)]))

def has_repeating_pair(s):
    for i in range(len(s)-3):
        if s[i:i+2] in s[i+2:]:
            return True

    return False

def has_repeating_letter_with_sep(s):
    for i in range(len(s)-2):
        if s[i] == s[i+2]:
            return True

    return False

def is_nice2(s):
    return has_repeating_pair(s) and has_repeating_letter_with_sep(s)

assert is_nice2("qjhvhtzxzqqjkmpb")
assert not is_nice2("uurcxstgmygtbstg")
assert not is_nice2("ieodomkazucvgmuy")

print("part2", len([i for i in I if is_nice2(i)]))