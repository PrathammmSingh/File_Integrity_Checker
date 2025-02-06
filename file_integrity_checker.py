import hashlib
import os
import json

def calculate_file_hash(file_path):
    """Calculate the SHA256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def scan_directory(directory):
    """Scan a directory and calculate hash values for all files."""
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hashes[file_path] = calculate_file_hash(file_path)
    return file_hashes

def save_hashes(file_hashes, output_file):
    """Save hash values to a JSON file."""
    with open(output_file, "w") as f:
        json.dump(file_hashes, f, indent=4)

def load_hashes(hash_file):
    """Load hash values from a JSON file."""
    with open(hash_file, "r") as f:
        return json.load(f)

def check_file_integrity(directory, hash_file):
    """Check for file integrity by comparing current and saved hashes."""
    saved_hashes = load_hashes(hash_file)
    current_hashes = scan_directory(directory)

    for file_path, current_hash in current_hashes.items():
        if file_path not in saved_hashes:
            print(f"New file detected: {file_path}")
        elif current_hash != saved_hashes[file_path]:
            print(f"Modified file detected: {file_path}")

    for file_path in saved_hashes.keys():
        if file_path not in current_hashes:
            print(f"Deleted file detected: {file_path}")

def main():
    """Main function to monitor file integrity."""
    directory = input("Enter the directory to monitor: ")
    hash_file = "file_hashes.json"

    if not os.path.exists(hash_file):
        print("Generating initial hashes...")
        file_hashes = scan_directory(directory)
        save_hashes(file_hashes, hash_file)
        print(f"Hashes saved to {hash_file}.")
    else:
        print("Checking file integrity...")
        check_file_integrity(directory, hash_file)

if __name__ == "__main__":
    main()
