# فصل ۱: انقلاب جدید در زیست‌شناسی

## بخش ۱-۴: مطالعه موردی: تشخیص سرطان با تصاویر پزشکی

در بخش قبل، با ابعاد ترسناک "سونامی داده" آشنا شدیم. اما گاهی، چالش در حجم داده نیست، بلکه در پیچیدگی و ظرافت اطلاعات نهفته در آن است. یک تصویر پزشکی، تنها چند مگابایت حجم دارد، اما اطلاعات درون آن می‌تواند مرگ و زندگی را رقم بزند. در این مطالعه موردی، می‌خواهیم ببینیم هوش مصنوعی چگونه به کمک یکی از حساس‌ترین و پراسترس‌ترین تخصص‌های پزشکی، یعنی رادیولوژی، می‌آید.

تصور کنید یک رادیولوژیست هستید. هر روز، صدها تصویر ماموگرافی از مقابل چشمان شما عبور می‌کند. هر تصویر، یک داستان بالقوه از زندگی یک انسان است. وظیفه شما این است که در میان انبوهی از بافت‌های سالم، کوچکترین نشانه‌های یک تومور بدخیم را پیدا کنید. این یک مسئولیت بسیار سنگین است. یک اشتباه کوچک می‌تواند به قیمت جان یک بیمار تمام شود.

### **چالش‌های پیچیده غربالگری سرطان پستان**

چالش بزرگ در این کار، تنها پیدا کردن سرطان نیست، بلکه نادیده گرفتن موارد غیرسرطانی است. دو نوع خطا در اینجا بسیار پرهزینه است:

1. **مثبت کاذب (False Positive):** زمانی که یک توده خوش‌خیم یا یک سایه بی‌خطر، به اشتباه به عنوان سرطان تشخیص داده می‌شود. این خطا منجر به اضطراب شدید بیمار و انجام نمونه‌برداری‌های دردناک و غیرضروری می‌شود.

2. **منفی کاذب (False Negative):** زمانی که یک تومور واقعی، از چشم رادیولوژیست پنهان می‌ماند و به بیمار گفته می‌شود که همه چیز طبیعی است. این خطرناک‌ترین نوع خطاست، زیرا به سرطان فرصت رشد و پیشرفت می‌دهد.

آمار جهانی نشان می‌دهد که این مشکل گسترده است. در ایالات متحده، حدود **۱۱٪** از ماموگرافی‌های غربالگری منجر به نتیجه مثبت کاذب می‌شوند، در حالی که در اروپا این رقم حدود **۲.۵٪** است[1][2]. اما آمار تجمعی نگران‌کننده‌تر است: تقریباً **۴۹٪** از زنان آمریکایی و **۲۰٪** از زنان اروپایی پس از ۱۰ بار غربالگری، حداقل یک بار با نتیجه مثبت کاذب مواجه می‌شوند[2][3].

این نرخ‌ها بر اساس سن نیز متفاوت است. زنان جوان‌تر (۴۰-۴۹ ساله) نرخ بالاتری از نتایج مثبت کاذب دارند - حدود **۱۲۱ مورد در هر ۱۰۰۰ غربالگری** - در مقایسه با زنان ۵۰-۵۹ ساله که این رقم به **۹۳ مورد در هر ۱۰۰۰ غربالگری** می‌رسد[4].

### **کمبود جهانی رادیولوژیست‌ها و چالش خوانش دوگانه**

به دلیل همین فشار و پیچیدگی، در بسیاری از کشورهای پیشرفته - شامل کشورهای اروپایی، انگلستان، و استرالیا - هر تصویر ماموگرافی توسط **دو رادیولوژیست** به صورت مستقل بررسی می‌شود[5][6]. این کار دقت را بالا می‌برد، اما حجم کار را نیز دو برابر می‌کند و با توجه به کمبود جهانی رادیولوژیست‌های متخصص، یک چالش بزرگ است.

