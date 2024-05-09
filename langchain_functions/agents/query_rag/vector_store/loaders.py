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

    loader = JSONLoader(file_path=path, text_content=False, json_lines=True)
    return loader.load()


async def image_pages(path: str):
    image_content = await image_to_text(path)
    return image_content


def encode_image(image) -> str:
    """takes in pillow image"""
    import io
    import base64

    byte_arr = io.BytesIO()
    image.save(byte_arr, format="JPEG")
    encoded_image = base64.b64encode(byte_arr.getvalue()).decode("utf-8")
    return encoded_image


async def image_to_text(image_path: str) -> object:
    from openai import OpenAI
    import json
    from PIL import Image

    image = encode_image(Image.open(image_path))

    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-4-turbo",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Transcribe the contents of this image and return a JSON object that contains the text. It must be structured in the following manner: two entries with the following keys: 'content' and 'text'. Content will be a line describing what the content of text will be, and text will be a simple transcription of the image",
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64;,{image}",
                            "detail": "high",
                        },
                    },
                ],
            }
        ],
    )
    return json.loads(response.choices[0].message.content)
