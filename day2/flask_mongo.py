from flask import Flask, redirect, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/flask"
mongo = PyMongo(app)
users=[]

@app.route('/users')
def index():
    users=list(mongo.db.Instructor.find({}))
    print(users)
    if users != []:
        return render_template('users.html',users_html=users)
    else :
        return "<h1> NO Users</h1>"
    
def get_id():
    user=list(mongo.db.Instructor.find({}).sort({"_id":-1}))
    if users != []:
        print(user[0]['_id'])
        print("list not empty")
        return user[0]['_id']+1
    else :
        print("list empty")
        return 1

@app.route('/adduser')
def get_users():
    name=request.args.get('name')
    age=request.args.get('age')
    if name!=None or age!=None :
        mongo.db.Instructor.insert_one({"_id":get_id(),"name":"aaa","age":30})
    return "ok"

@app.route('/delete/<string:id>')
def delete_user(id):
    user = mongo.db.Instructor.find_one({"_id": id})
    if user:
        mongo.db.Instructor.delete_one({"_id": id})
    return redirect('/users')


@app.route('/updateusr/<string:id>', methods=['GET', 'POST'])
def update_user(id):
    if request.method == 'GET':
        user = mongo.db.Instructor.find_one({"_id": id})
        return render_template('updateusr.html', user=user)
    else:
        name = request.form['name']
        age = request.form['age']
        print(f"Updating user with id: {id}, name: {name}, age: {age}")
        mongo.db.Instructor.update_one({"_id": id}, {"$set": {"name": name, "age": age}})
        print("User updated successfully.")
        return redirect('/users')
    

@app.route('/createusr', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        if name and age:
            user = {"name": name, "age": age}
            mongo.db.Instructor.insert_one(user)
            return redirect('/users')
    return render_template('createusr.html')
    