[→ بخش ۲-۱: از مغز انسان تا مغز مصنوعی: سفری به دنیای شبکه‌های عصبی](./01-from-brain-to-ann.md) | [بخش ۲-۳: کشف الگوهای پنهان: یادگیری بدون نظارت (Unsupervised Learning) ←](./03-unsupervised-learning.md)

# فصل ۲: ماشین چگونه یاد می‌گیرد؟

## بخش ۲-۲: یادگیری بانظارت: آموزش ماشین با یک معلم مجازی

شما چگونه یاد گرفتید که یک گربه را از یک سگ تشخیص دهید؟ به احتمال زیاد، در کودکی، بزرگترها با اشاره به این حیوانات، نام آن‌ها را به شما گفته‌اند. هزاران مثال دیده‌اید و هزاران بار بازخورد گرفته‌اید. این فرآیند "یادگیری با معلم" است. چگونه می‌توانیم همین فرآیند را برای یک ماشین شبیه‌سازی کنیم تا به او یاد بدهیم یک سلول سرطانی را از یک سلول سالم تشخیص دهد؟

در بخش قبل، با ساختار یک شبکه عصبی آشنا شدیم. دیدیم که این شبکه‌ها از نرون‌های مصنوعی و اتصالات وزن‌دار تشکیل شده‌اند. اما این وزن‌ها در ابتدا مقادیر تصادفی دارند[1][2]. شبکه عصبی ما در ابتدای کار، مانند یک نوزاد است که هیچ چیز نمی‌داند. چگونه می‌توانیم به این شبکه آموزش دهیم تا وظیفه مشخصی را یاد بگیرد؟

پاسخ در رایج‌ترین رویکرد یادگیری ماشین نهفته است: **یادگیری با نظارت (Supervised Learning)**[1][3][4].

### 🎯 مسئله محوری این بخش:

فرض کنید مجموعه داده بزرگی از ایمیل‌ها به شما داده شده و وظیفه شما ساختن یک فیلتر اسپم (هرزنامه) است[5][6][7]. برای هر ایمیل، شما متن کامل آن (ورودی) را در اختیار دارید. مهم‌تر از آن، برای هر ایمیل یک برچسب نیز وجود دارد: «اسپم» یا «اسپم نیست» که توسط کاربران مشخص شده است[8][9]. چگونه از این داده‌های «برچسب‌دار» استفاده می‌کنید تا به یک ماشین «یاد بدهید» که یک ایمیل کاملاً جدید را به طور خودکار دسته‌بندی کند؟ نقش «معلم» در این فرآیند چیست؟

### **یادگیری با برچسب: معلم مجازی**

تصور کنید می‌خواهید به یک کودک تفاوت بین سیب و پرتقال را یاد بدهید. شما یک سیب را به او نشان می‌دهید (ورودی) و می‌گویید: "این سیب است" (برچسب/پاسخ صحیح). سپس یک پرتقال را نشان می‌دهید و می‌گویید: "این پرتقال است". با تکرار این فرآیند با ده‌ها مثال مختلف از سیب و پرتقال، کودک به تدریج یاد می‌گیرد که الگوهای مشخصی (رنگ، شکل، بافت) را با هر میوه مرتبط کند[10][11].

یادگیری بانظارت دقیقاً به همین شکل عمل می‌کند[3][12][4]. ما به ماشین یک **مجموعه داده آموزشی (Training Dataset)** می‌دهیم که شامل دو بخش است[1][13][14]:

1. **داده‌های ورودی (Input Data):** نمونه‌هایی از چیزی که می‌خواهیم ماشین یاد بگیرد. (مثلاً تصاویر ماموگرافی، توالی‌های DNA، داده‌های بیان ژن)[15][16][17].
2. **برچسب‌های صحیح (Correct Labels):** پاسخ درست برای هر نمونه ورودی. (مثلاً برچسب "سرطانی" یا "سالم" برای هر تصویر، نام ژن برای هر توالی)[3][11][18].

این مجموعه داده برچسب‌دار، نقش یک **معلم مجازی** یا یک **پاسخنامه** را برای ماشین ایفا می‌کند[19][20][21].

### **فرآیند آموزش: یک چرخه بازخورد**

