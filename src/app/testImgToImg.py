import torch
import requests
from PIL import Image
from io import BytesIO
import random
from diffusers import StableDiffusionImg2ImgPipeline
from datetime import datetime
import json
from googletrans import Translator

device = "cuda"
pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
    "nitrosocke/Ghibli-Diffusion",
).to(device)

with open('data/input/input_file_path.txt') as input_file:
    input_file_path = input_file.read()
 
init_image = Image.open(input_file_path).convert("RGB")
init_image.thumbnail((768, 768))
init_image

current_time = datetime.now()
current_time_str=current_time.strftime('%Y-%m-%d_%H-%M-%S')
output_file_path = 'data/output/after/img_to_img_after_{}.jpg'.format(current_time_str)
random_number = random.randint(1, 1024)
strength_value=0.75
guidance_scale_value=7.5

with open('data/input/input_prompt.txt', "r") as input_file:
    prompt_ja = input_file.read()
translator = Translator()
prompt_en = translator.translate(prompt_ja, src='ja', dest='en').text

generator = torch.Generator(device=device).manual_seed(random_number)
image = pipe(prompt=prompt_en, image=init_image, strength=strength_value, guidance_scale=guidance_scale_value, generator=generator).images[0]
image

with open(output_file_path, 'wb') as input_file:
    image.save(input_file, format='JPEG')
    
#json形式への書き出しと保存
new_data = {
    "prompt_ja": prompt_ja, 
    "prompt_en": prompt_en,
    "create_time": current_time_str,
    "seed": random_number,
    "strength": strength_value,
    "guidance_scale": guidance_scale_value,
    "input_file": input_file_path, 
    "output_file": output_file_path
}

with open('data/log/log.json', 'r') as json_file:
    data = json.load(json_file)
    data.append(new_data)

with open('data/log/log.json', 'w') as json_file:
    json.dump(data, json_file, indent=2)
    
#コンソール出力
print(new_data)
print(f'before: {input_file_path}')
print(f'after : {output_file_path}')
    