def show_logo():
    logo = r"""
  _      ___               __    __  __                      __          ___         
 | | /| / (_)__  ___ ____ / /_  / / / /__  ___ ________ ____/ /__ ____  / _ \_______ 
 | |/ |/ / / _ \/ _ `/ -_) __/ / /_/ / _ \/ _ `/ __/ _ `/ _  / -_) __/ / ___/ __/ _ \
 |__/|__/_/_//_/\_, /\__/\__/  \____/ .__/\_, /_/  \_,_/\_,_/\__/_/   /_/  /_/  \___/
               /___/               /_/   /___/                                       
"""
    print(logo)

import os

def check_for_updates():
    print("Checking for available updates...\n")
    # Execute the command to list packages with available updates
    upgradable_packages = os.popen("winget upgrade").readlines()

    # If there are more than two lines, it means there are packages to update
    if len(upgradable_packages) <= 2:
        print("All packages are already up to date.\n")
        return []

    # Display upgradable packages
    print("Packages that can be upgraded:\n")
    for package in upgradable_packages[2:]:
        print(package.strip())

    return upgradable_packages[2:]

def confirm_update():
    response = input("\nDo you want to update all packages? (y/n): ").lower()

    if response == 'y':
        print("\nUpdating packages...")
        # Execute the command to update all packages
        os.system("winget upgrade --all")
        print("Packages successfully updated!")
    else:
        print("Update canceled.")

if __name__ == "__main__":
    show_logo()
    packages = check_for_updates()
    if packages:
        confirm_update()
