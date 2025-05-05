

from flask import Flask, render_template, redirect, url_for, request
from Model.RecordDAO import RecordDAO
from Model.RecordDTO import RecordDTO

app = Flask(__name__, template_folder='../templates', static_folder='../static')

# Database connection details
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "vishnu@123",
    "database": "class"
}

record_dao = RecordDAO(**db_config)

@app.route('/')
def index():
    # Read data from the MySQL database using the DAO
    records = record_dao.read_data_from_db()
    return render_template('index.html', records=records)

# Define a new route for adding new rows
@app.route('/add_new_rows')
def add_new_rows():
    return render_template('add.html')  # Redirect to the 'add' route

# Route to handle the form submission
@app.route('/submit_new_row', methods=['POST'])
def submit_new_row():
    if request.method == 'POST':
        # Extract data from the form
        student_no = request.form['column_a']
        name = request.form['column_b']
        email = request.form['column_c']
        phone = request.form['column_d']

        # Create a new RecordDTO object with the form data
        new_record = RecordDTO(student_no, name, email, phone)

        # Append the new row to the MySQL database
        record_dao.add_new_record(new_record)

        # Redirect back to the main view after adding the row
        return redirect(url_for('index'))

# Route to delete a record
@app.route('/delete_record/<string:record_id>', methods=['GET', 'POST'])
def delete_record(record_id):
    # Call the delete_record method in RecordDAO to delete the record
    record_dao.delete_record(record_id)
    # Redirect back to the main view after deleting the record
    return redirect(url_for('index'))

# Route to display the update form for a record
@app.route('/update_record/<string:record_id>', methods=['GET'])
def update_record_page(record_id):
    # Retrieve the record you want to update based on record_id
    record_to_update = record_dao.retrieve_record_by_id(record_id)

    if record_to_update:
        return render_template('update.html', record=record_to_update)
    else:
        return "Record not found"

# Route to handle the form submission for updating a record
@app.route('/update_record/<string:record_id>', methods=['POST'])
def update_record(record_id):
    if request.method == 'POST':
        # Extract data from the form
        student_no = request.form['column_a']
        name = request.form['column_b']
        email = request.form['column_c']
        phone = request.form['column_d']


        # Create a new RecordDTO object with the updated data
        updated_record = RecordDTO(student_no,name,email,phone)

        # Update the record in the MySQL database
        record_dao.update_record(record_id, updated_record)

        # Redirect back to the main view after updating the record
        return redirect(url_for('index'))
