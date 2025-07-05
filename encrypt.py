def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Keep case
            offset = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            # Leave other characters unchanged
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("=== Caesar Cipher ===")
    choice = input("Choose an option (encrypt/decrypt): ").lower()

    if choice not in ["encrypt", "decrypt"]:
        print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")
        return

    message = input("Enter your message: ")
    
    try:
        shift = int(input("Enter the shift value (e.g., 3): "))
    except ValueError:
        print("Shift value must be an integer.")
        return

    if choice == "encrypt":
        result = caesar_encrypt(message, shift)
        print(f"\n🔒 Encrypted Message: {result}")
    else:
        result = caesar_decrypt(message, shift)
        print(f"\n🔓 Decrypted Message: {result}")

if __name__ == "__main__":
    main()
