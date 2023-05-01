from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main_page():
    if request.method == 'GET':
        return "app service is success!"
    elif request.method == 'POST':
        return "POST is success!"

## 実行
if __name__ == "__main__":
    app.run(debug=True)