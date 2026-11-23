
# Elma Karalekesi – Meteorolojik Hastalık Tahmin Modelleri

## 1. Araştırmanın Amacı

Bu araştırmanın amacı, elma karalekesi (Venturia inaequalis) hastalığının meteorolojik koşullara bağlı enfeksiyon riskini değerlendirmek için uygun bilimsel modelleri incelemektir.

Proje kapsamında tek bir modele bağlı kalmak yerine farklı bilimsel yaklaşımlar karşılaştırılacaktır.


## 2. İncelenen Bilimsel Yaklaşımlar

### 2.1. Mills Enfeksiyon Tablosu

- Model türü: Sıcaklık ve sürekli yaprak ıslaklığı süresine dayalı eşik yaklaşımı.
- Temel değişkenler: Sıcaklık ve yaprak ıslaklığı süresi.
- Avantajı: Basit, açıklanabilir ve tarihsel açıdan önemli bir referanstır.
- Sınırlılığı: Enfeksiyon sürecinin tüm biyolojik aşamalarını modellemez.
- Projedeki rolü: Tarihsel karşılaştırma modeli.

### 2.2. Revised Mills – MacHardy ve Gadoury (1989)

- Model türü: Mills enfeksiyon kriterlerinin gözden geçirilmiş sürümü.
- Temel değişkenler: Sıcaklık, yaprak ıslaklığı süresi ve askospor salım zamanlaması.
- Katkısı: Özellikle gece başlayan yağışlarda askospor salımının zamanlamasını dikkate alır ve enfeksiyon sürelerini yeniden değerlendirir.
- Sınırlılığı: Eşik tabanlı yaklaşımın genel sınırlılıklarını taşır.
- Projedeki rolü: Karşılaştırma modeli.

### 2.3. Stensvand ve Arkadaşları (1997)

- Çalışmanın konusu: Düşük sıcaklıklarda Venturia inaequalis askospor ve konidiospor salımı ile enfeksiyonu.
- Temel değişkenler: Sıcaklık, spor türü ve yaprak ıslaklığı süresi.
- Katkısı: Özellikle 8°C ve altındaki sıcaklıklarda önceki enfeksiyon tablolarındaki sürelerin yeniden değerlendirilmesi gerektiğini gösterir.
- Sınırlılığı: Tek başına bütün enfeksiyon döngüsünü modelleyen kapsamlı bir sistem değildir.
- Projedeki rolü: Düşük sıcaklık koşullarında karşılaştırma ve parametre değerlendirmesi.

### 2.4. A-scab – Rossi, Giosuè ve Bugiani (2007)

- Model türü: Dinamik simülasyon modeli.
- Kapsamı: Elma karalekesinin birincil enfeksiyon sürecini simüle eder.
- Temel değişkenler: Hava sıcaklığı, yağış, bağıl nem ve yaprak ıslaklığı.
- Değerlendirdiği süreçler: Askospor olgunlaşması, salımı, yaprağa ulaşması ve enfeksiyon gelişimi.
- Avantajı: Enfeksiyon sürecini birden fazla biyolojik aşamayla değerlendirir.
- Sınırlılığı: Yaprak ıslaklığı ve biyolojik süreçlere ilişkin ayrıntılı girdiler gerektirir.
- Projedeki rolü: Gelişmiş model adayı.

**Önemli not:** Bu çalışmaların tümü aynı türde model değildir. Mills ve Revised Mills eşik yaklaşımlarıdır; Stensvand çalışması enfeksiyon kriterlerinin deneysel olarak yeniden değerlendirilmesine katkı sağlar; A-scab ise dinamik simülasyon modelidir.


## 3. Mevcut Veri Altyapısı

Projede şu meteorolojik değişkenler bulunmaktadır:

- 2 metre hava sıcaklığı
- 2 metre bağıl nem
- Yağış miktarı

Henüz doğrudan yaprak ıslaklığı ölçümü bulunmamaktadır.

İlerleyen aşamada meteorolojik değişkenlerden yaprak ıslaklığı tahmini yapılması araştırılacaktır.

## 4. Model Seçiminde Dikkate Alınacak Kriterler

1. Bilimsel geçerlilik
2. Türkiye koşullarında uygulanabilirlik
3. Gerekli meteorolojik verilerin erişilebilirliği
4. Yaprak ıslaklığı tahminine uygunluk
5. Farklı sıcaklık ve nem koşullarındaki performans
6. Açıklanabilirlik
7. Uzman görüşüyle doğrulanabilirlik
8. Yeni modellere uyarlanabilirlik

## 5. Planlanan Sistem Mimarisi

Sistem aşağıdaki bileşenlerden oluşacaktır:

1. Meteorolojik veri katmanı
2. Yaprak ıslaklığı tahmin katmanı
3. Enfeksiyon tahmin modelleri
4. Karşılaştırmalı risk değerlendirme katmanı
5. Belirsizlik yönetimi ve uzman yönlendirme katmanı

