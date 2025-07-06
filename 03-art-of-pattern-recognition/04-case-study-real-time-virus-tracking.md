[→ بخش ۳-۳: ساختن درخت زندگی: فیلوژنتیک مولکولی](./03-building-tree-of-life-phylogenetics.md) | [بخش ۳-۵: شبیه‌سازی: یک جستجوی BLAST روی کاغذ ←](./05-simulation-blast-on-paper.md)

# بخش ۳-۴: مطالعه موردی: ردیابی ویروس‌ها در زمان واقعی

در میانه یک پاندمی جهانی، هر روز هزاران نفر مبتلا می‌شوند و ویروس با سرعتی سرسام‌آور در سراسر جهان پخش می‌شود. به عنوان یک دانشمند یا مسئول بهداشت، شما با سوالات مرگ و زندگی روبرو هستید: ویروس از کجا می‌آید؟ چگونه پخش می‌شود؟ و آیا در حال خطرناک‌تر شدن است؟ شما به یک ابزار نیاز دارید که به شما اجازه دهد این دشمن نامرئی را "ببینید" و حرکات بعدی آن را پیش‌بینی کنید. چگونه می‌توان از توالی ژنتیکی ویروس که از بیماران مختلف جمع‌آوری شده، برای ساختن یک "نقشه ردپا" و ردیابی آن در زمان واقعی استفاده کرد؟

در اوایل سال ۲۰۲۰، جهان با یک بحران بی‌سابقه روبرو شد: پاندمی ویروس SARS-CoV-2[1]. در میان انبوهی از اطلاعات و عدم قطعیت‌ها، چند سوال حیاتی برای دانشمندان و مسئولان بهداشت عمومی وجود داشت:

- این ویروس چگونه از یک شهر به کل دنیا پخش شد؟
- آیا تمام موارد ابتلا در یک کشور از یک منبع واحد آمده‌اند یا ویروس چندین بار به طور مستقل وارد شده است؟
- آیا ویروس در حال تغییر و تکامل است؟ و اگر چنین است، آیا این تغییرات آن را خطرناک‌تر می‌کند؟

پاسخ به این سوالات در رشته‌ای به نام **اپیدمیولوژی ژنومی (Genomic Epidemiology)** نهفته بود که از تحلیل فیلوژنتیک به عنوان ابزار اصلی خود استفاده می‌کند[2][3].

### **کارآگاهان ژنومی وارد می‌شوند**

در سراسر جهان، آزمایشگاه‌ها شروع به توالی‌یابی ژنوم کامل ویروس SARS-CoV-2 از نمونه‌های بیماران کردند[4]. هر ژنوم ویروسی مانند یک "اثر انگشت" مولکولی عمل می‌کند. از آنجایی که ویروس‌ها هنگام تکثیر دچار جهش‌های کوچکی می‌شوند، ژنوم ویروس‌های نمونه‌برداری شده از افراد مختلف، تفاوت‌های جزئی با هم دارند[5]. با مقایسه این تفاوت‌ها، دانشمندان توانستند یک درخت فیلوژنتیک غول‌پیکر برای ویروس بسازند و داستان انتشار آن را در زمان واقعی بخوانند[6][7].

#### **کشف ۱: ردیابی مسیرهای ورود**

یکی از اولین اکتشافات این بود که ویروس در بسیاری از کشورها، نه یک بار، بلکه **چندین بار** و به طور مستقل وارد شده بود[8][9]. برای مثال، تحلیل‌های فیلوژنتیک در بریتانیا نشان داد که در موج اول، بیش از ۱۳۵۶ خط تکاملی (lineage) مختلف از ویروس، عمدتاً از کشورهای اروپایی مانند اسپانیا، فرانسه و ایتالیا، وارد این کشور شده بودند[10][11]. این اطلاعات حیاتی بود، زیرا نشان می‌داد که بستن مرزها به روی یک کشور خاص کافی نیست و ویروس از مسیرهای متعددی در حال ورود است[8][9].

#### **کشف ۲: شناسایی زنجیره‌های انتقال محلی**

