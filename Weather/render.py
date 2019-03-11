from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
def template():
    return render_template('rendering_template.html')

if __name__ == '__main__':
    app.run()