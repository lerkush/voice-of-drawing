# main.py — FastAPI Backend
import os
import uuid
from pathlib import Path
from dotenv import load_dotenv

# Mutlak yol ile .env yükle ve environment'a işle
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

# Token'ları kontrol et
print("ANTHROPIC:", os.getenv("ANTHROPIC_API_KEY", "YOK")[:15])
print("HF_TOKEN:", os.getenv("HF_TOKEN", "YOK")[:15])
print("REPLICATE:", os.getenv("REPLICATE_API_TOKEN", "YOK")[:15])

from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware

from database import init_db, kaydet, getir_hepsini, getir_uuid
from agents.gorsel_analist import gorseli_analiz_et
from agents.sair import siir_yaz
from agents.besteci import muzik_tasarla
from agents.ses_veren import muzik_uret

app = FastAPI(title="Voice of Drawing — Çizginin Sesi")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/audio", StaticFiles(directory="audio"), name="audio")

@app.on_event("startup")
def startup():
    init_db()
    Path("audio").mkdir(exist_ok=True)
    Path("static/audio").mkdir(parents=True, exist_ok=True)

@app.get("/")
def ana_sayfa():
    return FileResponse("static/index.html")

@app.post("/api/isle")
async def isle(
    dosya: UploadFile = File(...),
    tema: str = Form(...)
):
    if tema not in ["ask", "olum", "vatan"]:
        raise HTTPException(status_code=400, detail="Geçersiz tema")

    gorsel_bytes = await dosya.read()
    eser_id = uuid.uuid4().hex

    try:
        gorsel_analiz = gorseli_analiz_et(gorsel_bytes, tema)
        duygu = gorsel_analiz.get("duygu", "huzur")

        siir_sonuc = siir_yaz(tema, duygu, gorsel_analiz.get("gorsel_detay", ""))
        sair = siir_sonuc["sair"]
        siir = siir_sonuc["siir"]
        neden = siir_sonuc["neden"]

        muzik_tasarim = muzik_tasarla(tema, duygu, siir, gorsel_analiz)

        ses_sonuc = muzik_uret(muzik_tasarim["muzik_prompt"], tema, duygu)

        kaydet(
            uuid=eser_id,
            tema=tema,
            gorsel_analiz=str(gorsel_analiz),
            duygu=duygu,
            sair=sair,
            siir=siir,
            muzik_prompt=muzik_tasarim["muzik_prompt"],
            muzik_url=ses_sonuc["muzik_url"],
            muzik_lokal=ses_sonuc["muzik_lokal"],
            siirden_alinan_imge=muzik_tasarim["siirden_alinan_imge"],
            ton=muzik_tasarim["ton"],
            tempo=muzik_tasarim["tempo"],
            bpm=muzik_tasarim["bpm"],
            enstruman_1=muzik_tasarim["enstruman_1"],
            enstruman_2=muzik_tasarim["enstruman_2"],
        )

        return JSONResponse({
            "uuid": eser_id,
            "tema": tema,
            "gorsel_analiz": gorsel_analiz,
            "sair": sair,
            "sair_neden": neden,
            "siir": siir,
            "muzik_tasarim": muzik_tasarim,
            "muzik_url": ses_sonuc["muzik_url"],
            "muzik_lokal": ses_sonuc["muzik_lokal"],
            "basarili": ses_sonuc["basarili"],
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/eserler")
def eserler():
    return getir_hepsini()

@app.get("/api/eser/{uuid}")
def eser_getir(uuid: str):
    eser = getir_uuid(uuid)
    if not eser:
        raise HTTPException(status_code=404, detail="Eser bulunamadı")
    return eser

@app.get("/health")
def health():
    return {"durum": "çalışıyor", "proje": "Voice of Drawing"}