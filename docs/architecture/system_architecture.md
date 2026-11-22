# Tarımsal Hastalık Erken Uyarı ve Doğrulama Sistemi

## 1. Sistem Amacı ve Kapsamı

### 1.1. Sistem Amacı

Bu projenin amacı, tarımsal üretimde hastalıkların erken tespit edilmesini, hastalık risklerinin değerlendirilmesini ve farklı veri kaynaklarından elde edilen bulguların doğrulanmasını sağlayan yapay zekâ destekli, modüler bir karar destek sistemi geliştirmektir.

Sistem; meteorolojik verileri, bitki görüntülerini, bilimsel hastalık modellerini ve uzman değerlendirmelerini bir araya getirerek üreticilere açıklanabilir ve güvenilir karar desteği sunmayı hedeflemektedir.

### 1.2. Sistem Kapsamı

Sistem dört temel bileşenden oluşacaktır:

1. **Meteorolojik Hastalık Risk Analizi:** Hava sıcaklığı, bağıl nem, yağış ve diğer uygun çevresel verileri kullanarak hastalık oluşum ve enfeksiyon riskini değerlendirir.
2. **Görüntü Tabanlı Hastalık Tespiti:** Bitki görüntülerini analiz ederek hastalık belirtilerini ve olası hastalıkları belirler.
3. **Çapraz Doğrulama:** Meteorolojik risk sonuçları ile görüntü analizinden elde edilen bulguları karşılaştırır.
4. **AI Agent Destekli Karar Mekanizması:** Bulguları birlikte değerlendirir, belirsizlikleri belirler, açıklanabilir sonuçlar üretir ve gerektiğinde uzman değerlendirmesine yönlendirir.

### 1.3. İlk Pilot Çalışma

İlk geliştirme ve doğrulama çalışması elma karalekesi (*Venturia inaequalis*) hastalığı üzerinden yürütülecektir.

Bu aşamada meteorolojik veriler kullanılarak hastalık risk analiz motoru geliştirilecek ve bilimsel kaynaklarla uyumluluğu değerlendirilecektir.

Elma karalekesi, sistemin genel kapsamını sınırlandıran bir tercih değil, modüler mimarinin ilk uygulama alanıdır.

### 1.4. Temel Tasarım İlkeleri

- Bilimsel kaynaklara ve doğrulanabilir verilere dayanma.
- Farklı bitki ve hastalık türlerine genişletilebilir olma.
- Veri kalitesini ve veri kaynağını takip etme.
- Belirsizliği gizlemek yerine açıkça ifade etme.
- Hastalık riskini kesin teşhis olarak sunmama.
- Uzman görüşüyle doğrulamaya imkân sağlama.
- Her bileşeni bağımsız geliştirilebilir ve test edilebilir tasarlama.

## 2. Sistem Bileşenleri ve Veri Akışı

### 2.1. Genel Mimari

Sistem, birbirinden bağımsız geliştirilebilen ancak ortak bir karar mekanizması üzerinden birlikte çalışabilen modüler bileşenlerden oluşacaktır.

Meteorolojik analiz ve görüntü tabanlı hastalık tespiti paralel olarak çalışabilecek şekilde tasarlanacaktır. Her iki bileşenin çıktıları çapraz doğrulama katmanına aktarılacaktır.

### 2.2. Meteorolojik Hastalık Risk Analizi

**Girdiler:**
- Hava sıcaklığı
- Bağıl nem
- Yağış miktarı
- Uygun olduğunda yaprak ıslaklığı veya bu durumu temsil eden çevresel göstergeler
- Tarih, saat ve konum bilgileri

**İşlemler:**
- Meteorolojik verilerin toplanması
- Eksik ve hatalı verilerin kontrol edilmesi
- Hastalığa özgü çevresel koşulların değerlendirilmesi
- Enfeksiyon riskinin bilimsel modellerle hesaplanması

**Çıktılar:**
- Hastalık türü
- Risk seviyesi
- Risk hesaplama zamanı ve dönemi
- Kullanılan meteorolojik veriler
- Model ve bilimsel kaynak bilgisi
- Belirsizlik ve veri kalitesi bilgisi

### 2.3. Görüntü Tabanlı Hastalık Tespiti

**Girdiler:**
- Bitki veya bitki organına ait görüntüler
- Uygun olduğunda bitki türü ve organ bilgisi

**İşlemler:**
- Görüntü ön işleme
- Belirti analizi
- Eğitilmiş görüntü modelinin çalıştırılması
- Model tahmininin güven ve belirsizlik açısından değerlendirilmesi

**Çıktılar:**
- Olası hastalık veya belirti sınıfı
- Model tahmin güveni
- Görüntü kalitesi bilgisi
- Değerlendirme sonucu ve belirsizlik bilgisi

### 2.4. Çapraz Doğrulama

Bu katman, meteorolojik analiz ve görüntü analizinden elde edilen sonuçları birlikte değerlendirir.

