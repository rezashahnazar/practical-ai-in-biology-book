[→ بخش ۴-۳: کار با رشته‌ها: تحلیل توالی‌های DNA و پروتئین](./03-working-with-strings-dna-sequences.md) | [بخش ۴-۵: پروژه: محاسبه محتوای GC ←](./05-project-gc-content-calculation.md)

# فصل ۴: اولین جعبه‌ابزار شما: پایتون

## بخش ۴-۴: منطق زیستی در کد: حلقه‌ها و دستورات شرطی

**برداشت اصلی:** با دستورات شرطی (`if`، `elif`، `else`) و حلقه‌ها (`for`)، می‌توانیم به کامپیوتر «قدرت تصمیم‌گیری» و «استقامت» برای پردازش مقادیر عظیم داده‌های زیستی بدهیم.

### 🎯 مسئله‌محوری

- چگونه می‌توانیم کامپیوتر را وادار کنیم بر اساس درصد GC یک توالی تصمیم بگیرد؟
- چگونه می‌توانیم یک عملیات را میلیون‌ها بار بدون خستگی تکرار کنیم؟

## ۱. تصمیم‌گیری با `if`، `elif` و `else`

در زیست‌شناسی، بسیاری از رویدادها به شرط خاصی وابسته‌اند:

- یک سلول تنها **اگر** سیگنال رشد دریافت کند، تقسیم می‌شود.
- یک آنزیم تنها **اگر** pH مناسب باشد، به درستی کار می‌کند.

در پایتون از دستورات شرطی استفاده می‌کنیم تا بر اساس درست (`True`) یا نادرست (`False`) بودن یک عبارت، شاخه‌ای از کد اجرا شود[1]:

````python
# مثال: تشخیص توالی GC-rich
dna = "ATGCGCGCGATTAG"
g_count = dna.count('G')
c_count = dna.count('C')
gc_content = (g_count + c_count) / len(dna)
print(f"درصد GC: {gc_content:.2f}")

if gc_content > 0.6:
    print("این توالی غنی از GC است (GC-rich).")
elif gc_content `, `<`, `==`, `!=` (برای برابری) هستند[2].

## ۲. تکرار با حلقه‌ی `for`
برای پیمایش رشته‌ها، لیست‌ها و مجموعه‌ها از حلقه‌ی `for` استفاده می‌کنیم[3]:
```python
dna = "AGTC"
for base in dna:
    print("باز فعلی:", base)
print("پایان حلقه!")
````

این حلقه برای هر کاراکتر در رشته `dna` یک بار اجرا می‌شود.

### ۲.۱ مثال: پیاده‌سازی دستی شمارش G

```python
dna = "AGGTCCGATAAGCTTAGGAT"
g_counter = 0
for base in dna:
    if base == 'G':
        g_counter += 1
print("تعداد نهایی گوانین:", g_counter)
```

خروجی:

```
تعداد نهایی گوانین: 6
```

این الگو—حلقه برای پیمایش و شرط برای تصمیم‌گیری—بنیاد بسیاری از الگوریتم‌های بیوانفورماتیک است.

## ۳. تمرین تحلیلی: یافتن کدون شروع

کدون شروع معمولاً `ATG` است. باید با بررسی سه‌حرفی‌های متوالی در توالی، اولین محل `ATG` را بیابیم و سپس حلقه را قطع کنیم:

```python
dna = "GGACAGCATGAGGATTGCA"
found = False

for i in range(len(dna) - 2):
    codon = dna[i:i+3]
    if codon == "ATG":
        print(f"کدون شروع 'ATG' در ایندکس {i} پیدا شد.")
        found = True
        break

if not found:
    print("کدون شروع در این توالی پیدا نشد.")
```

خروجی نمونه:

```
کدون شروع 'ATG' در ایندکس 7 پیدا شد.
```

## ۴. نکات کلیدی این بخش

| مفهوم                            | شرح                                                                  |
| -------------------------------- | -------------------------------------------------------------------- |
| دستورات شرطی                     | `if`, `elif`, `else` برای قدرت تصمیم‌گیری بر اساس شروط[1][2]         |
| حلقه‌ی `for`                     | تکرار بر روی آیتم‌های یک دنباله (رشته، لیست و…) بدون نیاز به شاخص[3] |
| تورفتگی (Indentation)            | برای تعیین بلوک‌های کد در پایتون ضروری است                           |
| ترکیب حلقه و شرط                 | **قوی‌ترین الگو** در بیوانفورماتیک: پیمایش داده + تحلیل شرطی         |
| خروج زودهنگام از حلقه با `break` | بهینه‌سازی پیمایش برای یافتن اولین پاسخ و قطع ادامه تکرار            |

با درک و تسلط بر دستورات شرطی و حلقه‌ها، شما پایه‌ی اصلی پیاده‌سازی **هر** الگوریتم بیوانفورماتیکی را فراگرفته‌اید. در بخش بعدی، این مفاهیم را در یک پروژهٔ کوچک و عملی ترکیب خواهیم کرد.

---

## **منابع**

[1] https://www.w3resource.com/python/python-if-else-statements.php
[2] https://www.geeksforgeeks.org/python-if-else/
[3] https://www.w3schools.com/python/python_for_loops.asp
[4] http://www.cs.toronto.edu/~leijiang/ta/mie453/tutorial/tut3/index.htm
[5] https://www.w3schools.com/python/python_conditions.asp
[6] https://www.youtube.com/watch?v=KWgYha0clzw
[7] http://www.cellbiol.com/bioinformatics_web_development/chapter-4-adding-a-dynamic-layer-introducing-the-php-programming-language/php-programming-language-basics-conditional-statements-if-elseif-else/
[8] https://www.datacamp.com/tutorial/elif-statements-python
[9] https://www.ibm.com/reference/python/for-loop
[10] https://pmc.ncbi.nlm.nih.gov/articles/PMC10591307/
[11] https://www.w3schools.com/python/gloss_python_elif.asp
[12] https://www.youtube.com/watch?v=23vCap6iYSs
[13] https://www.reddit.com/r/gamemaker/comments/1ani28d/does_the_order_of_ifelse_statements_matter_for/
[14] https://note.nkmk.me/en/python-if-elif-else/
[15] https://www.simplilearn.com/tutorials/python-tutorial/python-for-loop
[16] https://www.bioinformaticist.com/2018/01/bioinformatics-101-004-if-else-statement.html
[17] https://wiingy.com/learn/python/python-if-elif-else/
[18] https://www.reddit.com/r/learnpython/comments/p47d1n/can_not_understand_for_loops/
[19] https://open.oregonstate.education/computationalbiology/chapter/bioinformatics-knick-knacks-and-regular-expressions/
[20] https://www.dataquest.io/blog/python-for-loop-tutorial/
