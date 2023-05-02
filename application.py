from flask import Flask,render_template,request
import os
import openai

app = Flask(__name__)

openai.api_key = os.environ.get('OPENAI_API_KEY')

def chat(query):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": query}
        ]
    )

    return response.choices[0]["message"]["content"].strip()

@app.route("/", methods=["GET", "POST"])
def main_page():
    if request.method == 'GET':
        query = request.args.to_dict()['q']
        return chat(query)
    elif request.method == 'POST':
        return "POST is success!"

## 実行
if __name__ == "__main__":
    app.run(debug=True)