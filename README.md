
# TallyClient

**TallyClient Software**

TallyClient is a pivotal component of the Voucher Automation Software Suite, crafted using Python and incorporating Tkinter and CustomTkinter. This user-friendly desktop application serves as the front-end interface for users, facilitating the creation of various vouchers and centralizing their storage in MongoDB Atlas, a robust NoSQL database.

*NOTE: You have to be connnected to the internet for this application to work



### Softwares:

1. [TallyMain](https://github.com/jaypunekar/AutoVoucherTally)
2. [TallyAccounts](https://github.com/jaypunekar/TallyAccounts)
3. [TallyClient](https://github.com/jaypunekar/TallyClient)

## Contents

- [Overview](#overview)
- [TallyClient Setup](#tallyclient-setup)
- [Installation](#installation)
- [Packaging](#packaging-the-application)
- [Screenshots](#screenshots)


## Overview
Key Features:

1. **Intuitive Voucher Creation:** TallyClient offers a simple and intuitive interface, empowering users to generate diverse voucher types, including sales invoices, purchase orders, receipts, payments, and more. It streamlines the data input process, ensuring accurate and well-structured voucher information.

2. **Seamless Data Storage:** The app securely stores all voucher data in MongoDB Atlas, providing a centralized and easily accessible repository for vouchers. This centralized storage simplifies data retrieval and enables the subsequent applications in the suite to access and process vouchers efficiently.

5. **Efficient Workflow:** TallyClient significantly streamlines the voucher creation process, enabling users to swiftly generate and save vouchers to MongoDB Atlas. This efficiency optimizes productivity and reduces the time required for manual voucher entry.

TallyClient provides an efficient and user-friendly platform for generating and storing vouchers in a centralized database, streamlining the initial stage of the voucher automation process. By leveraging Python and integrating with MongoDB Atlas, this application ensures seamless data flow and sets the foundation for accurate and automated voucher management within the Voucher Automation Software Suite.



## TallyClient Setup


You can get all the files for the project by cloning the project repository.

```bash
  git clone https://github.com/jaypunekar/TallyClient.git
```
Go to the project directory
```bash
  cd TallyClient
```

You will get all the files in AutoVoucherTally directory.

Step 1: In this software there is only one file that we are concerned with i.e. main.py. In the files you will find a section right after imports where the code to connect to MongoDB database is there.

[![mongoinside.png](https://i.postimg.cc/G2yVQcrs/mongoinside.png)](https://postimg.cc/S2mgQbny)

Setep 2: Change the mongo_url to the url you got earlier while setting up MongoDB Atlas. And change the database name and collection name as well (You should have all of it if you have followed the MongoDB Atlas Setup section).

*NOTE:- Keep localhost as it is.

Step 3: There is a fucntion save_button inside which you will find the structure of the collection that will be made in mongoDB. You can modifiy it but remember you might also have to modify the layout of all three software. So understand the code before making any changes.

[![tc1.png](https://i.postimg.cc/Jz2SBRCD/tc1.png)](https://postimg.cc/SncgBFsk)
## Installation
### Software Requirement.

1. [TallyClient](https://github.com/jaypunekar/TallyClient)
2. [TallyAccounts](https://github.com/jaypunekar/TallyAccounts)
3. [TallyMain](https://github.com/jaypunekar/AutoVoucherTally)

You should have already run first two command if you followed [TallyAccounts Setup](#tallyaccounts-setup)

Clone the project:

```bash
  git clone https://github.com/jaypunekar/TallyClient.git
```
Go to the project directory
```bash
  cd TallyClient
```

Create conda virtual enviornment (This step in not necessory. Anaconda should be installed for this step to work):
```bash
conda create -p venv python==3.8 -y
```
```bash
conda activate venv/
```

OR 
```bash
conda activate venv
```
Install dependencies:
```bash
pip install -r requirements.txt
```
#### Complete MongoDB Atlas and AutoVoucherTally Setup first else the following command won't work.

To run the program using Terminal:
```bash
python main.py
```
OR
```bash
python3 main.py
```


## Packaging the Application

In the Terminal (In AutoVoucherTally dir) run:
```bash
pyinstaller --onefile main.py  
```

Then run:

```bash
pyinstaller --name TallyClient --onefile --windowed --main.py
```

If you want to add an icon run (icon.ico should be in TallyClient dir):
```bash
pyinstaller --name TallyClient --onefile --windowed --icon=icon.ico --main.py
```
#### You will see a "dist" folder in TallyClient directory. Inside the "dist" folder you will get the executable file.

## Screenshots
[![img12.png](https://i.postimg.cc/8CPjbvZW/img12.png)](https://postimg.cc/qNSJJNVM)

[![img22.png](https://i.postimg.cc/Ss9qLNbC/img22.png)](https://postimg.cc/k67kqC4g)
