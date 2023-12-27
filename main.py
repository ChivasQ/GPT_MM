from flask import Flask, render_template, request

import prompt

app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():
    text = ""
    if request.method == "POST":
        print(request.form)
        #text = prompt.ask_gpt(request.form["prompt"])
    return render_template("main.html", title="adawd", text="re")


if __name__ == "__main__":
    app.run(debug=True)