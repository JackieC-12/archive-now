from flask import Blueprint, render_template, redirect, request
from flask_login import current_user
from app.models import Archive, db
from app.forms import ArchiveForm
from app.api.aws_helpers import upload_file_to_s3, get_unique_filename, convert_url_to_pdf, PDF


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

    form["csrf_token"].data = request.cookies["csrf_token"]

    if request.method == "POST":
        if form.validate_on_submit():
            archive = Archive()
            form.populate_obj(archive)
            archive.userId = current_user.id

            filename = get_unique_filename(archive.title + '.pdf')
            fileUrl = archive.url

            newPDF = PDF(filename, fileUrl)

            upload = upload_file_to_s3(newPDF)

            print(upload)

            archive.fileLink = upload["url"]

            db.session.add(archive)
            db.session.commit()
            return redirect("/")
    return render_template("simple_form.html", form=form)

