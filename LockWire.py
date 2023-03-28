import argparse
import os
import rsa

def generate_key(keyfile):
    (public_key, private_key) = rsa.newkeys(4096)
    with open(keyfile + "_pub.pem", "wb") as f:
        f.write(public_key.save_pkcs1())
    with open(keyfile + "_priv.pem", "wb") as f:
        f.write(private_key.save_pkcs1())
    print("New key pair generated.")

def encrypt(keyfile, message_file, output_file):
    with open(keyfile + "_pub.pem", "rb") as f:
        pubkey_data = f.read()
    pubkey = rsa.PublicKey.load_pkcs1(pubkey_data)
    with open(message_file, "rb") as f:
        message = f.read()
    crypto = rsa.encrypt(message, pubkey)
    with open(output_file, "wb") as f:
        f.write(crypto)
    print("Message encrypted successfully.")
    print(f"Encrypted message saved to {output_file}")

def decrypt(keyfile, message_file, output_file):
    with open(keyfile + "_priv.pem", "rb") as f:
        privkey_data = f.read()
    privkey = rsa.PrivateKey.load_pkcs1(privkey_data)
    with open(message_file, "rb") as f:
        crypto = f.read()
    message = rsa.decrypt(crypto, privkey)
    with open(output_file, "wb") as f:
        f.write(message)
    print("Message decrypted successfully.")
    print(f"Decrypted message saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Encrypt or decrypt a message using RSA 4096-bit.")
    parser.add_argument("-g", "--generate-key", action="store_true", help="Generate a new key pair.")
    parser.add_argument("-e", "--encrypt", metavar="FILE", help="Encrypt a message from the specified input file.")
    parser.add_argument("-d", "--decrypt", metavar="FILE", help="Decrypt a message from the specified input file.")
    parser.add_argument("-k", "--keyfile", default="key", help="Specify the name of the key file (default: key).")
    parser.add_argument("-o", "--output-file", help="Specify the output file.")
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 2.0")
    args = parser.parse_args()

    if args.generate_key:
        generate_key(args.keyfile)
    elif args.encrypt:
        if not args.output_file:
            print("Error: Output file not specified.")
            return
        encrypt(args.keyfile, args.encrypt, args.output_file)
    elif args.decrypt:
        if not args.output_file:
            print("Error: Output file not specified.")
            return
        decrypt(args.keyfile, args.decrypt, args.output_file)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
