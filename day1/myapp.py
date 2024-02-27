from flask import Flask,request,render_template,redirect,url_for

app=Flask(__name__)

users=[{"id":1,"name":"aaa","age":30},{"id":2,"name":"bbb","age":20},{"id":3,"name":"ccc","age":10}]

if __name__ == "__main__":
    app.run(debug=True)


@app.route('/')
def index():
    return render_template("index.html")

def get_id():
    if len(users)<0:
        return users[-1]['id']+1
    else:
        return 1

@app.route('/users')
def get_users():
    name=request.args.get('name')
    age=request.args.get('age')
    if name!=None or age!=None :
        users.append({"id":get_id(),"name":name,"age":age})
    print(users)
    if users != []:
        return render_template('users.html',users_html=users)
    else :
        return "<h1> NO Users</h1>"
    
@app.route('/delete/<int:id>')
def delete_user(id):
    if id != None and len(users) !=0 : 
        for i in range(len(users)):
            if users[i]['id']==id:
                del users[i]
                break
    return redirect('/users')

@app.route('/updateusr/<int:id>', methods=['GET', 'POST'])
def update_user(id):
    if id != None and len(users) !=0 : 
        for i in range(len(users)):
            if users[i]['id']==id:
                user = users[i]
                break
    if request.method == 'POST':
        user['name'] = request.form['name']
        user['age'] = request.form['age']
        return redirect('/users')
    return render_template('updateusr.html', user=user)


# @app.route('/user')
# def get_user():
#     name=request.args.get('name')
#     return f"user is name={name}"

# @app.route('/user/<int:id>')
# def get_one_user(id):
#     for user in users :
#         if user['id'] == id :
#             return user
#     return "<h1>User not found plz try again later</h1>"
       