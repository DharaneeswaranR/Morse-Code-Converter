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
    
    decrypted_text = ""

    try:
        for char in text:
            if char in morseDict.keys():
                decrypted_text += morseDict[char] + ' '
            else:
                decrypted_text += '/ '
            
    except:
        pass

    return decrypted_text

def decrypt(code):
    morseDict = {
                    '.-':'A', 
                    '-...':'B',
                    '-.-.':'C',
                    '-..':'D', 
                    '.':'E',
                    '..-.':'F', 
                    '--.':'G', 
                    '....':'H',
                    '..':'I', 
                    '.---':'J', 
                    '-.-':'K',
                    '.-..':'L', 
                    '--':'M', 
                    '-.':'N',
                    '---':'O', 
                    '.--.':'P', 
                    '--.-':'Q',
                    '.-.':'R', 
                    '...':'S', 
                    '-':'T',
                    '..-':'U', 
                    '...-':'V', 
                    '.--':'W',
                    '-..-':'X', 
                    '-.--':'Y', 
                    '--..':'Z',                                        
                    '----.':'1',                    
                    '---..':'2',                    
                    '--...':'3',                    
                    '-....':'4',                    
                    '.....':'5',                    
                    '....-':'6',                    
                    '...--':'7',                   
                    '..---':'8',                   
                    '.----':'9',                   
                    '-----':'0',                    
                    '--..--':',',                    
                    '-.-.-.':'.',                    
                    '..--..':'?',                    
                    '.-..-':'/',                   
                    '-....-':'-',                    
                    '.--.-':'(',                    
                    '-.--.-':')',  
                }
    
    decrypted_text = ""

    code_list = code.split(" ")

    for char in code_list:
        if char in morseDict.keys():
            decrypted_text += morseDict[char]
        else:
            decrypted_text += ' '

    return decrypted_text

def main():
    print("\n########################### MORSE CODE ###########################")
    
    choice = True

    while choice:
        print("\nConvert to:\n1. Text to Morse code\n2. Morse code to text")
        oper = input("\nEnter choice(1 or 2)\n>> ")

        if oper == '1':
            text = input("\nEnter text to be converted into Morse code\n>> ")
            print("\nMorse code\n>> ", encrypt(text))
        elif oper == '2':
            text = input("\nEnter Morse code to be converted into text\n>> ")
            print("\nMorse code\n>> ", decrypt(text))
        else:
            print("Operation unavailable. Enter 1 or 2 only.")

        print("\nDo you want to try again? (Y/N)")

        choice = True if input(">> ") in ('Yes', 'YES', 'yes', 'Y', 'y') else False

    print("\n########################## THANK YOU! ###########################\n")

if __name__ == '__main__':
    main()
            
    