[→ بخش ۴-۱: سلام، دنیای پایتون! آشنایی با Python و Google Colab](./01-hello-python-world.md) | [بخش ۴-۳: کار با رشته‌ها: توالی DNA به عنوان متن ←](./03-working-with-strings-dna-sequences.md)

# فصل ۴: اولین جعبه ابزار شما: پایتون

## بخش ۴-۲: متغیرها: قفسه‌هایی برای داده‌های زیستی

در بخش قبل اولین دستور خود را به کامپیوتر دادید. اما برای انجام کارهای جدی‌تر، نیاز داریم تا اطلاعات را در حافظه کامپیوتر ذخیره، نام‌گذاری و مدیریت کنیم. این کار با استفاده از **متغیرها (Variables)** و **انواع داده (Data Types)** انجام می‌شود که الفبای زیست‌شناسی دیجیتال هستند.

### 🎯 مسئله محوری: چگونه زبان زیست‌شناسی را به زبان قابل فهم برای کامپیوتر ترجمه کنیم؟

دنیای زیست‌شناسی پر از اطلاعات است: توالی یک ژن، تعداد کروموزوم‌ها، غلظت یک دارو یا حتی یک گزاره‌ی ساده مانند «جهش وجود دارد». اما کامپیوترها ذاتاً چیزی از «ژن» یا «پروتئین» نمی‌دانند و فقط با اعداد و داده‌های ساختاریافته کار می‌کنند. در این بخش می‌آموزیم چگونه با «متغیر» و «انواع داده» این مفاهیم متنوع را به واحدهای اطلاعاتی مشخص ترجمه کنیم. این اولین و حیاتی‌ترین قدم برای ذخیره، مدیریت و تحلیل داده‌های زیستی در محیط محاسباتی است.

### متغیر: لوله آزمایش برچسب‌دار شما

یک متغیر را مانند یک **لوله آزمایش در آزمایشگاه** در نظر بگیرید. شما برای اینکه محتویات لوله‌های مختلف را با هم اشتباه نگیرید، روی آنها برچسب می‌زنید. مثلاً `Sera_Patient_A` یا `DNA_Sample_3`.

در پایتون، متغیر نامی است که به یک قطعه داده در حافظه اشاره می‌کند. برای ساختن یک متغیر از عملگر تخصیص (`=`) استفاده می‌کنیم[1].

```python
# ساخت متغیری به نام gene_name و ذخیره‌ی نام ژن در آن
gene_name = "TP53"

# دسترسی به محتوای متغیر
print(gene_name)  # خروجی: TP53
```

### انواع داده: محتویات لوله‌های آزمایش

همان‌طور که در آزمایشگاه لوله‌ها می‌توانند حاوی مایعات، پودرها یا گازها باشند، در پایتون نیز متغیرها می‌توانند انواع مختلفی از داده‌ها را نگه دارند. نوع داده مشخص می‌کند چه عملیات و محاسباتی روی آن مجاز است[2].

#### ۱. رشته (String)

برای ذخیره‌ی متن استفاده می‌شود. هر چیزی که بین دو کوتیشن (`"..."` یا `'...'`) قرار بگیرد رشته است. توالی‌های DNA و پروتئین مثال‌های زیستی برای رشته‌ها هستند[2].

```python
dna_sequence = "AGCTTGCCAG"
protein_sequence = "MKLFW"

print(dna_sequence)
print(protein_sequence)
```

#### ۲. عدد صحیح (Integer)

اعداد کامل (بدون بخش کسری) را نگه می‌دارد. تعداد کروموزوم‌ها یا طول ژن مثال‌های متداول هستند[2].

```python
number_of_chromosomes = 46
gene_length = 1250

print(number_of_chromosomes)
```

#### ۳. عدد اعشاری (Float)

برای اعداد با بخش کسری استفاده می‌شود. غلظت محلول یا درصد GC نمونه‌ها مثال‌هایی از این نوع هستند[2].

```python
gc_content = 0.45
concentration = 12.5

print(gc_content)
```

#### ۴. بولین (Boolean)

دو مقدار `True` یا `False` می‌گیرد. برای نمایش وضعیت‌های دوتایی مانند وجود جهش یا پاسخ دارویی کاربرد دارد[2].

