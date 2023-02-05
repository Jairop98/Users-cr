from flask import render_template, request, redirect
#receives incoming requests

from flask_app import app
from flask_app.models.user import User
# gets all users and returns them in a list of user objects .

# routes - expected requests
# functions associated with routes - how our server responds
@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def users():
    return render_template("users.html",users=User.get_all())


@app.route('/user/new')
def new():
    return render_template("new_user.html")

@app.route('/user/create',methods=['POST'])
def create():
        #We make a data dictionary from our request.form coming from our template 
    #The keys in data need to line up exactly with the variables in our query string
    print(request.form)
    User.save(request.form)
    #Redirect after saving to the database
    return redirect('/users')


@app.route('/user/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("edit_user.html",user=User.get_one(data))

@app.route('/user/show/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("show_user.html",user=User.get_one(data))


@app.route('/user/update',methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/user/destroy/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    User.destroy(data)
    return redirect('/users')