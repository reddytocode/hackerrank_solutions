def minion_game(string):
    kevin, stuart= 0, 0
    vowels = "AEIOU"
    lenght = len(string)

    for index, letter in enumerate(string):
        if letter in vowels:
            kevin += (length - index)
        else:
            stuart += (length - index)

    if kevin == stuart:
        print("Draw")
    elif kevin > stuart:
        print("Kevin", kevin)
    else:
        print("Stuart", stuart)


# Stuart 12
# Kevin 9

minion_game("BANANA")
