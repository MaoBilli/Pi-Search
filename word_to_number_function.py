def word_to_digits(word):
    result = ""
    for letter in word:
        if letter.isalpha():
            place = ord(letter.upper()) - 64
            result += str(place)
    return result