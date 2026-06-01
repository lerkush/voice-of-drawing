# Çizginin Sesi — Voice of Drawing

> *Söylenemeyen şeyin de bir dili vardır.*

**ÜretJAM 2026** | Ankara Bilim Üniversitesi + Üretken Akademi | 30–31 Mayıs 2026

---

## Bir Cümleyle

İnsan söyleyemediğini çiziyor. Ajan o çizginin sesini buluyor, önce şiire, sonra müziğe dönüştürüyor.

---

## Felsefe

Dil bazen yetmez. Acı çok büyük, kelimeler çok küçük kalır. İnsan o anda çizmeye başlar — bilinçsizce, içgüdüyle. O çizgi bir şey taşır: söylenemeyen şeyi.

Çizginin Sesi, o çizgiyi dinler.

Sistem üç varoluşsal temayı işler: **Aşk**, **Ölüm**, **Vatan**. Her tema bir felsefi soruyla açılır. Ajan zinciri çizgiyi okur, duyguyu tespit eder, şiire ve müziğe dönüştürür. İnsan üretir, ajan yanıt verir — bu sıra değişmez.

---

## Sanat Dalları ve Kesişim Noktası

Çizginin Sesi tek bir sanat dalına ait değil. Üç sanat alanının kesişiminde duruyor:

**Görsel Sanat → Edebiyat → Müzik**

Bu zincir tesadüf değil, bilinçli bir tasarım. İnsan önce görsel üretiyor — kalemle, fırçayla, tabletle. Ajan o görseli okuyup duyguyu tespit ediyor. Türk şiir geleneğinden seçilen bir şairin üslubuyla o duyguyu dizeleştiriyor. Son olarak şiirden ve çizimden beslenerek 30 saniyelik bir müzik üretiyor.

Her sanat dalı bir öncekini taşıyor. Çizgi şiiri doğuruyor, şiir müziği.

**Bu proje ne çözüyor?**

İnsan bazen ne hissettiğini bilir ama anlatamaz. Kelimeleri yoktur. Terapide, sanatta, günlük hayatta — "bunu nasıl anlatsam bilmiyorum" denen o an. Çizginin Sesi, o anı bir giriş noktasına dönüştürüyor. Çiz, gerisini sistem halleder. Söylenemeyen şey önce şiire, sonra müziğe dönüşür — ve belki o zaman kelimeler de gelir.

**Neden bu üç tema?**

Aşk, Ölüm, Vatan — insanlığın en evrensel ve en söylenmesi zor üç duygusu. Her kültürde, her dilde bu üç tema var. Ve her birinde dil yetersiz kalır: Aşkı anlatmak onu küçültür. Ölümü konuşmak onu gerçekleştirir. Vatanı tarif etmek onu yok eder. Bu yüzden çizgi bu üç tema için en doğru giriş.

**Neden Türk şairleri?**

Türk şiiri söylenemeyen şeyi söyleme geleneğinde çok güçlü. Nazım Hikmet vatan acısını, Cemal Süreya aşkın bedenselliğini, Cahit Sıtkı ölümün sessizliğini kelimeyle değil imgeyle anlatır. Bu gelenek, yapay zekanın en iyi beslenebileceği hammadde.

---

## Eserler

Projede beş insan eseri var. Her çizim bir tema taşır. Ajan bu çizimleri işleyerek şiir ve müzik üretir.

### Ruhların Kokusu — Zeynep Toprak | Aşk
İki beden yok — sadece elbiseler var. Pembe gelinlik ve krem takım, bedensiz, yüzsüz, adsız. Ama aralarındaki mesafe ve çiçek denizi her şeyi anlatıyor. Aşk bazen bedeni aşar, sadece izi kalır — koku gibi, görünmez ama hissedilir.

### Aşkın Halleri ve Engelleri — Zeynep Toprak | Aşk
Bir el, yatay bir çizginin üzerinde duruyor. Altında yansıması var — ama yansıma farklı, karanlık, yıldızlı. Gerçek ile hayal arasındaki o ince çizgi. Aşk hem yukarıda hem aşağıda, hem ışıkta hem karanlıkta yaşıyor.

