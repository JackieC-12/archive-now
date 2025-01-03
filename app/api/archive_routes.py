from flask import Blueprint, render_template, redirect, request
from app.models import db, Archive
from app.forms import ArchiveForm

archive_routes = Blueprint('archive', __name__, url_prefix='/archive')

# '''
# GET specific archive by ID
# '''

@archive_routes.route('/')
def archive_home():
    return render_template("main_page.html")

'''
POST new archive
'''
@archive_routes.route("/new", methods=["GET", "POST"])
def new_archive():
    form = ArchiveForm()

    if request.method == "POST":
        if form.validate_on_submit():
            archive = Archive()
            form.populate_obj(archive)

            url = archive.url
            print(url)
            
            db.session.add(archive)
            db.session.commit()
            return redirect("/")
    return render_template("simple_form.html", form=form)


# @archive_routes.route("/new", methods=["GET", "POST"])
# def new_archive():
#     form = ArchiveForm()

#     if request.method == "POST":
#         if form.validate_on_submit():
#             archive = Archive()
#             form.populate_obj(archive)

#             url = archive.url

#             print(url)

#             db.session.add(archive)
#             db.session.commit()
#             return redirect("/home")
#     return render_template("simple_form.html", form=form)
