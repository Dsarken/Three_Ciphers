def vernamecipher(text_message, key):
    binary_string = ""
    binary_key = ""
    ciphertext = ""
    # convert plaintext message to binary
    for letter in text_message:
        binary_char = format(ord(letter), 'b')
        binary_string += binary_char
    # convert key to binary
    for letter in key:
        binary_char = format(ord(letter), 'b')
        binary_key += binary_char
    # repeat the key until its length is equal to the binary_string
    while len(binary_key) < len(binary_string):
        binary_key += binary_key
    # XOR plaintext message and key
    for i in range(len(binary_string)):
        ciphertext += str(int(binary_string[i]) ^ int(binary_key[i]))
    final_ciphertext = ""
    for i in range(0, len(ciphertext), 8):
        final_ciphertext += chr(int(ciphertext[i:i + 8], 2))
    return final_ciphertext


def vigenerecipher(keyphrase, text_message):
    output_string = ""
    for i in range(len(text_message)):
        char = text_message[i]
        key_char = keyphrase[i % len(keyphrase)]
        if char.isalpha():
            char_ascii = ord(char.lower()) - ord('a')
            key_char_ascii = ord(key_char.lower()) - ord('a')
            output_string += chr((char_ascii + key_char_ascii) % 26 + ord('a'))
        else:
            output_string += char
    return output_string


def caesarcipher(text_message, key_choice):
    letters = "abcdefghijklmnopqrstuvwxyz"
    output_message = ""
    for i in text_message:
        if i in letters:
            letter_index = letters.index(i)
            output_message += letters[(letter_index + key_choice) % 26]
        else:
            output_message += i
    return output_message


def main():
    print("Enter your text message")
    text_message = input("> ")
    print("Which cipher do you wish to use?")
    print("1.  Caesar Cipher")
    print("2. Vigenere Cipher")
    print("3. Vernam Cipher")
    choice = int(input("> "))
    if choice == 1:
        key = int(input("Enter a key from 1 to 25: "))
        print(caesarcipher(text_message, key))
    if choice == 2:
        keyphrase = input("Enter a key-phrase: ")
        print(vigenerecipher(keyphrase, text_message))
    if choice == 3:
        key = input("Enter a key")
        print(vernamecipher(text_message, key))


if __name__ == '__main__':
    main()
