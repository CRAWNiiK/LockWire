import rsa
import os

def generate_key():
    (public_key, private_key) = rsa.newkeys(4096)
    return (public_key, private_key)

def save_keypair():
    (pubkey, privkey) = generate_key()
    with open("key_pub.txt", "w") as f:
        f.write(pubkey.save_pkcs1().decode('utf-8'))
    with open("key_private.txt", "w") as f:
        f.write(privkey.save_pkcs1().decode('utf-8'))

def load_keypair():
    with open("key_pub.txt", "r") as f:
        pubdata = f.read().encode('utf-8')
        pubkey = rsa.PublicKey.load_pkcs1(pubdata)
    with open("key_private.txt", "r") as f:
        privdata = f.read().encode('utf-8')
        privkey = rsa.PrivateKey.load_pkcs1(privdata)
    return (pubkey, privkey)

def encrypt_message(pubkey, message):
    crypto = rsa.encrypt(message.encode('utf-8'), pubkey)
    with open("encrypted_message.txt", "wb") as f:
        f.write(crypto)
    return crypto

def decrypt_message(privkey, crypto):
    message = rsa.decrypt(crypto, privkey).decode('utf-8')
    with open("decrypted_message.txt", "w") as f:
        f.write(message)
    return message

while True:
    choice = input("Press 1 for encryption or press 2 for decryption: ")

    if choice == '1':
        option = input("Press 1 to generate new keypair or press 2 to use existing keypair: ")
        if option == '1':
            save_keypair()
            print("Keypair generated successfully!")
        elif option == '2':
            try:
                pubkey, privkey = load_keypair()
            except:
                print("Unable to load keypair, please generate a new keypair.")
                continue
            message = input("Enter the message to be encrypted: ")
            crypto = encrypt_message(pubkey, message)
            print("Message encrypted successfully!")
            print(f"Encrypted message saved to encrypted_message.txt")
    elif choice == '2':
        try:
            pubkey, privkey = load_keypair()
        except:
            print("Unable to load keypair, please generate a new keypair.")
            continue
        with open("encrypted_message.txt", "rb") as f:
            crypto = f.read()
        message = decrypt_message(privkey, crypto)
        print("Message decrypted successfully!")
        print(f"Decrypted message saved to decrypted_message.txt")
    else:
        print("Invalid input. Please try again.")
        continue

    choice = input("Press 1 for encryption or press 2 for decryption. Press any other key to exit: ")
    if choice != '1' and choice != '2':
        break
