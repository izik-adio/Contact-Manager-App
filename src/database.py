import sqlite3 as sq
import logging

Format = "%(asctime)s %(levelname)s %(message)s"
logging.basicConfig(
    filename="./log/DatabaseLog.log", level=logging.DEBUG, format=Format
)


class DataBase:
    def __init__(self) -> None:
        """Initialize a new instance of the Database class.

        This method creates a new instance of the Database class and automatically calls the createDb method
        to set up the necessary database for the Contacts application.
        """
        self.createDb()

    def createDb(self):
        """Create the database and necessary table for the Contacts application.

        This method establishes a connection to the SQLite database located at "./data/contacts.db" and creates
        a 'contacts' table with columns for 'name' (contacts name), 'phone_num' (contact phone number), 'email'
        (contacts email), and 'adress' (contact adress).

        If the table already exists, it logs a warning but does not raise an error.
        """
        self.connection = sq.connect("./data/contacts_data.db")
        try:
            with self.connection:
                self.cursor = self.connection.cursor()
                self.cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS contacts (
                        name text,
                        phone_num text,
                        email text,
                        address text
                    )
                    """
                )
        except sq.Error as e:
            logging.error(f"Cant create table:  {e}")

    def create_contact(self, name, phone_num, email, addr):
        if (name and phone_num) and not self.contact_detail(name, phone_num):

            try:
                self.cursor.execute(
                    """INSERT INTO contacts VALUES (?,?,?,?)""",
                    (name.title(), phone_num, email, addr),
                )
                self.connection.commit()
                return True
            except sq.Error as e:
                logging.error(f"Unable to create contact: {e}")
        else:
            logging.warning("Incomplete data was provided")

    def contact_detail(self, name="", phone_num=""):
        try:
            self.cursor.execute(
                "SELECT * FROM contacts WHERE name = ? OR phone_num = ?",
                (name, phone_num),
            )
            return self.cursor.fetchone()
        except sq.Error as e:
            logging.error(f"Unable to load the detail for {name} or {phone_num}\n\t{e}")
            return None

    def update_contact(
        self, previous_name, name, email, phone_num, addr, previous_num=""
    ):
        if self.contact_detail(previous_name, previous_num):
            try:
                self.cursor.execute(
                    """ UPDATE contacts SET name = ?, phone_num = ?, email = ?, address = ? WHERE name = ? OR phone_num = ? """,
                    (name, phone_num, email, addr, previous_name, previous_num),
                )
                self.connection.commit()
            except sq.Error as e:
                logging.error(f"Unable to update contact \t\t{e}")
        else:
            logging.error(
                f"No contact with the name {previous_name} phone_num {previous_num}"
            )

    def del_contact(self, name, phone_num=""):
        if self.contact_detail(name):
            if phone_num:  # Check if phone_num is provided
                self.cursor.execute(
                    "DELETE FROM contacts WHERE name = ? AND phone_num = ?",
                    (name, phone_num),
                )
            else:
                self.cursor.execute(
                    "DELETE FROM contacts WHERE name = ?",
                    (name,),
                )
            self.connection.commit()
        else:
            logging.error(f"contact does not exist")

    def search(self, name="", phone_num=""):
        try:
            modified_name = f"%{name}%"
            modified_num = f"%{phone_num}%"
            self.cursor.execute(
                "SELECT * FROM contacts WHERE name LIKE ? AND phone_num LIKE ?  ORDER BY name ASC",
                (
                    modified_name,
                    modified_num,
                ),
            )
            return self.cursor.fetchall()
        except sq.Error as e:
            logging.warning(f"No contact found. \t {e}")


if __name__ == "__main__":
    data_b = DataBase()
    data = data_b.search("adio")
    print(data)