فرآیند آموزش یک مدل یادگیری بانظارت، یک چرخه تکراری از پیش‌بینی، مقایسه و اصلاح است[22][23][24]. بیایید این چرخه را با مثال تشخیص سرطان دنبال کنیم[15][16][25]:

1. **پیش‌بینی (Predict):** یک تصویر از مجموعه آموزشی به شبکه عصبی (که وزن‌هایش هنوز تصادفی است) داده می‌شود[14][22]. شبکه آن را پردازش کرده و یک پیش‌بینی اولیه ارائه می‌دهد. مثلاً می‌گوید: "به احتمال ۳۰٪ سرطانی است"[26][27].

2. **مقایسه (Compare):** این پیش‌بینی با برچسب واقعی مقایسه می‌شود[26][28][29]. برچسب واقعی این تصویر در مجموعه داده ما، "سرطانی" (یعنی احتمال ۱۰۰٪) است. واضح است که پیش‌بینی شبکه اشتباه بوده و یک "خطا" یا "زیان" (Error / Loss) قابل توجهی وجود دارد[27][30][31].

3. **اصلاح (Correct / Backpropagation):** اینجاست که جادوی یادگیری اتفاق می‌افتد[22][32][23]. الگوریتم با استفاده از یک فرآیند ریاضی هوشمندانه به نام **پس‌انتشار (Backpropagation)**، این خطا را به صورت معکوس در شبکه به عقب برمی‌گرداند[22][33][34]. این الگوریتم محاسبه می‌کند که هر "وزن" در شبکه، چقدر در این خطای نهایی مقصر بوده است[32][35][36].

4. **تنظیم (Adjust):** سپس، وزن‌ها به مقدار بسیار کمی در جهتی تنظیم می‌شوند که خطا را کاهش دهند[37][24][38]. وزن‌هایی که بیشتر مقصر بودند، بیشتر تغییر می‌کنند[39][40].

این چرخه (پیش‌بینی -> مقایسه -> اصلاح -> تنظیم) هزاران یا میلیون‌ها بار برای تمام نمونه‌های موجود در مجموعه داده آموزشی تکرار می‌شود[1][14][11]. در هر تکرار، شبکه عصبی کمی بهتر می‌شود و پیش‌بینی‌هایش به پاسخ‌های صحیح نزدیک‌تر می‌گردد[24][38][30]. این فرآیند، مانند دانش‌آموزی است که مدام تمرین حل می‌کند، پاسخ‌هایش را با پاسخنامه چک می‌کند و از اشتباهاتش درس می‌گیرد.

### **نمودار چرخه یادگیری بانظارت**

```mermaid
flowchart TD
    %% Style Definitions
    classDef phase fill:#f8f9fa,stroke:#2c3e50,stroke-width:1.5px,color:#2c3e50
    classDef input fill:#e1f5fe,stroke:#01579b,stroke-width:1px,color:#01579b
    classDef process fill:#e6f2e6,stroke:#2e7d32,stroke-width:1px,color:#2e7d32
    classDef model fill:#f3e8f7,stroke:#6a1b9a,stroke-width:1px,color:#6a1b9a
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px,color:#e65100

    %% Supervised Learning Process
    subgraph Training [" "]
        direction TB
        A["ورودی برچسب‌دار<br>تصویر ماموگرافی + برچسب 'سرطان'"]
        B["شبکه عصبی<br>با وزن‌های اولیه"]
        C["پیش‌بینی مدل<br>'احتمال سرطان: ۳۰٪'"]
        D["محاسبه خطا<br>مقایسه پیش‌بینی با برچسب واقعی"]
        E["پس‌انتشار<br>محاسبه سهم هر وزن در خطا"]
        F["تنظیم وزن‌ها<br>کاهش خطای آینده"]
    end

    subgraph Inference [" "]
        direction TB
        G["مدل آموزش‌دیده"]
        H["داده جدید بدون برچسب"]
        I["پیش‌بینی نهایی"]
    end

    %% Training Loop Connections
    A -->|"۱. ورودی"| B
    B -->|"۲. پیش‌بینی"| C
    C -->|"۳. ارزیابی"| D
    D -->|"خطا زیاد است"| E
    E -->|"۴. بهینه‌سازی"| F
    F -->|"تکرار"| B

    %% Inference Connections
    F -->|"آموزش تمام شد"| G
    H -->|"داده جدید"| G
    G -->|"پیش‌بینی"| I

    %% Apply Styles
    class Training,Inference phase
    class A,H input
    class B,C,D,E,F process
    class G model
    class D decision

    %% Additional Styling for Rounded Shapes and Spacing
    style Training fill:#f8f9fa,stroke:#2c3e50,stroke-width:1.5px
    style Inference fill:#f8f9fa,stroke:#2c3e50,stroke-width:1.5px
    linkStyle default stroke:#6c757d,stroke-width:1.2px
```

