# address-book
## Description
A Python 3 command-line address book program using a Sqlite database to store information.

## Overview
This project is a basic command line address book application written
in Python. This can be used to store personal information of colleagues 
including name, address, phone number, and email address. One does not
have to enter all information for a person except first and last name. 
The program prompts the user for each piece of contact information.

To use the program one must download the repository, move to the directory
and then run the program.

```
python contacts.py -a "Doe"
```

One can update the contact by contact_id and the method will only update 
the information specified by the user.

The 'list' method returns a list of all the contacts including
the information.
```
python contacts.py -l


Contact ID, Last Name, First Name, Email Address, Phone Number, Address, Creation Date
================================================================================
(1, 'Pablo', 'Abed', None, '425-555-1234', None, '2022-03-22 23:30:16')
(2, 'Test', 'Tim', 'tim.test@test.com', None, None, '2022-03-22 23:31:16')
(3, 'Doe', 'Jane', None, None, '1234 Test St. Seattle, WA', '2022-03-22 23:32:17')
(4, 'Smith', 'John', '800-555-1234', 'johnsmith1@test.com', '13579 Test St. Seattle, WA', '2022-03-24 23:57:42')

```

The 'listname' method returns a list of all the contacts sorted 
by last name and includes all available information.

The 'listdate' method returns a list of all the contacts sorted 
by creation date and includes all available information.
