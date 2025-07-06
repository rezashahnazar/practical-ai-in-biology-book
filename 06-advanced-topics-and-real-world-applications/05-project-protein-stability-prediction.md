[→ بخش ۶-۴: اخلاق در هوش مصنوعی زیستی: فراتر از کد](./04-ethics-in-bio-ai.md) | [آزمون فصل ششم ←](./exam/index.md)

# فصل ۶: مباحث پیشرفته و کاربردهای دنیای واقعی

## بخش ۶-۵: پروژه: پیش‌بینی پایداری پروتئین

برای آخرین پروژه این کتاب، ما به سراغ یک مسئله رگرسیون کلاسیک و بسیار مهم در بیوانفورماتیک می‌رویم: پیش‌بینی پایداری یک پروتئین. پایداری یک پروتئین، که اغلب با «دمای ذوب» (Tm) آن اندازه‌گیری می‌شود، نقطه‌ای است که در آن نیمی از جمعیت پروتئین‌ها «غیرفرمی» (unfolded) و نیمی دیگر «فرم‌گرفته» (folded) هستند[1][2]. دمای ذوب معیار استانداردی برای مقایسه پایداری پروتئین‌ها در شرایط مختلف است و در طراحی داروها و آنزیم‌های صنعتی کاربرد حیاتی دارد[3].

### 🎯 مسئله‌‌محوری

چگونه می‌توانیم با استفاده از هوش مصنوعی و توالی اسیدهای آمینه، پایداری (Tm) یک پروتئین را پیش از تولید آزمایشگاهی پیش‌بینی کنیم؟

در مهندسی پروتئین، پیش‌بینی زودهنگام Tm می‌تواند هزینه‌ و زمان آزمایش‌های بیولوژیکی را به‌طور چشمگیری کاهش دهد و دریچه‌ای به سوی طراحی هوشمند مولکول‌های زیستی باز کند.

### اسکریپت کامل در Google Colab

کد زیر گردش کار پایه (با **داده‌های نمونه و شبیه‌سازی شده**) را نشان می‌دهد. توجه کنید که برای کاربرد واقعی باید از دیتاست‌های بزرگ‌تر مانند Meltome Atlas استفاده کنید تا مدل‌ها تعمیم‌پذیری بهتری داشته باشند.

```python
# ===================================================================
# مرحله ۱: وارد کردن کتابخانه‌ها
# ===================================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

# ===================================================================
# مرحله ۲: آماده‌سازی داده‌های شبیه‌سازی‌شده
# ===================================================================
data = {
    'percent_hydrophobic': [45,50,55,40,60,65,35,58,48,62],
    'percent_polar':      [35,30,25,40,20,15,45,22,32,18],
    'percent_charged':    [20]*10,
    'melting_temperature':[65.1,68.7,72.3,62.5,75.1,78.9,60.2,74.0,67.5,76.8]
}
df_proteins = pd.DataFrame(data)

# ===================================================================
# مرحله ۳: جداسازی ویژگی‌ها و هدف
# ===================================================================
X = df_proteins[['percent_hydrophobic','percent_polar','percent_charged']]
y = df_proteins['melting_temperature']

# ===================================================================
# مرحله ۴: تقسیم داده‌ها
# ===================================================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# ===================================================================
# مرحله ۵: آموزش و پیش‌بینی با RandomForestRegressor
# ===================================================================
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_preds = rf_model.predict(X_test)

# ===================================================================
# مرحله ۶: ارزیابی مدل Random Forest
# ===================================================================
rf_mae = mean_absolute_error(y_test, rf_preds)
rf_mse = mean_squared_error(y_test, rf_preds)
print(f"RF MAE: {rf_mae:.2f}°C, RF MSE: {rf_mse:.2f}")

# ===================================================================
# مرحله ۷: آموزش و پیش‌بینی با LinearRegression
# ===================================================================
lin_model = LinearRegression()
lin_model.fit(X_train, y_train)
lin_preds = lin_model.predict(X_test)

# ===================================================================
# مرحله ۸: ارزیابی مدل خطی
# ===================================================================
lin_mae = mean_absolute_error(y_test, lin_preds)
lin_mse = mean_squared_error(y_test, lin_preds)
print(f"Lin MAE: {lin_mae:.2f}°C, Lin MSE: {lin_mse:.2f}")

# ===================================================================
# مرحله ۹: رسم نمودار مقایسه
# ===================================================================
plt.figure(figsize=(6,6))
plt.scatter(y_test, lin_preds, label='Linear', alpha=0.7, s=80, edgecolors='k')
plt.scatter(y_test, rf_preds, label='Random Forest', alpha=0.7, s=80, marker='s', edgecolors='k')
lims = [min(y_test.min(), lin_preds.min(), rf_preds.min())-1,
        max(y_test.max(), lin_preds.max(), rf_preds.max())+1]
plt.plot(lims, lims, '--', color='red')
plt.xlabel('دمای ذوب واقعی (Actual Tm)')
plt.ylabel('دمای ذوب پیش‌بینی‌شده (Predicted Tm)')
plt.title('مقایسه مدل‌های رگرسیون')
plt.legend()
plt.grid(True)
plt.show()
```

