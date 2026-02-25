"""ソラトビコミックス LP用の画像を Gemini (Nano Banana) で生成するスクリプト"""
import os
import sys
from pathlib import Path
from google import genai
from google.genai import types

API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    print("[エラー] GEMINI_API_KEY が設定されていません")
    sys.exit(1)

client = genai.Client(api_key=API_KEY)
OUTPUT_DIR = Path(__file__).parent / "images"
OUTPUT_DIR.mkdir(exist_ok=True)

MODEL = "gemini-2.5-flash-image"

prompts = {
    "hero": (
        "A wide banner illustration for a comic promotion company called 'Soratobi Comics'. "
        "Pop and colorful style. A cute stylized blue bird flying upward carrying manga/comic books, "
        "with speech bubbles and comic effects (speed lines, stars) around it. "
        "Bright sky blue and white background with soft clouds. "
        "Modern, clean, professional yet fun. No text. Wide aspect ratio 16:9. "
        "Flat illustration style, vector-like quality."
    ),
    "service_manga": (
        "A small square icon illustration: a cute manga artist character drawing on a tablet, "
        "pop and colorful style, flat vector illustration, pastel colors, white background, simple and clean."
    ),
    "service_promo": (
        "A small square icon illustration: a megaphone with comic speech bubbles and stars coming out, "
        "pop and colorful style, flat vector illustration, bright colors, white background, simple and clean."
    ),
    "service_content": (
        "A small square icon illustration: a smartphone showing a comic panel with a play button, "
        "surrounded by social media reaction icons (hearts, likes), "
        "pop and colorful style, flat vector illustration, bright colors, white background, simple and clean."
    ),
    "service_promotion": (
        "A small square icon illustration: a blue bird character wearing a cape, "
        "holding up a comic book triumphantly, with sparkles and X/Twitter-like elements, "
        "pop and colorful style, flat vector illustration, bright colors, white background, simple and clean."
    ),
}

for name, prompt in prompts.items():
    print(f"[生成中] {name}...")
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE", "TEXT"],
            ),
        )

        saved = False
        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                ext = "png" if "png" in part.inline_data.mime_type else "jpg"
                out_path = OUTPUT_DIR / f"{name}.{ext}"
                out_path.write_bytes(part.inline_data.data)
                print(f"  → 保存: {out_path}")
                saved = True
                break

        if not saved:
            print(f"  [警告] {name}: 画像が返されませんでした")
            if response.candidates[0].content.parts:
                print(f"  テキスト応答: {response.candidates[0].content.parts[0].text[:200]}")

    except Exception as e:
        print(f"  [エラー] {name}: {e}")

print("\n[完了]")
