#Version 1 (victor)
'''
from math import log

def shannon_entropy(text: str):
    text = text.lower()
    probs = [text.count(c) / len(text) for c in set(text)]
    entropy = -sum([p * log(p) / log(2.0) for p in probs])
    return entropy

input_usuario=input("Introduce password: ")
entropy_value = shannon_entropy(input_usuario)
print('Valor de entropía = ', entropy_value)
'''

#Version 2 (github)
'''
import math


def calculate(length, char_amount):
    return math.log2(char_amount) * length


def find_chars(password):
    char_amount = 0
    char_sets = [False, False, False, False]
    char_nums = [26, 26, 10, 32]
    for i in password:
        if i.islower():
            char_sets[0] = True
        if i.isupper():
            char_sets[1] = True
        if i.isdigit():
            char_sets[2] = True
        if not i.isalnum() and i.isascii():
            char_sets[3] = True

    for x in range(4):
        if char_sets[x]:
            char_amount += char_nums[x]

    return len(password), char_amount


if __name__ == "__main__":
    password = input("Enter A Password: ")
    length, amount = find_chars(password)
    print("Entropy: ", calculate(length, amount))
'''

#Version 3 (chatgpt)
import math
from collections import Counter

def calculate_entropy(length, char_set_size):
    if char_set_size == 0:
        return 0
    return math.log2(char_set_size) * length

def find_char_set_size(password):
    char_set_size = 0
    char_sets = [False, False, False, False]  # Lowercase, Uppercase, Digits, Special characters
    char_nums = [26, 26, 10, 32]  # Size of each character set

    for char in password:
        if char.islower():
            char_sets[0] = True
        elif char.isupper():
            char_sets[1] = True
        elif char.isdigit():
            char_sets[2] = True
        elif not char.isalnum() and char.isascii():
            char_sets[3] = True

    for idx, char_set in enumerate(char_sets):
        if char_set:
            char_set_size += char_nums[idx]

    return len(password), char_set_size

def shannon_entropy(password):
    if not password:
        return 0
    count = Counter(password)
    length = len(password)
    probs = [freq / length for freq in count.values()]
    entropy = -sum(p * math.log2(p) for p in probs)
    return entropy
