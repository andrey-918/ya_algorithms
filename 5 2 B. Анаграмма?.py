def get_word_count(word):
    word_count = {}
    for letter in word:
        if letter not in word_count:
            word_count[letter] = 0
        word_count[letter] += 1
    return word_count

first_word = input()
second_word = input()
print( 'YES' if get_word_count(first_word) == get_word_count(second_word) else 'NO' )
