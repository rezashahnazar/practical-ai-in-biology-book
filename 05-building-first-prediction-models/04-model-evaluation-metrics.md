[→ بخش ۵-۳: اولین مدل طبقه‌بندی: آموزش یک تصمیم‌گیرنده دیجیتال](./03-first-classification-model-knn.md) | [بخش ۵-۵: پروژه: ساخت مدل تشخیص سرطان ←](./05-project-cancer-detection-model.md)

# فصل ۵: ساخت اولین مدل‌های پیش‌بینی: از داده تا تشخیص

## بخش ۵-۴: ارزیابی مدل: آیا به پیش‌بینی‌ها می‌توان اعتماد کرد؟

در بخش قبل، ما اولین مدل خود را آموزش دادیم و با استفاده از آن پیش‌بینی‌هایی انجام دادیم. اما چگونه می‌توانیم به‌صورت کمّی و استاندارد بگوییم که این مدل چقدر خوب است؟ صرفاً مقایسه چشمی پیش‌بینی‌ها با برچسب‌های واقعی کافی نیست، به‌ویژه وقتی با مجموعه داده‌های بزرگ سروکار داریم. در این بخش، با معیارهای ارزیابی مدل آشنا می‌شویم تا عملکرد آن را مانند یک دانشمند دقیق «کالبدشکافی» کنیم.

### 🎯 مسئله محوری

چگونه به مدل خود «نمره» بدهیم و بفهمیم در چه بخش‌هایی قوی است و در چه بخش‌هایی ضعف دارد؟

نمرهٔ ساده «دقت» (Accuracy) گاهی گمراه‌کننده است. مثلاً یک مدل تشخیص سرطان که در جمعیتِ آزمایش فقط یک بیمار واقعی وجود دارد و همه را سالم تشخیص می‌دهد، دقت ۹۹٪ خواهد داشت، اما عملاً در شناسایی بیمار ناموفق است. بنابراین باید خطاهای مدل را با معیارهای دقیق‌تری بررسی کنیم:

- **حساسیت (Recall)**: چه سهمی از بیماران واقعی را شناسایی کرده‌ایم؟
- **دقت (Precision)**: از بین پیش‌بینی‌های «بیمار»، چه سهمی واقعاً بیمار بوده‌اند؟

برای این کار ابتدا ماتریس درهم‌ریختگی (Confusion Matrix) را می‌آموزیم.

## ۱. معیار پایه: دقت (Accuracy)

دقت نسبت تعداد پیش‌بینی‌های درست به کل پیش‌بینی‌ها است[1]:

$$
\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}
$$

```python
from sklearn.metrics import accuracy_score

# فرض می‌کنیم y_test و predictions تعریف شده‌اند
accuracy = accuracy_score(y_test, predictions)
print(f"دقت مدل ما: {accuracy * 100:.2f}%")
```

اگرچه دقت معیار ساده و ابتدایی است، اما در داده‌های نامتوازن (مثلاً تشخیص بیماری نادر) می‌تواند گمراه‌کننده باشد.

## ۲. ماتریس درهم‌ریختگی: بازنمایی انواع خطا

ماتریس درهم‌ریختگی (Confusion Matrix) جدول ۲×۲ است که تعداد صحیح‌ها و انواع خطاها را نشان می‌دهد[2]:

|            | پیش‌بینی مثبت (سرطانی) | پیش‌بینی منفی (سالم) |
| ---------- | ---------------------- | -------------------- |
| واقعی مثبت | True Positive (TP)     | False Negative (FN)  |
| واقعی منفی | False Positive (FP)    | True Negative (TN)   |

- **True Positive (TP):** بیمار سرطانی بوده و مدل درست تشخیص داده.
- **True Negative (TN):** بیمار سالم بوده و مدل درست تشخیص داده.
- **False Positive (FP):** بیمار سالم اما مدل اشتباهاً سرطانی تشخیص داده (هشدار غلط).
- **False Negative (FN):** بیمار سرطانی اما مدل آن را سالم تشخیص داده (خطرناک‌ترین خطا).

در مسائل پزشکی، FN پرهزینه‌تر از FP است.

```python
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

cm = confusion_matrix(y_test, predictions)

plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['سالم (0)', 'سرطانی (1)'],
            yticklabels=['سالم (0)', 'سرطانی (1)'])
plt.xlabel('پیش‌بینی مدل')
plt.ylabel('برچسب واقعی')
plt.title('ماتریس درهم‌ریختگی')
plt.show()
```

## ۳. فراتر از دقت: Precision و Recall

با استفاده از اجزای ماتریس درهم‌ریختگی می‌توانیم دو معیار کلیدی را محاسبه کنیم[3]:

- **Precision (دقت مثبت):**

  $$
  \text{Precision} = \frac{TP}{TP + FP}
  $$

  «از میان پیش‌بینی‌های مثبت، چه سهمی واقعاً مثبت بوده‌اند؟»

