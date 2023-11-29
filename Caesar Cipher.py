print ('''This program is a simple Caesar Cipher that will Encrypt and  
Decrypt a message, there is also an option for the user to learn how a 
Caesar Cipher works and also learn some history about the Cipher''')

# Below is a string that contains each letter of the alphabet.
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while True:
    print('Would you like to (e)ncrypt or (d)ecrypt a message')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif responce.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d.')