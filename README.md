File Integrity Checker
Objective:
To create a tool that monitors the integrity of files within a specified directory. This tool ensures that the files have not been tampered with or altered by calculating and comparing their hash values.

Description:
The File Integrity Checker is a Python-based tool that helps detect unauthorized changes in files by comparing hash values. The script uses hashing algorithms (e.g., SHA-256) to generate unique hashes for each file. These hashes are stored and compared with future versions of the files to identify any modifications. This is particularly useful for maintaining the integrity of sensitive files and detecting potential tampering or data corruption.

Key Features:

Generates hash values for each file in a directory.
Stores hashes in a JSON file.
Compares file hashes periodically or when prompted.
Alerts the user if any file's hash has changed, indicating possible corruption or tampering.
Tools Used:

hashlib: For generating hash values.
json: For saving and loading hash values.