مطالعات نشان می‌دهند که برای پیاده‌سازی سیستم خوانش دوگانه در سطح جهان، به **۱۲,۰۰۰ تا ۱۴,۰۰۰ رادیولوژیست اضافی** نیاز است[7][8]. این در حالی است که بسیاری از کشورها در حال حاضر با کمبود جدی رادیولوژیست مواجه هستند.

### **ورود یک همکار خستگی‌ناپذیر: هوش مصنوعی**

اینجا جایی است که هوش مصنوعی وارد میدان می‌شود. در یک مطالعه پیشگامانه که در ژانویه ۲۰۲۰ در مجله معتبر **Nature** منتشر شد، یک تیم تحقیقاتی از گوگل یک سیستم هوش مصنوعی را توسعه داد که می‌توانست تصاویر ماموگرافی را با دقتی فراتر از متخصصان انسانی تحلیل کند[1][9].

این سیستم هوش مصنوعی بر روی مجموعه داده عظیمی شامل ماموگرافی‌های **بیش از ۹۱,۰۰۰ زن** از بریتانیا و ایالات متحده آموزش دیده بود[10][11]. درست مانند یک رادیولوژیست کارآموز که با دیدن هزاران مثال یاد می‌گیرد، این هوش مصنوعی نیز الگوهای ظریف و پیچیده‌ای را که نشان‌دهنده سرطان هستند، از دل داده‌ها استخراج کرد.

### **نتایج شگفت‌انگیز: دقت بالاتر، خطای کمتر**

نتایج این تحقیق، جامعه پزشکی را شگفت‌زده کرد:

- **کاهش خطاهای تشخیصی:** این سیستم توانست موارد **مثبت کاذب** را تا **۵.۷٪** در مجموعه داده آمریکایی و **۱.۲٪** در مجموعه داده بریتانیایی کاهش دهد. همزمان، موارد **منفی کاذب** (یعنی سرطان‌های دیده‌نشده) را تا **۹.۴٪** در آمریکا و **۲.۷٪** در بریتانیا کم کرد[1][9].

- **عملکرد بهتر از متخصصان:** در یک مقایسه مستقیم با شش رادیولوژیست خبره، سیستم هوش مصنوعی عملکردی **۱۱.۵٪ بهتر** از میانگین آن‌ها بر اساس سطح زیر منحنی ROC داشت[1][12].

- **کاهش حجم کار:** شبیه‌سازی‌ها نشان داد که اگر از این هوش مصنوعی به عنوان "خواننده دوم" در کنار یک رادیولوژیست انسانی استفاده شود، می‌توان حجم کاری که نیاز به بررسی توسط رادیولوژیست دوم دارد را تا **۸۸٪** کاهش داد[1]! این یعنی آزاد شدن وقت متخصصان برای تمرکز بر روی موارد پیچیده‌تر.

### **تأیید نتایج در مطالعات بعدی**

مطالعات بعدی این نتایج را تأیید کرده‌اند. در سال ۲۰۲۳، مطالعه بزرگ PRAIM در آلمان با **۴۶۳,۰۹۴ زن** نشان داد که AI-supported double reading منجر به **۱۷.۶٪ افزایش در نرخ تشخیص سرطان** شد، بدون اینکه نرخ فراخوانی (recall rate) افزایش یابد[13]. همچنین مطالعات در سوئد نشان دادند که AI می‌تواند حجم کار رادیولوژیست‌ها را تا **۶۲.۶٪** کاهش دهد[14].

### **نمودار: هوش مصنوعی به عنوان خواننده دوم**

بیایید فرآیند خوانش دوگانه را با و بدون هوش مصنوعی مقایسه کنیم:

