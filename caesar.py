import string

SHIFT_DEFAULT = 3

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            shifted_code = (ord(char) - offset + shift) % 26 + offset
            result += chr(shifted_code)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    shift_value = int(input(f"Enter shift value (default {SHIFT_DEFAULT}): ") or SHIFT_DEFAULT)

    with open("password.txt", "r") as infile:
        plain_passwords = infile.read()

    cipher_passwords = encrypt(plain_passwords, shift_value)

    with open("passwords_encrypted.txt", "w") as outfile:
        outfile.write(cipher_passwords)
    print("✓ Passwords encrypted → passwords_encrypted.txt")

    recovered_passwords = decrypt(cipher_passwords, shift_value)

    with open("passwords_decrypted.txt", "w") as verify_file:
        verify_file.write(recovered_passwords)
    print("✓ Passwords decrypted → passwords_decrypted.txt")

if __name__ == "__main__":
    main()
