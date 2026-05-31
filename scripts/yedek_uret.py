# scripts/yedek_uret.py — 21 yedek MP3 üret
import sys
import os
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from dotenv import load_dotenv
load_dotenv(Path(__file__).parent.parent / ".env")

import replicate
import httpx

KOMBINASYONLAR = [
    ("ask", "agirlik", "solo piano, slow melancholic, heartbreak, cinematic, no vocals"),
    ("ask", "kirilma", "piano and cello, bittersweet fragile melody, emotional, no vocals"),
    ("ask", "umut", "piano and violin, hopeful romantic, warm crescendo, no vocals"),
    ("ask", "huzur", "soft piano, gentle strings, peaceful, tender, no vocals"),
    ("ask", "ofke", "dramatic strings, passionate intense, fire and emotion, no vocals"),
    ("ask", "yalnizlik", "solo piano, lonely melody, empty space, minimal, no vocals"),
    ("ask", "ozgurluk", "violin and piano, soaring uplifting, liberation, no vocals"),
    ("olum", "agirlik", "deep cello, heavy orchestra, funeral march, dark grief, no vocals"),
    ("olum", "kirilma", "cello and piano, broken melody, tragic fragile, no vocals"),
    ("olum", "umut", "piano solo, hopeful despite sadness, light through darkness, no vocals"),
    ("olum", "huzur", "ambient strings, peaceful acceptance, ethereal calm, no vocals"),
    ("olum", "ofke", "dramatic orchestra, rage, powerful brass, dark energy, no vocals"),
    ("olum", "yalnizlik", "solo cello, lonely minimal, silence between notes, no vocals"),
    ("olum", "ozgurluk", "soaring strings, transcendent ascending, peaceful release, no vocals"),
    ("vatan", "agirlik", "flute and cello, heavy longing, exile grief, slow mournful, no vocals"),
    ("vatan", "kirilma", "flute and strings, broken exile, displacement, fragile, no vocals"),
    ("vatan", "umut", "flute and violin, hopeful return, homeland dream, warm folk, no vocals"),
    ("vatan", "huzur", "flute solo, peaceful memory, Anatolian folk, calm warm, no vocals"),
    ("vatan", "ofke", "drums and trumpet, resistance march, powerful bold, no vocals"),
    ("vatan", "yalnizlik", "solo flute, exile loneliness, hollow echo, deeply sad, no vocals"),
    ("vatan", "ozgurluk", "trumpet and drums, national celebration, triumphant march, no vocals"),
]

def uret():
    cikti_dizin = Path(__file__).parent.parent / "static" / "audio"
    cikti_dizin.mkdir(parents=True, exist_ok=True)

    token = os.getenv("REPLICATE_API_TOKEN", "")
    client = replicate.Client(api_token=token)

    for tema, duygu, prompt in KOMBINASYONLAR:
        dosya = cikti_dizin / f"fallback_{tema}_{duygu}.mp3"
        if dosya.exists():
            print(f"✓ Zaten var: {dosya.name}")
            continue

        print(f"⏳ Üretiliyor: {tema}_{duygu}...")
        try:
            output = client.run(
                "meta/musicgen:671ac645ce5e552cc63a54a2bbff63fcf798043055d2dac5fc9e36a837eedcfb",
                input={
                    "prompt": prompt,
                    "model_version": "melody-large",
                    "output_format": "mp3",
                    "duration": 30,
                }
            )
            muzik_url = str(output)
            with httpx.Client(timeout=120.0) as http:
                r = http.get(muzik_url)
                dosya.write_bytes(r.content)
            print(f"✅ Tamamlandı: {dosya.name}")
        except Exception as e:
            print(f"❌ Hata: {tema}_{duygu} — {e}")

if __name__ == "__main__":
    uret()