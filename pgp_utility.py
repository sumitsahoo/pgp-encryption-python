from typing import Any

import gnupg

gpg = (
    gnupg.GPG()
)  # '/usr/local/bin/gpg' path is optional but gnupg needs to be installed
# '/opt/homebrew/Cellar/gnupg'

# Get key and file path as input from the user

path = input("Enter complete path to the file: ")
symmetricKey = input("Enter symmetric key: ")

# Enable zlib compression when encrypting the file
extra_args_encryption = ["--compress-algo", "zlib"]

# Give user a choice if he wants to encrypt or decrypt
choice = input("Enter 'e' to encrypt or 'd' to decrypt: ")


# Define a function to encrypt the file
def encrypt_file(path, symmetricKey, extra_args_encryption):
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
        else:
            print(
                "File encryption failed, Error details: " + str(encryptionStatus.status)
            )
    except Exception as e:
        print("Exception occurred: " + str(e))


# Define a function to decrypt the file
def decrypt_file(path, symmetricKey):
    try:
        with open(path, "rb") as file:
            decryptionStatus = gpg.decrypt_file(
                file, passphrase=symmetricKey, output=path + ".decrypted"
            )
        if decryptionStatus.ok:
            print("File decrypted successfully")
        else:
            print(
                "File decryption failed, Error details: " + str(decryptionStatus.status)
            )
    except Exception as e:
        print("Exception occurred: " + str(e))


# Call the functions based on the choice variable
if choice == "e":
    encrypt_file(path, symmetricKey, extra_args_encryption)
elif choice == "d":
    decrypt_file(path, symmetricKey)
else:
    print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")
