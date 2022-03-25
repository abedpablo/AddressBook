from address_book import AddressBook
import argparse
import re


def phone_format(phone_number):
    try:
        clean_phone_number = re.sub('[^0-9]+', '', phone_number)
        formatted_phone_number = re.sub(r"(\d)(?=(\d{3})+(?!\d))",
                                        r"\1-", "%d" % int(clean_phone_number[:-1])) + clean_phone_number[-1]
        return formatted_phone_number
    except ValueError as e:
        print(f'Invalid phone number entered: \n{e} {phone_number}')


def email_format(email_address):
    if ' ' in email_address:
        print('Invalid email address entered because of whitespace', "\n", email_address)
        return None
    if not re.match(r'[^@]+@[^@]+\.[^@]+', email_address):
        print('Invalid email address entered, no @ or . found', "\n", email_address)
        return None
    else:
        return email_address


def collect_info():
    first = input("Enter the first name (else press the Enter key to continue): ")
    email = input("Enter an email address (else press the Enter key to continue): ")
    if email:
        email = email_format(email)
    phone = input("Enter a phone number (else press the Enter key to continue): ")
    if phone:
        phone = phone_format(phone)
    address = input("Enter an address (else press the Enter key to continue): ")
    return first, email, phone, address


def get_args():
    parser = argparse.ArgumentParser(description='Address Book database storage')

    parser.add_argument('-a', '--add', type=str, help='Add contact with last name')
    parser.add_argument('-u', '--update', type=int, help='Update contact information by integer primary key')
    parser.add_argument('-d', '--delete', type=int, help='Delete contact by integer primary key')
    parser.add_argument('-g', '--get', type=int, help='Get contact information by integer primary key')
    parser.add_argument('-l', '--list', action='store_true', help='List contact information')
    parser.add_argument('-ln', '--listname', action='store_true', help='List contact information by last name')
    parser.add_argument('-ld', '--listdate', action='store_true', help='List contact information by creation date')

    return parser.parse_args()


def print_contacts(contacts):
    print('')
    print("Contact ID, Last Name, First Name, Email Address, Phone Number, Address, Creation Date")
    print("=" * 80)
    for c in contacts:
        print(c)
    print('')


def main(args):
    book = AddressBook()

    if args.add:
        last = args.add
        first, phone, email, address = collect_info()
        book.add_contact(last_name=last, first_name=first, email=email, address=address, phone=phone)

    if args.update:
        contact_id = args.update
        last = input("Enter the last name (else press the Enter key to continue): ")
        first, phone, email, address = collect_info()
        book.update_contact(contact_id, last_name=last, first_name=first, email=email, address=address, phone=phone)

    if args.delete:
        contact_id = args.delete
        book.delete_contact(contact_id)

    if args.list:
        all_contacts = book.list_records()
        print_contacts(all_contacts)

    if args.listname:
        all_contacts = book.list_records_alpha()
        print_contacts(all_contacts)

    if args.listdate:
        all_contacts = book.list_records_date()
        print_contacts(all_contacts)


if __name__ == '__main__':
    argss = get_args()
    main(argss)
