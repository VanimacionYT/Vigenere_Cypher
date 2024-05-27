import time, getpass, os
from variables import *

def CreateFormats():
    #Creates the value "Repetition" based in a division of (Lenght of the original text / Lenght of the Keyword) (minus 1 to avoid an extra repetition)
    repetition = int((round(len(plaintext)/len(plaintextkeyword), 0)) - 1)

    #Using 2 for loops it creates Fplaintextkeyword by appending individual letters form the original plaintextkeyword
        #First loop uses the created variable (repetition) to represent the general word 
        #Second loop uses the lenght of the original plaintext to appen every songle letter
    for x in range(repetition):
        for x in range(len(formatplaintextkeyword)):
            formatplaintextkeyword.append(formatplaintextkeyword[x])
    
    #This for loop saves special characters, not alphabetical, in a dictionary (position / character) for later removal on the cypher proces and future addon for the final cyher text
    for x in range(len(formatplaintext)):
        if formatplaintext[x].isalpha() == False:
            formatplaintextspecial[x] = formatplaintext[x]
    
    #The first loop deletes special characters from the original Fplaintext in reversed order
    for x in reversed(formatplaintextspecial):
        formatplaintext.pop(x)
    
    #Creates the value "Repetition" based in the difference (-) of the lenght between the Fkeyword and the Ftext (It shows the exceeding letters on Fplaintextkeyword)
    repetition = int(round(len(formatplaintextkeyword) - len(formatplaintext), 0))

    #If there was a difference in the lengh between the Fkeyword and the Ftext, the loop eliminates the necesary exceeding letters
    for x in range(repetition):
        formatplaintextkeyword.pop()

def CreateAlphabet():
    #The first option is to create a normal Vigenere alphabet, using the standart 26 letters
    if alphabettype == "normal":
        #The for loop selects the character to move (chartomove) in the original alphabet (alphabet) and saves it in a variable (chartomove)
        #After that it storages the alphabet string in a list (formatalphabet)
        #Using Pop, the first letter (chartomove) is deleted
        #Finally, using append, that letter (chartomove) is storaged at the end
        for x in range(len(alphabet)):
            formatalphabet.append(alphabet[:])
            print(f"{formatalphabet[x]}")
            chartomove = alphabet[0]
            alphabet.pop(0)
            alphabet.append(chartomove)
            time.sleep(0.02)

    #The second option is there to create a Vigenere alphabet with a key word. The keyword can't have double letters
    elif alphabettype == "keyed":
        
        #The for loop checks that the alphabet keyword doesen't have any dupples
        #The check value is used in the search of dupplicated letters
        check = []
        try:
            for x in formatalphabetkeyword:
                if x in check: raise ValueError
                check.append(x)
        except:
            print("Error!")
            exit(0)
        
        #The for loop selects the letters from the alphabetkeyword and shuffles them into the first positions
        for x in range(len(alphabetkeyword)):
            chartomove = alphabetkeyword[x]
            alphabet.pop(alphabet.index(chartomove))
            alphabet.insert(x, chartomove)
            
        #The for loop selects the character to move (chartomove) in the original alphabet (alphabet) and saves it in a variable (chartomove).
        #After that it storages the alphabet string in a list (formatalphabet)
        #Using Pop, the first letter (chartomove) is deleted
        #Finally, using append, that letter (chartomove) is storaged at the end
        for x in range(len(alphabet)):
            formatalphabet.append(alphabet[:])
            print(f"{formatalphabet[x]}")
            chartomove = alphabet[0]
            alphabet.pop(0)
            alphabet.append(chartomove)
            time.sleep(0.02)

def CypherText():
    #The first for loop uses the lenght of the Fplaintext to store the horizontal (Fplaintext) and vertical (Fplaintextkeyword) letter to search in the Falphabet
    #The second for loop uses if conditions to replace the letter for it's corresponding numerical coordinate
    #Finnaly on the first for loop the two numerical coordinates are used to store the corresponding cyphered letter in Fcyphertext
    for longitudec in range(len(formatplaintext)):    
        horizontalletter = formatplaintext[longitudec]
        verticalletter = formatplaintextkeyword[longitudec]
        for x in range(len(formatalphabet)):
            if formatalphabet[0][x] == horizontalletter:
                horizontalletter = x
            if formatalphabet[0][x] == verticalletter:
                verticalletter = x
        formatcyphertext.append(formatalphabet[verticalletter][horizontalletter])

def ShowResults():
    print(f"\nFormat Plain Text - \t\t{formatplaintext}\nFormat Plain Text Keyword - \t{formatplaintextkeyword}\nFormat Cyphered Text - \t\t{formatcyphertext}\n")

#---WIP---#
def Cypher():
    alphabettype = getpass.getpass("[-    Alphabet Type    -]\n\t1) Normal  -->  (a,b,c,d,e,f,g...)\n\t2) Keyed  -->  (w,o,r,d,a,b,c,e...)")
    if alphabettype == "1":
        alphabettype = "normal"
    elif alphabettype == "2":
        alphabettype = "keyed"
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Wrong Option")
        time.sleep(3)