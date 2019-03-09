from flask import Flask, render_template, redirect
app = Flask(__name__)
@app.route("/")
@app.route("/feeds/")
def getFeeds():
    options = [
    {"name":"Feed","selected":True,"link":"#"},
    {"name":"My Profile","selected":False,"link":"#"},
    {"name":"My Network","selected":False,"link":"#"},
    {"name":"New Post","selected":False,"link":"#"}
    ]
    return render_template("feed.html",title="Feed", nav_options = options)

@app.route("/login/")
def login():
    options = [
    {"name":"Feed","selected":False,"link":"#"},
    {"name":"My Profile","selected":False,"link":"#"},
    {"name":"My Network","selected":False,"link":"#"},
    {"name":"New Post","selected":False,"link":"#"}
    ]
    return render_template("authenticate.html",title="Login",nav_options= options)

if __name__ == "__main__":
    app.run(debug=True)
