from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)

# Configure SQLAlchemy settings to connect to the PostgreSQL database running in Docker
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/postgres'

# Initialize SQLAlchemy instance with the Flask application
db = SQLAlchemy(app)

# Define a SQLAlchemy model representing the 'Data' table in the database
class Data(db.Model):
    # Define columns for the 'Data' table
    id = db.Column(db.Integer, primary_key=True)  # Primary key column
    name = db.Column(db.String(80))                # Name column of maximum length 80 characters

    # Representation method for the Data model
    def __repr__(self):
        return '<User %r>' % self.name

# Function to create the database table based on the defined models
def create_table():
    # Use app context to access the application context for database operations
    with app.app_context():
        # Create all database tables defined in the application
        db.create_all()

# Define a route for the root URL ('/') of the web application
@app.route('/', methods=['GET', 'POST'])
def index():
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Extract 'name' from the form submission
        name = request.form['name']
        # Create a new Data object with the extracted 'name'
        new_data = Data(name=name)
        # Add the new Data object to the session
        db.session.add(new_data)
        # Commit the session to persist the changes to the database
        db.session.commit()
        # Redirect the user to the index route (refreshes the page)
        return redirect(url_for('index'))
    else:
        # If the request method is GET, query all data from the 'Data' table
        data = Data.query.all()
        # Render the index.html template with the queried data
        return render_template('index.html', data=data)

# Entry point to the application
if __name__ == '__main__':
    # Call create_table function to ensure database table exists
    create_table()
    # Run the Flask application on host '0.0.0.0' and enable debug mode
    app.run(host='0.0.0.0', debug=True)
