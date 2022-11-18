square = [[0, 1, 2, 3, 4, 5],
          [1, "A", "B", "C", "D", "E"],
          [2, "F", "G", "H", "I", "J"],
          [3, "K", "L", "M", "N", "O"],
          [4, "P", "Q", "R", "S", "T"],
          [5, "U", "V", "W", "X", "Y"],
          [6, "Z", "?", " ", "@", "."]]


def display(square):
    for x in range(len(square)):
        row = ""
        for y in range(len(square[x])):
            row += str(square[x][y])
            row += " | "
        print(row)
        print("-----------------------")
    pass


def deCipher(cryptogram):
    cryptogram = cryptogram.replace(" ", "")  # remove spaces
    crypto = cryptogram.split(",")  # split by comma and change converts to a list

    word = ""  # initialise the value of word to empty string

    # .......................... MISSING CODE   ..................................
    #                         Write the missing code
    #
    for n in crypto:
        row = int(n[0])
        column = int(n[1])
        letter = square[row][column]
        word += letter
    return word


def encrypt(plain):
    plain = plain.upper()
    for x in str(plain):
        for y in "ABCDEFGHIJKLMNOPQRSTUVWXYZ? @.":
            if x != y:
                print("The plaintext includes unsupported characters...")
                print("Quitting...")
                import sys
                sys.exit()
            else:
                pass


def main():
    code = input(" Enter Cryptogram (the ciphered message) ...  ")

    print("The Secret word is ... " + deCipher(code))


display(square)
main()
