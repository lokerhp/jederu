from flask import Flask, request, render_template, redirect, url_for, session, flash
import os
import yaml
import time
import subprocess
import sys
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = "bot/"

app.secret_key = os.urandom(24)

def load_yaml(file):
    with open(file, "r") as fileding:
        global data
        data = yaml.load(fileding)
    return data

def dump_yaml(username, password, file):
    with open(file, "w") as fileding:
        print(data)
        data[username] = password
        print(data)
        yaml.dump(data, fileding, default_flow_style=False)
        print("done")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ["py", "js"]

@app.route("/")
def index():
    try:
        username = session["user"]
    except:
        return redirect(url_for("login"))
    try:
        if session["logged"] == True:
            return render_template("index.html", username=username)
        else:
            return redirect(url_for("login"))
    except:
        return redirect(url_for("login"))

@app.route("/upload", methods=["GET"])
def uploadhtml():
    try:
        username = session["user"]
    except:
        return redirect(url_for("login"))
    try:
        if session["logged"] == True:
            return render_template("upload.html", username=username)
        else:
            return redirect(url_for("login"))
    except:
        return redirect(url_for("login"))

@app.route("/control", methods=["GET"])
def control():
    try:
        username = session["user"]
    except:
        return redirect(url_for("login"))
    try:
        if session["logged"] == True:
            return render_template("control.html", username=username)
        else:
            return redirect(url_for("login"))
    except:
        return redirect(url_for("login"))

@app.route("/admin", methods=["GET"])
def admin():
    try:
        username = session["user"]
    except:
        print("test1")
        return redirect(url_for("login"))
    try:
        if session["logged"] == True:
            if username == "admin":
                tot_m, used_m, free_m = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
                return render_template("admin.html", username=username, tot_m=tot_m, used_m=used_m, free_m=free_m)
            else:
                print("test4")
                return redirect(url_for("login"))
        else:
            print("test2")
            return redirect(url_for("login"))
    except:
        print("test3")
        return redirect(url_for("login"))

@app.route("/admin/accounts", methods=["GET"])
def accounts():
    try:
        username = session["user"]
    except:
        return redirect(url_for("login"))
    try:
        if session["logged"] == True:
            if username == "admin":
                return render_template("accounts.html", username=username)
            else:
                return redirect(url_for("login"))
        else:
            return redirect(url_for("login"))
    except:
        return redirect(url_for("login"))

@app.route("/admin/addaccount", methods=["POST"])
def addaccount():
    try:
        username = session["user"]
    except:
        return redirect(url_for("login"))
    try:
        if session["logged"] == True:
            try:
                if username == "admin":
                    try:
                        dump_yaml(request.form["username"], request.form["password"], "data/accounts.yml")
                        return render_template("accounts.html", username=username)
                    except:
                        return redirect(url_for("login"))
                else:
                    return redirect(url_for("login"))
            except:
                return redirect(url_for("login"))
        else:
            return redirect(url_for("login"))
    except:
        return redirect(url_for("login"))

@app.route("/admin/delaccount", methods=["POST"])
def delaccount():
    try:
        username = session["user"]
    except:
        return redirect(url_for("login"))
    try:
        if session["logged"] == True:
            try:
                if username == "admin":
                    try:
                        if request.form["username"] == "admin":
                            return render_template("accounts.html", username=username)
                        else:
                            dump_yaml(request.form["username"], None, "data/accounts.yml")
                            return render_template("accounts.html", username=username)
                    except:
                        return redirect(url_for("login"))
                else:
                    return redirect(url_for("login"))
            except:
                return redirect(url_for("login"))
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
                session["logged"] = True
                session["user"] = username
                return "<meta http-equiv='refresh' content='0; url=/' />"
            else:
                return render_template("login.html")
        else:
            return render_template("login.html")
    else:
        return render_template("login.html")

@app.route("/logout/<user>", methods=["POST"])
def logout(user):
    session["logged"] = False
    return "<meta http-equiv='refresh' content='0; url=/login' />"

@app.route("/start/<user>/py", methods=["POST"])
def startpy(user):
    subprocess.call("pkill -f {}.index.py".format(user), shell=True)
    subprocess.Popen("python3 bot/{}.index.py".format(user), shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
    print(user + " heeft zijn python bot aangezet")
    return "<meta http-equiv='refresh' content='0; url=/control' />"


@app.route("/stop/<user>/py", methods=["POST"])
def stop(user):
    subprocess.call("pkill -f {}.index.py".format(user), shell=True)
    print(user + " heeft zijn python bot uitgezet")
    return "<meta http-equiv='refresh' content='0; url=/control' />"


@app.route("/start/<user>/js", methods=["POST"])
def startjs(user):
    subprocess.call("pkill -9 -f {}.index.js".format(user), shell=True)
    subprocess.Popen("node bot/{}.index.js".format(user), shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
    print(user + " heeft zijn javascript bot aangezet")
    return "<meta http-equiv='refresh' content='0; url=/control' />"

@app.route("/stop/<user>/js", methods=["POST"])
def stopjs(user):
    subprocess.call("pkill -9 -f {}.index.js".format(user), shell=True)
    print(user + " heeft zijn javascript bot uitgezet")
    return "<meta http-equiv='refresh' content='0; url=/control' />"

@app.route("/start/<user>/java", methods=["POST"])
def startjava(user):
    subprocess.call("pkill -9 -f {}.index.jar".format(user), shell=True)
    subprocess.Popen("java -jar bot/{}.index.jar".format(user), shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
    print(user + " heeft zijn javascript bot aangezet")
    return "<meta http-equiv='refresh' content='0; url=/control' />"

@app.route("/stop/<user>/java", methods=["POST"])
def stopjava(user):
    subprocess.call("pkill -9 -f {}.index.jar".format(user), shell=True)
    print(user + " heeft zijn javascript bot uitgezet")
    return "<meta http-equiv='refresh' content='0; url=/control' />"

@app.route("/upload/<user>", methods=["POST"])
def upload(user):
    try:
        if 'file' not in request.files:
                flash('Geen bestand')
                return "<meta http-equiv='refresh' content='0; url=/upload' />"
    except:
        flash('Geen bestand')
        return "<meta http-equiv='refresh' content='0; url=/upload' />"
    file = request.files['file']
    print(file)
    if file and allowed_file(file.filename):
        filename = secure_filename(user + "." + file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return "<meta http-equiv='refresh' content='0; url=/upload' />"
    else:
        return "<meta http-equiv='refresh' content='0; url=/upload' />"


if __name__ == "__main__":
    app.run(debug=True, port=10000, host="0.0.0.0")
