# agents/besteci.py — Ajan 3: Besteci (Mistral önce, Claude fallback)
import anthropic
import httpx
import os
import json
from pathlib import Path
from dotenv import load_dotenv
from config import TEMALAR, SIIR_IMGE_MUZIK, DUYGU_NORMALIZASYON

env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

def muzik_tasarla(tema: str, duygu: str, siir: str, gorsel_analiz: dict) -> dict:
    duygu_norm = DUYGU_NORMALIZASYON.get(duygu, "huzur")
    tema_bilgi = TEMALAR[tema]
    tema_isim = tema_bilgi["isim"]
    tema_felsefi_soru = tema_bilgi["felsefi_soru"]

    yogunluk = gorsel_analiz.get("yogunluk", "orta")
    hareket = gorsel_analiz.get("hareket", "statik")
    renkler = gorsel_analiz.get("renkler", "")
    gorsel_detay = gorsel_analiz.get("gorsel_detay", "")

    siirden_imge = "sessizlik"
    for kelime, enstruman in SIIR_IMGE_MUZIK.items():
        if kelime in siir.lower():
            siirden_imge = kelime
            break

    prompt_icerik = f"""Sen bir film müziği bestecisi ajansısın.

TEMA: {tema_isim}
Felsefi soru: {tema_felsefi_soru}
DUYGU: {duygu_norm}
GÖRSEL: Renkler: {renkler} | Yoğunluk: {yogunluk} | Hareket: {hareket}
Detay: {gorsel_detay}
ŞİİR: {siir}
ŞİİRDEN İMGE: {siirden_imge}

MusicGen için müzik parametrelerini belirle.
Enstrümanlar: piano, violin, cello, flute, guitar, trumpet, drums, strings, orchestra.
Vatan temasında flute ve cello tercih et.

Sadece JSON döndür:
{{
  "ton": "D minör",
  "tempo": "Adagio",
  "bpm": 60,
  "enstruman_1": "piano",
  "enstruman_2": "cello",
  "muzik_prompt": "İngilizce 20-30 kelime, no vocals ile bitsin."
}}"""

    # Önce Mistral dene
    sonuc = _mistral_ile_dene(prompt_icerik)
    
    # Mistral başarısızsa Claude
    if not sonuc:
        print("Besteci: Mistral başarısız, Claude fallback devreye giriyor")
        sonuc = _claude_ile_dene(prompt_icerik)
    
    # İkisi de başarısızsa sabit fallback
    if not sonuc:
        sonuc = _sabit_fallback(tema, duygu_norm, yogunluk, hareket)

    sonuc["siirden_alinan_imge"] = siirden_imge
    return sonuc


def _mistral_ile_dene(prompt: str) -> dict:
    try:
        mistral_prompt = f"<s>[INST] {prompt} [/INST]"
        response = httpx.post(
            "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3",
            headers={"Authorization": f"Bearer {os.getenv('HF_TOKEN')}"},
            json={
                "inputs": mistral_prompt,
                "parameters": {
                    "max_new_tokens": 300,
                    "temperature": 0.4,
                    "return_full_text": False,
                }
            },
            timeout=30.0
        )
        data = response.json()
        if isinstance(data, list) and len(data) > 0:
            metin = data[0].get("generated_text", "").strip()
            return _json_coz(metin)
    except Exception as e:
        print(f"Mistral hata: {e}")
    return None


def _claude_ile_dene(prompt: str) -> dict:
    try:
        client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        mesaj = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=400,
            messages=[{"role": "user", "content": prompt}]
        )
        metin = mesaj.content[0].text.strip()
        return _json_coz(metin)
    except Exception as e:
        print(f"Claude besteci hata: {e}")
    return None


def _json_coz(metin: str) -> dict:
    try:
        if "```" in metin:
            metin = metin.split("```")[1]
            if metin.startswith("json"):
                metin = metin[4:]
        if "{" in metin and "}" in metin:
            metin = metin[metin.find("{"):metin.rfind("}")+1]
        sonuc = json.loads(metin.strip())
        return {
            "ton": sonuc.get("ton", "A minör"),
            "tempo": sonuc.get("tempo", "Andante"),
            "bpm": int(sonuc.get("bpm", 72)),
            "enstruman_1": sonuc.get("enstruman_1", "piano"),
            "enstruman_2": sonuc.get("enstruman_2", "strings"),
            "muzik_prompt": sonuc.get("muzik_prompt", "piano and strings, emotional, no vocals"),
        }
    except:
        return None


def _sabit_fallback(tema: str, duygu: str, yogunluk: str, hareket: str) -> dict:
    bpm_map = {
        "agirlik": 46, "kirilma": 54, "umut": 80, "huzur": 64,
        "ofke": 120, "yalnizlik": 48, "ozgurluk": 100
    }
    bpm = bpm_map.get(duygu, 72)
    if yogunluk == "yuksek":
        bpm = min(bpm + 16, 160)
    elif yogunluk == "dusuk":
        bpm = max(bpm - 12, 36)
    if hareket == "dinamik":
        bpm = min(bpm + 8, 160)

    prompt_map = {
        ("ask", "agirlik"): "solo piano, slow melancholic, heartbreak, cinematic, no vocals",
        ("ask", "umut"): "piano and violin, hopeful romantic, warm crescendo, no vocals",
        ("ask", "ofke"): "dramatic strings, passionate, fire and intensity, no vocals",
        ("olum", "agirlik"): "deep cello, heavy orchestra, funeral march, dark grief, no vocals",
        ("olum", "huzur"): "ambient strings, peaceful acceptance, ethereal, no vocals",
        ("olum", "yalnizlik"): "solo cello, lonely minimal, silence between notes, no vocals",
        ("vatan", "yalnizlik"): "solo flute, exile loneliness, hollow echo, deeply sad, no vocals",
        ("vatan", "ozgurluk"): "trumpet and drums, national celebration, triumphant, no vocals",
        ("vatan", "ofke"): "powerful drums and trumpet, resistance march, bold, no vocals",
    }
    enstruman_map = {
        "ask": ("piano", "violin"),
        "olum": ("cello", "strings"),
        "vatan": ("flute", "cello"),
    }
    e1, e2 = enstruman_map.get(tema, ("piano", "strings"))
    muzik_prompt = prompt_map.get((tema, duygu), f"piano and strings, {duygu}, emotional, no vocals")

    return {
        "ton": "A minör",
        "tempo": "Andante",
        "bpm": bpm,
        "enstruman_1": e1,
        "enstruman_2": e2,
        "muzik_prompt": muzik_prompt,
    }
