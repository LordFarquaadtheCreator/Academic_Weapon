import chromadb
from chromadb.utils import embedding_functions
from upload_data_to_db import upload_to_db


def encode_image(image) -> str:
    import io
    import base64

    byte_arr = io.BytesIO()
    image.save(byte_arr, format="JPEG")
    encoded_image = base64.b64encode(byte_arr.getvalue()).decode("utf-8")
    return encoded_image

async def image_to_text(image) -> object:
    from openai import OpenAI
    import json

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


async def add_data(dir: str, client):
    # recursive
    import os
    from pdf2image import convert_from_path

    dirs = os.listdir(dir)
    for path in dirs:
        if os.path.isdir(os.path.join(dir, path)):
            await add_data(os.path.join(dir, path), client)  # recursive call

        if os.path.join(dir, path).endswith(".pdf"):
            images = convert_from_path(os.path.join(dir, path))
            print(f"Processing {path}")
            for i, image in enumerate(images):
                encoded_image = encode_image(image)
                text = await image_to_text(encoded_image)
                upload_to_db(text)


if __name__ == "__main__":
    import asyncio
    asyncio.run(add_data("data/"))
