# 使用get参数来传递参数  传入的参数形式为 &key1=val1&key2=val2&...
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/echo/')
def echo():
    thing = request.args.get('thing')
    place = request.args.get('place')
    return render_template('flask3.html', thing=thing, place=place)

app.run(port=9999, debug=True)