درخت فیلوژنتیک مانند یک نقشه برای ردیابی خوشه‌های شیوع عمل می‌کرد[12][13]. اگر ژنوم ویروس‌های چند بیمار در یک شهر بسیار شبیه به هم بود و در یک خوشه مشخص روی درخت قرار می‌گرفت، این یک مدرک قوی برای انتقال محلی ویروس بین آن افراد بود[12]. این تکنیک به شناسایی و کنترل خوشه‌های شیوع در بیمارستان‌ها، خانه‌های سالمندان و رویدادهای ابرناقل (super-spreading events) کمک شایانی کرد[13][14].

#### **کشف ۳: ظهور واریانت‌های نگران‌کننده (Variants of Concern)**

شاید مهم‌ترین کمک فیلوژنتیک، شناسایی سریع واریانت‌های جدید بود[15][16]. در اواخر سال ۲۰۲۰، دانشمندان در بریتانیا متوجه یک شاخه جدید و به سرعت در حال رشد در درخت فیلوژنتیک ویروس شدند[17][18]. این شاخه، که بعدها **واریانت آلفا (B.1.1.7)** نام گرفت، به طور غیرمعمولی تعداد زیادی جهش جدید داشت[18][19]. تحلیل‌های فیلوژنتیکی نشان داد که این واریانت با سرعت بسیار بیشتری نسبت به سویه‌های قبلی در حال انتشار است[18][20]. این کشف، زنگ خطر را در سراسر جهان به صدا درآورد و منجر به تغییر سیاست‌های بهداشتی و تسریع در برنامه‌های واکسیناسیون شد[16][18].

مدتی بعد، سناریوهای مشابهی در آفریقای جنوبی (واریانت بتا)، برزیل (واریانت گاما) و هند (واریانت دلتا) تکرار شد[15][21]. در هر مورد، این تحلیل فیلوژنتیک بود که اولین بار، ظهور یک شاخه تکاملی جدید و خطرناک را به جهان هشدار داد[15][16].

```mermaid
graph TD
    subgraph "درخت تکاملی SARS-CoV-2"
        A(سویه اولیه ووهان) --> B(سویه‌های اولیه در اروپا)
        B --> C{انتقال در جامعه}
        C --> D("بیمار ۱ - لندن")
        C --> E("بیمار ۲ - منچستر")

        B --> F(شاخه جدید با جهش‌های متعدد)
        F --> G{واریانت آلفا (B.1.1.7)}
        G --> H("بیمار ۳ - کنت")
        G --> I("بیمار ۴ - کنت")
        G --> J("بیمار ۵ - لندن")
    end

    subgraph "توضیحات"
        NodeF("یک شاخه جدید با سرعت رشد بالاو چندین جهش کلیدی (مانند N501Y)روی درخت ظاهر می‌شود.")
        NodeG("این شاخه به عنوان یک'واریانت نگران‌کننده'شناسایی می‌شود.")
    end

    style F fill:#E74C3C,stroke:#C0392B,stroke-width:2px
    style G fill:#F39C12,stroke:#D35400,stroke-width:2px
```

این مطالعه موردی نشان می‌دهد که تحلیل فیلوژنتیک یک ابزار صرفاً آکادمیک برای مطالعه گذشته نیست، بلکه یک تکنولوژی حیاتی برای **نظارت، پیش‌بینی و مدیریت** پاندمی‌ها در زمان واقعی است[14][22]. با خواندن تاریخچه نوشته شده در ژنوم ویروس‌ها، ما می‌توانیم برای مقابله با تهدیدهای آینده آماده‌تر شویم[4][23].

### 🔬 تمرین تحلیلی: تفسیر نقشه ویروسی

به نمودار mermaid ارائه شده در این بخش با دقت نگاه کنید.

**سوالات:**

1. فرض کنید شما مسئول بهداشت شهر لندن هستید. با مشاهده این درخت، چه تفاوتی در الگوی انتشار بین "بیمار ۱" و "بیمار ۵" مشاهده می‌کنید؟ این تفاوت چه مفهومی برای استراتژی کنترل شما دارد؟
2. اگر یک بیمار جدید در اسکاتلند با سویه‌ای متعلق به شاخه "واریانت آلفا" شناسایی شود، محتمل‌ترین منبع عفونت او چیست؟ آیا او به احتمال زیاد ویروس را از یک مسافر بازگشته از ووهان گرفته یا از یک فرد مبتلا در بریتانیا؟
3. چرا شناسایی "گره F" (شاخه جدید با جهش‌های متعدد) از نظر بهداشت عمومی یک نقطه عطف حیاتی محسوب می‌شود؟

