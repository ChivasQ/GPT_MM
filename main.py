from time import sleep

from flask import Flask, render_template, request

import prompt

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
async def index():

    if request.method == "POST" and request.form["prompt"]:
        print(request.form)
        # request.input_stream
        #text = await prompt.ask_gpt(request.form["prompt"])
        file = open("test.txt", "r")
        s = file.read()

    return render_template("main.html", title="title", blocklist_level1=[1,2,3], blocklist_level2=[1,2,3])



if __name__ == "__main__":
    app.run(debug=True)