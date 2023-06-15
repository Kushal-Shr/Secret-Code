## RULES...

#Translate a message into a secret code language. Use the rules below to translate.

#Coding:
#- If the word contains atleast 3 characters, remove the first letter and append it at the end.
#- Now append first three charaters at the end and last three characters at the start
#- If the word is lesser than 3 then reverse the string

#Decoding:
#- If the word contains less than 3 characters, reverse it
#- Else remove 3 random charaters from start and end. Now remove the last letter and append it to the begining

#Your Program should ask whether you want to code or decode

# PROGRAM...

print('\n---Welcome to Secret Code Generator and Decoder___\n')

while True:

    print('Select:\n1 --> Generating a secret code\n2 --> Decoding a secret code\n3 --> Exit\n')

    choice = int(input('Enter your choice 1 or 2 or 3 :'))

    if choice == 1:
        secret_code_lst = []
        print('\nLet\'s start generating a secret code...\n')
        sentence = input('Enter a phrase you want you transform into a secret code :')

        words = sentence.split()

        for word in words:

            if len(word) >= 3:
                coded_word = word[-3 : len(word)] + word[1 : ] + word[0] + word[ : 3]

                secret_code_lst.append(coded_word)

            else:
                coded_word = word[ : : -1]

                secret_code_lst.append(coded_word)

        secret_code = ' '.join(secret_code_lst)
        print(f'Secret Code : {secret_code}\n')

    elif choice == 2:

        real_phrase = []
        coded_phrase = input('\nEnter the secret code needed to be decoded :')
        words = coded_phrase.split()

        for word in words:
            if len(word) < 3:
                real_word = word[ : : -1]

                real_phrase.append(real_word)

            else:
                real_word = word[-4] + word[3 : -4]

                real_phrase.append(real_word)

        decoded_phrase = ' '.join(real_phrase)
        print(f'The decoded phrase is : {decoded_phrase}\n')

    else:
        print('Thanks...')
        break