```mermaid
flowchart TD
    %% Style Definitions
    classDef phase fill:#f8f9fa,stroke:#2c3e50,stroke-width:1.5px,color:#2c3e50
    classDef input fill:#e1f5fe,stroke:#01579b,stroke-width:1px,color:#01579b
    classDef process fill:#e6f2e6,stroke:#2e7d32,stroke-width:1px,color:#2e7d32
    classDef model fill:#f3e8f7,stroke:#6a1b9a,stroke-width:1px,color:#6a1b9a

    %% Standard Double Reading Process
    subgraph A ["فرآیند استاندارد خوانش دوگانه | Standard Double Reading"]
        direction LR
        Mammo("تصویر ماموگرافی<br>Mammogram") --> Rad1("رادیولوژیست ۱<br>Radiologist 1")
        Mammo --> Rad2("رادیولوژیست ۲<br>Radiologist 2")
        Rad1 --> Consensus{تصمیم‌گیری نهایی<br>Final Decision}
        Rad2 --> Consensus
    end

    %% AI-Assisted Double Reading Process
    subgraph B ["فرآیند با کمک هوش مصنوعی | AI-Assisted Reading"]
        direction LR
        Mammo2("تصویر ماموگرافی<br>Mammogram") --> Rad1_2("رادیولوژیست ۱<br>Radiologist 1")
        Mammo2 --> AI("هوش مصنوعی<br>AI (Second Reader)")
        Rad1_2 --> Consensus2{تصمیم‌گیری نهایی<br>Final Decision}
        AI --> Consensus2
    end

    %% Connections Between Processes
    A ---|"مقایسه"| B

    %% Apply Styles
    class A,B phase
    class Mammo,Mammo2 input
    class Rad1,Rad2,Rad1_2,Consensus,Consensus2 process
    class AI model

    %% Additional Styling for Rounded Shapes and Spacing
    style A fill:#f8f9fa,stroke:#2c3e50,stroke-width:1.5px
    style B fill:#f8f9fa,stroke:#2c3e50,stroke-width:1.5px
    linkStyle default stroke:#6c757d,stroke-width:1.2px
```

در مدل جدید، هوش مصنوعی می‌تواند نقش رادیولوژیست دوم را با سرعت و دقت بالا ایفا کند و تنها در موارد مشکوک یا پیچیده، نظر یک رادیولوژیست انسانی دیگر خواسته شود.

### **تأثیر False Positive بر بیماران**

مطالعات جدید نشان می‌دهند که نتایج مثبت کاذب تأثیر منفی قابل توجهی بر رفتار غربالگری آتی بیماران دارد. زنانی که نتیجه مثبت کاذب دریافت می‌کنند، کمتر مایل به بازگشت برای غربالگری‌های بعدی هستند:

- پس از فراخوانی برای تصویربرداری اضافی: **۲٪ کاهش** در نرخ بازگشت
- پس از توصیه Follow-up کوتاه‌مدت: **۱۶٪ کاهش** در نرخ بازگشت
- پس از توصیه برای بیوپسی: **۱۰٪ کاهش** در نرخ بازگشت[15]

### 🔬 تمرین تحلیلی: شما یک رادیولوژیست هستید!

تصور کنید سه تصویر ماموگرافی به شما داده شده است. سیستم هوش مصنوعی برای هر کدام یک "امتیاز ریسک" از ۰ تا ۱۰۰ محاسبه کرده است. رادیولوژیست همکار شما نیز نظر خود را اعلام کرده است. با توجه به اطلاعات زیر، برای هر بیمار چه تصمیمی می‌گیرید؟ (نمونه‌برداری، بررسی بیشتر، یا اعلام نتیجه سالم)

| بیمار       | امتیاز ریسک هوش مصنوعی | نظر رادیولوژیست همکار | اطلاعات تکمیلی                                  | تصمیم شما؟ |
| :---------- | :--------------------- | :-------------------- | :---------------------------------------------- | :--------- |
| **بیمار A** | ۹۵                     | بسیار مشکوک           | بیمار سابقه خانوادگی سرطان دارد.                |            |
| **بیمار B** | ۴۰                     | احتمالاً خوش‌خیم      | توده شکلی منظم و حاشیه صاف دارد.                |            |
| **بیمار C** | ۸                      | بدون مورد مشکوک       | بیمار هیچ علامتی ندارد و این یک چکاپ روتین است. |            |

