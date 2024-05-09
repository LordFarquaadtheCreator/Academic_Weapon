from agents.query_rag.vector_store.upload_data_to_db import upload_to_db


async def add_file(path: str):
    """will add data to database"""
    import os

    if os.path.join(path).endswith(".pdf"):
        from agents.query_rag.vector_store.loaders import pdf_pages

        await upload_to_db(pdf_pages(path))

    if os.path.join(path).endswith(".html"):
        from agents.query_rag.vector_store.loaders import html_pages

        await upload_to_db(html_pages(path))

    if os.path.join(path).endswith(".json"):
        from agents.query_rag.vector_store.loaders import json_pages

        await upload_to_db(json_pages(path))

    if os.path.join(path).endswith(".jpg") or os.path.join(path).endswith(".png"):
        from agents.query_rag.vector_store.loaders import image_pages

        await add_text(image_pages(path))

    if os.path.join(path).endswith(".txt"):
        from agents.query_rag.vector_store.loaders import text_pages

        await upload_to_db(text_pages(path))

    raise Exception("File type not supported - got ${path}")


async def add_text(string: str):
    """will add data to database"""
    if isinstance(string, str):
        from agents.query_rag.vector_store.upload_data_to_db import upload_text

        await upload_text(string)
        return

    raise Exception("Input not a string - got ${string}")
