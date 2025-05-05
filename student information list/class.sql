create schema class;
use class

CREATE TABLE Students (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    StudentNo VARCHAR(20),
    Name VARCHAR(100),
    Email VARCHAR(100),
    Phone VARCHAR(20),
    UNIQUE(StudentNo)
)

INSERT INTO Students (StudentNo, Name, Email, Phone)
VALUES
    (1001, 'John Doe', 'john@example.com', '123-456-7890'),
    (1002, 'Jane Smith', 'jane@example.com', '987-654-3210'),
    (1003, 'Alice Johnson', 'alice@example.com', '111-222-3333'),
    (1004, 'Bob Brown', 'bob@example.com', '444-555-6666'),
    (1005, 'Eva Martinez', 'eva@example.com', '777-888-9999'),
    (1006, 'Michael Lee', 'michael@example.com', '333-222-1111'),
    (1007, 'Sophia Garcia', 'sophia@example.com', '666-555-4444'),
    (1008, 'William Wilson', 'william@example.com', '999-888-7777'),
    (1009, 'Olivia Anderson', 'olivia@example.com', '222-333-4444'),
    (1010, 'Daniel Thompson', 'daniel@example.com', '555-444-3333');
