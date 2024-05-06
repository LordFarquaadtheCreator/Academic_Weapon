# import pdf loader
from pdf2image import convert_from_path


# load all images from pdf
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

async def get_images():
    res = []
    images = convert_from_path("301-05.01.24.pdf")
    for i, image in enumerate(images):
        encoded_image = encode_image(image)
        text = await image_to_text(encoded_image)
        res.append(text)
        print(f"Page {i} transcribed")

    return res

# query gpt to translate images to text
async def query(text):
    from openai import OpenAI
    import json

    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "Your job is to answer the exercise posed and respond to the problem in LaTeX. It's a little deep into the query, but it's clearly labeled as an excercise. You can use any resources you like, but you must provide the LaTeX code for the text. If you don't have enough information, just ask for more information - but this should be enough information.",
                    },
                ],
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": str(text),
                    },
                ],
            },
        ],
    )
    return response.choices[0].message.content


# add all this context as a query to gpt and get latex code back
# save response to txt
def to_txt(text):
    with open("response.txt", "w") as f:
        f.write(str(text))

def load_txt():
    with open("response.txt", "r") as f:
        return f.read()

if __name__ == "__main__":
    import asyncio

    async def main():
        # images = await get_images()
        # to_txt(images)
        result = await query(load_txt())
        to_txt(result)

    asyncio.run(main())