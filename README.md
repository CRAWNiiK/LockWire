# LockWire

LockWire is a Python script that allows you to encrypt and decrypt messages using RSA 4096-bit.

## Requirements
- Python 3.x
- `rsa` module (you can install it using `pip install rsa`)

## Usage

### Generating a new key pair
To generate a new key pair, use the `-g` or `--generate-key` argument. By default, the key files will be named `key_pub.pem` and `key_priv.pem`. To specify a custom name, use the `-g` or `--generate-key` argument followed by the desired name.

Example: `python LockWire.py -g mykey`

This will generate a new key pair with the file names `mykey_pub.pem` and `mykey_priv.pem`.

### Encrypting a message
To encrypt a message, use the `-e` or `--encrypt` argument followed by the name of the input file, and the `-o` or `--output-file` argument followed by the desired output file name. The public key file will be loaded based on the `-k` or `--keyfile` argument.

Example: `python LockWire.py -e message.txt -k mykey -o encrypted-message.txt`

This will encrypt the contents of `message.txt` using the public key in `key_pub.pem`, and save the encrypted message to `encrypted-message.txt`.

### Decrypting a message
To decrypt a message, use the `-d` or `--decrypt` argument followed by the name of the input file, and the `-o` or `--output-file` argument followed by the desired output file name. The private key file will be loaded based on the `-k` or `--keyfile` argument.

Example: `python LockWire.py -d encrypted-message.txt -k mykey -o decrypted-message.txt`

This will decrypt the contents of `encrypted-message.txt` using the private key in `key_priv.pem`, and save the decrypted message to `decrypted-message.txt`.
