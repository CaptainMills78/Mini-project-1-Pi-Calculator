print("hello world")


def secret1(word):
    word = word + "abcdefghijklmnoprstuvwxyz"
    grid1 = ""
    for x in range(len(word)):
        if word[x] not in grid1:
            grid1 = grid1 + word[x]
    return grid1


def secret2(word):
    word = word + "abcdefghikjlmnoprstuvwxyz"
    grid2 = ""
    reverse = ""
    for x in range(len(word)):
        if word[x] not in reverse:
            reverse = reverse + word[x]
    for x in range(1, len(reverse)+1):
        grid2 = grid2 + reverse[-1 * x]
    return grid2

# Main code


grid1st = secret1(input("Please enter the first secret word:"))
grid2nd = secret2(input("Please enter the 2nd word"))