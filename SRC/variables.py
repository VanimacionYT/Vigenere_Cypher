#################
#   VARIABLES   #
#################

#Default Alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
#Alphabet After Formatting
formatalphabet = []
#The Alphabet Type
alphabettype = "normal" #normal or keyed
#In Case Of Keyed Alphabet This Is The Keyed Word
alphabetkeyword = ""
#Alphabet Keyword After Formatting
formatalphabetkeyword = list(alphabetkeyword)
#Text To Chypher
plaintext = ""
#Text To Chypher After Formatting
formatplaintext = list(plaintext)
#Dictionary that stores special characters in the format plain text (position : character)
formatplaintextspecial = {}
#Word Used As Password To Cypher The Plain Text Using The Vigenere Alphabet
plaintextkeyword = ""
#Word Password After Formatting
formatplaintextkeyword = list(plaintextkeyword)
#Cyphered Text in formatting
formatcyphertext = []