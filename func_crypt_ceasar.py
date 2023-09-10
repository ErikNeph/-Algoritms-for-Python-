def ceasar():
    alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    stringToEncrypt = input('Please enter a message to encrypt: ')
    shiftAmout = int(input('Please enter a whole number from 1-25 to be your key.'))
    encryptedString = ''
    for currentCharacter in stringToEncrypt:
        position = alphabet.find(currentCharacter)
        newPosition = position + shiftAmout
        if currentCharacter in alphabet:
            encryptedString += alphabet[newPosition]
        else:
            encryptedString += currentCharacter
    print('Your encrypted message is:', encryptedString)


ceasar()
