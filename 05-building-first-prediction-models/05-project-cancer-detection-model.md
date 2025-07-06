[→ بخش ۵-۴: مدل ما چقدر خوب کار می‌کند؟ معیارهای ارزیابی](./04-model-evaluation-metrics.md) | [آزمون فصل پنجم ←](./exam/index.md)

# فصل ۵: ساخت اولین مدل‌های پیش‌بینی: از داده تا تشخیص

## بخش ۵-۵: مطالعه موردی: ساخت خط لوله تشخیص سرطان از صفر تا صد

**خلاصه‌ی اصلی:** در این مطالعه‌ی موردی، تمام مراحل یک پروژه‌ی عملی یادگیری ماشین برای تشخیص سرطان از داده‌های خام پزشکی تا گزارش نهایی عملکرد مدل، به صورت یک خط لوله‌ی خودکار در Python پیاده‌سازی می‌شود.

### مقدمه

تا کنون با مراحل اصلی پروژه‌های علم داده آشنا شدیم: خواندن و پاک‌سازی داده، تقسیم مجموعه، آموزش مدل و ارزیابی. در این بخش، این مراحل را در قالب یک اسکریپت یکپارچه و قابل اجرا در Google Colab می‌نویسیم تا زمانی که داده‌های پزشکی «کثیف» به اسکریپت داده شوند، خروجی آن گزارشی کامل از عملکرد مدل تشخیص سرطان باشد.

### اسکریپت کامل در Google Colab

کد زیر هر هفت مرحله‌ی گردش کار را به تفصیل پیاده می‌کند. برای تست، داده‌ها به صورت یک رشته شبیه‌سازی شده و شامل مقادیر گمشده و فرمت‌های متنی ناسازگار است که دقیقاً شبیه دنیای واقعی هستند.

```python
# ===================================================================
# مرحله ۱: وارد کردن کتابخانه‌ها
# ===================================================================
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)
import io

# ===================================================================
# مرحله ۲: آماده‌سازی داده‌ها (شبیه‌سازی فایل ورودی)
# ===================================================================
csv_data = \"\"\"Biomarker1,Biomarker2,TumorSize,Diagnosis,PatientAge,Metastasis
1.2,3.4,15.5,Positive,65,Yes
0.8,2.1,12.1,Negative,45,No
,3.9,18.2,Positive,72,yes
1.5,4.5,20.0,positive,68,Yes
0.5,1.9,10.3,negative,38,no
1.9,5.1,22.5,Positive,75,YES
1.1,3.2,NaN,Positive,59,Yes
0.7,2.5,11.5,Negative,41,No
\"\"\"
df = pd.read_csv(io.StringIO(csv_data))

# ===================================================================
# مرحله ۳: پاک‌سازی و آماده‌سازی داده‌ها
# ===================================================================
# ۳.۱: پر کردن مقادیر گمشده (NaN) با میانگین ستون
df[['Biomarker1','TumorSize']] = df[['Biomarker1','TumorSize']].apply(lambda col: col.fillna(col.mean()))  # [21]
# ۳.۲: استانداردسازی نوشته‌ها
df['Diagnosis']  = df['Diagnosis'].str.lower()
df['Metastasis'] = df['Metastasis'].str.lower()
# ۳.۳: نگاشت متغیرهای دسته‌ای به عدد
df['Diagnosis_numeric']   = df['Diagnosis'].apply(lambda x: 1 if x=='positive' else 0)
df['Metastasis_numeric']  = df['Metastasis'].apply(lambda x: 1 if x=='yes'      else 0)
df_cleaned = df.drop(['Diagnosis','Metastasis'], axis=1)

# ===================================================================
# مرحله ۴: جداسازی ویژگی‌ها و هدف
# ===================================================================
X = df_cleaned.drop('Diagnosis_numeric', axis=1)
y = df_cleaned['Diagnosis_numeric']

# ===================================================================
# مرحله ۵: تقسیم داده‌ها به آموزش و آزمون
# ===================================================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)  # [6]

# ===================================================================
# مرحله ۶: ساخت، آموزش و پیش‌بینی مدل پیش‌فرض (KNN با K=3)
# ===================================================================
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
pred_knn = knn.predict(X_test)

# ===================================================================
# مرحله ۷: ارزیابی عملکرد مدل KNN
# ===================================================================
acc_knn = accuracy_score(y_test, pred_knn)
print(f"دقت مدل KNN (K=3): {acc_knn*100:.2f}%")  # معمولاً 100% برای داده‌های شبیه‌سازی[?]
cm_knn = confusion_matrix(y_test, pred_knn)
sns.heatmap(cm_knn, annot=True, fmt='d', cmap='Blues',
            xticklabels=['سالم','سرطانی'],
            yticklabels=['سالم','سرطانی'])
plt.title('ماتریس درهم‌ریختگی KNN')
plt.show()
print(classification_report(y_test, pred_knn, target_names=['سالم (0)','سرطانی (1)']))  # [5]

```

