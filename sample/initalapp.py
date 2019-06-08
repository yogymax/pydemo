from flask import Flask

app = Flask(__name__)

@app.route("/welcomepage/")
def newmethod():
    return "frm new method..>!"


if __name__ == '__main__':
    app.run(debug=True,port=5002)