### **آزمون نهایی: مرحله استنتاج (Inference)**

وقتی فرآیند آموزش کامل شد و وزن‌های شبکه بهینه شدند، مدل ما آماده استفاده در دنیای واقعی است[13][4][11]. به این مرحله **استنتاج (Inference)** یا **پیش‌بینی (Prediction)** می‌گویند. حالا ما می‌توانیم یک تصویر ماموگرافی **جدید** که مدل هرگز آن را ندیده و برچسبی ندارد، به آن بدهیم[17][41][42]. از آنجایی که مدل الگوهای مرتبط با سرطان را یاد گرفته است، می‌تواند با دقت بالایی پیش‌بینی کند که آیا این تصویر جدید، سرطانی است یا خیر[16][25][43].

### 🔬 تمرین تحلیلی: ارزیابی یک مدل پزشکی

**سناریو:** یک بیمارستان داده‌های ۱۰۰۰ بیمار را برای پیش‌بینی ریسک دیابت در اختیار شما قرار می‌دهد[44][45][46]. برای هر بیمار، ورودی‌هایی مانند سن، BMI و سطح قند خون و همچنین برچسب خروجی («دیابتی» یا «غیردیابتی») را دارید. شما یک مدل یادگیری بانظارت را آموزش می‌دهید.

**نتایج تست:** مدل شما بر روی ۱۰۰ بیمار جدید تست می‌شود. نتایج به این صورت است: مدل ۴۵ نفر از ۵۰ فرد غیردیابتی را به درستی و ۴۰ نفر از ۵۰ فرد دیابتی را به درستی شناسایی می‌کند.

#### نتایج ارزیابی مدل:

| معیار                  | مقدار | توضیحات                                                                |
| ---------------------- | ----- | ---------------------------------------------------------------------- |
| **دقت کلی (Accuracy)** | 85.0% | صحت کلی پیش‌بینی‌ها[47][48][49]                                        |
| **دقت (Precision)**    | 0.889 | از موارد پیش‌بینی شده دیابتی، چند درصد واقعاً دیابتی بودند[47][50][49] |
| **حساسیت (Recall)**    | 0.800 | از موارد واقعی دیابتی، چند درصد به درستی شناسایی شدند[47][48][50]      |
| **F1-Score**           | 0.842 | میانگین هارمونیک دقت و حساسیت[48][50][51]                              |

#### تحلیل خطاها:

| نوع خطا                        | تعداد  | خطرات در زمینه پزشکی                                    |
| ------------------------------ | ------ | ------------------------------------------------------- |
| **مثبت کاذب (False Positive)** | 5 نفر  | افراد سالم به اشتباه دیابتی تشخیص داده شدند[52][53][54] |
| **منفی کاذب (False Negative)** | 10 نفر | افراد دیابتی به اشتباه سالم تشخیص داده شدند[52][55][56] |

**سوال ۱:** دقت کلی (Overall Accuracy) مدل شما روی این مجموعه تست **85.0%** است.

**سوال ۲:** در زمینه پزشکی، **منفی کاذب (False Negative)** خطرناک‌تر است[53][54][57]. دلیل این موضوع این است که:

- **منفی کاذب:** بیماران واقعی دیابتی به اشتباه سالم تشخیص داده می‌شوند، که منجر به تأخیر در درمان و تشدید عوارض بیماری می‌شود[52][55][58].
- **مثبت کاذب:** افراد سالم به اشتباه بیمار تشخیص داده می‌شوند، که اگرچه باعث اضطراب و آزمایش‌های اضافی می‌شود، اما خطر جانی مستقیمی ندارد[53][54].

### 💡 نکات کلیدی این بخش

