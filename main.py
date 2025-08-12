import requests
import os
from utils import save_image_from_url

def try_api(api_url, params):
    try:
        response = requests.get(api_url, params=params, timeout=10)  # Reduced timeout
        response.raise_for_status()
        try:
            data = response.json()
        except Exception:
            print(f"Invalid JSON from {api_url}: {response.text}")
            return None
        image_url = data.get("image") or data.get("url")
        if image_url:
            return image_url
    except Exception as e:
        print(f"API {api_url} failed: {e}")
    return None

def generate_image(prompt):
    apikey = "gifted"  # Update to your real key if/when you get one!
    safe_prompt = prompt.replace(" ", "_")
    output_path = f"static/images/{safe_prompt}.png"
    params = {"apikey": apikey, "prompt": prompt}

    # 1. Try FluxIMG API
    fluximg_url = "https://api.giftedtech.co.ke/api/ai/fluximg"
    image_url = try_api(fluximg_url, params)
    if not image_url:
        # 2. Try Stable Diffusion API
        sd_url = "https://api.giftedtech.co.ke/api/ai/sd"
        image_url = try_api(sd_url, params)
    if not image_url:
        # 3. Try DeepIMG API
        deepimg_url = "https://api.giftedtech.co.ke/api/ai/deepimg"
        image_url = try_api(deepimg_url, params)
    if not image_url:
        # 4. Try Vision API
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
