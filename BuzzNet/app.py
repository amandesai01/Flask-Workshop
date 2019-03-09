from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)
db = SQLAlchemy(app)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(32), nullable=False)
    def __repr__():
        return f"User('{self.id}','{self.email}','{self.password}')"




@app.route("/")
@app.route("/feeds/")
def getFeeds():
    options = [
    {"name":"Feed","selected":True,"link":url_for("getFeeds")},
    {"name":"My Profile","selected":False,"link":url_for("getProfile")},
    {"name":"My Network","selected":False,"link":url_for("getFriends")},
    {"name":"New Post","selected":False,"link":url_for("newPost")}
    ]
    return render_template("feed.html",title="Feed", nav_options = options)

@app.route("/login/")
def login():
    options = [
    {"name":"Feed","selected":False,"link":url_for("getFeeds")},
    {"name":"My Profile","selected":False,"link":url_for("getProfile")},
    {"name":"My Network","selected":False,"link":url_for("getFriends")},
    {"name":"New Post","selected":False,"link":url_for("newPost")}
    ]
    return render_template("authenticate.html",title="Login",nav_options= options)
@app.route("/friends/")
def getFriends():
    options = [
    {"name":"Feed","selected":False,"link":url_for("getFeeds")},
    {"name":"My Profile","selected":False,"link":url_for("getProfile")},
    {"name":"My Network","selected":True,"link":url_for("getFriends")},
    {"name":"New Post","selected":False,"link":url_for("newPost")}
    ]
    return render_template("friends.html",title="Friends",nav_options= options)
@app.route("/profile/")
def getProfile():
    options = [
    {"name":"Feed","selected":False,"link":url_for("getFeeds")},
    {"name":"My Profile","selected":True,"link":url_for("getProfile")},
    {"name":"My Network","selected":False,"link":url_for("getFriends")},
    {"name":"New Post","selected":False,"link":url_for("newPost")}
    ]
    return render_template("profile.html",title="Profile",nav_options= options)
@app.route("/post/new/")
def newPost():
    options = [
    {"name":"Feed","selected":False,"link":url_for("getFeeds")},
    {"name":"My Profile","selected":False,"link":url_for("getProfile")},
    {"name":"My Network","selected":False,"link":url_for("getFriends")},
    {"name":"New Post","selected":True,"link":url_for("newPost")}
    ]
    return redirect(url_for("getFeeds"))
    #return render_template("profile.html",title="Profile",nav_options= options)

if __name__ == "__main__":
    app.run(debug=True)
