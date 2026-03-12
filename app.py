from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/caregivers")
def caregivers():
    return render_template("caregivers.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/upload", methods=["GET","POST"])
def upload():
    if request.method == "POST":
        file = request.files["report"]
        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)
            return "Report uploaded successfully!"
    return render_template("upload.html")

@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")

@app.route("/grievance", methods=["GET","POST"])
def grievance():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        complaint = request.form["complaint"]

        with open("complaints.txt","a") as f:
            f.write(name + " | " + email + " | " + complaint + "\n")

        return "Complaint submitted successfully!"

    return render_template("grievance.html")

if __name__ == "__main__":
    app.run(debug=True)