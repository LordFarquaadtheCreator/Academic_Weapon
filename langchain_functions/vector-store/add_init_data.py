from upload_data_to_db import upload_to_db
from langchain_community.document_loaders import PyPDFLoader
import os
from loaders import pdf_pages


def add_data_from_data_dir(dir: str):
    # recursive
    dirs = os.listdir(dir)

    for path in dirs:
        if os.path.isdir(os.path.join(dir, path)):  # if dir spotted, recurse into it
            add_data_from_data_dir(os.path.join(dir, path))  # recursive call

        if os.path.join(dir, path).endswith(".pdf"):
            print(f"Processing {path}")
            upload_to_db(pdf_pages(path))


if __name__ == "__main__":
    add_data_from_data_dir("data/")
