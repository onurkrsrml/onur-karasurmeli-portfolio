# Onur Karasurmeli — Portfolyo Sitesi

`anilozturk.net` sitesindeki tasarım mantığı (sol tarafta ince bir menü, üstte
başlık ve ince çizgi, ortalanmış tek sütun içerik, "Download CV" kutusu)
temel alınarak hazırlanmış, senin CV ve LinkedIn bilgilerinle doldurulmuş
statik bir portfolyo sitesi.

## Neden Python değil de HTML/CSS/JS?

GitHub Pages **sadece statik dosyaları** (HTML/CSS/JS) yayınlayabilir; sunucu
tarafında Python çalıştırmaz. Bu yüzden site saf HTML/CSS/JS olarak
oluşturuldu — bu, github.io üzerinde çalışacak en sağlıklı ve verimli yöntem.

Yine de PyCharm'da rahatça çalışabilmen için `serve.py` adında küçük bir
Python betiği ekledim; bunu çalıştırdığında siteyi tarayıcında canlı önizleme
olarak açar (kod değişikliklerini görmek için sayfayı yenilemen yeterli).

## Klasör yapısı

```
portfolio-site/
├── index.html          → About (ana sayfa)
├── education.html      → Education
├── experience.html     → Experience
├── projects.html       → Projects
├── skills.html         → Skills
├── serve.py            → PyCharm'dan çalıştırıp local önizleme için
├── css/style.css        → Tüm sayfaların ortak tasarımı
├── js/script.js         → Aktif menü vurgusu + mobil menü
└── assets/
    ├── Onur_Karasurmeli_CV.pdf   → "Download CV" butonunun bağlandığı dosya
    └── images/                   → İleride ekleyeceğin görseller için boş klasör
```

## PyCharm'da açma

1. PyCharm'da **File → Open** ile `portfolio-site` klasörünü aç.
2. `serve.py` dosyasına sağ tıklayıp **Run 'serve'** de.
3. Otomatik olarak `http://localhost:8000` tarayıcıda açılacak.
4. HTML/CSS'te değişiklik yaptıkça tarayıcıyı yenile (F5), sunucuyu yeniden
   başlatmana gerek yok.

## Senin bilgilerinle ilgili notlar

- **LinkedIn linkini düzelttim:** yazdığın `https://www.linkedin/in/...`
  eksikti, doğrusu `https://www.linkedin.com/in/onurkarasurmeli/` — sitede bu
  şekilde kullandım.
- **Profil fotoğrafı:** Elimde fotoğrafın olmadığı için baş harflerinle
  ("OK") bir daire yer tutucu koydum. Kendi fotoğrafını eklemek için:
  1. Fotoğrafını `assets/images/profile.jpg` olarak kaydet.
  2. `index.html` içinde şu satırı bul:
     `<div class="avatar" aria-hidden="true">OK</div>`
     ve şununla değiştir:
     `<div class="avatar"><img src="assets/images/profile.jpg" alt="Onur Karasurmeli" style="width:100%;height:100%;border-radius:50%;object-fit:cover;"></div>`
- **Projeler sayfası:** GitHub repo linklerin CV'de yazmadığı için `#`
  bıraktım — `projects.html` içindeki `href="#"` kısımlarını kendi gerçek
  repo linklerinle değiştir.
- **Sertifika/Yayın/Patent sayfaları:** CV'nde bu bilgiler olmadığı için
  eklemedim (referans sitedeki Certifications/Publications/Patents
  bölümlerini uydurmak yerine çıkardım). İleride bir sertifikan olursa
  `education.html`'e benzer bir `entry` bloğu ekleyerek kolayca
  genişletebilirsin.

## GitHub Pages'e yayınlama

1. GitHub'da yeni bir repo oluştur. Kullanıcı adın `onurkarasurmeli` ise,
   repo adını tam olarak **`onurkarasurmeli.github.io`** yap — bu isimde bir
   repo otomatik olarak `https://onurkarasurmeli.github.io` adresinde
   yayınlanır (ekstra ayara gerek kalmaz).
2. Bu klasördeki tüm dosyaları repoya yükle (terminalden):

   ```bash
   cd portfolio-site
   git init
   git add .
   git commit -m "İlk portfolyo sürümü"
   git branch -M main
   git remote add origin https://github.com/onurkarasurmeli/onurkarasurmeli.github.io.git
   git push -u origin main
   ```

3. Repo adını farklı seçtiysen (örn. `portfolio`): GitHub'da **Settings →
   Pages** kısmından `main` branch'i seç ve kaydet; site
   `https://onurkarasurmeli.github.io/portfolio/` adresinde yayınlanır.
4. Birkaç dakika içinde site canlıya çıkar.

## Değişiklik yapmak

Metinleri güncellemek için PyCharm'da ilgili `.html` dosyasını aç, ilgili
paragrafı düzenle ve kaydet — tasarım/CSS'e dokunman gerekmiyor. Tüm
sayfalardaki ortak görünüm (renkler, boşluklar, yazı tipleri) tek bir yerden,
`css/style.css` dosyasından yönetiliyor.
