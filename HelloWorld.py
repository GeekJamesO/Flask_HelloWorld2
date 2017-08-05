from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_work():
    return render_template('index.html', template_folder='template')

app.run(debug=True)
