import os
from utils import save_image

def generate_image(prompt):
    # Placeholder: Replace with your AI model/image generation code
    # For now, just copy a placeholder image
    placeholder = "static/images/placeholder.png"
    output_path = f"static/images/{prompt.replace(' ', '_')}.png"
    save_image(placeholder, output_path)
    return output_path