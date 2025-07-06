[→ فصل ۵: مقدمه](./00-introduction.md) | [بخش ۵-۲: هنر رام کردن داده‌ها: پاک‌سازی و آماده‌سازی ←](./02-art-of-data-wrangling.md)

# فصل ۵: ساخت اولین مدل‌های پیش‌بینی: از داده تا تشخیص

**نکته کلیدی:** با استفاده از کتابخانه‌های **NumPy**، **Pandas** و **Scikit-learn**، پایتونِ ساده به یک پلتفرم قدرتمند برای تحلیل داده‌های زیستی و ساخت مدل‌های پیش‌بینی تبدیل می‌شود.

## بخش ۵-۱: کتابخانه‌های قدرتمند: آشنایی با NumPy, Pandas و Scikit-learn

یک **کتابخانه** مجموعه‌ای از کدها، توابع و ابزارهای از پیش آماده است که توسط متخصصان نوشته و بهینه‌سازی شده‌اند. استفاده از این کتابخانه‌ها به ما اجازه می‌دهد که به جای اختراع دوباره چرخ، بر روی حل مسائل علمی تمرکز کنیم.

### ۱. NumPy: موتور محاسباتی پایتون

**NumPy** (Numerical Python) بنیادی‌ترین کتابخانه برای محاسبات علمی در پایتون است.

- **هدف اصلی:** ساختار داده‌ی **آرایه (ndarray)** را برای کار با داده‌های عددی چندبعدی فراهم می‌کند[1].
- **کارایی:** عملیات روی آرایه‌های NumPy با پیاده‌سازی به زبان C سریع‌تر از لیست‌های معمولی پایتون است؛ به‌عنوان مثال، جمع دو آرایه یک‌میلیون‌تایی در NumPy حدود 9 برابر سریع‌تر از لیست‌ها انجام می‌شود[1][2].
- **آنالوژی:** اگر پایتون استاندارد یک ماشین‌حساب ساده باشد، NumPy یک ابرکامپیوتر محاسباتی است.

```python
import numpy as np

# ساخت یک آرایه NumPy از داده‌های بیان ژن
gene_expressions = np.array([12.5, 4.2, 18.0, 9.7])
print("آرایه بیان ژن:", gene_expressions)

# انجام یک عملیات ریاضی بر روی تمام عناصر به صورت برداری
normalized_expressions = gene_expressions / 2
print("بیان ژن نرمال‌شده:", normalized_expressions)
```

نتیجه:

```
بیان ژن نرمال‌شده: [6.25 2.1  9.   4.85]
```

(عملیات برداری NumPy بدون نیاز به حلقه صریح، کارایی را افزایش می‌دهد)[1].

### ۲. Pandas: جعبه‌ابزار تحلیل داده

**Pandas** بر پایه NumPy ساخته شده و ابزارهای قدرتمندی برای کار با **داده‌های جدولی (DataFrame)** فراهم می‌کند.

- **هدف اصلی:** ارائه دو ساختار داده‌:
  - **Series** برای آرایه‌های یک‌بعدی
  - **DataFrame** برای داده‌های دوبعدی جدول‌مانند[3].
- **کاربرد زیستی:** داده‌هایی مانند نتایج آزمایش‌ها، بیان ژن و اطلاعات بیماران معمولاً در قالب جدول هستند؛ Pandas خواندن، پاک‌سازی، فیلتر و گروه‌بندی این داده‌ها را آسان می‌کند[4].
- **آنالوژی:** Pandas دفتر آزمایشگاهی دیجیتال شماست که داده‌ها را در آن ثبت و سازمان‌دهی می‌کنید.

```python
import pandas as pd

# ساخت یک DataFrame برای اطلاعات بیماران
data = {
    'PatientID': ['P001', 'P002', 'P003'],
    'Age': [45, 62, 38],
    'Diagnosis': ['Cancer', 'Healthy', 'Cancer']
}
patient_df = pd.DataFrame(data)
print(patient_df)
```

| PatientID | Age | Diagnosis |
| --------- | --- | --------- |
| P001      | 45  | Cancer    |
| P002      | 62  | Healthy   |
| P003      | 38  | Cancer    |

### ۳. Scikit-learn: جعبه‌ابزار یادگیری ماشین

**Scikit-learn** یکی از محبوب‌ترین کتابخانه‌ها برای **یادگیری ماشین کلاسیک** است.

