from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def index(name="TreeHouse"):
    return render_template('index.html', name=name)


@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
@app.route('/add/<int:num1>/<float:num2>')
def add(num1, num2):
    return render_template('add.html', num1=num1, num2=num2)

if __name__ == "__main__":
    app.run(debug=True, port=7000)
