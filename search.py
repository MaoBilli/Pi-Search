# ---------- load the digits of pi that we saved earlier ----------
with open("my_pi_100m.txt", "r") as f:
    digits = f.read()          # one long string of digits (no "3." at the front)


# ---------- turn a word into digits: A=1, B=2, ... Z=26 ----------
def word_to_digits(word):
    result = ""                              # we build the answer here, a bit at a time
    for letter in word:                      # go through the word one letter at a time
        if letter.isalpha():                 # skip anything that isn't a letter (numbers, !, spaces)
            place = ord(letter.upper()) - 64 # ord("A") is 65, so this gives A=1, B=2, ... Z=26
            result += str(place)             # add the number to the end, as text
    return result


# ---------- setup ----------
wanted = ""        # the digits we will look for
count = 0          # how many times we find them
first_positions = []     # the place of every match

# ---------- ask: number or word? (keeps asking until the answer is valid) ----------
while True:
    choice = input("number or word? ").lower().strip()   # lower() and strip() so "Word " still works
    if choice == "number" or choice == "word":
        break                                            # valid answer, leave the loop
    print("Please type either 'number' or 'word'.")     # not valid, so the loop asks again

# ---------- get what to search for (also keeps asking until valid) ----------
if choice == "number":
    while True:
        wanted = input("What number(s) do you want to search pi for: ").strip()
        if wanted.isdigit():                             # isdigit() is True only if every character is 0-9
            break
        print("Please type digits only (0-9), with no letters or symbols.")
else:  # choice must be "word", because the loop above only lets "number" or "word" through
    while True:
        word = input("What word do you want to search pi for: ")
        wanted = word_to_digits(word)                    # turn the word into digits
        if wanted != "":                                 # empty means there were no letters in it
            break
        print("Please type at least one letter (A-Z).")
    print(f"Searching for the digits: {wanted}")

# ---------- search ----------
position = digits.find(wanted)                           # first match, or -1 if there is none
while position != -1:                                    # keep going until there are no more matches
    count += 1                                           # one more match found
    first_positions.append(position + 1)                       # +1 because find() counts from 0 but people count from 1
    position = digits.find(wanted, position + 1)         # search again, starting one place after this match began
                                                         # (this also catches matches that overlap)

# ---------- show the result ----------
if count == 0:
    print(f"Those digits were not found in the first {len(digits):,} digits of pi")
else:
    print("First found at digit", first_positions[0])
    print(f"There are {count} times where your number(s) have shown up, the first few digit places include {first_positions[:5]}")