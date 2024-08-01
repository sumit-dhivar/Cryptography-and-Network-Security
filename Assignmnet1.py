#Caesar Cipher Python Implementation
def encrypt(text,s):
    result = ""
    # traverse text
    for i in range(len(text)):
        char = text[i]
        
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)

        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result
def decrypt(text,s):
    result = ""
    # traverse text
    for i in range(len(text)):
        char = text[i]
        
        if (char.isupper()):
            result += chr((ord(char) - s-65) % 26 + 65)

        else:
            result += chr((ord(char) - s - 97) % 26 + 97)

    return result
#check the above function
text = input("Enter the text:-")
s = int(input("Enter the key:- "))
cipher = encrypt(text,s)
print ("Text  : " + text)
print ("Shift : " + str(s))
print ("Cipher: " + cipher)
print("Decoded from cipher:- " + decrypt(cipher,s))