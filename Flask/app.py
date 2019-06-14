from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL
#from werkzeug import generate_password_hash, check_password_hash

app = Flask(__name__)
alex = MySQL()
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Alex1920$'
app.config['MYSQL_DATABASE_DB'] = 'Bucketlist'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
alex.init_app(app)

conn = alex.connect()
cursor = conn.cursor()
cursor.callproc('sp_createUser',("name", "email", "password"))

data= cursor.fetchall()

if len(data) is 0:
    conn.commit()
    return json.dumps({'message':'User created successfully !'})
else:
     return json.dumps({'error':str(data[0])})

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/showSignUp")
def showSignUp():
    return render_template("signup.html")

@app.route("/signUp", methods=["POST"])
def signUp():

     # read the posted values from the UI
    name = request.form["inputName"]
    email = request.form["inputEmail"]
    password = request.password["inputPassword"]

    # validate the received values
    if name and email and password:
        return json.dumps ({"html": "<span> All fields good !! </span>"})
    else:
        return json.dumps ({"html": "<span> Enter the required fields </span>"})

if __name__ == "__main__":
    app.run(debug = True, port=5002)
