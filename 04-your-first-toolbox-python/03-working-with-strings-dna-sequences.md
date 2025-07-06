[→ بخش ۴-۲: متغیرها: قفسه‌هایی برای داده‌های زیستی](./02-variables-for-bio-data.md) | [بخش ۴-۴: منطق ماشین: حلقه‌ها و شرط‌ها ←](./04-machine-logic-loops-and-conditions.md)

# فصل ۴: اولین جعبه‌ابزار شما: پایتون

## بخش ۴-۳: کار با رشته‌ها: تحلیل توالی‌های DNA و پروتئین

برای یک متخصص بیوانفورماتیک، **رشته‌ها** تنها یک‌دنباله از کاراکترها نیستند؛ آن‌ها نمایش دیجیتال مولکول‌های زیستی‌اند. یادگیری تکنیک‌های پایه‌ای کار با رشته‌ها در پایتون، معادل فراگیری مهارت‌های اساسی در آزمایشگاه زیست‌مولکولی است. در این بخش، با عملگرها و توابع کلیدی پایتون آشنا می‌شویم تا تحلیل‌هایی مانند اندازه‌گیری طول ژن، تشخیص موتیف‌های عملکردی و شمارش نوکلئوتیدها را به‌صورت خودکار انجام دهیم.

### 🎯 مسئله محوری

چگونه می‌توانیم یک توالی DNA را مانند یک زیست‌شناس آزمایشگاهی، برش دهیم، اندازه بگیریم و موتیف‌های مهم را پیدا کنیم؟

برای مثال‌های این بخش، از توالی فرضی زیر استفاده می‌کنیم:

```python
dna = "AGGTCCGATAAGCTTAGGAT"
```

### ۱. محاسبه طول توالی با `len()`

برای یافتن طول یک رشته در پایتون، تابع داخلی `len()` را به‌کار می‌بریم:

```python
dna_length = len(dna)
print("طول توالی DNA:", dna_length)
```

خروجی:

```
طول توالی DNA: 20
```

> تابع `len()` تعداد کاراکترهای رشته را برمی‌گرداند[1].

### ۲. دسترسی به نوکلئوتید خاص (Indexing)

در پایتون، اندیس‌گذاری رشته‌ها از صفر آغاز می‌شود. برای دسترسی به کاراکترهای فردی از `[]` استفاده می‌کنیم:

```python
first_base = dna[0]
fifth_base = dna[4]

print("اولین باز:", first_base)
print("پنجمین باز:", fifth_base)
```

خروجی:

```
اولین باز: A
پنجمین باز: C
```

### ۳. برش زیررشته (Slicing)

برای استخراج یک ناحیه (مثلاً اگزون یا پروموتر) از سینتکس `[start:end]` بهره می‌گیریم. بازه شامل `start` می‌شود اما اندیس `end` جزو قطعه نیست:

```python
promoter_region = dna[6:12]
print("ناحیه فرضی پروموتر:", promoter_region)
```

خروجی:

```
ناحیه فرضی پروموتر: GATAAG
```

### ۴. چسباندن رشته‌ها (Concatenation)

برای اتصال دو قطعه ژن (مثلاً دو اگزون) از عملگر `+` استفاده می‌کنیم:

```python
exon1 = "ATGGCC"
exon2 = "AATTAG"
full_gene = exon1 + exon2

print("ژن کامل:", full_gene)
```

خروجی:

```
ژن کامل: ATGGCCAATTAG
```

### ۵. شمارش نوکلئوتید یا موتیف با `.count()`

متد `.count()` تعداد تکرار یک کاراکتر یا زیررشته را می‌شمارد:

```python
g_count = dna.count('G')
a_count = dna.count('A')
ga_motif_count = dna.count('GA')

print("تعداد گوانین (G):", g_count)
print("تعداد آدنین (A):", a_count)
print("تعداد موتیف 'GA':", ga_motif_count)
```

خروجی:

```
تعداد گوانین (G): 6
تعداد آدنین (A): 6
تعداد موتیف 'GA': 2
```

> متد `.count()` برای شمارش زیررشته در رشته به‌کار می‌رود[2].

### ۶. یافتن جایگاه یک الگو با `.find()`

برای پیدا کردن اندیس اولین وقوع زیررشته، متد `.find()` را استفاده می‌کنیم. اگر زیررشته یافت نشود، `-1` برمی‌گرداند:

```python
dna_with_start = "ATG" + dna
start_codon_index = dna_with_start.find("ATG")
tata_box_index = dna_with_start.find("TATA")

print("جایگاه کدون شروع:", start_codon_index)
print("جایگاه TATA box:", tata_box_index)
```

