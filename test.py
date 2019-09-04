output = ""
secret_word = "Salami"
letters_guessed = ["a", "p", "s", "i"]
for letter in secret_word:
    if letter in letters_guessed:
        output += letter
    else:
        output += "_"
print(output)


# find_letter_indexes("xdskhfdsjxjdksfhsdkjfxkejwhrkejxj", "x")
