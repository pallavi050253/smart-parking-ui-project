from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import os, uuid
from src.parking_analyzer import analyze_image

app = Flask(__name__)
UPLOAD_DIR = "data/input"
RESULT_DIR = "results"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(RESULT_DIR, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    if request.method == "POST":
        file = request.files.get("image")
        if not file or not file.filename:
            error = "Please select a parking image."
        else:
            filename = secure_filename(file.filename)
            input_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4().hex[:8]}_{filename}")
            file.save(input_path)
            try:
                result = analyze_image(input_path, "data/config/parking_spaces.json", RESULT_DIR)
            except Exception as exc:
                error = str(exc)
    return render_template("index.html", result=result, error=error)

@app.route("/results/<path:filename>")
def results(filename):
    return send_from_directory(RESULT_DIR, filename)

if __name__ == "__main__":
    app.run(debug=True)
