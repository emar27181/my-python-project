import torch
import requests
from PIL import Image
from io import BytesIO
import random
from diffusers import StableDiffusionImg2ImgPipeline
from datetime import datetime
import json



device = "cuda"
pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
    "nitrosocke/Ghibli-Diffusion",
).to(device)
# init_image = Image.open("data/output/before/saveCanvas - 2023-10-10T194006.802.png").convert("RGB")
init_image = Image.open("data/output/after/img_to_img_after_2023-10-10_19-51-34.jpg").convert("RGB")
# init_image = Image.open("data/output/before/saveCanvas - 2023-10-05T212050.177.png").convert("RGB")
# init_image = Image.open("data/output/saveCanvas - 2023-10-10T124818.646.png").convert("RGB")
# init_image = Image.open("data/output/img_to_img_after_3.jpg").convert("RGB")
init_image.thumbnail((768, 768))
init_image

current_time = datetime.now()
current_time_str=current_time.strftime('%Y-%m-%d_%H-%M-%S')
file_name_before = 'data/output/before/img_to_img_before_{}.jpg'.format(current_time_str)
file_name_after = 'data/output/after/img_to_img_after_{}.jpg'.format(current_time_str)
random_number = random.randint(1, 1024)

with open(file_name_before, 'wb') as input_file:
    init_image.save(input_file, format='JPEG')


with open('data/input/input_prompt.txt', "r") as input_file:
    prompt = input_file.read()
generator = torch.Generator(device=device).manual_seed(random_number)
image = pipe(prompt=prompt, image=init_image, strength=0.75, guidance_scale=7.5, generator=generator).images[0]
image

with open(file_name_after, 'wb') as input_file:
    image.save(input_file, format='JPEG')
    
#json形式への書き出しと保存
new_data = {
    "prompt": prompt,
    "create_time": current_time_str,
    "seed": random_number
}

with open('data/log/log.json', 'r') as json_file:
    data = json.load(json_file)
    data.append(new_data)

with open('data/log/log.json', 'w') as json_file:
    json.dump(data, json_file, indent=2)
    
#コンソール出力
print(new_data)
print(f'before: {file_name_before}')
print(f'after : {file_name_after}')
    