### Doğuş — Zeynep Toprak | Ölüm
Kafatasının içinden bir zambak filizleniyor. Kökler kafatasına sarılmış, çiçek ışığa uzanıyor. Ölüm bir son değil — içinden yeni bir hayat doğuyor. En karanlık yerden en güzel şey çıkıyor.

### Kum Saati Figür — Zeynep Toprak | Ölüm
Bir figür yavaşça kuma dönüşüyor. Zaman akıyor, beden dağılıyor. Ölüm burada bir son değil — bir geçiş, bir dönüşüm. Figür direniyor ama kum durmaksızın akıyor.

### Unutulmuş Ruh — Yasemin Mahmut | Vatan
Gurbet; kaybolmaya ant içmiş anılara tutunurken ruhun sessiz bir işkenceyle parçalanmasıdır. Beden yıllar geçse de alışamaz ama zihin o çok özlenen diyarı yavaşça unutur. En acısı — canından çok sevdiğin yurdun seni unutmuş, yok saymış ve reddetmiş olmasıdır. Yine de ruh ondan vazgeçemez. Bu çizim, o görünmez parçalanmanın estetik bir dışavurumudur.

---

## Ajan Mimarisi

Dört ajan sırayla çalışır. Her ajan bir öncekinin çıktısını alır. Her kararı arayüzde görünür.

```
Çizim + Tema
     ↓
Ajan 1: Gözetleyici  →  duygu + görsel analiz
     ↓
Ajan 2: Şair         →  şair seçimi + özgün şiir
     ↓
Ajan 3: Besteci      →  ton + tempo + BPM + enstrüman + müzik promptu
     ↓
Ajan 4: Ses Veren    →  30 saniyelik MP3
```

---

### Ajan 1 — Gözetleyici
**Model:** Claude Sonnet Vision (Anthropic) — Kapalı kaynak ⚠️

Çizimi ve temayı birlikte görür. Felsefi soruyla analiz eder. Renk, form, yoğunluk, hareket ve duyguyu tespit eder. Duygu tespiti tüm pipeline'ı yönlendirir.

**Çıktı:** `agirlik / kirilma / umut / huzur / ofke / yalnizlik / ozgurluk`

**Neden Claude:** Vision analizi için kararlı açık kaynak alternatif yok. LLaVA vb. hackathon ortamında stabil değil.

---

### Ajan 2 — Şair
**Model:** Claude Sonnet (Anthropic) — Kapalı kaynak ⚠️

Tema+duygu kombinasyonuna göre Türk şair seçer. Meryem Özden ve Zehra Güleç'in hammadde dizelerinden ilham alarak o şairin üslubuyla özgün şiir üretir. Meryem ve Zehra'nın dizeleri ilham kaynağı — birebir kopya değil.

**Şair Matrisi:**

| Duygu | Aşk | Ölüm | Vatan |
|-------|-----|------|-------|
| Ağırlık | Cemal Süreya | Cahit Sıtkı Tarancı | Nazım Hikmet |
| Kırılma | Özdemir Asaf | Edip Cansever | Ahmet Arif |
| Umut | Nazım Hikmet | Mevlana Rumi | Nazım Hikmet |
| Huzur | Özdemir Asaf | Cahit Sıtkı Tarancı | Mevlana Rumi |
| Öfke | Cemal Süreya | Edip Cansever | Ahmet Arif |
| Yalnızlık | Edip Cansever | Cahit Sıtkı Tarancı | Nazım Hikmet |
| Özgürlük | Cemal Süreya | Nazım Hikmet | Ahmet Arif |

**Neden Claude:** Mistral-7B test edildi. Türkçe şiir üsluplarını işlemede yetersiz kaldı. Bu karar şeffaf belgelenmiştir.

---

### Ajan 3 — Besteci
**Model:** Mistral-7B-Instruct (HuggingFace) — Apache 2.0 ✅ Açık kaynak
**Fallback:** Claude Sonnet (ağ erişimi başarısız olursa)

