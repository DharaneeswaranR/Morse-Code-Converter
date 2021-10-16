def encrypt(text):
    morseDict = {
                    'A':'.-', 
                    'B':'-...',
                    'C':'-.-.',
                    'D':'-..', 
                    'E':'.',
                    'F':'..-.', 
                    'G':'--.', 
                    'H':'....',
                    'I':'..', 
                    'J':'.---', 
                    'K':'-.-',
                    'L':'.-..', 
                    'M':'--', 
                    'N':'-.',
                    'O':'---', 
                    'P':'.--.', 
                    'Q':'--.-',
                    'R':'.-.', 
                    'S':'...', 
                    'T':'-',
                    'U':'..-', 
                    'V':'...-', 
                    'W':'.--',
                    'X':'-..-', 
                    'Y':'-.--', 
                    'Z':'--..',
                    'a':'.-', 
                    'b':'-...',
                    'c':'-.-.',
                    'd':'-..', 
                    'e':'.',
                    'f':'..-.', 
                    'g':'--.', 
                    'h':'....',
                    'i':'..', 
                    'j':'.---', 
                    'k':'-.-',
                    'l':'.-..', 
                    'm':'--', 
                    'n':'-.',
                    'o':'---', 
                    'p':'.--.', 
                    'q':'--.-',
                    'r':'.-.', 
                    's':'...', 
                    't':'-',
                    'u':'..-', 
                    'v':'...-', 
                    'w':'.--',
                    'x':'-..-', 
                    'y':'-.--', 
                    'z':'--..',
                    '1':'.----', 
                    '2':'..---', 
                    '3':'...--',
                    '4':'....-', 
                    '5':'.....', 
                    '6':'-....',
                    '7':'--...', 
                    '8':'---..', 
                    '9':'----.',
                    '0':'-----', 
                    ',':'--..--', 
                    '.':'.-.-.-',
                    '?':'..--..', 
                    '/':'-..-.', 
                    '-':'-....-',
                    '(':'-.--.', 
                    ')':'-.--.-'
                }
    
    encryted_text = ""

    try:
        for char in text:
            if char in morseDict.keys():
                encryted_text += morseDict[char] + ' '
            else:
                encryted_text += '/'
            
    except:
        pass

    return encryted_text

def main():
    print("\n########################### MORSE CODE ###########################")
    
    choice = True

    while choice:
        text = input("\nEnter text to be converted into Morse code\n>> ")
        print("\nMorse code\n>> ", encrypt(text))

        print("\nDo you want to try again? (Y/N)")

        choice = True if input(">> ") in ('Yes', 'YES', 'yes', 'Y', 'y') else False

    print("\n########################## THANK YOU! ###########################\n")

if __name__ == '__main__':
    main()
            
    