### تفسیر نتایج

- مدل Random Forest:  
  MAE ≈ 1.43°C، MSE ≈ 3.02
- مدل Linear Regression:  
  MAE ≈ 0.35°C، MSE ≈ 0.14

در این مجموعه داده کوچک، **رگرسیون خطی** عملکرد بهتری نشان داد. اما در مقیاس بزرگ‌، که روابط غیرخطی قوی‌تر ظاهر می‌شوند، مدل‌های جنگل تصادفی یا سایر مدل‌های غیرخطی ممکن است عملکرد بهتری ارائه دهند[4].

### 🔬 تمرین تحلیلی: مهندسی ویژگی و مقایسه مدل

**وظایف:**

1. **مقایسه مدل:**

   - مدل `RandomForestRegressor` را با `LinearRegression` جایگزین کرده و عملکرد آن‌ها را با MAE و MSE مقایسه کنید.
   - نمودار پراکندگی را تفسیر کنید: کدام مدل نقاط را به خط قرمز نزدیک‌تر می‌آورد؟

2. **مهندسی ویژگی:**
   - ویژگی جدید `hydro_polar_ratio` را اضافه کنید:
     ```python
     df_proteins['hydro_polar_ratio'] = df_proteins['percent_hydrophobic'] / df_proteins['percent_polar']
     ```
   - این ویژگی را به مجموعه `X` اضافه کرده و دوباره هر دو مدل را آموزش دهید.
   - آیا شاخص‌های MAE و MSE بهبود یافتند؟ چه نتیجه‌ای می‌گیرید؟

## نکات کلیدی این بخش

در طراحی یک پروژه پیش‌بینی پایداری پروتئین:

| موضوع                              | توضیح                                                                                         |
| ---------------------------------- | --------------------------------------------------------------------------------------------- |
| کاربرد رگرسیون                     | پیش‌بینی مقادیر پیوسته مانند Tm پروتئین‌ها[4].                                                |
| معنا و محاسبه Tm                   | دمایی که در آن 50٪ جمعیت پروتئین‌ها unfolded می‌شوند[1][2].                                   |
| تعاملات هیدروفوبیک                 | بیش از ۶۰٪ پایداری پروتئین‌ها را تشکیل می‌دهند؛ تقریباً ۱.۱ kcal/mol به ازای هر گروه –CH₂[5]. |
| ارزیابی بصری                       | نمودار پراکندگی واقعی vs. پیش‌بینی‌شده برای هر دو مدل، ابزار سریع درک عملکرد است.             |
| مقایسه مدل‌ها                      | هیچ مدلی بر همه مسائل مسلط نیست؛ همواره چند مدل را آزمون و مقایسه کنید.                       |
| مهندسی ویژگی (Feature Engineering) | ایجاد ویژگی‌های جدید (نسبت‌ها، ترکیبات غیرخطی و…) می‌تواند تأثیر زیادی داشته باشد.            |

تبریک! شما اکنون مهارت‌های اساسی برای بارگیری، پردازش، مدل‌سازی و ارزیابی داده‌های بیولوژیکی با استفاده از AI را کسب کردید.

---

## **منابع**

[1] https://support.nanotempertech.com/hc/en-us/articles/23443481117713-How-is-the-protein-melting-point-Tm-determined
[2] https://support.nanotempertech.com/hc/en-us/articles/23803406512273-Inflection-Point-IP-vs-Melting-Temperature-Tm
[3] https://pmc.ncbi.nlm.nih.gov/articles/PMC6128648/
[4] https://pubmed.ncbi.nlm.nih.gov/19896904/
[5] https://pmc.ncbi.nlm.nih.gov/articles/PMC3086625/
[6] https://en.wikipedia.org/wiki/Transmembrane_domain
[7] https://en.wikipedia.org/wiki/Denaturation_midpoint
[8] https://pmc.ncbi.nlm.nih.gov/articles/PMC10627164/
[9] https://research.vu.nl/files/42787876/complete%20dissertation.pdf
[10] https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/transmembrane-protein
[11] https://www.nature.com/articles/srep28285
[12] https://www.reddit.com/r/Mcat/comments/14dqshq/definition_of_melting_temperature_tm/
[13] https://en.wikipedia.org/wiki/Transmembrane_protein
[14] https://arxiv.org/pdf/1312.3858.pdf
[15] https://pmc.ncbi.nlm.nih.gov/articles/PMC2913670/
[16] https://www.sciencedirect.com/science/article/pii/S200103702200143X
[17] https://www.wisdomlib.org/concept/transmembrane-protein
[18] https://pubmed.ncbi.nlm.nih.gov/8453376/
[19] https://www.azonano.com/article.aspx?ArticleID=1224
[20] https://www.news-medical.net/whitepaper/20231113/Exploring-the-Significance-of-Transmembrane-Protein-Expression-for-Advancing-Science-and-Medicine.aspx
