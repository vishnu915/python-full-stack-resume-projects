import mysql.connector
from Model.RecordDTO import RecordDTO

class RecordDAO:


    """
    Initializes a connection to the MySQL database.
    Args:
        host (str): MySQL server host.
        user (str): MySQL username.
        password (str): MySQL password.
        database (str): MySQL database name.
    """
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    """
    Reads records from the 'Students' table in the database.
    Args:
        num_records (int): The number of records to retrieve.
    Returns:
        list: A list of RecordDTO objects.
    """
    def read_data_from_db(self):
        try:
            query = "SELECT StudentNo, Name, Email, Phone FROM Students"
            self.cursor.execute(query)
            records = []
            for row in self.cursor.fetchall():
                record = RecordDTO(*row)
                records.append(record)
            return records
        except Exception as e:
            print(f"An error occurred while reading a new record: {str(e)}")

    """
    Adds a new record to the 'Students' table in the database.
    Args:
        record_dto (RecordDTO): The RecordDTO object to be added.
    """
    def add_new_record(self, record_dto):
        try:
            query = "INSERT INTO Students (StudentNo, Name, Email, Phone) VALUES (%s, %s, %s, %s)"
            values = (
                record_dto.StudentNo,
                record_dto.Name,
                record_dto.Email,
                record_dto.Phone,
            )
            self.cursor.execute(query, values)
            self.connection.commit()
        except Exception as e:
            print(f"An error occurred while adding a new record: {str(e)}")

    """
    Deletes a record from the 'Students' table based on the ref_number.
    Args:
        record_id (str): The ref_number of the record to be deleted.
    """
    def delete_record(self, record_id):
        try:
            query = "DELETE FROM Students WHERE StudentNo = %s"
            self.cursor.execute(query, (record_id,))
            self.connection.commit()
        except Exception as e:
            print(f"An error occurred while deleting the record: {str(e)}")

    """
    Retrieves a record from the 'Students' table based on the ref_number.
    Args:
        record_id (str): The ref_number of the record to retrieve.
    Returns:
        RecordDTO or None: The RecordDTO object if found, or None if the record is not found.
    """
    def retrieve_record_by_id(self, record_id):
        try:
            query = "SELECT StudentNo, Name, Email, Phone FROM Students WHERE StudentNo = %s"
            self.cursor.execute(query, (record_id,))
            row = self.cursor.fetchone()
            if row:
                record = RecordDTO(*row)
                return record
        except Exception as e:
            print(f"An error occurred while retrieving the record: {str(e)}")
        return None

    """
    Updates a record in the 'Students' table based on the ref_number.
    Args:
        record_id (str): The ref_number of the record to be updated.
        updated_record_dto (RecordDTO): The updated RecordDTO object.
    """
    def update_record(self, record_id, updated_record_dto):
        try:
            query = "UPDATE Students SET Name = %s, Email = %s, Phone= %s WHERE StudentNo = %s"
            values = (

                updated_record_dto.Name,
                updated_record_dto.Email,
                updated_record_dto.Phone,
                record_id,
            )
            self.cursor.execute(query, values)
            self.connection.commit()
        except Exception as e:
            print(f"An error occurred while updating the record: {str(e)}")


    """
    Closes the database connection and cursor.
    """
    def close_connection(self):
        self.cursor.close()
        self.connection.close()
