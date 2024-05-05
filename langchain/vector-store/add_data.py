from upload_data_to_db import upload_to_db

def add_file(path: str):
    """ will add data to database   """
    import os

    if os.path.join(path).endswith(".pdf"):
        from loaders import pdf_pages
        upload_to_db(pdf_pages(path))

    if os.path.join(path).endswith(".html"):
        from loaders import html_pages
        upload_to_db(html_pages(path))

    if os.path.join(path).endswith(".json"):
        from loaders import json_pages
        upload_to_db(json_pages(path))

    if os.path.join(path).endswith(".jpg") or os.path.join(path).endswith(".png"):
        from loaders import image_pages
        upload_to_db(image_pages(path))

    if os.path.join(path).endswith(".txt"):
        from loaders import text_pages
        upload_to_db(text_pages(path))

    raise Exception("File type not supported - got ${path}")

def add_text(string: str):
    """ will add data to database   """
    if type(string) == "string":
        from loaders import text_pages
        upload_to_db(text_pages(string))
        return 

    raise Exception("Input not a string - got ${string}")