Modeller birbirinden bağımsız geliştirilecek ve gerektiğinde yeni modeller sisteme eklenebilecektir.

## 6. Uzman Doğrulaması Bekleyen Konular

- Türkiye'de kullanılabilecek en uygun elma karalekesi enfeksiyon modeli.
- Mills ve alternatif modellerin yerel koşullardaki geçerliliği.
- Meteorolojik verilerden yaprak ıslaklığı tahmini için uygun yöntem.
- Yağış ve bağıl nemin yaprak ıslaklığı tahminindeki rolü.
- Fenolojik gelişim ve askospor uçuşu bilgilerinin modele dahil edilmesi.
- Risk seviyelerinin belirlenmesi.

## 7. Araştırma ve Geliştirme İlkesi

Başlangıçta bilimsel kaynaklara dayanan bir prototip geliştirilecektir.

Model parametreleri, kaynakları ve varsayımları kayıt altında tutulacaktır.

Ziraat mühendisi ve ilgili uzmanlardan alınan geri bildirimler doğrultusunda model güncellenecek, eski ve yeni sonuçlar karşılaştırılacaktır.

Hiçbir model çıktısı, yerel koşullarda doğrulanmadan kesin enfeksiyon gerçekleştiği şeklinde yorumlanmayacaktır.


## 8. Kaynaklar

### 8.1. Bilimsel Yayınlar

1. Mills, W. D. (1944). *Efficient use of sulfur dusts and sprays during rain to control apple scab.* Cornell Extension Bulletin 630, 1–4.

   - Mills yaklaşımının temel tarihsel yayını.
   - [Yayın bilgisi](https://doi.org/10.1094/Phyto-79-304) değil; özgün bülten kaydı için Cornell ve APS kaynakları ayrıca incelenmelidir.

2. Mills, W. D., & La Plante, A. A. (1951). *Diseases and insects in the orchard.* Cornell Extension Bulletin 711.

   - Mills–La Plante tablosunun ilişkilendirildiği tarihsel kaynak.

3. MacHardy, W. E., & Gadoury, D. M. (1989). A revision of Mills's criteria for predicting apple scab infection periods. *Phytopathology, 79*, 304–310.

   - DOI: https://doi.org/10.1094/Phyto-79-304

4. Stensvand, A., Gadoury, D. M., Amundsen, T., Semb, L., & Seem, R. C. (1997). Ascospore release and infection of apple leaves by conidia and ascospores of Venturia inaequalis at low temperatures. *Phytopathology, 87*(10), 1046–1053.

   - DOI: https://doi.org/10.1094/PHYTO.1997.87.10.1046

5. Rossi, V., Giosuè, S., & Bugiani, R. (2007). A-scab (Apple-scab), a simulation model for estimating risk of Venturia inaequalis primary infections. *EPPO Bulletin, 37*(2), 300–308.

   - DOI: https://doi.org/10.1111/j.1365-2338.2007.01125.x

### 8.2. Türkiye'deki Teknik Kaynaklar

6. T.C. Tarım ve Orman Bakanlığı, Tarımsal Araştırmalar ve Politikalar Genel Müdürlüğü. (2022). *Elma, Armut ve Ayva Entegre Mücadele Teknik Talimatı.* Ankara.

   - [Resmî PDF](https://www.tarimorman.gov.tr/TAGEM/Belgeler/Entegre/Elma%2C%20Armut%20ve%20Ayva%20Entegre%20M%C3%BCcadele%20Teknik%20Talimat%C4%B1.pdf)

7. T.C. Tarım ve Orman Bakanlığı. (2008). *Zirai Mücadele Teknik Talimatları, Cilt IV.*

   - Mills–Laplante tablosunun yer aldığı tarihsel teknik kaynak.
   - Baskı ve yayın künyesi uygulama öncesinde fiziksel veya dijital belge üzerinden doğrulanacaktır.

### 8.3. Kaynak Kullanımına İlişkin Notlar

- 1944 tarihli Mills yayını ile 1951 tarihli Mills–La Plante bülteni birbirinden ayrı kaynaklardır.
- MacHardy ve Gadoury (1989), Mills kriterlerinin gözden geçirilmiş yaklaşımını açıklar.
- Stensvand ve arkadaşları (1997), özellikle düşük sıcaklıklardaki spor salımı ve enfeksiyon koşullarını araştırır.
- Rossi ve arkadaşları (2007), A-scab dinamik simülasyon modelini tanımlar.
- Yayınların sonuçları, Türkiye koşullarında doğrudan geçerli kabul edilmeyecektir.
- Model parametreleri uygulamaya aktarılmadan önce özgün yayınlar ve ilgili teknik tablolar incelenecektir.

