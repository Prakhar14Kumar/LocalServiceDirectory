from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

# Database connection settings
db = pymysql.connect(host='127.0.0.1', user='root', password='', database='datalsd', port=3306)
cursor = db.cursor()


@app.route('/')
def index():
  return render_template('appointments.html')


@app.route('/submit', methods=['POST'])
def submit():
  if request.method == 'POST':
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    service = request.form['service']
    sub_service = request.form['subService']
    date = request.form['date']
    message = request.form['message']

    # Validation
    if not all([name, email, phone, date]):
      return "Please fill out all required fields."

    def is_valid_email(email):
      return '@' in email and '.' in email

    # Validate email
    if not is_valid_email(email):
      return "Invalid email format."

    # Insert data into the database
    cursor.execute(
      "INSERT INTO appointments (name, email, phone, service, sub_service, date, message) VALUES (%s, %s, %s, %s, %s, %s, %s)",
      (name, email, phone, service, sub_service, date, message))
    db.commit()

    return "Form submitted successfully."


if __name__ == '__main__':
  app.run(debug=True)