**Temel görevleri:**
- Bulgular arasındaki uyumu incelemek
- Çelişkili sonuçları belirlemek
- Eksik veya yetersiz verileri tespit etmek
- Bir bileşenin sonucunun diğerini kesin olarak doğrulamadığını gözetmek

### 2.5. AI Agent Destekli Karar Mekanizması

AI Agent, önceki katmanlardan gelen yapılandırılmış çıktıları değerlendirir.

**Temel görevleri:**
- Bulguları anlaşılır biçimde açıklamak
- Belirsizlikleri ve veri eksikliklerini belirtmek
- Gerekli durumlarda ek veri veya görüntü istemek
- Uzman değerlendirmesi gerektiren durumları belirlemek
- Üreticiye karar destek çıktısı sunmak

AI Agent, bilimsel risk hesaplama motorunun yerine geçmez. Bilimsel modellerin ve analiz sonuçlarının yorumlanmasına yardımcı olur.

### 2.6. Nihai Çıktı

Sistem kullanıcıya aşağıdaki bilgileri sunmayı hedefler:

- Değerlendirilen bitki ve hastalık
- Meteorolojik risk sonucu
- Görüntü analiz sonucu
- Bulgular arasındaki uyum veya çelişki
- Güvenilirlik ve belirsizlik bilgisi
- Önerilen sonraki adımlar
- Gerekli durumlarda uzman yönlendirmesi

## 3. Veri Kaynakları ve Veri Yönetimi

### 3.1. Veri Kaynakları

Sistem farklı kaynaklardan veri alabilecek şekilde tasarlanacaktır.

**Meteorolojik Veri Kaynakları**
- Meteoroloji servislerinin API'leri
- Açık meteorolojik veri platformları
- Uygun olduğunda yerel meteoroloji istasyonları ve sensörler

**Görüntü Veri Kaynakları**
- Kullanıcı tarafından yüklenen bitki görüntüleri
- Bilimsel araştırmalarda yayımlanmış görüntü veri setleri
- Kullanım koşulları uygun olan açık erişimli veri setleri

**Bilimsel Bilgi Kaynakları**
- Hakemli bilimsel makaleler
- Tarımsal araştırma kurumlarının yayınları
- Hastalık modellerine ait bilimsel tablolar ve teknik dokümanlar
- Uzman değerlendirmeleri

Veri kaynaklarının güvenilirliği, güncelliği, erişim koşulları ve kullanım izinleri ayrıca değerlendirilecektir.

### 3.2. Veri Yönetimi Katmanları

Veriler üç temel aşamada yönetilecektir:

1. **Raw Data:** Kaynaktan elde edilen orijinal veriler, mümkün olduğunca değiştirilmeden saklanır.
2. **Processed Data:** Temizlenmiş, doğrulanmış ve analiz için hazırlanmış veriler saklanır.
3. **Analysis Results:** Risk motoru, görüntü analiz modeli ve doğrulama katmanının ürettiği sonuçlar saklanır.

Ham veriler ile işlenmiş veriler birbirinden ayrı tutulacaktır. Böylece analizlerin yeniden üretilmesi ve sonuçların denetlenmesi mümkün olacaktır.

### 3.3. Ortak Veri Yapısı

Farklı bileşenlerden gelen sonuçların birlikte değerlendirilebilmesi için standart veri yapıları kullanılacaktır.

Analiz sonuçlarında mümkün olduğunca aşağıdaki bilgiler bulunacaktır:

- **record_id:** Analiz kaydının benzersiz kimliği
- **crop_type:** Bitki türü
- **disease:** Değerlendirilen hastalık
- **location:** Konum bilgisi
- **observation_time:** Verinin gözlemlendiği zaman
- **data_source:** Verinin elde edildiği kaynak
- **analysis_type:** Analiz türü
- **result:** Analiz sonucu
- **confidence:** Model tarafından üretilen güven bilgisi, uygun olduğunda
- **uncertainty:** Belirsizlik bilgisi
- **quality_status:** Veri kalitesi durumu
- **model_version:** Kullanılan model veya kural setinin sürümü

Her analiz türünün kendine özgü ek alanları bulunabilir. Ortak alanlar, farklı modüllerin birbirleriyle uyumlu çalışmasını sağlayacaktır.

### 3.4. Veri İzlenebilirliği

Sistemin ürettiği her önemli sonuç için kullanılan veri kaynakları, analiz zamanı, model veya kural seti sürümü ve ilgili parametreler takip edilebilir olmalıdır.

Bu sayede sonuçların hangi verilere ve hangi bilimsel varsayımlara dayanarak üretildiği incelenebilecektir.

### 3.5. Veri Güvenilirliği ve Sınırlılıklar

- Eksik veya hatalı veriler kontrol edilmeden analizde kullanılmamalıdır.
- Veri kaynağı ve ölçüm yöntemi kayıt altına alınmalıdır.
- Tahmin edilen değerler gerçek ölçümlerden ayırt edilmelidir.
- Görüntü modelinin tahmini kesin teşhis olarak sunulmamalıdır.
- Bilimsel dayanağı doğrulanmamış eşikler kesin kurallar olarak kabul edilmemelidir.