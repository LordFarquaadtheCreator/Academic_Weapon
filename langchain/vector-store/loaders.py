def pdf_pages(pdf_path: str):
    """Will return all strings in pdf given path"""
    from langchain_community.document_loaders import PyPDFLoader

    loader = PyPDFLoader(pdf_path)

    return loader.load_and_split()


def html_pages(path: str):
    from langchain_community.document_loaders import UnstructuredHTMLLoader

    loader = UnstructuredHTMLLoader(path)

    return loader.load()

def json_pages(path: str):
    from langchain_community.document_loaders import JSONLoader

    loader = JSONLoader(
        file_path=path,
        text_content=False,
        json_lines=True
    )

    return loader.load()
