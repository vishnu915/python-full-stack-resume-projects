

# Import the Flask application from controller.py
from Controller.controller import app

# Check if this script is the main entry point
if __name__ == '__main__':
    app.run(debug=True)
