import hashlib
import os
import shutil
from fs.osfs import OSFS


def calculate_checksum(filepath):

    sha256 = hashlib.sha256()

    with open(filepath, "rb") as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            sha256.update(chunk)

    return sha256.hexdigest()

def find_duplicates(directory, min_size):

    filesystem = OSFS(directory)

    checksums = {}
    duplicates = {}

    print("\nScanning files...\n")

    for path in filesystem.walk.files():

        full_path = os.path.join(directory, path.lstrip("/"))

        size = os.path.getsize(full_path)

        if size < min_size:
            continue

        checksum = calculate_checksum(full_path)

        if checksum in checksums:

            duplicates.setdefault(checksum, []).append(full_path)

        else:

            checksums[checksum] = full_path

    return checksums, duplicates


def generate_report(checksums, duplicates):

    with open("duplicate_report.txt", "w") as report:

        report.write("Duplicate File Report\n")
        report.write("=====================\n\n")

        for checksum, files in duplicates.items():

            report.write(f"Checksum: {checksum}\n")

            report.write(f"Original: {checksums[checksum]}\n")

            for f in files:
                report.write(f"Duplicate: {f}\n")

            report.write("\n")

    print("\nReport saved to duplicate_report.txt\n")


def handle_duplicates(checksums, duplicates):

    if not duplicates:
        print("No duplicate files found.")
        return

    print("\nDuplicate files detected:\n")

    for checksum, files in duplicates.items():

        print("Original:", checksums[checksum])

        for f in files:
            print("Duplicate:", f)

        print()

    choice = input("Delete duplicates or move them? (delete/move/skip): ")

    if choice == "delete":

        for files in duplicates.values():

            for f in files:
                os.remove(f)
                print("Deleted:", f)

    elif choice == "move":

        target = input("Enter folder to move duplicates: ")

        os.makedirs(target, exist_ok=True)

        for files in duplicates.values():

            for f in files:

                shutil.move(f, os.path.join(target, os.path.basename(f)))

                print("Moved:", f)


directory = input("Enter directory to scan: ")

min_size_mb = float(input("Minimum file size to scan (MB): "))

min_size = int(min_size_mb * 1024 * 1024)

checksums, duplicates = find_duplicates(directory, min_size)

generate_report(checksums, duplicates)

handle_duplicates(checksums, duplicates)