```python
is_mutation_present = True
is_toxic = False

print(is_mutation_present)
```

### چگونه نوع یک متغیر را بفهمیم؟

پایتون تابع داخلی `type()` را فراهم کرده تا نوع داده‌ی یک متغیر را نشان دهد[2].

```python
dna_sequence = "AGCTTGCCAG"
gene_length = 1250
gc_content = 0.45
is_mutation_present = True

print(type(dna_sequence))        #
print(type(gene_length))         #
print(type(gc_content))          #
print(type(is_mutation_present)) #
```

### 🔬 تمرین تحلیلی: برچسب‌گذاری داده‌های زیستی

یک دانشمند داده‌های زیر را از یک آزمایش جمع‌آوری کرده است. برای هر مورد، یک نام متغیر مناسب در پایتون انتخاب کنید و نوع داده (str, int, float, bool) را مشخص نمایید.

| داده جمع‌آوری شده                                                 | نام متغیر پیشنهادی شما          | نوع داده |
| ----------------------------------------------------------------- | ------------------------------- | -------- |
| توالی ژنوم ویروس کرونا                                            | `sars_cov2_genome`              | str      |
| تعداد آمینواسیدها در پروتئین Spike                                | `spike_aa_count`                | int      |
| دمای بهینه برای فعالیت یک آنزیم (مثلاً 37.5 درجه سلسیوس)          | `optimal_enzyme_temp`           | float    |
| آیا ژن مورد نظر باعث مقاومت به آنتی‌بیوتیک می‌شود؟ (پاسخ بله/خیر) | `confers_antibiotic_resistance` | bool     |

### 💡 نکات کلیدی این بخش

- **متغیر (Variable):** نامی برچسب‌دار برای ذخیره‌ی داده در حافظه کامپیوتر است (مانند `gene_name = "TP53"`)[1].
- **انواع داده (Data Types):** ماهیت اطلاعات ذخیره‌شده را تعیین می‌کند و مشخص می‌کند چه عملیاتی روی آن مجاز است[2].
- **رشته (String):** برای متن، مانند توالی‌های DNA (`"AGTC"`) استفاده می‌شود[2].
- **عدد صحیح (Integer):** برای اعداد کامل، مانند طول ژن (`1250`) کاربرد دارد[2].
- **عدد اعشاری (Float):** برای اعداد کسری، مانند غلظت دارو (`0.5`) کاربرد دارد[2].
- **بولین (Boolean):** برای مقادیر درست/نادرست (`True` یا `False`)، مانند وجود جهش، کاربرد دارد[2].

درک این مفاهیم پایه، الفبای برنامه‌نویسی برای زیست‌شناسی است. در بخش بعدی، بر مهم‌ترین نوع داده برای بیوانفورماتیسین — **رشته‌ها** — تمرکز خواهیم کرد و یاد می‌گیریم چگونه توالی‌های DNA را دستکاری و تحلیل کنیم.

---

## **منابع**

[1] https://realpython.com/python-variables/
[2] https://www.w3schools.com/python/python_datatypes.asp
[3] https://www.w3schools.com/python/python_variables.asp
[4] https://www.geeksforgeeks.org/python/python-data-types/
[5] https://www.geeksforgeeks.org/python-variables/
[6] https://www.digitalocean.com/community/tutorials/python-data-types
[7] https://www.simplilearn.com/tutorials/python-tutorial/python-variables
[8] https://docs.python.org/3/library/datatypes.html
[9] https://www.youtube.com/watch?v=7IoQ5BGkTJo
[10] https://docs.python.org/3/library/typing.html
[11] https://docs.python.org/3/tutorial/index.html
[12] https://docs.python.org/3/library/stdtypes.html
[13] https://www.learnpython.org/en/Variables_and_Types
[14] https://docs.python.org/3/tutorial/datastructures.html
[15] https://docs.python.org/3/tutorial/introduction.html
[16] https://docs.python.org/3/reference/datamodel.html
[17] https://www.tutorialspoint.com/python/python_variables.htm
[18] https://www.linode.com/docs/guides/python-data-types/
