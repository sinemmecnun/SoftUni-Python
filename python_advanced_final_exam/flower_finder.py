from collections import deque

vowels = deque(input().split())
consonants = input().split()

words_to_search = ['rose', 'tulip', 'lotus', 'daffodil']
found_words = words_to_search.copy()
word_found = False

while vowels and consonants:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()
    i = 0
    while True:
        if current_vowel in words_to_search[i]:
            words_to_search[i] = words_to_search[i].replace(current_vowel, '')
        if current_consonant in words_to_search[i]:
            words_to_search[i] = words_to_search[i].replace(current_consonant, '')
        for word in words_to_search:
            if word == '':
                word_found = True
                break
        if word_found:
            break
        i += 1
        if i >= len(words_to_search):
            break

    if word_found:
        break
if word_found:
    for i in range(len(words_to_search)):
        if words_to_search[i] == '':
            print(f"Word found: {found_words[i]}")
            break

else:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")