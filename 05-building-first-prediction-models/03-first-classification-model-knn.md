[→ بخش ۵-۲: هنر رام کردن داده‌ها: پاک‌سازی و آماده‌سازی](./02-art-of-data-wrangling.md) | [بخش ۵-۴: مدل ما چقدر خوب کار می‌کند؟ معیارهای ارزیابی ←](./04-model-evaluation-metrics.md)

# فصل ۵: ساخت اولین مدل‌های پیش‌بینی: از داده تا تشخیص

## بخش ۵-۳: اولین مدل طبقه‌بندی: آموزش یک تصمیم‌گیرنده دیجیتال

در بخش‌های قبل، داده‌ها را به دو بخش ویژگی‌ها (X) و هدف (y) تقسیم کردیم. اکنون می‌خواهیم اولین مدل طبقه‌بندی خود را بسازیم تا بر اساس ویژگی‌های یک بیمار، وضعیت «سالم» یا «سرطانی» را پیش‌بینی کند. این کار با استفاده از الگوریتم KNN و اصل «تقسیم داده به آموزش و آزمون» انجام می‌شود.

### 🎯 مسئله محوری

چگونه به یک ماشین «یاد بدهیم» که بین دو کلاس تمایز قائل شود و مطمئن شویم مدل ما واقعاً الگوها را یاد گرفته و صرفاً پاسخ‌های آموزشی را ذخیره نکرده است؟

## طبقه‌بندی (Classification)

در **طبقه‌بندی** هدف پیش‌بینی یک برچسب گسسته است:

- کلاس 0: سرطان (malignant)
- کلاس 1: سالم (benign) [1]

## قانون طلایی: تقسیم داده به آموزش و آزمون

**هیچ‌گاه** مدل را با داده‌های آموزشی خودش ارزیابی نکنید. این کار مانند پرسیدن همان سؤالات تمرینی در امتحان نهایی است؛ نمره‌ی بالا ارزشی ندارد.  
برای ارزیابی صادقانه:

- مجموعه آموزش (Training Set): معمولاً ۷۰–۸۰٪ داده‌ها برای یادگیری الگوریتم
- مجموعه آزمون (Test Set): ۲۰–۳۰٪ داده‌ها برای ارزیابی عملکرد روی داده‌های جدید

کتابخانه Scikit-learn تابع `train_test_split` را برای این کار فراهم می‌کند[2]:

```python
from sklearn.model_selection import train_test_split

# X و y از قبل آماده شده‌اند
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,      # ۲۰٪ برای آزمون
    random_state=42     # برای اطمینان از تکرارپذیری
)
print("Train shape:", X_train.shape)  # (455, 30)
print("Test shape:", X_test.shape)    # (114, 30)
```

| مجموعه         | نمونه‌ها | ویژگی‌ها |
| -------------- | -------- | -------- |
| Training Set   | 455      | 30       |
| Test Set       | 114      | 30       |
| **کل داده‌ها** | **569**  | **30**   |

(569 نمونه، 30 ویژگی[1])

## الگوریتم K-نزدیک‌ترین همسایه (KNN)

**منطق KNN**  
برای هر نقطه‌ی جدید:

1. فاصله‌ی آن را تا همه نمونه‌های آموزش (معمولاً با معیار Minkowski) محاسبه کن
2. **K** نزدیک‌ترین همسایه را انتخاب کن
3. برچسب اکثریت آن همسایه‌ها را به‌عنوان پیش‌بینی برگردان

> **مثال محله:** اگر K=5 و ۵ همسایه نزدیک شما سه نفر طرفدار تیم قرمز و دو نفر طرفدار تیم آبی باشند، شما هم تیم قرمز را انتخاب می‌کنید.

پارامترهای کلیدی[3]:

- `n_neighbors`: تعداد همسایه‌ها (K)، پیش‌فرض 5
- `weights`: نحوه وزن‌دهی ('uniform' یا 'distance')
- `algorithm`: روش جستجوی نزدیک‌ترین همسایه‌ها

