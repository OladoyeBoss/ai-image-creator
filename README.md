# AI Image Creator

A beautiful web application for generating AI images from text prompts using three fallback APIs (GiftedTech Stable Diffusion, DeepImg, Vision).

## Features

- Modern, responsive UI with Bootstrap.
- Generates images from user prompts using three AI APIs in fallback order:
    1. Stable Diffusion (`/api/ai/sd`)
    2. DeepIMG (`/api/ai/deepimg`)
    3. Vision (`/api/ai/vision`)
- If all fail, displays a placeholder image.
- Error feedback, loading spinner, and user prompt display.

## Setup

1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Create a `static/images/placeholder.png` file (any PNG image for fallback).

3. Run the app:

    ```bash
    python app.py
    ```

4. Go to `http://127.0.0.1:5000/` in your browser.

## Notes

- Uses a free API key (`gifted`) for demonstration. For production, secure your API keys.
- The Vision API uses a default seed image; you may update this logic for your use case.

---

**Enjoy creating with the power of AI!**