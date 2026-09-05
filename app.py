import os
from flask import Flask, request, render_template, redirect, url_for, flash, jsonify
from werkzeug.utils import secure_filename

from parser import parse_resume
import db

UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev-secret-key")
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # 10MB


@app.route("/")
def index():
    candidates = db.get_all_candidates()
    return render_template("index.html", candidates=candidates)


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("resume")
    if not file or file.filename == "":
        flash("Please choose a PDF file.")
        return redirect(url_for("index"))
    if not file.filename.lower().endswith(".pdf"):
        flash("Only PDF files are supported.")
        return redirect(url_for("index"))

    filename = secure_filename(file.filename)
    save_path = os.path.join(UPLOAD_DIR, filename)
    file.save(save_path)

    data = parse_resume(save_path, filename)
    db.insert_candidate(data)

    flash(f"Parsed and saved: {filename}")
    return redirect(url_for("index"))


@app.route("/candidate/<int:cid>")
def candidate_detail(cid):
    c = db.get_candidate(cid)
    if not c:
        return "Not found", 404
    return render_template("detail.html", c=c)


@app.route("/api/candidates")
def api_candidates():
    return jsonify(db.get_all_candidates())


db.init_db()

if __name__ == "__main__":
    app.run()
