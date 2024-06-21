#task1: create a python program that can encrypt and decrypt text using the Caesar cipher algorithm. Allow users to input a message and a shift value to perform encryption and decryption.

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryption(plain_text,shift_key):
    cipher_text=""
    for char in plain_text:
        char = char.lower()
        if char in alphabet:
            position = alphabet.index(char)
            new_position=(position+shift_key)%26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char  
    print(f"Encrypted Message:{cipher_text}")

def decryption(cipher_text,shift_key):
    plain_text=""
    for char in cipher_text:
        char = char.lower()
        if char in alphabet:
            position = alphabet.index(char)
            new_position=(position-shift_key)%26
            plain_text += alphabet[new_position]
        else:
            plain_text += char
    print(f"decrypted Message:{plain_text}")

flag=False
while not flag:
    Enc_Dec= input("Type 'Encrypt' for encryption, type 'Decrypt' for decryption:\n").lower()
    Input_message=input("Type your message:\n").lower()
    Shift_value=int(input("Enter the Shift Value:\n"))
    if Enc_Dec=="encrypt":
        encryption(plain_text=Input_message, shift_key=Shift_value)
    elif Enc_Dec=="decrypt":
        decryption(Input_message,Shift_value)
    
    wanna_play=input("Type 'yes' to continue, type 'no' to exit: ").lower()
    if wanna_play == 'no':
        flag = True
        print("Program end..")
