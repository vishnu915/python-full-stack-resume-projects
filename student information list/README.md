# Student Information List (Python Flask, MySQL HTML5, CSS, JavaScript, Unit test)

This project is a Python-based web application built using the Flask framework and follows the MVC architecture. It adds a feature allowing users to search records across multiple columns simultaneously.

## Key Features:
- **MVC Pattern**: The application separates data handling (Model), user interface (View), and control logic (Controller).
- **Multi-Column Search**: Users can input search terms for multiple columns and retrieve filtered results.
- **Database Integration**: Uses MySQL for storing and retrieving travel data, with SQL queries constructed dynamically based on user input.
- **Unit Testing**: Includes unit tests to validate the functionality of key components, ensuring the robustness of database queries and controller logic.

## Components:
- **Model**: Defines the data structure and database interaction logic (e.g., `RecordDAO.py` for querying and `RecordDTO.py` for data representation).
- **Controller**: Handles user input and business logic, such as processing form submissions and invoking database searches.
- **View**: HTML templates (`index.html`, `add.html`, `update.html` ) for displaying the records and search results.

## Setup:
1. Clone the repository.
2. Configure the database connection in `Controller.py`.
3. Run the Flask application using:

    ```bash
    source active
    python app.py
    click the url in the result (e.g. * Running on http://127.0.0.1:5000)
    ```

3.1 You can see the home page like below:
<img width="1275" alt="Screenshot 2024-09-27 at 02 45 31" src="https://github.com/user-attachments/assets/412dd5ea-63b6-4789-9bfa-2c530c9b3276">

3.2 You can search with multiple criteria to find the student information you want.
<img width="1269" alt="Screenshot 2024-09-27 at 02 47 27" src="https://github.com/user-attachments/assets/07a308a5-5e12-4bd7-9663-f14b0d155d13">

After you found the student you can click the Reset Search button to back to home page.

3.3 You can also add a new student information by clicking the Add New Rows button.
For example you can add the studnet information as below

StudentNo: 1010, Name: Alexa, Email: alexacc@mail.com, Phone: 555-331-6924.
<img width="1274" alt="Screenshot 2024-09-27 at 02 50 37" src="https://github.com/user-attachments/assets/3fb3a6cb-2de5-479b-905b-f3b2f61ed202">

After clicked the Add Row button, you will be redirected to home page and can see the one which you added.
<img width="1242" alt="Screenshot 2024-09-27 at 02 53 26" src="https://github.com/user-attachments/assets/87a82f66-29e2-4899-9d47-5600f217c3ad">

3.4 You can update student information as needed after click the update button.
For example you can update the Alexa phone number from 555-331-6924 to 555-999-1923.
<img width="1034" alt="Screenshot 2024-09-27 at 02 55 47" src="https://github.com/user-attachments/assets/df979ba0-b4f8-4a71-a234-a537da1140bf">

After clicked the update Record, you will be redirected to home page and can see the information has been updated.
<img width="1221" alt="Screenshot 2024-09-27 at 02 57 59" src="https://github.com/user-attachments/assets/029867eb-0184-4844-abaa-68d9ec63c33a">

3.5 You can delete student information as needed after click the delete button.
After clicked the delete button, you can see the student information has been removed.
For example, I remove the one Alexa who we just added here.
<img width="1190" alt="Screenshot 2024-09-27 at 03 00 16" src="https://github.com/user-attachments/assets/3828ab8b-0e3b-4b5f-9517-141e5bbdd76c">



4. To run the unit tests:

    ```bash
     python -m unittest CRUDtest.MyTestCase
    ```
    You can see that the CRUD results should all be successful.
![Screenshot 2024-09-27 at 03 03 09](https://github.com/user-attachments/assets/7936e35e-d2fe-41cf-85f0-e6cbad0d3a4f)

---



