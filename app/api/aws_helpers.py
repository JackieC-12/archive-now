import boto3
import botocore
import os
import uuid
import pdfkit
import io

class PDF:
    def __init__(self, name, url):
        self.name = name
        self.url = url

BUCKET_NAME = os.environ.get("S3_BUCKET")
S3_LOCATION = f"http://{BUCKET_NAME}.s3.amazonaws.com/"
ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg", "gif"}

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.environ.get("S3_KEY"),
    aws_secret_access_key=os.environ.get("S3_SECRET")
)

# Filename Helper Function
def get_unique_filename(filename):
    ext = filename.rsplit(".", 1)[1].lower()
    unique_filename = uuid.uuid4().hex
    return f"{unique_filename}.{ext}"


# Upload File Helper Function
def upload_file_to_s3(file, acl="public-read"):
    pdf_stream = convert_url_to_pdf(file.url)

    pdf_stream.seek(0)

    try:
        s3.upload_fileobj(
            pdf_stream,
            BUCKET_NAME,
            file.name,
            ExtraArgs={
                "ACL": acl,
                "ContentType": 'application/pdf'
            }
        )

    except Exception as e:
        # in case the your s3 upload fails
        return {"errors": str(e)}

    return {"url": f"{S3_LOCATION}{file.name}"}

# Convert HTML to PDF Helper Function
def convert_url_to_pdf(url):
    try:
        pdf_output = pdfkit.from_url(url)
        print(f"PDF generated")

        pdf_stream = io.BytesIO(pdf_output)
        return pdf_stream
    except Exception as e:
        print(f"PDF generation failed: {e}")

# Remove File Helper Function
def remove_file_from_s3(image_url):
    # AWS needs the image file name, not the URL,
    # so you split that out of the URL
    key = image_url.rsplit("/", 1)[1]
    try:
        s3.delete_object(
        Bucket=BUCKET_NAME,
        Key=key
        )
    except Exception as e:
        return { "errors": str(e) }
    return True
