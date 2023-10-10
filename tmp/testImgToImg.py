import torch
import requests
from PIL import Image
from io import BytesIO
from diffusers import StableDiffusionImg2ImgPipeline
from datetime import datetime
import json

current_time = datetime.now()

device = "cuda"
pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
    "nitrosocke/Ghibli-Diffusion",
).to(device)
init_image = Image.open("data/output/saveCanvas - 2023-10-05T212050.177.png").convert("RGB")
# init_image = Image.open("data/output/saveCanvas - 2023-10-10T124818.646.png").convert("RGB")
# init_image = Image.open("data/output/img_to_img_after_3.jpg").convert("RGB")
init_image.thumbnail((768, 768))
init_image

current_time_str=current_time.strftime('%Y-%m-%d_%H-%M-%S')
file_name_before = 'data/output/img_to_img_before_{}.jpg'.format(current_time_str)
file_name_after = 'data/output/img_to_img_after_{}.jpg'.format(current_time_str)

#with open('data/output/img_to_img.jpg', 'wb') as input_file:
with open(file_name_before, 'wb') as input_file:
    init_image.save(input_file, format='JPEG')

prompt = "meteor, oil painting, fantastic"
# prompt = "oil painting, Hellfire, fantastic, sacred water"
# prompt = "ukiyoe style, yellow mountain, beautiful lake and sea, orange villages"
# prompt = "ghibli style, a fantasy landscape with castles"
generator = torch.Generator(device=device).manual_seed(1024)
image = pipe(prompt=prompt, image=init_image, strength=0.75, guidance_scale=7.5, generator=generator).images[0]
image

with open(file_name_after, 'wb') as input_file:
    image.save(input_file, format='JPEG')
    
    
#json形式への書き出しと保存
    
new_data = {
    "prompt": "this is test text",
    "create_time": current_time_str
}

with open('data/log/log.json', 'r') as json_file:
    data = json.load(json_file)
    data.append(new_data)

with open('data/log/log.json', 'w') as json_file:
    json.dump(data, json_file, indent=2)
    