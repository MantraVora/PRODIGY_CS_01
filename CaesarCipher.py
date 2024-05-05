def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        choice = input("Enter 'E' to encrypt, 'D' to decrypt, or 'Q' to quit: ").upper()
        if choice == 'Q':
            print("Exiting...")
            break
        elif choice == 'E':
            message = input("Enter message to encrypt: ")
            shift = int(input("Enter shift value: "))
            encrypted_message = encrypt(message, shift)
            print("Encrypted message:", encrypted_message)
        elif choice == 'D':
            message = input("Enter message to decrypt: ")
            shift = int(input("Enter shift value: "))
            decrypted_message = decrypt(message, shift)
            print("Decrypted message:", decrypted_message)
        else:
            print("Invalid choice. Please enter 'E', 'D', or 'Q'.")

if __name__ == "__main__":
    main()
