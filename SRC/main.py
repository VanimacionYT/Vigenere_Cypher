import time
from variables import *

def CreateFormats():
    #Creates the value Repetition based in a division of (Lenght of the original text / Lenght of the Keyword) (minus 1 to avoid an extra repetition)
    repetition = int((round(len(plaintext)/len(plaintextkeyword), 0)) - 1)

    #Using 2 for loops it appends to the Fkeyword the letters of the original keyword to match the lenght of the original text
    """
    First loop uses the created variable (repetition) to represent the general word
    Second loop uses the lenght of the original plaintext to appen every songle letter."""
    for x in range(repetition):
        for x in range(len(formatplaintextkeyword)):
            formatplaintextkeyword.append(formatplaintextkeyword[x])

    #Creates the value Repetition based in the difference (-) of the lenght between the Fkeyword and the Ftext
    repetition = int(round(len(formatplaintextkeyword) - len(formatplaintext), 0))

    #If there was a difference in the lengh between the Fkeyword and the Ftext, the loop eliminates the necesary exceeding letters
    for x in range(repetition):
        formatplaintextkeyword.pop()
    
    #This for loop saves special characters in a dictionary (position / character)
    for x in range(len(formatplaintext)):
        if formatplaintext[x].isalpha() == False:
            print(f"False = {x}")
            formatplaintextspecial[x] = formatplaintext[x]
    
    #This for loop deletes the extra special characters using the dictionary
    for x in formatplaintextspecial:
        print(x)


def CreateAlphabet():
    #The first option is to create a normal Vigenere alphabet, using the standart 26 letters
    if alphabettype == "normal":
        """
        The for loop selects the character to move (chartomove) in the original alphabet (alphabet) and saves it in a variable (chartomove).
        After that it storages the alphabet string in a list (formatalphabet)
        Using Pop, the first letter (chartomove) is deleted
        Finally, using append, that letter (chartomove) is storaged at the end"""
        for x in range(len(alphabet)):
            formatalphabet.append(alphabet[:])
            print(f"{formatalphabet[x]}")
            chartomove = alphabet[0]
            alphabet.pop(0)
            alphabet.append(chartomove)
            time.sleep(0.02)

    #The second option is there to create a Vigenere alphabet with a key word. The keyword can't have double letters
    elif alphabettype == "keyed":
        """
        The for loop checks that the alphabet keyword doesen't have any dupples.
        The check value is used in the search of dupplicated letters."""
        check = []
        try:
            for x in formatalphabetkeyword:
                if x in check: raise ValueError
                check.append(x)
        except:
            print("Error!")
            exit(0)
        """
        The for loop selects the letters from the alphabetkeyword and shuffles them into the first positions"""
        for x in range(len(alphabetkeyword)):
            chartomove = alphabetkeyword[x]
            alphabet.pop(alphabet.index(chartomove))
            alphabet.insert(x, chartomove)
            
        """
        The for loop selects the character to move (chartomove) in the original alphabet (alphabet) and saves it in a variable (chartomove).
        After that it storages the alphabet string in a list (formatalphabet)
        Using Pop, the first letter (chartomove) is deleted
        Finally, using append, that letter (chartomove) is storaged at the end"""
        for x in range(len(alphabet)):
            formatalphabet.append(alphabet[:])
            print(f"{formatalphabet[x]}")
            chartomove = alphabet[0]
            alphabet.pop(0)
            alphabet.append(chartomove)
            time.sleep(0.02)

def SearchLetters():
    for x in range(formatalphabet):
        pass

CreateFormats()
CreateAlphabet()

print(f"\n{formatplaintext}\n{formatplaintextkeyword}\n{formatplaintextspecial}\n")