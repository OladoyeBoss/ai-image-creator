from flask import Flask, render_template, request, send_from_directory
from main import generate_image
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    image_path = None
    if request.method == "POST":
        prompt = request.form.get("prompt")
        if prompt:
            image_path = generate_image(prompt)
    return render_template("index.html", image_path=image_path)

@app.route("/static/images/<filename>")
def send_image(filename):
    return send_from_directory("static/images", filename)

if __name__ == "__main__":
    app.run(debug=True)