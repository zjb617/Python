from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return  "It's alive!"

app.run(debug=True)
