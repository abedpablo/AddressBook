import sqlite3


class AddressBook:
    def __init__(self):
        self.dbname = "addressbook.db"
        db = sqlite3.connect(self.dbname)
        c = db.cursor()
        c.execute(
            """CREATE TABLE IF NOT EXISTS contacts
            ( contact_internal_id INTEGER PRIMARY KEY,
              last_name     TEXT NOT NULL,
              first_name    TEXT NOT NULL,
              email         TEXT,
              phone         TEXT,
              address       TEXT
              )"""
            )
        db.commit()
        c.close()

    def add_contact(self, last_name='', first_name='', email=None, address=None, phone=None):
        db = sqlite3.connect(self.dbname)
        c = db.cursor()
        c.execute('INSERT INTO contacts(last_name, first_name, email, address, phone) \
                    VALUES(?,?,?,?,?)', (last_name, first_name, email, address, phone))
        db.commit()
        c.close()

    def update_contact(self, contact_id, last_name=None, first_name=None, email=None, address=None, phone=None):
        ignore = ['contact_id', 'self', 'arg_list', 'ignore']

        arg_list = [arg for arg, val in locals().items() if val is not None and arg not in ignore]
        data_list = [val for arg, val in locals().items() if val is not None and arg not in ignore]

        pending_query = ""
        for idx, item in enumerate(arg_list):
            if idx == len(arg_list) - 1:
                pending_query += item + "=?"
            else:
                pending_query += item + "=?,"

        db = sqlite3.connect(self.dbname)
        c = db.cursor()
        data_list += [contact_id]
        query = 'UPDATE contacts set ' + pending_query + ' WHERE contact_internal_id=?'

        c.execute(query, data_list)
        db.commit()
        c.close()

    def delete_contact(self, contact_id):
        db = sqlite3.connect(self.dbname)
        c = db.cursor()
        c.execute('DELETE FROM contacts where contact_internal_id=?', (contact_id,))
        db.commit()
        c.close()

    def list_all_records(self):
        db = sqlite3.connect(self.dbname)
        c = db.cursor()
        c.execute('SELECT * from contacts')
        contacts = c.fetchall()
        c.close()
        return contacts

    def get_record(self, contact_id):
        db = sqlite3.connect(self.dbname)
        c = db.cursor()
        c.execute('SELECT * from contacts WHERE contact_internal_id=?', (contact_id,))
        contacts = c.fetchall()
        c.close()
        return contacts[0]
