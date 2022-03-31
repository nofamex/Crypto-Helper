
#A python program to illustrate Caesar Cipher Technique
def encrypt(text,s):
    result = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    return result

def find_key(message):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for key in range(len(LETTERS)):
        translated = ''
        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                translated = translated + LETTERS[num]
            else:
                translated = translated + symbol
        print('Hacking key #%s: %s' % (key, translated))

def decrypt(message, key):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    translated = ''
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key
            if num < 0:
                num = num + len(LETTERS)
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol
    print('Hacking key #%s: %s' % (key, translated))
 
#check the above function
text = input("text: ")
met = input("Method (enc/hack/dec): ")

if met == "enc":
    key = int(input("key: "))
    print(encrypt(text.replace(" ", ""), key))
elif met == "dec":
    key = int(input("key: "))
    decrypt(text.replace(" ", ""), key)
else:
    find_key(text.replace(" ", ""))