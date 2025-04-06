import json
from flask import Blueprint, request, render_template, jsonify
from services.scraper import scrape_file, scrape_url,get_mdata

routes = Blueprint("routes", __name__)

@routes.route("/")
def index():
    return render_template("index.html")


@routes.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "No file part", 400
    file = request.files["file"]
    if file.filename == "":
        return "No selected file", 400
    return f"Extracted Title: {scrape_file(file)}"


@routes.route("/scrape", methods=["POST"])
def scrape_from_url():
    url = request.form.get("url")
    if not url:
        return "URL is required", 400
    return f"Extracted Title: {scrape_url(url)}"

@routes.route("/showdata",methods=["GET"])
def get_data():
    data = get_mdata()
    return jsonify(data) if data else"error"
