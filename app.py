# -*- coding: utf-8 -*-
"""동국홀딩스 2026 중간점검 시스템"""
import os

from flask import Flask, jsonify, redirect, url_for

from midtermperformance import performance_bp

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dgh_2026_admin_secret")
app.register_blueprint(performance_bp)


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/")
def index():
    return redirect(url_for("performance.login_page"))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    debug = os.environ.get("FLASK_DEBUG", "true").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=debug)
