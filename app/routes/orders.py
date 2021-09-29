from flask import Blueprint, render_template, url_for
from flask_login import login_required

bp = Blueprint("orders", __name__, url_prefix="")


@bp.route("/")
@login_required
def index():
    return render_template("orders.html", )
