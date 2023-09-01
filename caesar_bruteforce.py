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
    print('ceasar cipher key brute force using python')

banner()
print('\n')

text = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
user_message = str(input('Enter MESSAGE >> '))
for key in range(len(text)):
    output = ''
    for symbol in user_message:
        if symbol in text:
            dec_symbol_index = text.find(symbol) - key
            if dec_symbol_index<0:
                dec_symbol_index = dec_symbol_index + len(text)
            deciphered = text[dec_symbol_index]
            output = output + deciphered
        else:
            output = output + symbol
    print(f"key: #%d, Output: %s" %(key,output))
    