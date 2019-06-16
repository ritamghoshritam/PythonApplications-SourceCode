alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3
newMessage = ''

message = input('please enter a message: ')

for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position + key) % 26
        newCharacter = alphabet[newPosition]
        #print('The new character is:', newCharacter)
        newMessage += newCharacter
    else:
        newMessage += character
        
print('Your new message is', newMessage)
