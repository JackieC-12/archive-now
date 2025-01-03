from flask import Blueprint, request
from app.models import db, Archive
from app.forms import ArchiveForm

archive_routes = Blueprint('archive', __name__)

# '''
# GET specific archive by ID
# '''
# @archive_routes.route("/<id>", methods=["GET"])
# def archive(id):

'''
POST new archive
'''

@archive_routes.route("/new", methods=["POST"])
def new_archive():
    form = ArchiveForm()

    if form.validate_on_submit():
        archive = Archive()
        form.populate_obj(archive)
        db.session.add(archive)
        db.session.commit()
        return
    return form.errors, 401
