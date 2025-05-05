
class RecordDTO:
    """
    Represents a Data Transfer Object (DTO) for records.
    This class is used to encapsulate data for individual records, with attributes
    representing different columns in the data.
    Attributes:
        column_a (str: Description of column_a.
        column_b (str): Description of column_b.
        column_c (str): Description of column_c.
        column_d (str): Description of column_d.
    Args:
        student_no (str): Value for column_a.
        name (str): Value for column_b.
        email (str): Value for column_c.
        phone (str): Value for column_d.
    """

    def __init__(self, student_no, name, email, phone):
        """
        Initialize a new RecordDTO instance with the provided values for attributes.
        Args:
            column_a (str): Value for column_a.
            column_b (str): Value for column_b.
            column_c (str): Value for column_c.
            ...
            column_u (str): Value for column_u.
        """
        self.StudentNo = student_no
        self.Name = name
        self.Email = email
        self.Phone = phone


