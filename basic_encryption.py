import random
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
stored_keys = []
session_number = 0

while True: 
    session_number+=1
    option = input('Please choose function: (encrypt/decrypt) \n')
    if option.lower() == 'encrypt':
        user_message = input('Please enter your message: ')

        key = random.randint(0, 100)
        stored_keys.append(key)
        output_string = ''
        
        for letter in user_message:
            ascii_number = ord(letter)
            ascii_constant = 0
            #check if capital or normal or neither
            if 65 <= ascii_number <= 90:
                ascii_constant = 65
            elif 97 <= ascii_number <= 122:
                ascii_constant = 97

            position = ascii_number - ascii_constant
            new_position = (position + key) % 26
            new_letter = chr(ascii_constant + new_position)
            output_string += new_letter

        print(f'The session number is {session_number} and the encrypted message is {output_string}')
    elif option.lower() == 'decrypt':
        input_session = int(input('Please enter your session number: '))
        user_message = input('Please enter your message: ')

        if(len(stored_keys) == 0 or input_session > len(stored_keys)):
            print('Error cannot find session. \n')
            continue

        key = stored_keys[input_session-1]
        output_string = ''
        
        for letter in user_message:
            ascii_number = ord(letter)
            ascii_constant = 0
            #check if capital or normal or neither
            if 65 <= ascii_number <= 90:
                ascii_constant = 65
            elif 97 <= ascii_number <= 122:
                ascii_constant = 97

            position = ascii_number - ascii_constant
            new_position = (position + (26-key)) % 26
            new_letter = chr(ascii_constant + new_position)
            output_string += new_letter

        print(f'The decrypted message is {output_string}')
    elif option.lower() == 'exit':
        break
    else:
        print('Invalid command \n')