- **Recall (حساسیت):**
  $$
  \text{Recall} = \frac{TP}{TP + FN}
  $$
  «از میان نمونه‌های مثبت واقعی، چه سهمی شناسایی شده‌اند؟»

در کاربردهای پزشکی معمولاً **Recall** اولویت بالایی دارد تا کمترین بیمار واقعی را از دست بدهیم.

```python
from sklearn.metrics import classification_report

report = classification_report(y_test, predictions,
                               target_names=['سالم (0)', 'سرطانی (1)'],
                               digits=4)
print(report)
```

خروجی گزارش، دقت، حساسیت، F1-score و تعداد نمونه (support) را برای هر کلاس نمایش می‌دهد.

## 🔬 تمرین تحلیلی: تحلیل گزارش طبقه‌بندی

```
              precision    recall  f1-score   support
سالم (0)       0.98      0.95      0.96       100
بیمار (1)      0.85      0.93      0.89        30

accuracy                           0.94       130
macro avg      0.91      0.94      0.93       130
weighted avg   0.95      0.94      0.95       130
```

1. **Recall** برای کلاس «بیمار» 0.93 است. یعنی 93٪ از بیماران واقعی توسط مدل شناسایی شده‌اند.
2. **Precision** برای کلاس «بیمار» 0.85 است. یعنی از میان پیش‌بینی‌های «بیمار»، 85٪ درست بوده‌اند.
3. مدل در شناسایی بیماران (Recall=0.93) عملکرد بهتری نسبت به اعتبار پیش‌بینی مثبت (Precision=0.85) دارد.
4. اگر هدف اصلی از دست ندادن حتی یک بیمار باشد، Recall بالا مطلوب است. با Recall=0.93 مدل نسبتاً خوب عمل می‌کند اما هنوز 7٪ از بیماران واقعی را از دست می‌دهد که در برخی کاربردها ممکن است قابل قبول نباشد.

### 💡 نکات کلیدی این بخش

- **دقت (Accuracy):** معیار ساده اما گاهی گمراه‌کننده مخصوصاً در داده‌های نامتوازن[1].
- **ماتریس درهم‌ریختگی (Confusion Matrix):** ابزار قدرتمند برای تحلیل انواع خطاها[2].
- **False Negative (FN):** خطرناک‌ترین خطا در کاربردهای پزشکی.
- **Precision:** نشان می‌دهد در پیش‌بینی‌های مثبت چقدر می‌توان اعتماد کرد[3].
- **Recall:** نشان می‌دهد مدل در پیدا کردن تمام موارد مثبت واقعی چقدر تواناست[3].
- در مسائل حساس پزشکی غالباً Recall اولویت دارد، اما بایستی توازن مناسب با Precision نیز برقرار شود.

اکنون شما می‌توانید نه تنها مدل بسازید، بلکه عملکرد آن را با معیارهای استاندارد به‌طور حرفه‌ای ارزیابی کنید و نقاط قوت و ضعف آن را مشخص نمایید.  
در بخش بعدی، این پروژه را با جمع‌بندی آموخته‌هایمان به پایان می‌رسانیم.

---

## **منابع**

[1] https://www.ibm.com/docs/en/ws-and-kc?topic=metrics-accuracy
[2] https://en.wikipedia.org/wiki/Confusion_matrix
[3] https://en.wikipedia.org/wiki/Precision_and_recall
[4] https://celerdata.com/glossary/confusion-matrix
[5] https://encord.com/blog/classification-metrics-accuracy-precision-recall/
[6] https://static.hlt.bme.hu/semantics/external/pages/inform%C3%A1ci%C3%B3-visszakeres%C3%A9s/en.wikipedia.org/wiki/Precision_and_recall.html
[7] https://www.geeksforgeeks.org/confusion-matrix-machine-learning/
[8] https://www.iguazio.com/glossary/model-accuracy-in-ml/
[9] https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html
[10] https://www.artsyltech.com/blog/Accuracy-In-Machine-Learning
[11] https://www.reddit.com/r/learnmachinelearning/comments/b05s3o/could_some_please_explain_the_intuition_behind/
[12] https://www.ibm.com/think/topics/confusion-matrix
[13] https://www.geeksforgeeks.org/machine-learning/metrics-for-machine-learning-model/
[14] https://wiki.cloudfactory.com/docs/mp-wiki/metrics/precision-recall-curve-and-auc-pr
[15] https://www.coursera.org/articles/what-is-a-confusion-matrix
[16] https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall
[17] https://en.wikipedia.org/wiki/Evaluation_of_binary_classifiers
[18] https://towardsdatascience.com/performance-metrics-confusion-matrix-precision-recall-and-f1-score-a8fe076a2262/
[19] https://www.evidentlyai.com/classification-metrics/accuracy-precision-recall
[20] https://wiki.pathmind.com/accuracy-precision-recall-f1
