def get_content_type(filename):
    content_type = 'application/octet-stream'
    extension = filename.split('.')[-1].lower()
    if extension == 'gif':
        content_type = 'image/gif'
    elif extension == 'jpg' or extension == 'jpeg':
        content_type = 'image/jpeg'
    elif extension == 'png':
        content_type = 'image/png'
    elif extension == 'pdf':
        content_type = 'application/pdf'
    elif extension == 'txt':
        content_type = 'text/plain'
    elif extension == 'zip':
        content_type = 'application/zip'
    return content_type

filename = input("File name: ")
content_type = get_content_type(filename)
print(f"{content_type}")
