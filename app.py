from flask import Flask, render_template, request
app = Flask(__name__)

entries = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        mood = request.form.get("mood")
        note = request.form.get("note")
        entries.append((mood, note))
    return render_template("index.html", entries=entries)

if __name__ == "__main__":
    app.run(debug=True)