Çizim analizini, şiiri ve temayı birlikte okur. Ton, tempo, BPM, enstrüman ve MusicGen promptunu kendisi belirler. Şiirdeki anahtar kelimelerden enstrüman bağlantısı kurar:

| Şiirdeki imge | Enstrüman |
|---------------|-----------|
| su / akmak / nehir / yağmur | flute |
| toprak / ağırlık / kaya / dağ | cello |
| gece / sessizlik / karanlık | piano |
| ışık / umut / güneş | violin |
| özlem / uzaklık / yurt / vatan | ney |
| ateş / tutku / alev | guitar |

**Neden Mistral:** Açık kaynak (Apache 2.0), ücretsiz. Ağ erişimi başarısız olursa Claude fallback devreye girer.

---

### Ajan 4 — Ses Veren
**Model:** MusicGen via Replicate (Meta) — MIT ✅ Açık kaynak

Besteci'nin promptunu alır, 30 saniyelik MP3 üretir. Model: `melody-large`.

---

## Açık Kaynak Özeti

```
Gözetleyici:   ⚠️ Kapalı  Claude Vision    — kararlı açık alternatif yok
Şair:          ⚠️ Kapalı  Claude Sonnet    — Türkçe şiir kalitesi zorunlu
Besteci:       ✅ Açık    Mistral-7B       — Apache 2.0, $0.00
Ses Veren:     ✅ Açık    MusicGen (Meta)  — MIT
Backend:       ✅ Açık    FastAPI          — MIT
Veritabanı:    ✅ Açık    SQLite           — Public Domain
Görsel işleme: ✅ Açık    Pillow           — HPND

Araç açık kaynak oranı: 5/7 (%71)
Ajan açık kaynak oranı: 2/4 (%50) — kısıtlar gerekçeli belgelenmiş
```

---

## Token ve Maliyet

| Ajan | Model | Maliyet/çizim |
|------|-------|---------------|
| Gözetleyici | Claude Sonnet Vision | ~$0.007 |
| Şair | Claude Sonnet | ~$0.003 |
| Besteci | Mistral-7B (HF ücretsiz) | $0.00 |
| Ses Veren | MusicGen via Replicate | ~$0.0046 |
| **Toplam** | | **~$0.015/çizim** |

100 çizim ≈ $1.46 — ~1.800 token/çizim, sektör ortalamasının 8x altı.

---

## İnsan + Ajan Bütünleşik

Çizim olmadan şiir yok. Hammadde dizeleri olmadan ajan üslup kararı veremez. Sanatçı çizmeden sistem çalışmaz. Bu sıra değişmez — insan önce üretiyor, ajan yanıt veriyor.

**İnsan katkıları:**
- **Lütfiye Erkuş** — 4 ajan pipeline mimarisi, FastAPI backend, Railway deploy
- **Zeynep Toprak** — Aşk ve Ölüm çizimleri (Ruhların Kokusu, Aşkın Halleri ve Engelleri, Doğuş, Kum Saati Figür)
- **Yasemin Mahmut** — Vatan çizimi (Unutulmuş Ruh)
- **Meryem Özden** — 21 kombinasyon için şiir hammaddesi (3 tema × 7 duygu)
- **Zehra Güleç** — 21 kombinasyon için şiir hammaddesi yazımı (3 tema × 7 duygu)
- **Ebru Korkut** — Sunum metinleri & tanıtım videosu

---

## Şeffaflık

Her eser için izleyici şunları görebilir:

- Tema ve felsefi soru
- Gözetleyici'nin renk, form, duygu analizi
- Hangi şair seçildi ve neden
- Besteci'nin ton, tempo, BPM, enstrüman kararı
- Şiirden alınan imge ve müzik bağlantısı
- Üretilen şiir + 30 saniyelik müzik

---

## Girişim Potansiyeli

### Neden Şimdi?

