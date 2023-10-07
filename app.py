from flask import Flask

app = Flask(__name__)  # インスタンス化


@app.route("/")  # url / アクセスがあったら中の処理を実行する
def hello_world():
    return "Hello,World"


@app.route("/goodbye")  # url /goodbye アクセスがあったら中の処理を実行する
def goodbye():
    return "Good bye!!!"


@app.route("/user/<name>")
def hi(name):
    return f"Hi {name}"


@app.route("/about/<name>")
def pro(name):
    html = f"<html><body><h1>{name}'s Hello</h1></body></html>"
    return html


# HTMLを直接代入
@app.route("/hello")
def hello():
    html = "<html><head><style>h1{color: red;}</style></head><body><h1>Hello</h1></body></html>"
    return html


if __name__ == "__main__":
    # 使用するポートを明示
    app.run(port=8000, debug=True)
