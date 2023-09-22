# https://qiita.com/nabata/items/86cb2ac5b3e345ea86a7
# 上記リンクを参考して作成

import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
image = openai.Image.create(
  prompt="a white laptop",
  size="256x256"
)
print(image["data"][0]["url"])