- **یادگیری با داده‌های برچسب‌دار:** یادگیری بانظارت از داده‌های دارای برچسب (جفت‌های ورودی-خروجی) برای آموزش یک مدل استفاده می‌کند[1][3][12].

- **چرخه آموزش:** فرآیند آموزش شامل یک چرخه تکراری است: پیش‌بینی، مقایسه با برچسب صحیح، محاسبه خطا و تنظیم پارامترهای مدل[22][23][30].

- **هدف نهایی:** هدف اصلی، قادر ساختن مدل به انجام پیش‌بینی‌های دقیق بر روی داده‌های جدید و دیده‌نشده است[13][4][2].

- **الگوریتم کلیدی:** پس‌انتشار (Backpropagation) الگوریتم اصلی برای تنظیم وزن‌ها در شبکه‌های عصبی طی فرآیند آموزش است[22][32][33].

- **ارزیابی عملکرد:** معیارهای مختلفی مانند دقت، precision، recall و F1-score برای سنجش کیفیت مدل‌های یادگیری بانظارت استفاده می‌شود[47][48][49].

در بخش بعدی، با نوع دیگری از یادگیری آشنا می‌شویم که در آن، هیچ معلم یا پاسخنامه‌ای در کار نیست!

---

## **منابع**

[1] https://www.geeksforgeeks.org/supervised-machine-learning/
[2] https://en.wikipedia.org/wiki/Supervised_learning
[3] https://encord.com/blog/mastering-supervised-learning-a-comprehensive-guide/
[4] https://cloud.google.com/discover/what-is-supervised-learning
[5] https://github.com/kanagalingamsm/Email-Spam-Detection
[6] https://avinuty.ac.in/sites/avinuty.ac.in/files/2024-09/Thameena%20Report.pdf
[7] https://dergipark.org.tr/tr/pub/saufenbilder/issue/84130/1264476
[8] https://www.youtube.com/watch?v=Ps0y6w4cD_U
[9] https://www.geeksforgeeks.org/nlp/detecting-spam-emails-using-tensorflow-in-python/
[10] https://www.grammarly.com/blog/ai/what-is-supervised-learning/
[11] https://www.ibm.com/think/topics/supervised-learning
[12] https://encord.com/glossary/supervised-learning-definition/
[13] https://www.coursera.org/articles/supervised-learning
[14] https://www.mathworks.com/help/stats/supervised-learning-machine-learning-workflow-and-algorithms.html
[15] https://kili-technology.com/data-labeling/machine-learning/machine-learning-and-medical-diagnosis-an-introduction-to-how-ai-improves-disease-detection
[16] https://news.harvard.edu/gazette/story/2024/09/new-ai-tool-can-diagnose-cancer-guide-treatment-predict-patient-survival/
[17] https://health.google/caregivers/mammography/
[18] https://pmc.ncbi.nlm.nih.gov/articles/PMC8950225/
[19] https://www.oracle.com/tr/artificial-intelligence/machine-learning/supervised-learning/
[20] https://www.oracle.com/sg/artificial-intelligence/machine-learning/supervised-learning/
[21] https://www.seldon.io/supervised-vs-unsupervised-learning-explained-2/
[22] https://www.ibm.com/think/topics/backpropagation
[23] https://www.geeksforgeeks.org/machine-learning/backpropagation-in-neural-network/
[24] https://www.ibm.com/think/topics/gradient-descent
[25] https://newatlas.com/cancer/ai-cancer-diagnostic/
[26] https://towardsdatascience.com/loss-functions-and-their-use-in-neural-networks-a470e703f1e9/
[27] https://builtin.com/machine-learning/loss-functions
[28] https://www.scaler.com/topics/loss-functions-in-neural-networks/
[29] https://www.ibm.com/think/topics/loss-function
[30] https://www.datacamp.com/tutorial/loss-function-in-machine-learning
[31] https://www.geeksforgeeks.org/deep-learning/loss-functions-in-deep-learning/
[32] https://brilliant.org/wiki/backpropagation/
[33] https://en.wikipedia.org/wiki/Backpropagation
[34] https://neptune.ai/blog/backpropagation-algorithm-in-neural-networks-guide
[35] http://neuralnetworksanddeeplearning.com/chap2.html
[36] https://towardsdatascience.com/understanding-backpropagation-abcc509ca9d0/
[37] https://developers.google.com/machine-learning/crash-course/linear-regression/gradient-descent
[38] https://www.geeksforgeeks.org/gradient-descent-algorithm-and-its-variants/
[39] https://en.wikipedia.org/wiki/Gradient_descent
[40] https://builtin.com/data-science/gradient-descent
[41] https://www.cancer.gov/research/infrastructure/artificial-intelligence
[42] https://www.cancerresearch.org/blog/ai-cancer
[43] https://www.sciencedirect.com/science/article/abs/pii/S0344033823006970
[44] https://pmc.ncbi.nlm.nih.gov/articles/PMC10107388/
[45] https://www.nature.com/articles/s41598-024-78519-8
[46] https://www.sciencedirect.com/science/article/pii/S1877050920300557
[47] https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall
[48] https://www.geeksforgeeks.org/machine-learning/metrics-for-machine-learning-model/
[49] https://www.evidentlyai.com/classification-metrics/accuracy-precision-recall
[50] https://encord.com/blog/classification-metrics-accuracy-precision-recall/
[51] https://deepai.org/machine-learning-glossary-and-terms/evaluation-metrics
[52] https://en.wikipedia.org/wiki/False_positives_and_false_negatives
[53] https://pmc.ncbi.nlm.nih.gov/articles/PMC4942505/
[54] https://www.apbiocode.com/false-positives/
[55] https://gpnotebook.com/pages/general-practice/false-positives-and-negatives
[56] https://manoa.hawaii.edu/exploringourfluidearth/chemical/matter/properties-matter/practices-science-false-positives-and-false-negatives
[57] https://centerforhealthsecurity.org/sites/default/files/2022-11/201207-sensitivity-specificty-factsheet.pdf
[58] https://dergipark.org.tr/tr/pub/ejosat/issue/65857/1015816
[59] https://www.geeksforgeeks.org/machine-learning/real-life-examples-of-supervised-learning-and-unsupervised-learning/
[60] https://emeritus.org/blog/ai-and-ml-supervised-learning/
[61] https://www.v7labs.com/blog/supervised-vs-unsupervised-learning
[62] https://www.superannotate.com/blog/supervised-learning-and-other-machine-learning-tasks
[63] https://www.datacamp.com/blog/supervised-machine-learning
[64] https://developers.google.com/machine-learning/intro-to-ml/supervised
[65] https://www.altexsoft.com/blog/semi-supervised-learning/
[66] https://builtin.com/machine-learning/backpropagation-neural-network
[67] https://www.komtas.com/en/glossary/gradient-descent-nedir
[68] https://www.youtube.com/watch?v=i62czvwDlsw
[69] https://www.youtube.com/watch?v=Ilg3gGewQ5U
[70] https://www.youtube.com/watch?v=VMj-3S1tku0
[71] https://www.nature.com/articles/s41467-020-17419-7
[72] https://www.spectral-ai.com/blog/artificial-intelligence-in-medical-diagnosis-how-medical-diagnostics-are-improving-through-ai/
[73] https://eithealth.eu/news-article/machine-learning-in-healthcare-uses-benefits-and-pioneers-in-the-field/
[74] https://www.youtube.com/watch?v=GN9EejfU4aI
[75] https://www.cs.cornell.edu/courses/cs4780/2022fa/lectures/lecturenote01_MLsetup.html
[76] https://www.linkedin.com/advice/1/what-most-common-machine-learning-algorithms-used-0vpuf
[77] https://github.com/Karanmehra7107/Medical_Diagnosis
[78] https://www.sciencedirect.com/science/article/pii/S1746809422009351
[79] https://docs.edgeimpulse.com/docs/concepts/machine-learning/neural-networks/loss-functions
[80] https://www.nature.com/articles/s41598-024-56706-x
[81] https://www.digitalocean.com/community/tutorials/deep-learning-metrics-precision-recall-accuracy
[82] https://dergipark.org.tr/en/download/article-file/1648927
[83] https://www.aiacceleratorinstitute.com/evaluating-machine-learning-models-metrics-and-techniques/
[84] https://testfully.io/blog/false-positive-false-negative/
[85] https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset
[86] https://www.sciencedirect.com/topics/computer-science/evaluation-metric
[87] https://www.mdpi.com/2227-9032/13/1/37
