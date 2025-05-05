import unittest

from Model.RecordDAO import RecordDAO
from Model.RecordDTO import RecordDTO


class MyTestCase(unittest.TestCase):
    def setUp(self):
        # Create a RecordDAO instance for testing
        self.record_dao = RecordDAO("localhost", "cst8333", "sec310", "class")

        # Add a record for testing purposes
        initial_record = RecordDTO("1112", "initial", "initial@g.c", "111-111-1111")
        self.record_dao.add_new_record(initial_record)

    def tearDown(self):
        # Delete the test record created in setUp to clean up after each test
        self.record_dao.delete_record("1112")


    def test_read_data_from_db(self):
        # Test the read_data_from_db function
        records = self.record_dao.read_data_from_db()

        # Ensure that there's at least one record (assuming the initial data contains records)
        self.assertTrue(len(records) >= 1)


    def test_add_new_record(self):
        # Test the add_new_record function
        new_record = RecordDTO("1113", "new","g@c", "111-111-1121")
        # Get the initial record count
        initial_record_count = len(self.record_dao.read_data_from_db())

        # Add the new record
        self.record_dao.add_new_record(new_record)

        # Check if the record count increased after adding a new record
        updated_record_count = len(self.record_dao.read_data_from_db())
        self.assertEqual(updated_record_count, initial_record_count + 1)

    def test_update_record(self):
        # Test the update_record function
        # Update the record with new data
        updated_record = RecordDTO("1112", "updated", "updated@g.c", "222-222-2222")
        self.record_dao.update_record("1112", updated_record)

        # Retrieve the updated record
        updated_record_data = self.record_dao.retrieve_record_by_id("1112")

        # Assert that the data was updated correctly
        self.assertEqual(updated_record_data.Name, "updated")
        self.assertEqual(updated_record_data.Email, "updated@g.c")
        self.assertEqual(updated_record_data.Phone, "222-222-2222")


    def test_delete_record(self):
        # Test the delete_record function
        # Get the initial record count
        initial_record_count = len(self.record_dao.read_data_from_db())

        # Delete the records
        self.record_dao.delete_record("1112")
        self.record_dao.delete_record("1113")

        # Check if the record count decreased after deletion
        updated_record_count = len(self.record_dao.read_data_from_db())
        self.assertEqual(updated_record_count, initial_record_count - 2)
