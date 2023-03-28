# LockWire

RSA Encryption/Decryption Script

This is a command-line script for encrypting and decrypting messages using the RSA encryption algorithm.

Prerequisites
Before using this script, you will need to have Python 3.x and the rsa package installed. You can install the package using pip:

pip install rsa
Usage
To use the script, open a terminal window and navigate to the directory containing the script. Then, you can run the script using the following command:

python rsa_encrypt_decrypt.py [options]
Options
The script accepts the following options:

-e, --encrypt: Encrypt a message.
-d, --decrypt: Decrypt a message.
-k, --keyfile: Specify the name of the key file (default: key).
-f, --input-file: Specify the input file.
-o, --output-file: Specify the output file.
-g, --generate-key: Generate a new key pair.
-h, --help: Show help message and exit.
-v, --version: Show the version of the script.
Examples
Here are some examples of how to use the script:

Generate a new key pair
To generate a new key pair, run the script with the -g option:

`python rsa_encrypt_decrypt.py -g`
This will generate a new public/private key pair and save them to the default key files (key_pub.txt and key_private.txt).

Encrypt a message
To encrypt a message, run the script with the -e option and specify the message to encrypt:

python rsa_encrypt_decrypt.py -e "Hello, world!"
This will encrypt the message "Hello, world!" using the default public key and save the encrypted message to a file named output.txt.

Decrypt a message
To decrypt a message, run the script with the -d option and specify the encrypted message file:

python rsa_encrypt_decrypt.py -d -f "output.txt"
This will decrypt the message in the output.txt file using the default private key and save the decrypted message to a file named output_decrypted.txt.

License
This script is licensed under the MIT License. See the LICENSE file for details.
