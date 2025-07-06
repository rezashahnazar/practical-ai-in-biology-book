[→ بخش ۵-۱: کتابخانه‌های قدرتمند: NumPy، Pandas و Scikit-learn](./01-powerful-libraries-numpy-pandas-sklearn.md) | [بخش ۵-۳: اولین مدل طبقه‌بندی شما: الگوریتم K-نزدیک‌ترین همسایه (KNN) ←](./03-first-classification-model-knn.md)

# فصل ۵ بخش ۲: هنر آماده‌سازی داده‌های زیستی

**خلاصه کلیدی**  
کیفیت مدل‌‌های هوش مصنوعی مستقیماً به کیفیت داده‌های ورودی بستگی دارد؛ پژوهش‌های مختلف نشان می‌دهند که دانشمندان داده بین 45٪ تا 80٪ از زمان خود را صرف پاک‌سازی و آماده‌سازی داده‌ها می‌کنند[1][2].

## مسئلهٔ محوری

داده‌های زیستی در دنیای واقعی اغلب پر از مقادیر گمشده، فرمت‌های ناسازگار و خطاهای ورود اطلاعات هستند. هدف این بخش، **رام کردن** (taming) این داده‌های “وحشی” و تبدیل آن‌ها به یک مجموعه‌ی عددی، بدون نقص و آماده برای آموزش مدل است.

## ۱. اصل GIGO

اصطلاح **Garbage In, Garbage Out (GIGO)** بیان می‌کند که هر الگوریتمی، هرچقدر هم قدرتمند، اگر ورودی بی‌کیفیتی دریافت کند، خروجی بی‌ارزشی تولید خواهد کرد[3]. این عبارت برای اولین‌بار در یک مقالهٔ ۱۹۵۷ از ویلیام ملین (William D. Mellin) در مورد برنامه‌ریزی کامپیوترها به‌کار رفت[3].

## ۲. نمونه دادهٔ کثیف

ابتدا یک DataFrame کوچک با مشکلات رایج می‌سازیم:

```python
import pandas as pd
import numpy as np

data = {
    'PatientID': ['P001','P002','P003','P004','P005'],
    'Age': [45,62,np.nan,38,55],            # مقدار گمشده
    'Sex': ['F','M','F','M','Female'],      # مقادیر ناسازگار
    'Gene_Expression': [12.5,21.0,9.7,15.2,22.1],
    'Diagnosis': ['Cancer','Healthy','Cancer','Healthy','Cancer']
}
df = pd.DataFrame(data)
print(df)
```

| PatientID | Age  | Sex    | Gene_Expression | Diagnosis |
| --------- | ---- | ------ | --------------- | --------- |
| P001      | 45.0 | F      | 12.5            | Cancer    |
| P002      | 62.0 | M      | 21.0            | Healthy   |
| P003      | NaN  | F      | 9.7             | Cancer    |
| P004      | 38.0 | M      | 15.2            | Healthy   |
| P005      | 55.0 | Female | 22.1            | Cancer    |

## ۳. مراحل پاک‌سازی

### ۳.۱. رسیدگی به مقادیر گمشده

برای ستون `Age` مقدار `NaN` را نمی‌خواهیم حذف کنیم، بلکه با میانگین سنی پر می‌کنیم:

```python
mean_age = df['Age'].mean()
df['Age'] = df['Age'].fillna(mean_age)
```

### ۳.۲. استانداردسازی داده‌های دسته‌ای

برای ستون `Sex` همه مقادیر `Female` را به `F` تبدیل می‌کنیم:

```python
df['Sex'] = df['Sex'].replace({'Female':'F'})
```

### ۳.۳. تبدیل متن به عدد (Feature Engineering)

ابتدا ستون هدف (`Diagnosis`) را عددی می‌کنیم:

```python
df['Diagnosis'] = df['Diagnosis'].replace({'Healthy':0,'Cancer':1})
```

سپس برای ستون ویژگی (`Sex`) از **One-Hot Encoding** استفاده می‌کنیم تا داده‌ها «فقط» ۰ یا ۱ شوند و فرضیات ترتیبی نداشته باشیم[4][5]:

```python
df = pd.get_dummies(df, columns=['Sex'], drop_first=True)
```

حین استفاده از `inplace=True` دقت کنید که نسخه‌های جدید pandas هشدار می‌دهند؛ روش جایگزین امن‌تر همان‌طور که بالا نشان داده شد، برگشت مستقیم مقدار جدید به ستون است.

## ۴. جداسازی X و y

- `X`: ماتریس ویژگی‌ها (تمام ستون‌ها به‌جز `PatientID` و `Diagnosis`)
- `y`: بردار هدف (`Diagnosis`)

```python
X = df.drop(columns=['PatientID','Diagnosis'])
y = df['Diagnosis']
```

## جدول: مراحل آماده‌سازی و تبدیل داده

