[→ آزمون جامع نهایی](./index.md) | [سناریو ۲: سوالات ←](./scenario-02-questions.md) | [پاسخنامه سناریو ۱](./scenario-01-answers.md)

# سناریو ۱: فارماکوژنومیکس و پیش‌بینی پاسخ به دارو

یک شرکت داروسازی در حال توسعه داروی جدیدی به نام "Respondin" برای درمان نوعی سرطان ریه است. مطالعات اولیه نشان داده است که پاسخ بیماران به این دارو به شدت متفاوت است. تیم شما وظیفه دارد مدلی برای پیش‌بینی پاسخ بیماران بسازد تا در نهایت بتوان بیماران مناسب برای کارآزمایی بالینی فاز ۳ را انتخاب کرد.

---

### **بخش ۱-۱: تحلیل و پاک‌سازی داده‌های پیچیده**

تیم بالینی یک مجموعه داده شامل اطلاعات ۲۰ بیمار را در اختیار شما قرار داده است. این داده‌ها شامل سن بیمار، وجود یا عدم وجود دو جهش ژنتیکی (`EGFR_mut`, `TP53_mut`)، سطح یک بیومارکر پروتئینی (`C_Marker`)، و نوع بافت‌شناسی تومور (`Tumor_Type`) است. ستون `Response` که پاسخ بیمار به دارو را نشان می‌دهد، دارای مقادیر گمشده و ناهماهنگ است.

**داده‌های اولیه:**

```python
import pandas as pd
import numpy as np
import io

csv_data = """patient_id,age,EGFR_mut,TP53_mut,C_Marker,Tumor_Type,Response
P01,65,True,False,154.5,Adenocarcinoma,Responder
P02,72,False,True,88.2,Squamous Cell,Non-Responder
P03,58,True,True,171.1,Adenocarcinoma,Responder
P04,61,False,False,95.0,Large Cell,Non-Responder
P05,55,True,False,210.8,Adenocarcinoma,RESPONDER
P06,80,True,True,115.3,Adenocarcinoma,Non-Responder
P07,68,False,True,102.7,Squamous Cell,non-responder
P08,59,True,False,195.4,Adenocarcinoma,Responder
P09,63,False,False,121.0,Large Cell,
P10,75,True,True,165.7,Adenocarcinoma,Responder
P11,52,False,True,99.9,Squamous Cell,Non-Responder
P12,67,True,False,182.1,Adenocarcinoma,
P13,71,False,False,110.5,Large Cell,Non-Responder
P14,56,True,True,159.0,Adenocarcinoma,Responder
P15,79,False,True,92.4,Squamous Cell,Non-Responder
P16,60,True,False,225.0,Adenocarcinoma,Responder
P17,66,False,False,105.3,Large Cell,Non-Responder
P18,54,True,True,148.8,Adenocarcinoma,non-responder
P19,73,False,True,130.0,Squamous Cell,Non-Responder
P20,62,True,False,201.5,Adenocarcinoma,Responder
"""
df = pd.read_csv(io.StringIO(csv_data))
```

**سوال ۱:**
تیم تصمیم می‌گیرد برای پر کردن مقادیر گمشده ستون `Response`، از یک استراتژی هوشمند استفاده کند:

- ابتدا تمام مقادیر رشته‌ای در ستون `Response` به حروف بزرگ تبدیل شوند.
- سپس، برای بیمارانی که `Tumor_Type` آن‌ها `Adenocarcinoma` است، مقادیر گمشده با `RESPONDER` پر شوند.
- برای سایر `Tumor_Type` ها، مقادیر گمشده با `NON-RESPONDER` پر شوند.

پس از اجرای این استراتژی، چه تعداد بیمار `RESPONDER` و `NON-RESPONDER` در دیتافریم نهایی خواهیم داشت؟

الف) Responder: 10, Non-Responder: 10
ب) Responder: 11, Non-Responder: 9
ج) Responder: 9, Non-Responder: 11
د) Responder: 12, Non-Responder: 8

**سوال ۲:**
برای آماده‌سازی داده‌ها جهت ورود به مدل، شما باید ستون‌های غیرعددی را به فرمت عددی تبدیل کنید (`Encoding`). تیم شما تصمیم می‌گیرد از روش One-Hot Encoding برای ستون `Tumor_Type` استفاده کند. پس از این تبدیل، دیتافریم شما چند ستون اضافی خواهد داشت و مجموع مقادیر در ستون جدید `Tumor_Type_Adenocarcinoma` چقدر خواهد بود؟

