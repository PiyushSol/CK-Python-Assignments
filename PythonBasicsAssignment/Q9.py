import os
import shutil
import hashlib
import difflib

VERSION_DIR = "versions"

def setup_version_dir():
    if not os.path.exists(VERSION_DIR):
        os.makedirs(VERSION_DIR)

def file_hash(filepath):

    sha = hashlib.sha256()

    with open(filepath, "rb") as f:
        while chunk := f.read(4096):
            sha.update(chunk)

    return sha.hexdigest()

def get_next_version(filename):

    base = os.path.basename(filename)
    name, ext = os.path.splitext(base)

    version = 1

    while True:

        version_file = f"{name}_v{version}{ext}"
        path = os.path.join(VERSION_DIR, version_file)

        if not os.path.exists(path):
            return version

        version += 1

def save_version(filepath):

    if not os.path.isfile(filepath):
        return

    version = get_next_version(filepath)

    name, ext = os.path.splitext(os.path.basename(filepath))

    new_name = f"{name}_v{version}{ext}"

    dest = os.path.join(VERSION_DIR, new_name)

    shutil.copy(filepath, dest)

    print(f"Version saved: {new_name}")

def scan_directory(directory, file_hashes):

    for root, dirs, files in os.walk(directory):

        if root.endswith(VERSION_DIR):
            continue

        for file in files:

            path = os.path.join(root, file)

            current_hash = file_hash(path)

            if path not in file_hashes:
                file_hashes[path] = current_hash
                save_version(path)

            elif file_hashes[path] != current_hash:
                file_hashes[path] = current_hash
                save_version(path)

def restore_version(filename, version):

    name, ext = os.path.splitext(filename)

    version_file = f"{name}_v{version}{ext}"

    source = os.path.join(VERSION_DIR, version_file)

    if not os.path.exists(source):
        print("Version not found")
        return

    shutil.copy(source, filename)

    print("File restored:", filename)

def compare_versions(file1, file2):

    with open(file1) as f1, open(file2) as f2:

        diff = difflib.unified_diff(
            f1.readlines(),
            f2.readlines(),
            fromfile=file1,
            tofile=file2
        )

        print("".join(diff))

def cleanup_versions(filename, keep=3):

    name, ext = os.path.splitext(filename)

    versions = []

    for f in os.listdir(VERSION_DIR):

        if f.startswith(name) and f.endswith(ext):
            versions.append(f)

    versions.sort()

    if len(versions) > keep:

        old_versions = versions[:-keep]

        for v in old_versions:

            os.remove(os.path.join(VERSION_DIR, v))
            print("Deleted old version:", v)


def main():

    setup_version_dir()

    directory = input("Enter directory to monitor: ")

    file_hashes = {}

    while True:

        print("\n1. Scan for changes")
        print("2. Restore file version")
        print("3. Compare versions")
        print("4. Cleanup old versions")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            scan_directory(directory, file_hashes)

        elif choice == "2":

            file = input("Enter file name: ")
            version = input("Enter version number: ")

            restore_version(file, version)

        elif choice == "3":

            f1 = input("Enter first version file path: ")
            f2 = input("Enter second version file path: ")

            compare_versions(f1, f2)

        elif choice == "4":

            file = input("Enter file name: ")
            keep = int(input("Keep how many versions?: "))

            cleanup_versions(file, keep)

        elif choice == "5":
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()