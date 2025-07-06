[→ بخش ۴-۴: منطق ماشین: حلقه‌ها و شرط‌ها](./04-machine-logic-loops-and-conditions.md) | [آزمون فصل چهارم ←](./exam/index.md)

# فصل ۴: اولین جعبه‌ابزار شما: پایتون

## بخش ۴-۵: پروژه عملی: ساخت یک ماشین‌حساب ژنومی

اکنون زمان آن رسیده است که تمام مهارت‌هایی که در این فصل یاد گرفته‌اید—متغیرها، رشته‌ها، حلقه‌ها و دستورات شرطی—را با هم ترکیب کرده و اولین برنامه بیوانفورماتیکی کامل خود را بنویسید. این پروژه پلی است بین دانش تئوری و کاربرد عملی آن در دنیای واقعی.

### 🎯 مسئله محوری

چگونه می‌توانیم تمام قطعات پازل برنامه‌نویسی را کنار هم بگذاریم تا یک ابزار واقعی بیوانفورماتیک بسازیم؟

شما اکنون با مفاهیم پایهٔ پایتون آشنا شده‌اید. در این بخش، قصد داریم با ترکیب همهٔ این مفاهیم، یک برنامه بسازیم که درصد محتوای GC (نسبت بازهای Guanine و Cytosine به کل بازها) را در یک توالی DNA محاسبه کند. درصد GC یکی از مهم‌ترین پارامترها در تحلیل ژنوم است که بر پایدارسازی حرارتی DNA و شناسایی نواحی ژنی تأثیر دارد[1].

---

### هدف پروژه

نوشتن اسکریپتی که:

1. یک توالی DNA را به‌عنوان ورودی دریافت کند.
2. درصد محتوای GC را محاسبه و نمایش دهد.

### الگوریتم: نقشه راه ما

1. **مقداردهی اولیه**
   - تعریف متغیر `dna_sequence` برای ذخیره توالی DNA
   - تعریف `gc_counter = 0` برای شمارش بازهای G و C
2. **پیمایش**
   - استفاده از حلقه `for` برای حرکت روی هر باز در توالی
3. **تصمیم‌گیری**
   - درون حلقه، با `if base == 'G' or base == 'C'` بررسی می‌کنیم آیا باز جاری G/C است
4. **شمارش**
   - در صورت صحت شرط، `gc_counter += 1`
5. **محاسبه نهایی**
   - تعیین `total_length = len(dna_sequence)`
   - جلوگیری از تقسیم بر صفر:
     ```python
     if total_length > 0:
         gc_percentage = (gc_counter / total_length) * 100
     else:
         gc_percentage = 0
     ```
6. **نمایش خروجی**
   - چاپ توالی، طول کل، تعداد G/C، و درصد GC

---

### پیاده‌سازی کد: قدم به قدم

```python
# قدم ۱: مقداردهی اولیه
dna_sequence = "AGCTCCGTACGTAGCTAGCTAGCTACGATCAGCTACGATCGATCGATGC"
gc_counter = 0

# قدم ۲ و ۳ و ۴: پیمایش و تصمیم‌گیری و شمارش
for base in dna_sequence:
    if base == 'G' or base == 'C':
        gc_counter += 1

# قدم ۵: محاسبه نهایی
total_length = len(dna_sequence)
if total_length > 0:
    gc_percentage = (gc_counter / total_length) * 100
else:
    gc_percentage = 0

# قدم ۶: نمایش خروجی
print("توالی DNA:", dna_sequence)
print("طول کل توالی:", total_length)
print("تعداد بازهای G و C:", gc_counter)
print(f"درصد GC برابر است با: {gc_percentage:.2f} %")
```

**خروجی مورد انتظار:**

```
توالی DNA: AGCTCCGTACGTAGCTAGCTAGCTACGATCAGCTACGATCGATCGATGC
طول کل توالی: 49
تعداد بازهای G و C: 26
درصد GC برابر است با: 53.06 %
```

> **نکته:** طول توالی و تعداد GC بسته به رشتهٔ ورودی ممکن است متفاوت باشد؛ در این مثال طول 49 و GC برابر 26 محاسبه شد.

---

### 🔬 تمرین تحلیلی: ارتقاء ماشین‌حساب ژنومی