Yapay zeka araçları artık sanatsal üretimin içinde. Ama çoğu araç insanı seyirci yapıyor — "AI çizsin, AI yazsın." Çizginin Sesi tam tersini yapıyor: insan üretiyor, ajan dinliyor. Bu ayrım hem etik hem de pazarda güçlü bir konumlanma.

### Konumlanma

**"Terapi aracı" değil — "yaratıcı ifade platformu"**

Kelime bulamazsan çiz. Gerisini biz halledelim.

### Pazar

**Pazar 1 — Terapistler (İlk müşteri):**
Terapistler zaten AI araçlarına 400–1.000 TL/ay harcıyor (2026 TR verisi). Çizginin Sesi seans öncesi danışanın çizmesini sağlar, üretilen şiir ve müzik söze gelemeyen duygulara kapı açar. İlk kanal: DoktorTakvimi, Psikologlar.org, LinkedIn klinik psikologlar topluluğu.

**Pazar 2 — Kültür Kurumları (Büyüme):**
Özel müzeler, galeriler, bienaller. Tablet+kulaklık köşesi → ziyaretçi çizer → 40 sn şiir+müzik → QR ile indirir. Tüm ziyaretçi üretimleri kolektif arşiv oluşturur; küratörler analitik görür.

**Pazar 3 — B2C (Uzun vade):**
280 milyon göçmen özel segment — vatan teması evrensel bir duygu taşıyor.

### Fiyatlandırma (Türkiye)

| Paket | Fiyat | Kime |
|-------|-------|------|
| Freemium | 0 TL | 3 çizim/ay |
| Keşif | 199 TL/ay | Bireysel |
| Sınırsız | 349 TL/ay | Bireysel |
| Terapist Başlangıç | 799 TL/ay | 20 danışana kadar |
| Terapist Pro | 1.499 TL/ay | Sınırsız + rapor |
| Klinik | 3.999 TL/ay | 5 terapist koltuğu |
| Kurumsal | 3.999 TL/ay | Müze/Galeri |

### Fiyatlandırma (Global)

| Paket | Fiyat |
|-------|-------|
| Individual | $9.99/ay |
| Therapist | $49/ay |
| Clinic | $199/ay |
| Institution | $299/ay |
| Enterprise | Özel |

### Rekabet Farkı

Piyasadaki araçlar ya görsel üretiyor (Midjourney, DALL-E) ya metin üretiyor (ChatGPT). Hiçbiri insan çizgisini alıp şiir+müzik zinciri üretmiyor. Türk şiir geleneğini yapay zekaya entegre eden ilk platform.

---

## Teknik Stack

```
Backend:       Python 3.13 + FastAPI 0.115.12
Veritabanı:    SQLite
Bağımlılıklar: Poetry
Deploy:        Railway
Frontend:      Vanilla HTML/CSS/JS
```

---

## Kurulum

```bash
git clone https://github.com/lerkush/voice-of-drawing.git
cd voice-of-drawing
poetry install
```

`.env` dosyası oluştur:

```env
ANTHROPIC_API_KEY=sk-ant-...
HF_TOKEN=hf_...
REPLICATE_API_TOKEN=r8_...
```

Veritabanını başlat:

```bash
poetry run python database.py
```

Sunucuyu başlat:

```bash
poetry run uvicorn main:app --reload --port 8000
```

`http://localhost:8000` adresini aç.

---

## Canlı Demo

🌐 [voice-of-drawing-production.up.railway.app](https://voice-of-drawing-production.up.railway.app)

---

## Ekip

| İsim | Rol |
|------|-----|
| Lütfiye Erkuş | Takım Lideri & Yazılım Geliştirici |
| Zeynep Toprak | Resim Sanatçısı (Aşk + Ölüm) |
| Meryem Özden | Şiir & Edebiyat & Sunum |
| Yasemin Mahmut | Resim Sanatçısı (Vatan) & Tasarım |
| Zehra Güleç | Şiir Hammaddesi & Demo |
| Ebru Korkut | Sunum Metinleri & Tanıtım Videosu |

---

*ÜretJAM 2026 | Çizginin Sesi — Voice of Drawing*
*Söylenemeyen şeyin de bir dili vardır.*