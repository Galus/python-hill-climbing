#!/usr/bin/env python3

import sys
import random
from collections import Counter
from string import ascii_lowercase, ascii_uppercase
from consts import (
    ENGLISH_LETTERS_BY_FREQUENCY,
    ENGLISH_LETTER_FREQUENCIES as target_freq
)

# return a=0 b=1 c=2 ... z=26
def alpha2position(english_letter, offset=0):
    return ord(english_letter) - 97 + offset

def fitness(plaintext):
    # calc fitness
    score = 1
    return score

def get_frequency(string,character):
    counts = Counter(string)
    return counts[character]/len(string)

def get_frequency_score(string, debug=False):
    total_score = 0
    freqs = {}
    scores = {}
    for char in string:
        if char not in freqs:
            char_freq = get_frequency(string, char)
            freqs[char] = char_freq
            char_score = abs(char_freq - target_freq[char])
            total_score += char_score
            scores[char] = char_score
    if debug:
        print("char\ttarget freq\t\tactual freq\t\tscore")
        for char,freq in freqs.items():
            print(f"{char}\t{target_freq[char]}\t\t{freq}\t\t{scores[char]}")
    return total_score, scores

def climb(F, x):
    resp = F(x)

def substitute(text,alphabet,key):
    if len(alphabet) is not len(key):
        exit(f"alphabet-key length mismatch: alphabet \"{len(alphabet)}\" must match length of key \"{len(key)}\"")
    plaintext = ""
    lut = dict(zip(alphabet,key))
    for character in text:
        plaintext += lut[character]
    return plaintext

def main(args):
    if len(args) < 3:
        exit("needs ciphertext, alphabet, and key args")
    ciphertext = args[0]
    alphabet = args[1]
    key = args[2]
    capitals = [ letter.isupper() for letter in ciphertext ]

    plaintext = substitute(ciphertext, alphabet, key)
    print(f"{plaintext=}")

    score, scores = get_frequency_score(plaintext, True)
    print(score)

    sorted_scores = sorted(scores.items(), key=lambda x:-x[1])
    print(sorted_scores)

    i = 0
    while i < 0:
        key = random.sample(set(ascii_lowercase),26)
        climb(print,["Calc fit",i, ''.join(key)])
        i+=1

if __name__ == "__main__":
    print(alpha2position('a'))
    print(alpha2position('b'))
    main(sys.argv[1:])
