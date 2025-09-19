from flask import Blueprint, render_template, send_from_directory, current_app
import os


main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return render_template("index.html")


@main_bp.route("/curtain")
def curtain():
    return render_template("curtain.html")


@main_bp.route("/assets/<path:filename>")
def assets(filename: str):
    # Serve existing static assets from the old project without moving them
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "Meesho-Clone"))
    return send_from_directory(base_dir, filename)


