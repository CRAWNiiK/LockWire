import rsa
import os
import argparse

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
    with open(args.output_file, "wb") as f:
        f.write(crypto)
    return crypto

def decrypt_message(privkey, crypto):
    message = rsa.decrypt(crypto, privkey).decode('utf-8')
    with open(args.output_file, "w") as f:
        f.write(message)
    return message

parser = argparse.ArgumentParser(description="Encrypt or decrypt a message using RSA.")
parser.add_argument("-e", "--encrypt", action="store_true", help="Encrypt a message.")
parser.add_argument("-d", "--decrypt", action="store_true", help="Decrypt a message.")
parser.add_argument("-k", "--keyfile", default="key", help="Specify the name of the key file (default: key).")
parser.add_argument("-f", "--input-file", help="Specify the input file.")
parser.add_argument("-o", "--output-file", help="Specify the output file.")
parser.add_argument("-g", "--generate-keys", action="store_true", help="Generate a new pair of keys.")
parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.2')
args = parser.parse_args()

if args.generate_keys:
    save_keypair()
    print("New keypair generated successfully!")
    exit()

if args.encrypt and args.decrypt:
    print("Error: Only one of -e or -d can be specified at a time.")
    exit()

if not args.encrypt and not args.decrypt:
    print("Error: Either -e or -d must be specified.")
    exit()

if args.input_file is None:
    message = input("Enter the message to be encrypted/decrypted: ")
else:
    with open(args.input_file, "r") as f:
        message = f.read()

try:
    pubkey, privkey = load_keypair()
except:
    print("Unable to load keypair, please generate a new keypair.")
    exit()

if args.encrypt:
    crypto = encrypt_message(pubkey, message)
    print("Message encrypted successfully!")
    print(f"Encrypted message saved to {args.output_file}")

if args.decrypt:
    with open(args.input_file, "rb") as f:
        crypto = f.read()
    message = decrypt_message(privkey, crypto)
    print("Message decrypted successfully!")
    print(f"Decrypted message saved to {args.output_file}")