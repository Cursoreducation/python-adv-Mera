from flask import Blueprint, redirect, url_for, flash, render_template
from flask_login import login_required

from app.models import Recipient

recipient_blueprint = Blueprint("recipient", __name__)


@recipient_blueprint.route("/recipients", methods=["GET", "POST"])
@login_required
def list():
    recipients = Recipient.query.all()
    return render_template("recipient/list.html", recipients=recipients)