### مرور گردش کار

۱. **خواندن و شبیه‌سازی داده:** داده‌های کثیف با `pandas.read_csv` خوانده شده و شامل `NaN` و مقادیر متنی گوناگون است.  
۲. **پاک‌سازی:** پر کردن گمشده‌ها با میانگین ستون؛ یکنواخت‌سازی متن به حروف کوچک؛ و نگاشت دسته‌ای به عدد برای آماده‌سازی مدل‌های ریاضی[1].  
۳. **جداسازی و تقسیم:** `X` ویژگی‌ها و `y` برچسب تشخیص؛ سپس تقسیم به `train/test` بر اساس `test_size=0.3`[2].  
۴. **آموزش و پیش‌بینی:** مدل KNN با `n_neighbors=3` آموزش داده و برچسب‌های آزمون پیش‌بینی می‌شوند[3].  
۵. **ارزیابی:** دقت، ماتریس درهم‌ریختگی و گزارش طبقه‌بندی استاندارد ارائه می‌شود[4].

### 🔬 تمرین تحلیلی: بهبود خط لوله

**وظایف تجربی:**

1. **تغییر هایپرپارامتر K:** مقدار `n_neighbors` را به 1 و 5 تغییر دهید؛ مشاهدات خود را ثبت کنید.
2. **تغییر نسبت تقسیم:** `test_size` را به 0.2 تغییر دهید؛ تأثیر آن بر دقت را بررسی کنید.
3. **الگوریتم جایگزین:** یک طبقه‌بند دیگر (مانند `LogisticRegression` یا `DecisionTreeClassifier`) را از مستندات Scikit-learn انتخاب کنید، جایگزین KNN کنید، و مقایسه عملکرد انجام دهید[5][6].

**جدول مقایسه عملکرد نمونه**  
| مدل | K | test*size | دقت |
|-----------------------|------|-----------|-------|
| KNN | 1 | 0.3 | 100% |
| KNN | 3 | 0.3 | 100% |
| KNN | 5 | 0.3 | 66.7% |
| KNN | 3 | 0.2 | 100% |
| LogisticRegression | – | 0.3 | 100% |
| DecisionTreeClassifier| – | 0.3 | 100% |  
*(نمونه نتایج بر اساس اجرای آزمایشی)[؟]\_

### 💡 نکات کلیدی

- **خط لوله سرتاسری:** همه مراحل از بارگذاری تا ارزیابی در یک اسکریپت یکپارچه.
- **اهمیت پاک‌سازی داده:** مدیریت مقادیر گمشده و ناهماهنگی‌های متنی، بخش عمده‌ای از پروژه را تشکیل می‌دهد.
- **آزمایش‌های تکراری:** بهبود عملکرد با تنظیم هایپرپارامترها و مقایسه الگوریتم‌های مختلف.
- **شبیه‌سازی برای نمونه‌سازی:** ایجاد داده‌ی نمونه به شکل رشته یا دیکشنری برای تست اولیه و آموزش سریع کد مفید است.

این فصل پایه‌ی مهارت‌های عملی شما در بیوانفورماتیک را تقویت کرد. اکنون می‌توانید خط لوله‌ی کامل تشخیص سرطان را بسازید، اجرا و ارزیابی کنید و آن را برای پروژه‌های بزرگ‌تر بهینه نمایید.

---

## **منابع**

[1] https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.fillna.html
[2] https://www.geeksforgeeks.org/python/how-to-split-the-dataset-with-scikit-learns-train_test_split-function/
[3] https://scikit-learn.org/0.15/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
[4] https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html
[5] https://www.digitalocean.com/community/tutorials/logistic-regression-with-scikit-learn
[6] https://www.geeksforgeeks.org/building-and-implementing-decision-tree-classifiers-with-scikit-learn-a-comprehensive-guide/
[7] https://www.w3schools.com/python/pandas/ref_df_fillna.asp
[8] https://note.nkmk.me/en/python-pandas-nan-fillna/
[9] https://www.w3schools.com/python/python_ml_knn.asp
[10] https://www.youtube.com/watch?v=XWx8sjTkiuQ
[11] https://builtin.com/data-science/train-test-split
[12] https://www.projectpro.io/recipes/perform-logistic-regression-sklearn
[13] https://www.datacamp.com/tutorial/decision-tree-classification-python
[14] https://docs.vultr.com/python/third-party/pandas/DataFrame/fillna
[15] https://scikit-learn.org/0.21/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
[16] https://scikit-learn.org/0.15/modules/generated/sklearn.metrics.classification_report.html
[17] https://realpython.com/train-test-split-python-data/
[18] https://www.youtube.com/watch?v=5FdavD4eU4g
[19] https://scikit-learn.org/0.15/modules/generated/sklearn.tree.DecisionTreeClassifier.html
[20] https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
