from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def index():
    title = 'Welcome to My Website'
    message = 'Hello, Flask!'
    return render_template('index.html', title=title, message=message, )


@app.route('/submit', methods=['POST'])
def next_page():
    name1 = request.form.get('name1')
    name2 = request.form.get('name2')
    hcp1 = int(request.form.get('hcp1'))
    hcp2 = int(request.form.get('hcp2'))
    win_rate1 = 100 - hcp1 * 100 / (hcp1 + hcp2)
    win_rate2 = 100 - hcp2 * 100 / (hcp1 + hcp2)
    return render_template('next.html',  name1=name1, name2=name2, win_rate1=win_rate1, win_rate2=win_rate2)


@app.route("/greet/<name>")
def greet(name):
    return f"Hello, {name}"


@app.route("/multiply/<int:first_arg>/<int:second_arg>")
def multiply(first_arg: int, second_arg: int):
    return f"{first_arg * second_arg}"


with app.test_request_context():
    print(url_for('multiply', first_arg=2, second_arg=4, as_compex=True))


items_storage = []


@app.route("/items", methods=["GET", "POST"])
def items_endpoint():
    if request.method == "POST":
        item = request.form.get("item")
        items_storage.append(item)
    return render_template('items.html', items=items_storage)


if __name__ == "__main__":
    app.run(debug=True)
