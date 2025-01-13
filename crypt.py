import string
import bcrypt
import getpass
import sys

userData = {
    "username": "admin",
    "password": bcrypt.hashpw("admin".encode(), bcrypt.gensalt())
}

def createCipherAlphabet(keyword):
    keyword = "".join(sorted(set(keyword), key=keyword.index))
    alphabet = string.ascii_lowercase
    cipherAlphabet = keyword + ''.join([char for char in alphabet if char not in keyword])
    return cipherAlphabet

def encrypt(plaintext, keyword):
    alphabet = string.ascii_lowercase
    cipherAlphabet = createCipherAlphabet(keyword)
    encryptedText = ''.join([cipherAlphabet[alphabet.index(char)] if char in alphabet else char for char in plaintext.lower()])
    return encryptedText   

def decrypt(ciphertext, keyword):
    alphabet = string.ascii_lowercase
    cipherAlphabet = createCipherAlphabet(keyword)
    decryptedText = ''.join([alphabet[cipherAlphabet.index(char)] if char in cipherAlphabet else char for char in ciphertext.lower()])
    return decryptedText

def authenticateUser():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    if username == userData["username"] and bcrypt.checkpw(password.encode(), userData["password"]):
        return True
    else:
        return False

def main():
    while True:
        if authenticateUser():
            print("Authentication successful!")
            break
        else:
            while True:
                retry= input("Authentication failed. (R)etry or (Q)uit? ").lower()
                if retry != 'r' and retry != 'q':
                    print("Invalid input.")
                    continue
                elif retry == 'q':
                    sys.exit()
                else:
                    break

          
    while True:   
        action = input("Do you want to (E)ncrypt or (D)crypt text? ").lower()
        if action == 'e':
            keyword = input("Enter the keyword: ").lower()
            text =  input("Enter the text: ")
            encryptedText = encrypt(text, keyword)
            print("Encrypted text: ", encryptedText)
            while True:
                again = input("(E)xit? or (A)gain? ").lower()
                if (again != 'e' and again != 'a'):
                    print("Invalid input.")
                    continue
                elif again == 'e':
                    print("Ciao.")
                    sys.exit()
                else:
                    break
        elif action == 'd':
            keyword = input("Enter the keyword: ").lower()
            text =  input("Enter the text: ")
            decryptedText = decrypt(text, keyword)
            print("Decrypted text: ", decryptedText)
            while True:
                again = input("(E)xit? or (A)gain? ").lower()
                if again != 'e' and again != 'a':
                    print("Invalid input.")
                    continue
                elif again == 'e':
                    print("Ciao.")
                    sys.exit()
                else:
                    break
        else:
            print("Invalid action.")

if __name__ == "__main__":
    main()