- **هدف اصلی:** مجموعه‌ای از الگوریتم‌های آماده برای **طبقه‌بندی**، **رگرسیون**، **خوشه‌بندی** و **کاهش ابعاد** همراه با ابزارهای **ارزیابی مدل** را فراهم می‌کند[5].
- **رابط یکپارچه:** تمام الگوریتم‌ها از الگوی سه مرحله‌ای زیر پیروی می‌کنند[6]:
  1. نمونه‌سازی مدل
  2. آموزش با `.fit()`
  3. پیش‌بینی با `.predict()`
- **آنالوژی:** Scikit-learn جعبه‌ابزار یک مهندس یادگیری ماشین است که تمام ماشین‌آلات لازم را در اختیار دارد.

```python
from sklearn.ensemble import RandomForestClassifier

# نمونه‌سازی مدل
model = RandomForestClassifier(n_estimators=100, random_state=42)

# آموزش مدل با داده‌های آموزشی
model.fit(X_train, y_train)

# پیش‌بینی با داده‌های جدید
predictions = model.predict(X_test)
```

### 🔬 تمرین تحلیلی: انتخاب ابزار مناسب

| سناریو                                                                      | کتابخانه مناسب       |
| --------------------------------------------------------------------------- | -------------------- |
| ۱. خواندن یک فایل CSV با ۱۰۰ هزار ردیف و فیلتر کردن بیماران بالای ۵۰ سال.   | Pandas[4]            |
| ۲. ساخت مدل پیش‌بینی خوش‌خیم/بدخیم بودن تومور با داده‌های تصویربرداری.      | Scikit-learn[5][6]   |
| ۳. انجام عملیات ماتریسی پیچیده بر روی داده‌های سه‌بعدی مغز (fMRI).          | NumPy[1]             |
| ۴. محاسبه میانگین و انحراف معیار ستون "غلظت دارو" در جدول نتایج آزمایشگاهی. | Pandas + NumPy[4][1] |

## نکات کلیدی این بخش

- **کتابخانه‌ها** مجموعه‌ی کدهای آماده‌ برای افزودن قابلیت‌های جدید به پایتون‌اند.
- **NumPy** برای محاسبات عددی برداری و آرایه‌های چندبعدی ضروری است[1].
- **Pandas** استاندارد کار با داده‌های جدولی (DataFrame) است[4][3].
- **Scikit-learn** ابزار اصلی برای ساخت و ارزیابی مدل‌های یادگیری ماشین کلاسیک است[5][6].

با تسلط بر این سه کتابخانه، آماده‌ایم تا وارد دنیای واقعی **علم داده در زیست‌شناسی** شویم و اولین مدل‌های پیش‌بینی خود را بسازیم. در بخش بعد، به **پاک‌سازی و آماده‌سازی** داده‌ها برای مدل‌سازی می‌پردازیم.

---

## **منابع**

[1] https://www.geeksforgeeks.org/python/why-numpy-is-faster-in-python/
[2] https://www.reddit.com/r/Numpy/comments/1cz52op/why_is_numpy_much_faster_than_lists/
[3] https://www.nvidia.com/en-us/glossary/pandas-python/
[4] https://www.geeksforgeeks.org/pandas/python-pandas-dataframe/
[5] https://www.intel.com/content/www/us/en/developer/articles/technical/easy-introduction-to-scikit-learn.html
[6] https://scikit-learn.org/stable/faq.html
[7] https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-193.php
[8] https://scikit-learn.org/stable/api/index.html
[9] https://stackoverflow.com/questions/46860970/why-use-numpy-over-list-based-on-speed/46868693
[10] https://www.databricks.com/glossary/pandas-dataframe
[11] https://www.w3schools.com/Python/Pandas/pandas_dataframes.asp
[12] https://discuss.scientific-python.org/t/spec-2-api-dispatch/173
[13] https://www.dataleadsfuture.com/python-lists-vs-numpy-arrays-a-deep-dive-into-memory-layout-and-performance-benefits/
[14] https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
[15] https://stackoverflow.com/questions/59845191/api-calls-from-nltk-gensim-scikit-learn
[16] https://www.youtube.com/watch?v=cAmkgMnKx34
[17] https://realpython.com/pandas-dataframe/
[18] https://github.com/scikit-hep/pyhf/issues/2253
[19] https://www.linkedin.com/pulse/python-lists-vs-numpy-arrays-mohamed-hamdy-b5e9f
[20] https://stackoverflow.com/questions/42955713/what-is-the-use-purpose-of-pandas
