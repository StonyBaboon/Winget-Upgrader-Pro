Windows Package Updater

This Python script checks for updates on installed applications using winget and prompts the user to confirm if they want to update all the applications. It's a simple yet effective tool for keeping your Windows system up to date.
Features

  Check for Updates: Lists all applications that have available updates.
  User Confirmation: Asks the user if they want to proceed with updating the applications.
  Automated Updates: If confirmed, updates all applications automatically.

Prerequisites

  Python 3.x: Ensure you have Python 3 installed. You can download it from [Python Official Website](https://www.python.org).

  winget: The Windows Package Manager must be installed on your system. winget is available by default on Windows 10 version 1809 and later. You can learn more about it [here](https://learn.microsoft.com/en-us/windows/package-manager/winget/).

Installation

  Clone the repository:
```
  bash

git clone https://github.com//StonyBaboon/Winget-Upgrader-Pro.git
cd windows-package-updater
```
  Run the Script:
```
bash

  python apps_updated.py
```
Usage

  Start the Script:

  When you run the script, it will first display a logo, followed by a list of applications that can be updated.

  Confirm Updates:

  You will be asked whether you want to update all the listed applications. Type y for yes or n for no.

  Automatic Update:

  If you confirm, the script will automatically update all the applications using winget.

Example

When you run the script, it will look something like this:

```

  _      ___               __    __  __                      __          ___         
 | | /| / (_)__  ___ ____ / /_  / / / /__  ___ ________ ____/ /__ ____  / _ \_______ 
 | |/ |/ / / _ \/ _ `/ -_) __/ / /_/ / _ \/ _ `/ __/ _ `/ _  / -_) __/ / ___/ __/ _ \
 |__/|__/_/_//_/\_, /\__/\__/  \____/ .__/\_, /_/  \_,_/\_,_/\__/_/   /_/  /_/  \___/
               /___/               /_/   /___/                                       

Checking for available updates...

Packages that can be upgraded:

App1 v1.0 -> v1.1
App2 v2.3 -> v2.4
...

Do you want to update all packages? (y/n): y

Updating packages...
Packages successfully updated!

```
