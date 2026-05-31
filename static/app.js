// app.js — Çizginin Sesi

let secilenTema = 'ask';
let secilenDosya = null;

// Tema seçimi
document.querySelectorAll('.tema-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        document.querySelectorAll('.tema-btn').forEach(b => b.classList.remove('aktif'));
        btn.classList.add('aktif');
        secilenTema = btn.dataset.tema;
    });
});

// Dosya seçimi
document.getElementById('dosyaInput').addEventListener('change', (e) => {
    const dosya = e.target.files[0];
    if (!dosya) return;
    secilenDosya = dosya;

    const reader = new FileReader();
    reader.onload = (ev) => {
        const onizleme = document.getElementById('onizleme');
        onizleme.src = ev.target.result;
        onizleme.classList.remove('gizli');
        document.getElementById('yukleIci').style.display = 'none';
        document.getElementById('isleBtn').disabled = false;
    };
    reader.readAsDataURL(dosya);
});

// Sürükle bırak
const yukleAlan = document.getElementById('yukleAlan');
yukleAlan.addEventListener('dragover', (e) => { e.preventDefault(); });
yukleAlan.addEventListener('drop', (e) => {
    e.preventDefault();
    const dosya = e.dataTransfer.files[0];
    if (dosya && dosya.type.startsWith('image/')) {
        document.getElementById('dosyaInput').files = e.dataTransfer.files;
        document.getElementById('dosyaInput').dispatchEvent(new Event('change'));
    }
});

// İşle butonu
document.getElementById('isleBtn').addEventListener('click', isle);

async function isle() {
    if (!secilenDosya) return;

    // UI güncelle
    document.querySelector('.yukle-bolum').classList.add('gizli');
    document.getElementById('yukleniyorBolum').classList.remove('gizli');
    document.getElementById('sonucBolum').classList.add('gizli');

    // Adım animasyonu
    const adimlar = ['adim1', 'adim2', 'adim3', 'adim4'];
    let adimIndex = 0;
    const adimInterval = setInterval(() => {
        if (adimIndex > 0) {
            document.getElementById(adimlar[adimIndex - 1]).classList.remove('aktif');
            document.getElementById(adimlar[adimIndex - 1]).classList.add('tamam');
        }
        if (adimIndex < adimlar.length) {
            document.getElementById(adimlar[adimIndex]).classList.add('aktif');
            adimIndex++;
        }
    }, 8000);

    try {
        const form = new FormData();
        form.append('dosya', secilenDosya);
        form.append('tema', secilenTema);

        const yanit = await fetch('/api/isle', { method: 'POST', body: form });
        const veri = await yanit.json();

        clearInterval(adimInterval);

        if (!yanit.ok) throw new Error(veri.detail || 'Hata oluştu');

        sonucGoster(veri);

    } catch (hata) {
        clearInterval(adimInterval);
        alert('Hata: ' + hata.message);
        yeniden();
    }
}

function sonucGoster(veri) {
    document.getElementById('yukleniyorBolum').classList.add('gizli');
    document.getElementById('sonucBolum').classList.remove('gizli');

    const analiz = veri.gorsel_analiz || {};
    const muzik = veri.muzik_tasarim || {};

    document.getElementById('sonucDuygu').textContent = analiz.duygu || '-';
    document.getElementById('sonucYogunluk').textContent = analiz.yogunluk || '-';
    document.getElementById('sonucHareket').textContent = analiz.hareket || '-';
    document.getElementById('sonucRenkler').textContent = analiz.renkler || '-';
    document.getElementById('sonucGorselDetay').textContent = analiz.gorsel_detay || '';

    document.getElementById('sonucSair').textContent = veri.sair || '-';
    document.getElementById('sonucSairNeden').textContent = veri.sair_neden || '';
    document.getElementById('sonucSiir').textContent = veri.siir || '';

    document.getElementById('sonucTon').textContent = muzik.ton || '-';
    document.getElementById('sonucTempo').textContent = muzik.tempo || '-';
    document.getElementById('sonucBpm').textContent = muzik.bpm ? muzik.bpm + ' bpm' : '-';
    document.getElementById('sonucEnstruman').textContent =
        [muzik.enstruman_1, muzik.enstruman_2].filter(Boolean).join(' + ');
    document.getElementById('sonucImge').textContent = muzik.siirden_alinan_imge || '-';
    document.getElementById('sonucMuzikPrompt').textContent = muzik.muzik_prompt || '';

    const player = document.getElementById('muzikPlayer');
    if (veri.muzik_url) {
        player.src = veri.muzik_url;
        player.load();
    }
}

function yeniden() {
    secilenDosya = null;
    document.querySelector('.yukle-bolum').classList.remove('gizli');
    document.getElementById('yukleniyorBolum').classList.add('gizli');
    document.getElementById('sonucBolum').classList.add('gizli');
    document.getElementById('onizleme').classList.add('gizli');
    document.getElementById('yukleIci').style.display = '';
    document.getElementById('isleBtn').disabled = true;
    document.getElementById('dosyaInput').value = '';
    ['adim1','adim2','adim3','adim4'].forEach(id => {
        document.getElementById(id).classList.remove('aktif', 'tamam');
    });
}