الف) 2 ستون اضافی، مجموع: 10
ب) 3 ستون اضافی، مجموع: 10
ج) 2 ستون اضافی، مجموع: 12
د) 3 ستون اضافی، مجموع: 12

---

### **بخش ۱-۲: ساخت و ارزیابی مدل طبقه‌بندی**

با استفاده از داده‌های پاک‌شده و تبدیل‌شده، شما یک مدل طبقه‌بندی (Classifier) برای پیش‌بینی ستون `Response` آموزش می‌دهید. پس از آموزش و تست مدل روی مجموعه داده آزمون (که شامل ۵۰ نمونه بوده است)، ماتریس درهم‌ریختگی (Confusion Matrix) زیر به دست آمده است. در این ماتریس، کلاس ۱ نماینده "Responder" و کلاس 0 نماینده "Non-Responder" است.

|               | Predicted: 0 | Predicted: 1 |
| :------------ | :----------: | :----------: |
| **Actual: 0** |   TN = 28    |    FP = 2    |
| **Actual: 1** |    FN = 5    |   TP = 15    |

**سوال ۳:**
با توجه به این‌که هدف اصلی، انتخاب بیماران مناسب برای کارآزمایی بالینی است (یعنی به حداکثر رساندن شانس موفقیت دارو)، کدام معیار ارزیابی برای انتخاب بهترین مدل از اهمیت بالاتری برخوردار است و چرا؟

الف) **Accuracy**، زیرا نشان‌دهنده عملکرد کلی و صحیح مدل است.
ب) **Specificity (TN / (TN+FP))**، زیرا نشان می‌دهد مدل چقدر در شناسایی صحیح افراد غیرپاسخ‌دهنده موفق است.
ج) **Precision (TP / (TP+FP))**، زیرا تضمین می‌کند بیمارانی که به عنوان "Responder" انتخاب می‌شوند، به احتمال زیاد واقعاً به دارو پاسخ خواهند داد.
د) **Recall (TP / (TP+FN))**، زیرا تضمین می‌کند که هیچ بیمار پاسخ‌دهنده‌ای را از دست نمی‌دهیم، حتی به قیمت انتخاب چند بیمار اشتباه.

**سوال ۴:**
با توجه به ماتریس درهم‌ریختگی بالا، مقادیر **Precision**، **Recall** و **F1-Score** برای کلاس "Responder" (کلاس ۱) به ترتیب چقدر است؟ (اعداد را تا دو رقم اعشار گرد کنید)

الف) Precision=0.88, Recall=0.75, F1-Score=0.81
ب) Precision=0.85, Recall=0.79, F1-Score=0.82
ج) Precision=0.94, Recall=0.75, F1-Score=0.83
د) Precision=0.88, Recall=0.83, F1-Score=0.85

---

### **بخش ۱-۳: مدل‌سازی رگرسیون برای تحلیل بیومارکر**

تیم تحقیقاتی می‌خواهد رابطه بین سن بیمار (`age`) و سطح بیومارکر (`C_Marker`) را در میان بیماران **پاسخ‌دهنده (Responder)** تحلیل کند. آن‌ها یک مدل رگرسیون خطی ساده (`C_Marker = w * age + b`) بر روی داده‌های ۴ بیمار اول که `Responder` بودند، برازش می‌دهند.

داده‌های ۴ بیمار اول `Responder`:

- P01: (age=65, C_Marker=154.5)
- P03: (age=58, C_Marker=171.1)
- P05: (age=55, C_Marker=210.8)
- P08: (age=59, C_Marker=195.4)

**سوال ۵:**
کدام یک از گزینه‌های زیر بهترین توصیف برای رابطه بین `age` و `C_Marker` بر اساس این داده‌ها و یک مدل رگرسیون خطی است؟

الف) یک رابطه مثبت قوی وجود دارد؛ با افزایش سن، سطح C_Marker به شدت افزایش می‌یابد.
ب) یک رابطه منفی قوی وجود دارد؛ با افزایش سن، سطح C_Marker به شدت کاهش می‌یابد.
ج) تقریباً هیچ رابطه خطی وجود ندارد و این دو متغیر مستقل به نظر می‌رسند.
د) یک رابطه غیرخطی (مثلاً U شکل) وجود دارد.
