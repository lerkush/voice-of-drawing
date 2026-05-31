# database.py
import sqlite3

DB_PATH = "cizginin_sesi.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS eserler (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            uuid TEXT UNIQUE NOT NULL,
            tema TEXT NOT NULL,
            gorsel_analiz TEXT,
            duygu TEXT,
            sair TEXT,
            siir TEXT,
            muzik_prompt TEXT,
            muzik_url TEXT,
            muzik_lokal TEXT,
            siirden_alinan_imge TEXT,
            ton TEXT,
            tempo TEXT,
            bpm INTEGER,
            enstruman_1 TEXT,
            enstruman_2 TEXT,
            olusturulma TEXT DEFAULT CURRENT_TIMESTAMP,
            durum TEXT DEFAULT 'isleniyor'
        )
    """)
    conn.commit()
    conn.close()

def kaydet(uuid, tema, gorsel_analiz, duygu, sair, siir,
           muzik_prompt, muzik_url, muzik_lokal,
           siirden_alinan_imge, ton, tempo, bpm, enstruman_1, enstruman_2):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        INSERT OR REPLACE INTO eserler
        (uuid, tema, gorsel_analiz, duygu, sair, siir,
         muzik_prompt, muzik_url, muzik_lokal,
         siirden_alinan_imge, ton, tempo, bpm, enstruman_1, enstruman_2, durum)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'tamamlandi')
    """, (uuid, tema, gorsel_analiz, duygu, sair, siir,
          muzik_prompt, muzik_url, muzik_lokal,
          siirden_alinan_imge, ton, tempo, bpm, enstruman_1, enstruman_2))
    conn.commit()
    conn.close()

def getir_hepsini():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM eserler WHERE durum='tamamlandi' ORDER BY olusturulma DESC")
    rows = [dict(r) for r in c.fetchall()]
    conn.close()
    return rows

def getir_uuid(uuid):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM eserler WHERE uuid=?", (uuid,))
    row = c.fetchone()
    conn.close()
    return dict(row) if row else None

if __name__ == "__main__":
    init_db()
    print("✅ Veritabanı hazır.")