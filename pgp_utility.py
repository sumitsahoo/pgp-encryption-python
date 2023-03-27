from typing import Any
import gnupg
import os

# Documentation: https://gnupg.readthedocs.io/en/latest/

gpg = gnupg.GPG()   # '/usr/local/bin/gpg' path is optional but gnupg needs to be installed

# Encrypt

symmetricKey = input("Enter password: ")
path = input("Enter complete path to the file: ")

encryptedFilePath = path + '.encrypted'

# Enable zlib compression when encrypting the file
extra_args = ['--compress-algo', 'zlib']

# Function name: encrypt_file
# Purpose: Encrypts a file with a symmetric key
# Parameters:
#    path: path of the file to be encrypted
#    symmetricKey: symmetric key to be used for encryption
#    extra_args: extra arguments to be passed to the gpg binary
# Return value: status of the encryption

with open(path, 'rb') as file:
    status = gpg.encrypt_file(file, recipients=Any, symmetric=True, passphrase=symmetricKey,
                              output=path + ".encrypted", armor=False, extra_args=extra_args)

if(status.ok):
    print("File encrypted successfully")

# Decrypt

with open(encryptedFilePath, 'rb') as file:
    status = gpg.decrypt_file(
        file, passphrase=symmetricKey, output=path + ".decrypted")

if(status.ok):
    print("File decrypted successfully")
