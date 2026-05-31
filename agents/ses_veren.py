# agents/ses_veren.py
import replicate
import httpx
import os
import uuid as uuid_lib
from pathlib import Path

AUDIO_DIR = Path("audio")
AUDIO_DIR.mkdir(exist_ok=True)

def muzik_uret(muzik_prompt: str, tema: str, duygu: str) -> dict:
    dosya_adi = f"{uuid_lib.uuid4().hex}.mp3"
    lokal_yol = AUDIO_DIR / dosya_adi

    try:
        # Token'ı her çağrıda environment'dan al
        token = os.getenv("REPLICATE_API_TOKEN", "")
        print(f"MuzikUret token: {token[:15]}")
        client = replicate.Client(api_token=token)
        
        output = client.run(
            "meta/musicgen:671ac645ce5e552cc63a54a2bbff63fcf798043055d2dac5fc9e36a837eedcfb",
            input={
                "prompt": muzik_prompt,
                "model_version": "melody-large",
                "output_format": "mp3",
                "normalization_strategy": "peak",
                "duration": 30,
            }
        )

        if isinstance(output, str):
            muzik_url = output
        elif isinstance(output, list) and len(output) > 0:
            muzik_url = str(output[0])
        elif hasattr(output, 'url') and callable(output.url):
            muzik_url = output.url()
        else:
            muzik_url = str(output)

        with httpx.Client(timeout=120.0) as client:
            r = client.get(muzik_url)
            lokal_yol.write_bytes(r.content)

        return {
            "muzik_url": f"/audio/{dosya_adi}",
            "muzik_lokal": str(lokal_yol),
            "basarili": True
        }

    except Exception as e:
        print(f"MusicGen hata: {e}")
        return {
            "muzik_url": "",
            "muzik_lokal": "",
            "basarili": False,
            "hata": str(e)
        }