| مرحله                     | مشکل                      | روش حل                                                       |
| ------------------------- | ------------------------- | ------------------------------------------------------------ |
| مقادیر گمشده              | NaN در `Age`              | پر کردن با میانگین: `fillna(mean_age)`                       |
| داده‌های دسته‌ای ناسازگار | `Female` و `F` در `Sex`   | یکنواخت‌سازی: `replace({'Female':'F'})`                      |
| تبدیل هدف به عدد          | متن در `Diagnosis`        | جایگزینی: `{'Healthy':0,'Cancer':1}`                         |
| کدگذاری یک-گرمی           | فرض ترتیبی در `Sex`       | `pd.get_dummies(...,drop_first=True)`                        |
| جداسازی ویژگی و هدف       | وجود ستون غیرمرتبط (`ID`) | حذف با `drop(columns=['PatientID'])` و جداسازی `y = df[...]` |

## ۵. تمرین تحلیلی

دیتافریم زیر را پاک‌سازی کنید:

```python
data = {
    'SampleID': ['S1','S2','S3','S4'],
    'Tissue_Type': ['Tumor','Normal','Tumor','Unknown'],
    'Gene_A_Expr': [150.2,89.9,180.5,165.1],
    'Gene_B_Expr': [75.6,99.1,-1.0,82.3],     # مقدار منفی نامعتبر
    'Batch': [1,2,1,2]
}
new_df = pd.DataFrame(data)
```

**مراحل:**

1. حذف ردیف با `Tissue_Type=='Unknown'`
2. جایگزینی هر مقدار منفی در `Gene_B_Expr` با ۰
3. تبدیل `Tissue_Type` به عدد (`Normal`=0, `Tumor`=1)
4. چاپ نتیجه نهایی

```python
cleaned_df = new_df.copy()

# 1
cleaned_df = cleaned_df[cleaned_df['Tissue_Type']!='Unknown']

# 2
cleaned_df.loc[cleaned_df['Gene_B_Expr']<0,'Gene_B_Expr'] = 0

# 3
cleaned_df['Tissue_Type'] = cleaned_df['Tissue_Type'].replace({'Normal':0,'Tumor':1})

print(cleaned_df)
```

## نکات کلیدی

- **GIGO:** کیفیت خروجی به کیفیت ورودی بستگی دارد[3].
- **زمان صرف شده:** آماده‌سازی داده‌ها تا ۸۰٪ از زمان دانشمند داده را می‌گیرد، معمولاً بین ۴۵٪ تا ۸۰٪[1][2].
- **مقادیر گمشده:** روش‌های مختلف جایگزینی (میانگین، میانه، ثابت) یا حذف سطر.
- **استانداردسازی:** یکپارچه کردن فرمت‌ها (مثلاً `Female` → `F`).
- **تبدیل به عدد:** استفاده از جایگزینی مستقیم یا One-Hot Encoding.
- **جداسازی X و y:** همیشه قبل از آموزش مدل ویژگی‌ها و هدف را جدا کنید.

با داده‌های تمیز و عددی، آماده‌ایم تا در بخش بعدی—**ساخت اولین مدل طبقه‌بندی (KNN)**—گام برداریم و مهارت‌های عملی خود را به کار بگیریم.

---

## **منابع**

[1] https://www.bigdatawire.com/2020/07/06/data-prep-still-dominates-data-scientists-time-survey-finds/
[2] https://www.pragmaticinstitute.com/resources/articles/data/overcoming-the-80-20-rule-in-data-science/
[3] https://en.wikipedia.org/wiki/Garbage_in,_garbage_out
[4] https://www.kdnuggets.com/2023/07/pandas-onehot-encode-data.html
[5] https://www.geeksforgeeks.org/machine-learning/ml-one-hot-encoding/
[6] https://www.atlasobscura.com/articles/is-this-the-first-time-anyone-printed-garbage-in-garbage-out
[7] https://dataenso.com/en/garbage-in-garbage-out/
[8] https://stackoverflow.com/questions/37292872/how-can-i-one-hot-encode-in-python
[9] https://blog.ldodds.com/2020/01/31/do-data-scientists-spend-80-of-their-time-cleaning-data-turns-out-no/
[10] https://www.techtarget.com/searchsoftwarequality/definition/garbage-in-garbage-out
[11] https://www.dataversity.net/survey-shows-data-scientists-spend-time-cleaning-data/
[12] https://discuss.datasciencedojo.com/t/how-to-create-one-hot-encodings-for-categorical-variables-in-python/994
[13] https://www.projectpro.io/article/why-data-preparation-is-an-important-part-of-data-science/242
[14] https://www.ebsco.com/research-starters/computer-science/garbage-garbage-out-gigo
[15] https://www.datacamp.com/tutorial/one-hot-encoding-python-tutorial
[16] https://www.reddit.com/r/datascience/comments/bupmyf/data_scientists_spend_up_to_80_of_time_on_data/
[17] https://yourshepherdsheart.wordpress.com/2025/04/28/gigo/
[18] https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html
[19] https://admonsters.com/gigo-garbage-garbage-out/
[20] https://www.reddit.com/r/learnmachinelearning/comments/1d5unzs/pandas_factorize_and_one_hot_encoding/
