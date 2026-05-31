# agents/gorsel_analist.py — Ajan 1: Gözetleyici
import anthropic
import base64
import os
import io
from config import TEMALAR

def gorseli_sikistir(gorsel_bytes: bytes, max_kb: int = 800) -> bytes:
    """Görseli 800KB altına sıkıştır"""
    try:
        from PIL import Image
        img = Image.open(io.BytesIO(gorsel_bytes))
        # RGB'ye çevir (PNG alpha kanalı varsa)
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')
        # Boyutu küçült
        img.thumbnail((1024, 1024))
        output = io.BytesIO()
        quality = 85
        while quality > 20:
            output.seek(0)
            output.truncate()
            img.save(output, format='JPEG', quality=quality)
            if output.tell() <= max_kb * 1024:
                break
            quality -= 10
        return output.getvalue()
    except ImportError:
        # PIL yoksa olduğu gibi gönder
        return gorsel_bytes

def gorseli_analiz_et(gorsel_bytes: bytes, tema: str) -> dict:
    import json
    
    tema_bilgi = TEMALAR.get(tema, TEMALAR["ask"])
    felsefi_soru = tema_bilgi["felsefi_soru"]
    tema_isim = tema_bilgi["isim"]

    # Sıkıştır
    gorsel_bytes = gorseli_sikistir(gorsel_bytes)
    gorsel_b64 = base64.standard_b64encode(gorsel_bytes).decode("utf-8")

    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    prompt = f"""Sen bir sanat analisti ajansın. Felsefi bir bakışla çizimleri analiz ediyorsun.

Tema: {tema_isim}
Felsefi soru: {felsefi_soru}

Bu çizimi analiz et ve aşağıdaki JSON formatında yanıt ver:
{{
  "renkler": "çizimde gördüğün renkler veya renk yoksa karakalem/siyah-beyaz",
  "form": "çizimin genel formu ve şekilleri",
  "gorsel_detay": "çizimde ne görüyorsun, 2-3 cümle",
  "duygu": "tek kelime: agirlik/kirilma/umut/huzur/ofke/yalnizlik/ozgurluk",
  "yogunluk": "dusuk/orta/yuksek",
  "hareket": "statik/dinamik"
}}

Sadece JSON döndür, başka hiçbir şey yazma."""

    mesaj = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=600,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg",
                            "data": gorsel_b64,
                        },
                    },
                    {"type": "text", "text": prompt}
                ],
            }
        ],
    )

    metin = mesaj.content[0].text.strip()
    if "```" in metin:
        metin = metin.split("```")[1]
        if metin.startswith("json"):
            metin = metin[4:]

    try:
        return json.loads(metin.strip())
    except:
        return {
            "renkler": "belirsiz",
            "form": "serbest form",
            "gorsel_detay": "Çizim analiz edildi",
            "duygu": "huzur",
            "yogunluk": "orta",
            "hareket": "statik"
        }