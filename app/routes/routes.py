"""This module contains the routes to your different views"""

from flask import Blueprint, render_template

bp = Blueprint("home", __name__, url_prefix="")


@bp.get("/")
def hello_world():
    return render_template("layouts/generic.html")
