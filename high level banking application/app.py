from flask import Flask, render_template, request, redirect, session, url_for, flash
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
from decimal import Decimal, InvalidOperation

app = Flask(__name__)
app.secret_key = 'your_secure_secret_key_here'

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='vishnu@123',
        database='bank_db',
        auth_plugin='mysql_native_password'
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])

        conn = None
        cursor = None

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (name, email, password, balance) VALUES (%s, %s, %s, %s)",
                           (name, email, password, Decimal('100099.00')))
            conn.commit()
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
        except mysql.connector.Error as err:
            flash(f'Registration failed! {err.msg}', 'danger')
        finally:
            if cursor: cursor.close()
            if conn: conn.close()

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = None
        cursor = None

        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
            user = cursor.fetchone()

            if user and check_password_hash(user['password'], password):
                session['user_id'] = user['id']
                session['user_name'] = user['name']
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid email or password', 'danger')
        except mysql.connector.Error as err:
            flash(f'Login error: {err.msg}', 'danger')
        finally:
            if cursor: cursor.close()
            if conn: conn.close()

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = None
    cursor = None

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE id=%s", (session['user_id'],))
        user = cursor.fetchone()
        return render_template('dashboard.html', user=user)
    except mysql.connector.Error as err:
        flash(f'Database error: {err.msg}', 'danger')
        return redirect(url_for('index'))
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

@app.route('/transfer', methods=['POST'])
def transfer():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    receiver_email = request.form['receiver']
    
    try:
        amount = Decimal(request.form['amount'])
        if amount <= Decimal('0.00'):
            flash('Amount must be positive!', 'danger')
            return redirect(url_for('dashboard'))
    except InvalidOperation:
        flash('Invalid amount format!', 'danger')
        return redirect(url_for('dashboard'))

    conn = None
    cursor = None

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # Get sender info
        cursor.execute("SELECT * FROM users WHERE id=%s", (session['user_id'],))
        sender = cursor.fetchone()

        if sender['balance'] < amount:
            flash('Insufficient balance!', 'danger')
            return redirect(url_for('dashboard'))

        # Get receiver info
        cursor.execute("SELECT * FROM users WHERE email=%s", (receiver_email,))
        receiver = cursor.fetchone()

        if not receiver:
            flash('Receiver not found!', 'danger')
            return redirect(url_for('dashboard'))

        if sender['id'] == receiver['id']:
            flash('Cannot transfer to yourself!', 'danger')
            return redirect(url_for('dashboard'))

        # Update balances
        new_sender_balance = sender['balance'] - amount
        new_receiver_balance = receiver['balance'] + amount

        cursor.execute("UPDATE users SET balance=%s WHERE id=%s",
                      (new_sender_balance, sender['id']))
        cursor.execute("UPDATE users SET balance=%s WHERE id=%s",
                      (new_receiver_balance, receiver['id']))

        # Record transaction
        cursor.execute("""
            INSERT INTO transactions (sender_id, receiver_id, amount) 
            VALUES (%s, %s, %s)
        """, (sender['id'], receiver['id'], amount))

        conn.commit()
        flash('Transfer successful!', 'success')

    except mysql.connector.Error as err:
        conn.rollback()
        flash(f'Transfer failed: {err.msg}', 'danger')
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

    return redirect(url_for('dashboard'))

@app.route('/history')
def history():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = None
    cursor = None

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT t.*, u1.name as sender_name, u2.name as receiver_name 
            FROM transactions t
            JOIN users u1 ON t.sender_id = u1.id
            JOIN users u2 ON t.receiver_id = u2.id
            WHERE t.sender_id=%s OR t.receiver_id=%s 
            ORDER BY t.timestamp DESC
        """, (session['user_id'], session['user_id']))

        transactions = cursor.fetchall()
        return render_template('history.html', transactions=transactions)
    except mysql.connector.Error as err:
        flash(f'Database error: {err.msg}', 'danger')
        return redirect(url_for('dashboard'))
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)