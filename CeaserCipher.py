def ceaser(input_text):
    shift_pattern = 3
    cipher_result = " "

    for each_char in input_text:
        if each_char == " ":
            cipher_result = cipher_result + each_char
        elif each_char.isupper():
            cipher_result = cipher_result + chr(((ord(each_char)+ shift_pattern - 65) % 26) + 65)
        else:
            cipher_result = cipher_result + chr(((ord(each_char)+ shift_pattern - 97) % 26) + 97)
    return cipher_result

input_text = input("Enter text to be encrypted: ")
encrypted_text = ceaser(input_text)
print(f"The encrypted text is {encrypted_text}\n")