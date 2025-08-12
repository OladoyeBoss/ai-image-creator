import shutil
import requests

def save_image(src, dst):
    shutil.copy(src, dst)

def save_image_from_url(url, dst):
    response = requests.get(url, stream=True, timeout=40)
    if response.status_code == 200:
        with open(dst, "wb") as out_file:
            shutil.copyfileobj(response.raw, out_file)
    else:
        raise Exception(f"Failed to download image from {url}")