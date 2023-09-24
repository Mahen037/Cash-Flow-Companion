import sqlite3
from flask import Flask,redirect, render_template, request, url_for, session


index_html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Cash & Flow Companion</title>
   <style>
        body {
            background-image: url("https://www.nacubo.org/-/media/Images/Stock-Photos/Finance/iStock-1253379369.ashx?h=427&w=640&la=en&hash=C98A198E65A1F541E0B71835F1F6C49E0B1A6E3E");
            background-repeat: no-repeat;
            background-size: cover;
            font-family: Arial, Helvetica, sans-serif, sans-serif;
            margin: 0;
            padding: 0;
        }
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #41B3A3;
            padding: 35px;
        }
        .logo {
            font-size: 30px;
            font-weight: normal;
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        nav ul {
            list-style: none;
            margin: 0;
            padding: 0;
            display: flex;
        }
        nav li {
            margin-left: 20px;
        }
        nav a {
            color: white;
            text-decoration: none;
            font-size: 18px;
            font-weight: bold;
            letter-spacing: 1px;
        }
        nav a:hover {
            border-bottom: 2px solid white;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 15px;
            background-color: #7a7776; 
            box-shadow: 2 2 10px rgba(41, 197, 168, 0.2);
            border-radius: 10px;
            margin-top: 30px;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            font-size: 20px;
            align-items: center;
            align-self: center;
        }
        
    </style>
</head>
<body>
    <header class="header">
        <div class="logo">Cash & Flow Companion</div>
        <nav>
            <ul>
                <li><a href="index.html">Home</a></li>
                
           
                <li><a href="signup.html">Sign-Up</a></li>
                <li><a href="faq.html">FAQ</a></li>
                
                
                <li><a href="contact.html">Contact Us</a></li>
            </ul>
        </nav>
    </header>
   
    
    <div style="background-color: #34495E; color: white; padding: 20px; text-align: center; font-size: 18px; letter-spacing: 1px; position: fixed; bottom: 0; width: 100%;">
        Contact us: +1-(240)-927-7610 | Email: <a href="mailto:amukhs13@terpmail.umd.edu">amukhs13@terpmail.umd.edu</a>
    </div>
</head>
<body>
"""

signup_html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Signup Page</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color:#41B3A3;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
    }

    .container {
      background-color: #fff;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      width: 300px;
    }

    h1 {
      text-align: center;
    }

    label {
      display: block;
      margin-bottom: 5px;
    }

    input {
      width: 100%;
      padding: 10px;
      margin-bottom: 10px;
      border: 1px solid #ccc;
      border-radius: 5px;
    }

    button {
      width: 100%;
      padding: 10px;
      background-color: #4CAF50;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }

    button:hover {
      background-color: #45a049;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Signup</h1>
    <form id="signupForm">
      <label for="name">Name:</label>
      <input type="text" id="name" name="name" required>

      <label for="email">Email:</label>
      <input type="email" id="email" name="email" required>

      <label for="phone">Phone Number:</label>
      <input type="tel" id="phone" name="phone" required>

      <label for="occupation">Occupation:</label>
      <input type="text" id="occupation" name="occupation" required>

      <label for="income">Income:</label>
      <input type="number" id="income" name="income" required>

      <label for="expenses">Expenses:</label>
      <input type="number" id="expenses" name="expenses" required>

      <label for="riskTolerance">Risk Tolerance:</label>
      <select id="riskTolerance" name="riskTolerance" required>
        <option value="" disabled selected>Select risk tolerance</option>
        <option value="low">Low</option>
        <option value="medium">Medium</option>
        <option value="high">High</option>
      </select>

      <button type="submit">Submit</button>
    </form>
  </div>
</body>
</html>
"""








# flask connection
app = Flask(__name__)
app.secret_key = "Hehe1234"

# Connect to SQLite database
conn = sqlite3.connect('signup_data.db')
c = conn.cursor()

# Create a table to store signup data
c.execute('''CREATE TABLE IF NOT EXISTS signups
             (name TEXT, email TEXT, phone TEXT, occupation TEXT, income INTEGER, expenses INTEGER, risk_tolerance TEXT)''')
conn.commit()

@app.route('/index')
def index():
    return index_html_content

@app.route('/')
def root():
    return index_html_content

def root1():
    return signup_html_content





@app.route('/signup', methods=['POST'])
def signup():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    occupation = request.form['occupation']
    income = int(request.form['income'])
    expenses = int(request.form['expenses'])
    risk_tolerance = request.form['riskTolerance']

    # Insert the data into the database
    c.execute("INSERT INTO signups VALUES (?, ?, ?, ?, ?, ?, ?)", (name, email, phone, occupation, income, expenses, risk_tolerance))
    conn.commit()

    return "Signup successful. Data stored in the database."
    return redirect(url_for('signup_page'))   






if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8083,debug=True)




   