**فکر کنید:**

- در کدام مورد، نظر هوش مصنوعی و انسان همسو است و تصمیم‌گیری آسان‌تر است؟
- در کدام مورد، اختلاف نظر وجود دارد؟ در این شرایط، چه عاملی می‌تواند به تصمیم‌گیری نهایی کمک کند؟ (به ستون اطلاعات تکمیلی دقت کنید)
- اگر شما مسئول طراحی یک سیستم همکاری بین انسان و هوش مصنوعی بودید، چگونه قوانینی برای حل اختلاف نظرها وضع می‌کردید؟

### 💡 نکات کلیدی این بخش

- **دقت فراتر از انسان:** هوش مصنوعی می‌تواند تصاویر پزشکی را با دقتی معادل یا حتی فراتر از متخصصان انسانی تحلیل کند.
- **کاهش خطاهای تشخیصی:** AI به طور همزمان موارد مثبت و منفی کاذب را کاهش می‌دهد، که منجر به تشخیص‌های دقیق‌تر و کاهش اضطراب بیماران می‌شود.
- **حل بحران نیروی انسانی:** با کمبود جهانی رادیولوژیست‌ها، AI می‌تواند به عنوان "خواننده دوم" عمل کند و حجم کار را تا ۸۸٪ کاهش دهد.
- **همکاری انسان و ماشین:** آینده پزشکی پیشرفته در همکاری هوشمندانه پزشکان و سیستم‌های هوش مصنوعی نهفته است، نه در جایگزینی انسان توسط ماشین.
- **تأیید در مطالعات گسترده:** نتایج اولیه در مطالعات بزرگ‌تر و در شرایط واقعی تأیید شده‌اند.

این مطالعه موردی نشان می‌دهد که آینده پزشکی، نه در رقابت بین انسان و ماشین، بلکه در **همکاری هوشمندانه** این دو نهفته است. هوش مصنوعی می‌تواند با تحلیل حجم عظیمی از داده‌ها، الگوهایی را کشف کند که از چشم انسان پنهان می‌مانند و به پزشکان کمک کند تا تصمیمات بهتر و دقیق‌تری برای بیماران خود بگیرند.

---

## **منابع**

