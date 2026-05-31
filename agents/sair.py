# agents/sair.py — Ajan 2: Şair (Claude API)
import anthropic
import os
from pathlib import Path
from dotenv import load_dotenv
from config import SAIR_TEMA_DUYGU, SAIR_STIL, DUYGU_NORMALIZASYON, TEMALAR

env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

# poem_library opsiyonel
try:
    from poem_library import HAMMADDE
except ImportError:
    HAMMADDE = {}

def siir_yaz(tema: str, duygu: str, gorsel_detay: str) -> dict:
    duygu_norm = DUYGU_NORMALIZASYON.get(duygu, "huzur")
    sair = SAIR_TEMA_DUYGU.get((tema, duygu_norm), "Nazım Hikmet")
    sair_stil = SAIR_STIL.get(sair, "")
    tema_isim = TEMALAR[tema]["isim"]
    tema_felsefi_soru = TEMALAR[tema]["felsefi_soru"]
    neden = f"{tema_isim} teması + {duygu_norm} duygusu → {sair} sesi en uygun"

    # Meryem'in hammaddesi varsa ekle
    hammadde = HAMMADDE.get((tema, duygu_norm), {})
    dizeler = [d for d in hammadde.get("dizeler", []) if not d.startswith("#")]
    hammadde_str = ""
    if dizeler:
        hammadde_str = "\nMeryem Özden'in hammadde dizeleri (ilham al, kopyalama):\n"
        hammadde_str += "\n".join(f"- {d}" for d in dizeler)

    prompt = f"""Sen {sair} şiir dünyasından ilham alan bir şair sesisisin.

Tema: {tema_isim}
Felsefi soru: {tema_felsefi_soru}
Duygu: {duygu_norm}
Çizimden gelen: {gorsel_detay}

{sair} şiir özellikleri: {sair_stil}
{hammadde_str}

Türkçe, 4-5 dize yaz. O şairin sesinde, gerçek his ve imgeyle. Kalıp cümle değil. Sadece şiiri yaz, açıklama yapma."""

    try:
        client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        mesaj = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=300,
            messages=[{"role": "user", "content": prompt}]
        )
        siir = mesaj.content[0].text.strip()
        return {"sair": sair, "neden": neden, "siir": siir}

    except Exception as e:
        print(f"Şair hata: {e}")
        # Fallback — hammadde varsa kullan, yoksa minimal şiir
        if dizeler:
            return {"sair": sair, "neden": neden, "siir": "\n".join(dizeler[:4])}
        return {
            "sair": sair,
            "neden": neden,
            "siir": "Söylenemeyen bir şey var —\nçizgiler taşıyor onu\nkelimeler yerine."
        }