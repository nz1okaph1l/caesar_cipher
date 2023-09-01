#!/usr/bin/env python3
#Author: pr0rat
#Usage: python3 ceasar.py

# Creating a banner
def banner():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~   #######   ##   ######  #####    ##   #####      #######  # #####  #    # ###### #####  ~')
    print('~  #         #  #  #      #        #  #  #    #    #         # #    # #    # #      #    # ~')
    print('~ #         ###### ###     #####  ###### #####    #          # #####  ###### ####   #####  ~')
    print('~  #        #    # #            # #    # #   #     #       # # #      #    # #      #   #  ~')
    print('~   ####### #    # ######  #####  #    # #    #     #######  # #      #    # ###### #    # ~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    
    print('AUTHOR: pr0rat')
    print('Ceasar cipher encryption')
    print('This is a simple example of how to implement the')
    print('ceasar cipher cryptographic encryption using python')

banner()
print('\n')

# Taking the two inputs from the user
text = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
cipher_key = int(input('Enter KEY >> '))
user_message = str(input('Enter MESSAGE >> '))
print('Choose mode:')
print('a. encrypt')
print('b. decrypt')
mode  = str(input('Enter MODE >> '))
# Creating the function that will do the encryption
def message_encrypter(user_data,cipher_key,text):
    output = ''
    for symbol in user_data:
        if symbol in text:
            symbol_index = text.find(symbol)
            if mode == 'a':
                enc_symbol_index = symbol_index + cipher_key
                if enc_symbol_index >= len(text):
                    enc_symbol_index = enc_symbol_index - len(text)
                cipher_text = text[enc_symbol_index]
            elif mode == 'b':
                enc_symbol_index = symbol_index - cipher_key
                if enc_symbol_index <=0:
                    enc_symbol_index = enc_symbol_index + len(text)
                cipher_text = text[enc_symbol_index]
        else:
            cipher_text =  symbol            
        output += cipher_text
    return output

if __name__ == __name__:
    print('Your encrypted message: '+ str(message_encrypter(user_message, cipher_key,text)))