# LockWire

RSA Encryption and Decryption built in Python

`pip install rsa`

usage

`python LockWire.py -h`

Generate key pair

`python LockWire.py -g`

this will generate key_pub.pem and key_priv.pem

you can rename it but leave the _pub.pem alone

ex crawniik_pub.pem

Encrypt txt file contents

`python LockWire.py -e filetoencrypt.txt -k crawniik -o outputfile.txt `

Decrypt txt file contents

`python LockWire.py -d filetodecrypt.txt -k crawniik -o outputfile.txt `
