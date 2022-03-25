# address-book
## Description
A Python 3 command-line address book program using a Sqlite database to store information.

## Overview
This project is a basic command line address book application written
in Python. This can be used to store personal information of colleagues 
including name, address, phone number, and email address. One does not
have to enter all information for a person except first and last name. 
The program prompts the user for each piece of contact information.

One can update the contact by contact_id and the method will only update 
the information specified by the user.

The 'list' method returns a list of all the contacts including
the information.

The 'listname' method returns a list of all the contacts sorted 
by last name and includes all available information.

The 'listdate' method returns a list of all the contacts sorted 
by creation date and includes all available information.