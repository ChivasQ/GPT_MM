import json
from time import sleep

from flask import Flask, render_template, request

import prompt

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    text = ""
    blocklist_level1 = []
    blocklist_level2 = []
    if request.method == "POST":
        print(request.form)
        # request.input_stream
        text = prompt.ask_gpt(request.form["prompt"])
        file = open("test.txt", "r", encoding='cp1251')
        s = file.read()
        indexf = s.find('{')
        indexl = len(s) - s[::-1].find('}')
        print(text)
        s = s[indexf:indexl]
        json_object = json.loads(s)
        blocklist_level1 = json_object.keys()

    return render_template("main.html", title="title", blocklist_level1=text, blocklist_level2=blocklist_level2)



if __name__ == "__main__":
    app.run(debug=True)