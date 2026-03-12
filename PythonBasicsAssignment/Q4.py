import os
import logging

logging.basicConfig(
    filename="package_update.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def check_updates():

    print("Checking for package updates...\n")
    logging.info("Checking for available package updates")

    os.system("sudo apt update")

    os.system("apt list --upgradable > updates.txt")

    packages = []

    try:
        with open("updates.txt", "r") as f:
            lines = f.readlines()[1:]  

            if not lines:
                print("All packages are up to date.")
                logging.info("No updates available")
                return []

            print("Available Updates:\n")

            for i, line in enumerate(lines):
                pkg_name = line.split("/")[0]
                packages.append(pkg_name)

                print(f"{i}. {pkg_name}")

        logging.info("Successfully listed available updates")

    except Exception as e:
        print("Error reading update list.")
        logging.error(f"Error reading updates: {e}")

    return packages


def install_updates(packages):

    if not packages:
        return

    choice = input("\nUpdate all packages? (yes/no): ")

    try:

        if choice.lower() == "yes":

            print("\nUpdating all packages...\n")
            logging.info("User selected to update all packages")

            result = os.system("sudo apt upgrade -y")

            if result != 0:
                raise Exception("Upgrade command failed")

            print("All packages updated successfully.")
            logging.info("All packages updated successfully")

        else:

            index = int(input("Enter package index number to update: "))

            if index < 0 or index >= len(packages):
                print("Invalid index.")
                logging.warning("User entered invalid package index")
                return

            package = packages[index]

            print(f"\nUpdating package: {package}\n")
            logging.info(f"Updating package: {package}")

            result = os.system(f"sudo apt install -y {package}")

            if result != 0:
                raise Exception(f"Installation failed for {package}")

            print(f"{package} updated successfully.")
            logging.info(f"{package} updated successfully")

    except Exception as e:

        print("ALERT: Package update failed! Check logs.")
        logging.error(f"Package update failed: {e}")


packages = check_updates()

install_updates(packages)

print("\nProcess completed. Check 'package_update.log' for details.")