ممکن است در توالی فرضی ما جعبه TATA وجود نداشته باشد و `-1` بازگردد:

```
جایگاه کدون شروع: 0
جایگاه TATA box: -1
```

> متد `.find()` جایگاه زیررشته را بازمی‌گرداند یا `-1` اگر پیدا نشود[2].

### 🔬 تمرین تحلیلی: شناسایی سایت اتصال فاکتور رونویسی

یک فاکتور رونویسی به موتیف `GATAAG` متصل می‌شود[3]. با استفاده از ابزارهای فراگرفته، به سوالات زیر پاسخ دهید:

```python
dna_sequence = "AGGTCCGATAAGCTTAGGAT"
binding_site = "GATAAG"
```

۱. طول توالی چقدر است؟  
۲. اندیس شروع `binding_site` کجاست؟  
۳. قطعه مربوطه را با slicing استخراج و چاپ کنید.  
۴. تعداد تیمین (`'T'`) در کل توالی چقدر است؟

**پاسخ نمونه:**

```python
dna_sequence = "AGGTCCGATAAGCTTAGGAT"
binding_site = "GATAAG"

# ۱. طول توالی
length = len(dna_sequence)
print("طول کل توالی:", length)

# ۲. جایگاه شروع
start_index = dna_sequence.find(binding_site)
print("جایگاه شروع سایت اتصال:", start_index)

# ۳. استخراج قطعه
extracted_site = dna_sequence[start_index : start_index + len(binding_site)]
print("قطعه استخراج شده:", extracted_site)

# ۴. شمارش تیمین
t_count = dna_sequence.count('T')
print("تعداد باز تیمین:", t_count)
```

خروجی:

```
طول کل توالی: 20
جایگاه شروع سایت اتصال: 6
قطعه استخراج شده: GATAAG
تعداد باز تیمین: 5
```

### 💡 نکات کلیدی این بخش

- **رشته‌ها (Strings)** نمایش دیجیتال توالی‌های زیستی هستند.
- اندیس‌گذاری از **صفر** شروع می‌شود.
- تابع `len()` طول رشته را برمی‌گرداند[1].
- **Indexing** با `dna[i]` برای دسترسی به یک باز استفاده می‌شود.
- **Slicing** با `dna[start:end]` برای استخراج زیررشته کاربرد دارد.
- `+` برای **Concatenation** دو رشته به‌کار می‌رود.
- متد `.count()` تعداد تکرار کاراکتر یا زیررشته را می‌شمارد[2].
- متد `.find()` جایگاه اولین وقوع زیررشته را می‌یابد یا `-1` برمی‌گرداند[2].
- موتیف `GATAAG` متعلق به سایت‌های اتصال فاکتورهای GATA است[3].

با این ابزارهای ساده، قادر به انجام بسیاری از تحلیل‌های پایه‌ای بر روی توالی‌های DNA و پروتئین خواهید بود. در بخش بعد، با منطق شرطی و حلقه‌ها آشنا می‌شویم تا بتوانیم تصمیم‌گیری‌های پیچیده‌تر براساس نتایج این تحلیل‌ها را پیاده‌سازی کنیم.

---

## **منابع**

[1] https://docs.python.org/3/library/functions.html
[2] https://docs.python.org/3/library/string.html
[3] https://pmc.ncbi.nlm.nih.gov/articles/PMC331536/
[4] https://www.geeksforgeeks.org/python/python-string-length-len/
[5] https://docs.vultr.com/python/standard-library/str/find
[6] https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0144677
[7] https://docs.vultr.com/python/built-in/len
[8] https://discuss.python.org/t/how-to-use-search-in-the-documentation/29717
[9] https://realpython.com/len-python-function/
[10] https://www.codecademy.com/resources/docs/python/strings/find
[11] https://pmc.ncbi.nlm.nih.gov/articles/PMC359949/
[12] https://www.w3schools.com/PYTHON/gloss_python_string_length.asp
[13] https://www.w3schools.com/python/ref_string_find.asp
[14] https://academic.oup.com/bioinformatics/article/37/15/2103/6126807
[15] http://python-reference.readthedocs.io/en/latest/docs/str/find.html
[16] https://en.wikipedia.org/wiki/GATA_transcription_factor
[17] https://discuss.python.org/t/the-len-function/11260
[18] https://www.reddit.com/r/learnpython/comments/y69ccp/python_string_find_examples/
[19] https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/gata-transcription-factor
[20] https://forums.raspberrypi.com/viewtopic.php?t=341637
