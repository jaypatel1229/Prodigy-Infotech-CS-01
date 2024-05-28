
#Create Python Program that can encrypt and decrypt text using the Casar Cipher algorithm. Allow users to input a message and a shift value to perform encryption and decryption.
def encrypt(text, shift):  # method for encryption which use text and swift text in between 0-25
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted = shifted - 26
                elif shifted < ord('a'):
                    shifted = shifted + 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted = shifted - 26
                elif shifted < ord('A'):
                    shifted = shifted + 26
            encrypted_text = encrypted_text + chr(shifted)
        else:
            encrypted_text = encrypted_text + char
    return encrypted_text

def decrypt(text, shift):   # method for decryption which use text and swift text in between 0-25
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted > ord('z'):
                    shifted = shifted - 26
                elif shifted < ord('a'):
                    shifted = shifted + 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted = shifted - 26
                elif shifted < ord('A'):
                    shifted = shifted + 26
            decrypted_text = decrypted_text + chr(shifted)
        else:
            decrypted_text = decrypted_text +char
    return decrypted_text

def main():     # method for user input text
    while True:
        choice = input("Choose Encryption for E and Decryption for D :  ").strip().upper()
        if choice == 'E':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value (0-25): "))
            encrypted_message = encrypt(message, shift)
            print("Encrypted message:", encrypted_message)
        elif choice == 'D':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value (0-25): "))
            decrypted_message = decrypt(message, shift)
            print("Decrypted message:", decrypted_message)
        else:
            print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")

        cont = input("Do you want to continue? (y/n): ").strip().lower()
        if cont != 'y':
            break


if __name__ == "__main__":
    main()