## پیاده‌سازی با Scikit-learn

```python
from sklearn.neighbors import KNeighborsClassifier

# ۱. تعریف مدل با K=3
knn = KNeighborsClassifier(n_neighbors=3)

# ۲. آموزش مدل با داده‌های آموزش
knn.fit(X_train, y_train)
print("مدل آموزش دید!")

# ۳. پیش‌بینی بر روی داده‌های آزمون
predictions = knn.predict(X_test)

print("برچسب‌های واقعی آزمون:", y_test.values[:10])
print("پیش‌بینی‌های مدل:", predictions[:10])
```

## 🔬 تمرین تحلیلی: تاثیر پارامتر K

KNN یک **هایپرپارامتر** به نام `n_neighbors` دارد. برای درک بهتر:

1. مدل را با `K=1`، `K=3` و `K=5` اجرا کنید.
2. تفاوت پیش‌بینی‌ها را مقایسه کنید.
3. درباره خطرات `K=1` (حساسیت به نویز) و `K` خیلی بزرگ (تعمیم‌زدایی بیش‌ازحد) فکر کنید.

مثال نتایج اولیه (۵ پیش‌بینی اول):

| K   | پیش‌بینی‌ها | برچسب‌های واقعی |
| --- | ----------- | --------------- |
| 1   | [1, 0,[4]   | [1, 0, 0,       |
| 3   | [0, 0, 0,   | [1, 0, 0, 1,    |
| 5   | [1, 0, 0,   | [1, 0, 0, 1,    |

## 💡 نکات کلیدی این بخش

- **طبقه‌بندی:** پیش‌بینی برچسب‌های گسسته (سالم/سرطانی)
- **تقسیم آموزش/آزمون:** برای ارزیابی منصفانه مدل ضروری است[2]
- **تابع `train_test_split`:** ابزاری استاندارد برای تقسیم داده‌ها[2]
- **الگوریتم KNN:** تصمیم‌گیری بر اساس رای اکثریت K همسایه نزدیک[3]
- **API Scikit-learn:** همگی از ساختار `.fit()` و `.predict()` پیروی می‌کنند

در بخش بعد، به بررسی معیارهای ارزیابی مدل می‌پردازیم تا عملکرد پیش‌بینی را به‌صورت کمی بسنجیم.

---

## **منابع**

[1] https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html
[2] https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
[3] https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
[4] https://www.geeksforgeeks.org/python/how-to-split-the-dataset-with-scikit-learns-train_test_split-function/
[5] https://scikit-learn.org/0.15/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
[6] https://www.educative.io/answers/what-is-sklearndatasetsloadbreastcancer-in-python
[7] https://realpython.com/train-test-split-python-data/
[8] https://scikit-learn.org/0.18/modules/generated/sklearn.datasets.load_breast_cancer.html
[9] https://builtin.com/data-science/train-test-split
[10] https://pyts.readthedocs.io/en/stable/generated/pyts.classification.KNeighborsClassifier.html
[11] https://scikit-learn.org/0.22/modules/generated/sklearn.datasets.load_breast_cancer.html
[12] https://www.educative.io/answers/what-is-the-traintestsplit-function-in-sklearn
[13] https://fda.readthedocs.io/en/latest/modules/ml/autosummary/skfda.ml.classification.KNeighborsClassifier.html
[14] https://www.geeksforgeeks.org/machine-learning/python-sklearn-sklearn-datasets-load_breast_cancer-function/
[15] https://www.youtube.com/watch?v=_tex9QxBX-U
[16] https://ogrisel.github.io/scikit-learn.org/sklearn-tutorial/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
[17] https://scikit-learn.org/0.17/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
[18] https://stackoverflow.com/questions/70062816/scikit-learn-error-dataset-load-breast-cancer
[19] https://scikit-learn.org/0.18/modules/generated/sklearn.model_selection.train_test_split.html
[20] https://www.datacamp.com/tutorial/k-nearest-neighbor-classification-scikit-learn
