from flask import Flask, request, render_template, redirect, url_for, session
import os
import yaml
import time
import subprocess
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = "bot/"

app.secret_key = os.urandom(24)

ding = True

def load_yaml(file):
    with open(file, "r") as fileding:
        data = yaml.load(fileding)
    return data

def dump_yaml(data, file):
    with open(file, "w") as fileding:
        yaml.dump(data, fileding)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ["py"]

@app.route("/")
def index():
    try:
        if session["user"] == True:
            return render_template("index.html")
        else:
            return redirect(url_for("login"))
    except:
        return redirect(url_for("login"))

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session[request.form["username"]] = request.form["username"]
        username = request.form["username"]
        print(username)
        if load_yaml("data/accounts.yml").get(username) != None:
            if request.form["password"] == load_yaml("data/accounts.yml").get(username):
                print(load_yaml("data/accounts.yml").get(username))
                session["user"] = True
                return "<meta http-equiv='refresh' content='0; url=/' />"
            else:
                return render_template("login.html")
        else:
            return render_template("login.html")
    else:
        return render_template("login.html")

@app.route("/start", methods=["POST"])
def start():
    subprocess.call("pkill -f index.py", shell=True)
    subprocess.Popen("python3 bot/index.py", shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
    return "<meta http-equiv='refresh' content='0; url=/' />"


@app.route("/stop", methods=["POST"])
def stop():
    subprocess.call("pkill -f index.py", shell=True)
    return "<meta http-equiv='refresh' content='0; url=/' />"

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files['file']
    print(file)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return "<meta http-equiv='refresh' content='0; url=/' />"
    else:
        return "<meta http-equiv='refresh' content='0; url=/' />"


@app.route("/profiel")
@app.route("/profiel/<naam>")
def profiel(naam=None):
    return render_template("profiel.html", naam=naam)

if __name__ == "__main__":
    app.run(debug=True, port=10000, host="0.0.0.0")
