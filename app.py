from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nama = request.form.get("zahwa")
        return render_template("index.html", hasil=f"Halo, {nama}! selamat datang di ProjectFlask App 🚀")
    return render_template("index.html")

@app.route("/greet", methods=["POST"])
def greet():
    nama = request.form.get("zahwa")
    if not nama:
       name = "zahwa"
    return f"<h2>Halo, {nama}! selamat datang di ProjectFlask App 🚀</h2>"

if __name__ == "__main__":
    app.run(debug=True)