### 💡 نکات کلیدی این بخش

- **اپیدمیولوژی ژنومی:** استفاده از توالی‌یابی ژنوم و فیلوژنتیک برای مطالعه الگوهای انتشار بیماری‌ها[2][24].
- **ردیابی منابع:** تحلیل فیلوژنتیک می‌تواند نشان دهد که آیا یک شیوع ناشی از یک یا چند منبع مستقل ورود ویروس به یک منطقه بوده است[8][9].
- **شناسایی خوشه‌های انتقال:** گروه‌بندی بیماران بر روی درخت تکاملی به شناسایی و مهار زنجیره‌های انتقال محلی کمک می‌کند[12][13].
- **نظارت بر تکامل ویروس:** مهم‌ترین کاربرد این رشته، شناسایی سریع واریانت‌های جدید (مانند آلفا و دلتا) است که ممکن است سرعت انتقال یا شدت بیماری‌زایی متفاوتی داشته باشند[15][21].

این مطالعه موردی قدرت تحلیل‌های تکاملی را به خوبی نشان داد. این تحلیل‌ها بر پایه مقایسه توالی‌ها بنا شده‌اند. در بخش بعدی، به سراغ یک شبیه‌سازی عملی خواهیم رفت تا با ابزار کلیدی BLAST که در بخش‌های قبل با آن آشنا شدیم، کار کرده و نحوه استفاده از آن در یک سناریوی واقعی را تجربه کنیم.

---

## **منابع**

