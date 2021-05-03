from flask import Flask, render_template, request
import os
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/greet', methods=['POST'])
def greet():
    szyfr = request.form['szyfr']
    return render_template('deszyfrowanie.html', szyfr=szyfr)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
