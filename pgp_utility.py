from typing import Any
import gnupg
import os

# Documentation: https://gnupg.readthedocs.io/en/latest/

gpg = (
    gnupg.GPG()
)  # '/usr/local/bin/gpg' path is optional but gnupg needs to be installed
# '/opt/homebrew/Cellar/gnupg'
# Get key and file path as input from the user

symmetricKey = input("Enter password: ")
path = input("Enter complete path to the file: ")

encryptedFilePath = path + ".encrypted"

# Enable zlib compression when encrypting the file
extra_args_encryption = ["--compress-algo", "zlib"]

# Start file encryption and decryption
try:
    with open(path, "rb") as file:
        encryptionStatus = gpg.encrypt_file(
            file,
            recipients=Any,
            symmetric=True,
            passphrase=symmetricKey,
            output=path + ".encrypted",
            armor=False,
            extra_args=extra_args_encryption,
        )

    if encryptionStatus.ok:
        print("File encrypted successfully")
        print("Encrypted file path: " + encryptedFilePath)
        with open(encryptedFilePath, "rb") as file:
            decryptionStatus = gpg.decrypt_file(
                file, passphrase=symmetricKey, output=path + ".decrypted"
            )
        if decryptionStatus.ok:
            print("File decrypted successfully")
        else:
            print(
                "File decryption failed, Error details: " + str(decryptionStatus.status)
            )
    else:
        print("File encryption failed, Error details: " + str(encryptionStatus.status))
except Exception as e:
    print("Exception occurred: " + str(e))