برنامه را به‌گونه‌ای تغییر دهید که:

1. کاراکترهای نامعتبر (غیر از A, T, C, G) را نیز بشمارد.
2. درصد GC را تنها بر اساس بازهای معتبر محاسبه کند.
3. در صورت وجود نامعتبر، تعداد آن‌ها را با پیام هشدار نمایش دهد.

**توالی برای آزمایش:**

```
AGCTCCGTACGTNNAGCTAGCTANNNGCTACGATCAGCTACGATCGATCGATGC
```

**راهنمایی:**  
در حلقه `for` از `elif` برای A/T و `else` برای نامعتبر استفاده کنید.

#### پاسخ نمونه

```python
dna_sequence = "AGCTCCGTACGTNNAGCTAGCTANNNGCTACGATCAGCTACGATCGATCGATGC"
gc_counter = 0
invalid_counter = 0

for base in dna_sequence:
    if base == 'G' or base == 'C':
        gc_counter += 1
    elif base == 'A' or base == 'T':
        pass  # باز معتبر ولی AT، نیاز به شمارش نداریم
    else:
        invalid_counter += 1

total_length = len(dna_sequence)
valid_length = total_length - invalid_counter

if valid_length > 0:
    gc_percentage = (gc_counter / valid_length) * 100
else:
    gc_percentage = 0

print(f"درصد GC (فقط بازهای معتبر): {gc_percentage:.2f} %")
if invalid_counter > 0:
    print(f"هشدار: {invalid_counter} کاراکتر نامعتبر در توالی پیدا شد.")
```

**خروجی نمونه:**

```
درصد GC (فقط بازهای معتبر): 53.06 %
هشدار: 5 کاراکتر نامعتبر در توالی پیدا شد.
```

---

### 💡 نکات کلیدی این بخش

- **ترکیب مفاهیم:** اجزای پایه (متغیر، حلقه، شرط) زمانی قدرت واقعی پیدا می‌کنند که برای حل یک مسئله واقعی کنار هم قرار گیرند.
- **الگوریتم‌نویسی:** طراحی نقشه راه پیش از کدنویسی، خطاها را کاهش می‌دهد و فرآیند را ساده‌تر می‌کند.
- **اعتبارسنجی داده:** برنامه شما باید توانایی برخورد با داده‌های نامعتبر را داشته باشد تا در شرایط واقعی پایدار بماند.
- **اهمیت GC content:** درصد GC معیاری مهم در ژنومیک است که بر پایداری حرارتی DNA و شناسایی نواحی ژنی تأثیر دارد[1][2].

شما با تکمیل این پروژه، اولین قدم بزرگ را برای تبدیل شدن به یک متخصص بیوانفورماتیک برداشته‌اید. در بخش نهایی این فصل، دانش خود را با یک آزمون جامع به چالش خواهید کشید.

---

## **منابع**

[1] https://en.wikipedia.org/wiki/GC-content
[2] https://www.oxfordreference.com/abstract/10.1093/acref/9780198821489.001.0001/acref-9780198821489-e-6618
[3] https://pmc.ncbi.nlm.nih.gov/articles/PMC2746155/
[4] https://pmc.ncbi.nlm.nih.gov/articles/PMC152811/
[5] https://pmc.ncbi.nlm.nih.gov/articles/PMC4715772/
[6] https://pmc.ncbi.nlm.nih.gov/articles/PMC4349097/
[7] https://www.pnas.org/doi/10.1073/pnas.1321152111
[8] https://www.sciencedirect.com/science/article/pii/S0959437X22001356
[9] https://www.reddit.com/r/microbiology/comments/100l7p0/whats_the_relevance_of_highlow_gc_content_in/
[10] https://www.bioconductor.org/help/course-materials/2013/useR2013/Bioconductor-tutorial.pdf
[11] https://www.numberanalytics.com/blog/ultimate-guide-gc-content-population-genetics
[12] https://www.nature.com/articles/s41586-024-07682-9
[13] https://geneticeducation.co.in/what-is-the-importance-of-gc-content/
[14] https://onlinelibrary.wiley.com/doi/10.1111/tpj.15899
[15] https://www.sciencedirect.com/topics/neuroscience/gc-content
