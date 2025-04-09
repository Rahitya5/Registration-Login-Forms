from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import hashlib

app = Flask(__name__)

db_config = {
    'host' : 'localhost',
    'user' : 'root',
    'password' : '',
    'database' : 'registration'
}

def create_table():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        cursor.execute("""(CREATE TABLE IF NOT EXSISTS users id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, email VARCHAR(255) UNIQUE NOT NULL, password VARCHAR(255) NOT NULL)""")
        
        connection.commit()
        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

create_table()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.route('/',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['register_name']
        email = request.form['register_email']
        password = request.form['register_password']
        hashed_password = hash_password(password)

        try:
            Connection = mysql.connector.connect(**db_config)
            cursor = Connection.cursor()
            cursor.execute("INSERT INTO users (name, email, password) VALUES (%S, %S, %S)",(name, email, hashed_password))
            Connection.commit()
            cursor.close()
            Connection.close()

            return redirect(url_for('login'))
        except mysql.connector.Error as err:
            return f"Error: {err}"
    
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        hashed_password = hash_password(password)

        try:
            Connection = mysql.connector.connect(**db_config)
            cursor = Connection.cursor()

            cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s",(email, hashed_password))
            user = cursor.fetchone()

            cursor.close()
            Connection.close()

            if user:
                return "Login Successful!"
            else:
                return "Invalid credentials"
        
        except mysql.connector.Error as err:
            return f"Error: {err}"
        
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)