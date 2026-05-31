TEMALAR = {
    "ask": {
        "isim": "Aşk",
        "yorum": "Söylenemeyen duyguların en güçlüsü sevgidir.",
        "felsefi_soru": "Bu çizimde aşkın hangi yüzü gizli? Kavuşma mı, ayrılık mı, yoksa söylenemeyen mi?",
        "muzik_atmosfer": "romantic longing warm emotional intimate",
        "birincil_enstruman": ["piano", "violin"],
        "ikincil_enstruman": ["guitar", "cello"],
    },
    "olum": {
        "isim": "Ölüm",
        "yorum": "Ölüm hakkında konuşmak zordur çünkü dili yoktur.",
        "felsefi_soru": "Bu çizimde ölüm bir son mu, bir dönüşüm mü? Yas mı, kabul mü, yoksa geçiş mi?",
        "muzik_atmosfer": "contemplative heavy melancholic deep somber",
        "birincil_enstruman": ["cello", "piano"],
        "ikincil_enstruman": ["strings", "violin"],
    },
    "vatan": {
        "isim": "Vatan",
        "yorum": "Vatan bir yer değil, içeride taşınan bir sestir.",
        "felsefi_soru": "Bu çizimde vatan bir yer mi, bir dil mi, yoksa içeride taşınan mı?",
        "muzik_atmosfer": "longing exile distance nostalgic melancholic",
        "birincil_enstruman": ["ney", "cello"],
        "ikincil_enstruman": ["violin", "piano"],
    },
}

DUYGULAR = ["agirlik", "kirilma", "umut", "huzur", "ofke", "yalnizlik", "ozgurluk"]

DUYGU_NORMALIZASYON = {
    "ağırlık": "agirlik", "agirlik": "agirlik",
    "kırılma": "kirilma", "kirilma": "kirilma",
    "umut": "umut",
    "huzur": "huzur",
    "öfke": "ofke", "ofke": "ofke",
    "yalnızlık": "yalnizlik", "yalnizlik": "yalnizlik",
    "özgürlük": "ozgurluk", "ozgurluk": "ozgurluk",
}

SIIR_IMGE_MUZIK = {
    "su": "flute", "akmak": "flute", "nehir": "flute", "yağmur": "flute",
    "toprak": "cello", "ağırlık": "cello", "kaya": "cello", "dağ": "cello",
    "gece": "piano", "sessizlik": "piano", "karanlık": "piano",
    "ışık": "violin", "umut": "violin", "güneş": "violin",
    "özlem": "ney", "uzaklık": "ney", "yurt": "ney", "vatan": "ney",
    "ateş": "guitar", "tutku": "guitar", "alev": "guitar",
}
SAIR_TEMA_DUYGU = {
    ("ask", "agirlik"):    "Cemal Süreya",
    ("ask", "kirilma"):    "Özdemir Asaf",
    ("ask", "umut"):       "Nazım Hikmet",
    ("ask", "huzur"):      "Özdemir Asaf",
    ("ask", "ofke"):       "Cemal Süreya",
    ("ask", "yalnizlik"):  "Edip Cansever",
    ("ask", "ozgurluk"):   "Cemal Süreya",
    ("olum", "agirlik"):   "Cahit Sıtkı Tarancı",
    ("olum", "kirilma"):   "Edip Cansever",
    ("olum", "umut"):      "Mevlana Rumi",
    ("olum", "huzur"):     "Cahit Sıtkı Tarancı",
    ("olum", "ofke"):      "Edip Cansever",
    ("olum", "yalnizlik"): "Cahit Sıtkı Tarancı",
    ("olum", "ozgurluk"):  "Nazım Hikmet",
    ("vatan", "agirlik"):  "Nazım Hikmet",
    ("vatan", "kirilma"):  "Ahmet Arif",
    ("vatan", "umut"):     "Nazım Hikmet",
    ("vatan", "huzur"):    "Mevlana Rumi",
    ("vatan", "ofke"):     "Ahmet Arif",
    ("vatan", "yalnizlik"):"Nazım Hikmet",
    ("vatan", "ozgurluk"): "Ahmet Arif",
}

SAIR_STIL = {
    "Cemal Süreya":        "Bedensel ve duyusal imgeler, modern aşk dili, cesur ve beklenmedik metaforlar, kısa yoğun dizeler, erotik alt metin",
    "Özdemir Asaf":        "Aforizma gücü, sade ama derin, son dizede beklenmedik kırılma, günlük dilde felsefi derinlik, alaycı ama hüzünlü",
    "Edip Cansever":       "Varoluşsal iç ses, karanlık ve ağır imgeler, uzun soluklu dizeler, yalnızlık ve anlam arayışı, iç monolog",
    "Cahit Sıtkı Tarancı": "Ölümü sade güzellikle işleme, hüzün ve kabullenme, klasik ritim, içten ve samimi ses, doğa imgesi",
    "Nazım Hikmet":        "Güçlü ritim, umut ve direniş, somut ve yalın dil, halk imgesi, coşkulu ama gerçekçi, uzun dizeler",
    "Ahmet Arif":          "Dağ ve taş imgesi, Doğu Anadolu sesi, acı ve gurur iç içe, yalın ama ezberden uzak, isyan ve sevgi",
    "Mevlana Rumi":        "Ney ve ayrılık metaforu, sufi derinlik, özlem ve kavuşma, evrensel sevgi dili, döngüsel imgeler",
}