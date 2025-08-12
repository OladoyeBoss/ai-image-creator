import requests
import os
from utils import save_image_from_url

def try_api(api_url, params):
    try:
        response = requests.get(api_url, params=params, timeout=40)
        response.raise_for_status()
        data = response.json()
        image_url = data.get("image") or data.get("url")
        if image_url:
            return image_url
    except Exception as e:
        print(f"API {api_url} failed: {e}")
    return None

def generate_image(prompt):
    apikey = "gifted"
    safe_prompt = prompt.replace(" ", "_")
    output_path = f"static/images/{safe_prompt}.png"
    params = {"apikey": apikey, "prompt": prompt}

    # 1. Try Stable Diffusion API
    sd_url = "https://api.giftedtech.co.ke/api/ai/sd"
    image_url = try_api(sd_url, params)
    if not image_url:
        # 2. Try DeepIMG API
        deepimg_url = "https://api.giftedtech.co.ke/api/ai/deepimg"
        image_url = try_api(deepimg_url, params)
    if not image_url:
        # 3. Try Vision API (special: needs a base image url, so we use a default, but user prompt is still sent)
        vision_url = "https://api.giftedtech.co.ke/api/ai/vision"
        vision_params = {
            "apikey": apikey,
            "prompt": prompt,
            "url": "https://files.giftedtech.web.id/image/mygifted.png"
        }
        image_url = try_api(vision_url, vision_params)
    if image_url:
        try:
            save_image_from_url(image_url, output_path)
            return output_path, None
        except Exception as e:
            print(f"Failed to save image: {e}")
            return "static/images/placeholder.png", "Error downloading image."
    return "static/images/placeholder.png", "All AI image APIs failed. Showing placeholder."