[1] https://pubmed.ncbi.nlm.nih.gov/31894144/
[2] https://jamanetwork.com/journals/jamaoncology/fullarticle/2811409
[3] https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(04)17676-9/fulltext
[4] https://pmc.ncbi.nlm.nih.gov/articles/PMC5091936/
[5] https://www.sciencedirect.com/science/article/abs/pii/S0720048X25001871
[6] https://www.rsna.org/news/2022/september/trained-radiographers
[7] https://ajronline.org/doi/pdf/10.2214/AJR.08.1665
[8] https://ajronline.org/doi/10.2214/AJR.08.1665
[9] https://www.nature.com/articles/s41586-019-1799-6
[10] https://www.techzine.eu/news/analytics/44197/google-develops-ai-model-for-recognising-breast-cancer/
[11] https://futurism.com/neoscope/google-ai-spot-breast-cancer
[12] https://siliconangle.com/2020/01/01/googles-new-ai-detects-breast-cancer-accurately-doctors/
[13] https://www.nature.com/articles/s41591-024-03408-6
[14] https://pubs.rsna.org/doi/full/10.1148/ryai.230529
[15] https://pmc.ncbi.nlm.nih.gov/articles/PMC11970968/
[16] https://time.com/6237088/mammograms-google-ai/
[17] https://pubmed.ncbi.nlm.nih.gov/37541274/
[18] https://www.insideprecisionmedicine.com/topics/oncology/ai-algorithm-could-reduce-breast-cancer-mammogram-false-positive-rate/
[19] https://health.google/caregivers/mammography/
[20] https://www.bmj.com/content/374/bmj.n1872
[21] https://www.breast.or.kr/api/society/journal/download/40204/21_2_131-139.pdf
[22] https://www.sciencedirect.com/science/article/pii/S2352047723000710
[23] https://pmc.ncbi.nlm.nih.gov/articles/PMC8463596/
[24] https://www.sciencedirect.com/science/article/pii/S2949916X24000732
[25] https://www.rsna.org/news/2024/june/ai-detects-more-breast-cancers
[26] https://pmc.ncbi.nlm.nih.gov/articles/PMC11230971/
[27] https://www.thelancet.com/journals/landig/article/PIIS2589-7500(23)00153-X/fulltext
[28] https://pubs.rsna.org/doi/full/10.1148/ryai.230033
[29] https://www.nature.com/articles/s41467-025-57469-3
[30] https://www.cancer.gov/news-events/cancer-currents-blog/2024/mammogram-false-positives-affect-future-screening
[31] https://www.nature.com/articles/s41591-023-02625-9
[32] https://www.sciencedirect.com/science/article/pii/S3050577125000118
[33] https://pubs.rsna.org/doi/full/10.1148/radiol.222679
[34] https://pubs.rsna.org/doi/abs/10.1148/radiol.222691
[35] https://pmc.ncbi.nlm.nih.gov/articles/PMC10625863/
[36] https://pmc.ncbi.nlm.nih.gov/articles/PMC11605140/
[37] https://pmc.ncbi.nlm.nih.gov/articles/PMC11655727/
[38] https://deephealth.com/evidence/publications/radiologists-using-categorical-ai-for-screening-mammography-improve-more-than-double-reading-alone/
[39] https://www.newscientist.com/article/2228752-ai-system-is-better-than-human-doctors-at-predicting-breast-cancer/
[40] https://www.nature.com/articles/s41598-024-62324-4
[41] https://www.bmj.com/content/368/bmj.m16
[42] https://deepmind.google/discover/blog/international-evaluation-of-an-ai-system-for-breast-cancer-screening/
[43] https://www1.racgp.org.au/newsgp/clinical/breast-screening-false-positives-could-discourage
[44] https://www.auntminnie.com/clinical-news/womens-imaging/breast/article/15631828/could-radiographers-help-with-double-reading-of-mammography
[45] https://pmc.ncbi.nlm.nih.gov/articles/PMC9818874/
[46] https://dialnet.unirioja.es/descarga/articulo/9873218.pdf
[47] https://digital.nhs.uk/data-and-information/publications/statistical/breast-screening-programme/england---2020-21/qualitystatement3
[48] https://pubs.rsna.org/doi/full/10.1148/radiol.212951
[49] https://www.uspreventiveservicestaskforce.org/home/getfilebytoken/PGYTn_cWQnmAr9-3du5StE
[50] https://www.insideprecisionmedicine.com/topics/oncology/ai-enhances-breast-cancer-detection-rates-can-reduce-radiologist-shortages/
[51] https://www.nature.com/articles/s41598-025-86993-x
[52] https://www.sciencedirect.com/science/article/pii/S1078817424003560
[53] https://pmc.ncbi.nlm.nih.gov/articles/PMC10825593/
[54] https://www.auntminnieeurope.com/radiographers/article/15657144/radiographers-can-add-value-in-double-reading-of-mammography
[55] https://pmc.ncbi.nlm.nih.gov/articles/PMC11891547/
[56] https://www.lunit.io/en/company/blog/lunit-ai-game-changer-in-breast-cancer-screening-replacing-one-human-reader-in-europe
[57] https://pubs.rsna.org/doi/full/10.1148/radiol.223299
[58] https://pubmed.ncbi.nlm.nih.gov/22972811/
[59] https://healthcare-in-europe.com/en/news/radiologist-shortage-trained-radiographers.html
[60] https://www.sciencedirect.com/science/article/pii/S096097762400033X
[61] https://www.nature.com/articles/s41467-024-51725-8
[62] https://pubs.rsna.org/doi/full/10.1148/radiol.232034
[63] https://physicsworld.com/a/ai-rivals-human-radiologists-at-breast-cancer-detection/
