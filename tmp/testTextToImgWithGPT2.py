# https://dev.classmethod.jp/articles/openai-create-images/
# 上記リンクを基に作成

import openai
import os
import base64

NUMBER_OF_IMAGES = 2

openai.api_key = os.environ["OPENAI_API_KEY"]

response = openai.Image.create(
    prompt="An impressionist painter's illustration of three calico cats playing together.",
    n=NUMBER_OF_IMAGES,
    size="512x512",
    response_format="b64_json",
)

for data, n in zip(response["data"], range(NUMBER_OF_IMAGES)):
    img_data = base64.b64decode(data["b64_json"])
    with open(f"image_{n}.png", "wb") as f:
        f.write(img_data)
