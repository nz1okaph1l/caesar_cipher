## Caesar Cipher
Caesar cipher, which is named after `Julius Caesar` who used it 2000 years ago works by substituting each letter of a message with a new letter after shifting the alphabet over. For example, Julius Caesar substituted letters in his messages by shifting the letters in the alphabet down by three, and then replacing every letter with the letters in his shifted alphabet.

For example, every `A` in the message would be replaced by a `D`, every `B` would be an `E`, and so on. When Caesar needed to shift letters at the end of the alphabet, such as `Y`, he would wrap around to the beginning of the alphabet and shift three places to `B`.

Doing the same in python, we all the possible characters in a constant variable:
```python
text = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
``` 
And then take in the cipher, the message and mode from the user.
```python
cipher_key = int(input('Enter KEY >> '))
user_message = str(input('Enter MESSAGE >> '))
print('Choose mode:')
print('a. encrypt')
print('b. decrypt')
mode  = str(input('Enter MODE >> '))
```

We then loop through the user message that you want to encrypt. for evey symbol in the user message we check whether it exists in our defined characters, if it does, we check its index, then add or subtract the key to it to get the new index of our encrypted or decrypted character, depending on whether we want to encrypt or decrypt respectively and then append our character in a `output` variable. When it is done looping, the final result is returned to the program by the function.
```python
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
```

![image](/img/caesar.png)

## Caesar Cipher key Brute force
This works similar as the decryption, the only difference is that in this, we dont know the `key` used to encypt the message. So we have to brute force it by trying all every key to the length of the string of characters and symbols used.

![image](/img/caesar_brute.png)