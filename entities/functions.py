# Reference : https://www.javatpoint.com/django-file-upload

from datetime import datetime


def handle_uploaded_file(file_object):
    if file_object is not None:
        incoming_file_name = file_object.name
        file_extension = incoming_file_name.split('.')[1]

        # make Unique file name for the uploading file
        # Sample filename :
        upload_file_name = "entity_" + str(datetime.now())
        upload_file_name = upload_file_name.replace("-", "")
        upload_file_name = upload_file_name.replace(":", "")
        upload_file_name = upload_file_name.replace(".", "")
        upload_file_name = upload_file_name.replace(" ", "")
        upload_file_name = upload_file_name + "." + file_extension
        try:
            with open('entities/static/upload/entities/' + upload_file_name, 'wb+') as destination:
                for chunk in file_object.chunks():
                    destination.write(chunk)
            return upload_file_name
        except:
            return None
    else:
        return None