[1] https://pmc.ncbi.nlm.nih.gov/articles/PMC7153464/
[2] https://www.nature.com/articles/s43856-023-00328-3
[3] https://pmc.ncbi.nlm.nih.gov/articles/PMC7314511/
[4] https://pmc.ncbi.nlm.nih.gov/articles/PMC5210220/
[5] https://www.nature.com/articles/s41598-020-79484-8
[6] https://nextstrain.org
[7] https://github.com/nextstrain/ncov
[8] https://www.pnas.org/doi/10.1073/pnas.2012008118
[9] https://www.nature.com/articles/s41564-020-00838-z
[10] https://www.bbc.com/news/health-52993734
[11] https://virological.org/t/preliminary-analysis-of-sars-cov-2-importation-establishment-of-uk-transmission-lineages/507
[12] https://pmc.ncbi.nlm.nih.gov/articles/PMC9554197/
[13] https://journals.asm.org/doi/10.1128/spectrum.01900-22
[14] https://academic.oup.com/cid/advance-article/doi/10.1093/cid/ciaf216/8122482
[15] https://pmc.ncbi.nlm.nih.gov/articles/PMC10338667/
[16] https://pmc.ncbi.nlm.nih.gov/articles/PMC8216402/
[17] https://pmc.ncbi.nlm.nih.gov/articles/PMC9752794/
[18] https://en.wikipedia.org/wiki/SARS-CoV-2_Alpha_variant
[19] https://pubmed.ncbi.nlm.nih.gov/36533153/
[20] https://www.nature.com/articles/s41586-021-04245-0
[21] https://en.wikipedia.org/wiki/SARS-CoV-2_Delta_variant
[22] https://www.solugenomics.com
[23] https://www.nature.com/articles/s41576-022-00483-8
[24] https://www.cdc.gov/advanced-molecular-detection/php/training/index.html
[25] https://www.nature.com/articles/s41598-023-42065-6
[26] https://journals.tubitak.gov.tr/biology/vol44/iss7/3/
[27] https://www.who.int/europe/news/item/12-07-2023-tracking-the-paths-of-infectious-diseases--t-rkiye-s-national-genomic-surveillance-strategy-nears-completion
[28] https://pubmed.ncbi.nlm.nih.gov/38379564/
[29] https://www.nature.com/articles/d41586-025-02039-2
[30] https://pmc.ncbi.nlm.nih.gov/articles/PMC10383548/
[31] https://www.sciencedirect.com/science/article/pii/S0042682223001824
[32] https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2022.851323/full
[33] https://www.ncbi.nlm.nih.gov/books/NBK562769/
[34] https://www.ncbi.nlm.nih.gov/books/NBK562773/
[35] https://www.sciencedirect.com/science/article/pii/S1471492221002051
[36] https://www.mdpi.com/2073-4425/15/7/876
[37] https://www.publichealthontario.ca/en/Data-and-Analysis/Infectious-Disease/COVID-19-Data-Surveillance/Nextstrain
[38] https://pmc.ncbi.nlm.nih.gov/articles/PMC10525159/
[39] https://dergipark.org.tr/tr/pub/phnx/article/950042
[40] https://www.yalemedicine.org/news/covid-19-variants-of-concern-omicron
[41] https://pmc.ncbi.nlm.nih.gov/articles/PMC10394493/
[42] https://www.uchealth.com/en/media-room/covid-19/alpha-beta-gamma-delta-omicron-covid-19-variants-explained
[43] https://www.ecdc.europa.eu/en/covid-19/variants-concern
[44] https://www.nature.com/articles/s41467-021-26803-w
[45] https://www.archbronconeumol.org/es-new-variants-in-sars-cov-2-what-articulo-S030028962200285X
[46] https://www.sciencedirect.com/science/article/pii/S1755436524000665
[47] https://academic.oup.com/ve/article/8/1/veac010/6528444
[48] https://www.sciencedirect.com/science/article/abs/pii/S0013935122001438
[49] https://academic.oup.com/mbe/article/39/2/msac013/6509545
[50] https://www.news-medical.net/news/20220310/Origins-and-evolutions-of-SARS-CoV-2-Alpha-variant-in-the-UK.aspx
[51] https://www.medrxiv.org/content/10.1101/2024.07.01.24309632v1.full-text
[52] https://www.nature.com/articles/s41579-023-00878-2
[53] https://www.nature.com/articles/s41467-023-36449-5
[54] https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2022.1004201/full
[55] https://pubmed.ncbi.nlm.nih.gov/34580736/
[56] https://www.sciencedirect.com/science/article/pii/S120197122030566X
[57] https://emergencies.pubpub.org/pub/pathogen-genomics
[58] https://pubmed.ncbi.nlm.nih.gov/33410223/
[59] https://academic.oup.com/mbe/article/38/5/1777/6030946
[60] https://reflectionsipc.com/2025/01/07/tracking-outbreaks-in-hospitals-can-genomic-surveillance-help/
[61] https://www.thelancet.com/journals/langlo/article/PIIS2214-109X(23)00169-9/fulltext
[62] https://www.science.org/doi/10.1126/science.abe3261
[63] https://www.sciencedirect.com/org/science/article/pii/S2379504224001838
[64] https://www.sciencedirect.com/science/article/pii/S1201971220325571
[65] https://www.nature.com/articles/s41598-021-00267-w
[66] https://pubs.rsc.org/en/content/articlelanding/2021/me/d1me00086a
[67] https://elifesciences.org/articles/65365
[68] https://pmc.ncbi.nlm.nih.gov/articles/PMC7986995/
[69] https://pmc.ncbi.nlm.nih.gov/articles/PMC8158177/
[70] https://gvn.org/covid-19/delta-b-1-617-2/
[71] https://www.nature.com/articles/s41586-020-2895-3
[72] https://www.nature.com/articles/s41586-021-03944-y
[73] https://pmc.ncbi.nlm.nih.gov/articles/PMC8455130/
[74] https://www.nature.com/articles/s41467-020-19808-4
[75] https://dergipark.org.tr/en/pub/jmid/issue/68845/1086226
[76] https://www.nature.com/articles/s41418-021-00846-4
[77] https://pubmed.ncbi.nlm.nih.gov/33243994/
[78] https://pmc.ncbi.nlm.nih.gov/articles/PMC8935235/
[79] https://www.sciencedirect.com/science/article/pii/S2590098621000075
[80] https://www.news-medical.net/health/D614G-Mutation.aspx
[81] https://pmc.ncbi.nlm.nih.gov/articles/PMC9359381/
[82] https://www.thelancet.com/journals/laninf/article/PIIS1473-3099(21)00007-4/fulltext
[83] https://www.sciencedirect.com/science/article/pii/S0006349522009419
[84] https://www.orthoatlanta.com/health-news/when-where-was-the-first-case-of-covid-19
[85] https://www.aa.com.tr/en/asia-pacific/no-sign-covid-spread-in-wuhan-before-dec-2019-who/2138755
[86] https://health.ucsd.edu/news/press-releases/2021-03-18-novel-coronavirus-circulated-undetected-months-before-first-covid-19-cases-in-wuhan-china/
[87] https://en.wikipedia.org/wiki/COVID-19
[88] https://www.who.int/docs/default-source/coronaviruse/situation-reports/20200121-sitrep-1-2019-ncov.pdf
[89] https://pmc.ncbi.nlm.nih.gov/articles/PMC7068164/
[90] https://www.webmd.com/covid/coronavirus-history
[91] https://pmc.ncbi.nlm.nih.gov/articles/PMC7095345/
[92] https://www.cdc.gov/museum/timeline/covid19.html
[93] https://weekly.chinacdc.cn/en/article/doi/10.46234/ccdcw2020.022
[94] https://en.wikipedia.org/wiki/COVID-19_pandemic
[95] https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_2019
[96] https://en.wikipedia.org/wiki/SARS-CoV-2
[97] https://www.gov.uk/government/publications/wuhan-novel-coronavirus-background-information
[98] https://www.who.int/news/item/27-04-2020-who-timeline---covid-19
[99] https://www.nm.org/healthbeat/medical-advances/new-therapies-and-drug-trials/covid-19-pandemic-timeline
[100] https://www.sciencedirect.com/science/article/pii/S2213007120304330
[101] https://www.hzjz.hr/en/dogadaji-en/visualisation-of-sequenced-sars-cov-2-samples-in-croatia/
[102] https://en.wikipedia.org/wiki/List_of_phylogenetic_tree_visualization_software
[103] https://www.auspathogen.org.au/blog/genomics-platform-enables-real-time-surveillance-of-pathogens-nationally
[104] https://www.reddit.com/r/bioinformatics/comments/4zr035/what_is_the_best_visualization_tools_for/
[105] https://krisp.org.za/manuscripts/SARS-CoV-2_Nomenclatur_Nat_Micro.pdf
[106] http://etetoolkit.org/treeview/
[107] https://pubmed.ncbi.nlm.nih.gov/40302215/
[108] https://gisaid.org
[109] https://www.ibri.org.in/blog/phylogenetic-analysis
[110] https://nanoporetech.com/resource-centre/real-time-genomic-surveillance-with-nanopore-sequencing
[111] https://nextstrain.org/ncov/gisaid/global/6m
[112] https://www.geneious.com/features/phylogenetic-tree-building
[113] https://www.solugenomics.com/platform
[114] https://nextstrain.org/ncov/gisaid/reference
[115] https://bcb.unl.edu/yyin/teach/PBB/phylogeny-1.pdf
[116] https://www.frontiersin.org/journals/science/articles/10.3389/fsci.2024.1298248/full
[117] https://twitter.com/nextstrain/status/1247147772555517955
[118] https://www.statista.com/chart/21994/uk-imported-covid-19-origins/
[119] https://pubmed.ncbi.nlm.nih.gov/32265007/
[120] https://www.eurosurveillance.org/content/10.2807/1560-7917.ES.2020.25.13.2000305
[121] https://pmc.ncbi.nlm.nih.gov/articles/PMC7127394/
[122] https://www.nature.com/articles/s41586-021-03677-y
[123] https://cov-lineages.org/global_report_B.1.1.7.html
[124] https://researchportal.ukhsa.gov.uk/files/24650715/Holden2020COVID_19PublicHealthManagementOfTheFirstTwoEpidemiolInfect.pdf
[125] https://academic.oup.com/ve/article/11/1/veaf004/7984523
[126] https://pubmed.ncbi.nlm.nih.gov/33349681/
[127] https://www.nottingham.ac.uk/news/missed-covid-cases
[128] https://www.thelancet.com/journals/lanam/article/PIIS2667-193X(21)00010-7/fulltext
