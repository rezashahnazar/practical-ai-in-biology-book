[← مقدمه فصل دوم](./00-introduction.md) | [بخش ۲-۲: یادگیری با معلم: یادگیری تحت نظارت (Supervised Learning) →](./02-supervised-learning.md)

# فصل ۲: ماشین چگونه یاد می‌گیرد؟

## بخش ۲-۱: از مغز انسان تا مغز مصنوعی: سفری به دنیای شبکه‌های عصبی

مغز انسان، پیچیده‌ترین ساختار شناخته‌شده در جهان، چگونه از میلیاردها سلول ساده به نام نرون، قابلیت‌های شگفت‌انگیزی مانند یادگیری، تشخیص چهره و خلاقیت را به وجود می‌آورد؟ آیا می‌توانیم با الهام از این شاهکار طبیعت، یک "مغز مصنوعی" بسازیم که به کامپیوترها قدرت یادگیری بدهد؟ در این بخش، به قلب هوش مصنوعی مدرن سفر می‌کنیم.

در فصل اول، دیدیم که هوش مصنوعی می‌تواند کارهای شگفت‌انگیزی مانند تشخیص سرطان و تحلیل داده‌های ژنومی را انجام دهد. اما سوال اصلی این است: یک ماشین چگونه "فکر" می‌کند؟ چگونه یاد می‌گیرد که الگوها را تشخیص دهد؟ پاسخ در یکی از زیباترین ایده‌های مهندسی نهفته است که از خود طبیعت الهام گرفته شده: **شبکه‌های عصبی مصنوعی (Artificial Neural Networks)**.

### 🎯 مسئله محوری این بخش:

فرض کنید باید ماشینی ساده بسازید که بتواند دایره را از مربع تشخیص دهد. شما نمی‌توانید از قوانین ثابت (مثلاً «اگر ۴ گوشه داشت، مربع است») استفاده کنید؛ ماشین باید خودش از روی مثال‌ها یاد بگیرد. به نظر شما، اجزای حداقلی برای ساخت یک «سلول» یادگیرنده چه چیزهایی هستند؟ این سلول چگونه اطلاعات (تصویر) را پردازش کرده و به یک تصمیم می‌رسد؟

### **الهام از یک شاهکار بیولوژیک: مغز**

مغز شما از **حدود ۸۶ میلیارد** سلول تخصصی به نام **نرون** تشکیل شده است[1][2][3]. هر نرون به تنهایی یک واحد پردازشی بسیار ساده است. اما وقتی این میلیاردها نرون از طریق اتصالات پیچیده‌ای به نام **سیناپس** با یکدیگر ارتباط برقرار می‌کنند، یک سیستم فوق‌العاده قدرتمند برای یادگیری، تحلیل و تصمیم‌گیری به وجود می‌آید[4].

وقتی شما چهره دوستتان را در یک جمعیت شلوغ تشخیص می‌دهید، این فرآیند در مغز شما چگونه رخ می‌دهد؟

1. **ورودی (Input):** نور از چهره دوستتان به چشمان شما می‌رسد و سلول‌های شبکیه آن را به سیگنال‌های الکتریکی تبدیل می‌کنند[5].

2. **پردازش (Processing):** این سیگنال‌ها از طریق عصب بینایی به مغز شما سفر می‌کنند[6]. در آنجا، لایه‌های مختلفی از نرون‌ها به صورت سلسله‌مراتبی این اطلاعات را پردازش می‌کنند[7]. یک لایه ممکن است خطوط و لبه‌های ساده را تشخیص دهد. لایه بعدی این خطوط را با هم ترکیب کرده و شکل‌هایی مانند چشم و بینی را شناسایی می‌کند. لایه بالاتر، این اَشکال را با هم ترکیب کرده و در نهایت چهره کامل را بازشناسی می‌کند.

3. **خروجی (Output):** پس از این پردازش چندلایه‌ای، مغز شما به یک نتیجه می‌رسد: "بله، این دوست من است!" و یک سیگنال برای شما ارسال می‌کند تا برایش دست تکان دهید[8].

### **ساخت یک مغز ساده: نرون مصنوعی**

حالا بیایید این ایده را به زبان ریاضی و کامپیوتر ترجمه کنیم. یک **نرون مصنوعی** یا **گره (Node)** یک واحد محاسباتی ساده است که سعی می‌کند از یک نرون بیولوژیک تقلید کند[9][10].

```mermaid
flowchart TD
    %% Style Definitions
    classDef phase fill:#f8f9fa,stroke:#2c3e50,stroke-width:1.5px,color:#2c3e50
    classDef input fill:#e1f5fe,stroke:#01579b,stroke-width:1px,color:#01579b
    classDef process fill:#e6f2e6,stroke:#2e7d32,stroke-width:1px,color:#2e7d32
    classDef output fill:#f3e8f7,stroke:#6a1b9a,stroke-width:1px,color:#6a1b9a

    %% Biological vs Artificial Neuron Comparison
    subgraph Biological [" "]
        direction TB
        A["نرون بیولوژیک"]
        Dendrite["دندریت‌ها<br>ورودی"]
        Soma["سوما<br>پردازشگر"]
        Axon["آکسون<br>خروجی"]
    end

    subgraph Artificial [" "]
        direction TB
        B["نرون مصنوعی"]
        Input["ورودی‌ها"]
        Node["گره<br>پردازشگر"]
        Output["خروجی"]
    end

    %% Biological Neuron Connections
    Dendrite -->|"انتقال سیگنال"| Soma
    Soma -->|"انتقال سیگنال"| Axon

    %% Artificial Neuron Connections
    Input -->|"انتقال داده"| Node
    Node -->|"انتقال داده"| Output

    %% Apply Styles
    class Biological,Artificial phase
    class Dendrite,Input input
    class Soma,Node process
    class Axon,Output output

    %% Additional Styling for Rounded Shapes and Spacing
    style Biological fill:#f8f9fa,stroke:#2c3e50,stroke-width:1.5px
    style Artificial fill:#f8f9fa,stroke:#2c3e50,stroke-width:1.5px
    linkStyle default stroke:#6c757d,stroke-width:1.2px
```

همانطور که در نمودار می‌بینید:

- **ورودی‌ها (Inputs):** مانند دندریت‌ها، اطلاعات را دریافت می‌کنند[11][6]. در مثال تشخیص سرطان، این ورودی‌ها می‌توانند مقادیر پیکسل‌های مختلف یک تصویر ماموگرافی باشند[12][13].

- **گره (Node):** مانند سوما (جسم سلولی)، یک محاسبه ساده روی ورودی‌ها انجام می‌دهد[14][15]. این گره، هر ورودی را در یک "وزن" (Weight) ضرب می‌کند. این وزن‌ها اهمیت هر ورودی را مشخص می‌کنند (درست مانند اینکه برخی سیناپس‌ها قوی‌تر از بقیه هستند)[5][16]. سپس تمام این مقادیر وزن‌دار را با هم جمع کرده و از یک **تابع فعال‌سازی (Activation Function)** عبور می‌دهد[14][17].

- **خروجی (Output):** مانند آکسون، نتیجه نهایی را به گره‌های بعدی ارسال می‌کند[11][6]. تابع فعال‌سازی تصمیم می‌گیرد که آیا سیگنال باید به لایه بعد منتقل شود یا نه (شبیه به پتانسیل عمل در نرون واقعی)[8].

### **شبکه عصبی: قدرت در همکاری**

یک نرون به تنهایی قدرت چندانی ندارد[18]. جادو زمانی اتفاق می‌افتد که ما هزاران یا میلیون‌ها از این نرون‌های مصنوعی را در لایه‌های مختلف به هم متصل کنیم و یک **شبکه عصبی مصنوعی** بسازیم[19][20].

یک شبکه عصبی ساده معمولاً سه نوع لایه دارد[20][21]:

```mermaid
flowchart TD
    %% Style Definitions
    classDef phase fill:#f8f9fa,stroke:#2c3e50,stroke-width:1.5px,color:#2c3e50
    classDef input fill:#e1f5fe,stroke:#01579b,stroke-width:1px,color:#01579b
    classDef hidden fill:#e6f2e6,stroke:#2e7d32,stroke-width:1px,color:#2e7d32
    classDef output fill:#f3e8f7,stroke:#6a1b9a,stroke-width:1px,color:#6a1b9a

    %% Artificial Neural Network Architecture
    subgraph ANN ["شبکه عصبی مصنوعی"]
        direction TB

        %% Input Layer
        subgraph InputLayer ["لایه ورودی"]
            I1["ورودی ۱<br>پیکسل ۱"]
            I2["ورودی ۲<br>پیکسل ۲"]
            I3["..."]
        end

        %% Hidden Layer
        subgraph HiddenLayer ["لایه پنهان"]
            H1["نرون H1"]
            H2["نرون H2"]
            H3["نرون H3"]
        end

        %% Output Layer
        subgraph OutputLayer ["لایه خروجی"]
            O1["خروجی ۱<br>احتمال 'سرطان'"]
            O2["خروجی ۲<br>احتمال 'سالم'"]
        end
    end

    %% Input to Hidden Layer Connections
    I1 --> H1
    I1 --> H2
    I1 --> H3
    I2 --> H1
    I2 --> H2
    I2 --> H3
    I3 --> H1
    I3 --> H2
    I3 --> H3

    %% Hidden to Output Layer Connections
    H1 --> O1
    H1 --> O2
    H2 --> O1
    H2 --> O2
    H3 --> O1
    H3 --> O2

    %% Apply Styles
    class ANN,InputLayer,HiddenLayer,OutputLayer phase
    class I1,I2,I3 input
    class H1,H2,H3 hidden
    class O1,O2 output

    %% Additional Styling for Rounded Shapes and Spacing
    style ANN fill:#f8f9fa,stroke:#2c3e50,stroke-width:1.5px
    linkStyle default stroke:#6c757d,stroke-width:1.2px
```

1. **لایه ورودی (Input Layer):** این لایه داده‌های خام را دریافت می‌کند[20][22]. برای یک تصویر، هر نرون در این لایه می‌تواند معرف یک پیکسل از تصویر باشد[18][23].

2. **لایه‌های پنهان (Hidden Layers):** این‌ها لایه‌های میانی هستند که پردازش اصلی در آن‌ها انجام می‌شود[24][20]. مانند مغز، این لایه‌ها ویژگی‌های پیچیده‌تر را به صورت سلسله‌مراتبی استخراج می‌کنند[25]. لایه پنهان اول ممکن است لبه‌ها و رنگ‌ها را یاد بگیرد، لایه دوم ممکن است بافت‌ها و اَشکال ساده را تشخیص دهد و لایه‌های بعدی این‌ها را برای شناسایی مفاهیم پیچیده‌تر (مانند یک تومور) ترکیب می‌کنند[26][27]. هرچه تعداد لایه‌های پنهان بیشتر باشد، به آن **یادگیری عمیق (Deep Learning)** می‌گویند[28][29].

3. **لایه خروجی (Output Layer):** این لایه نتیجه نهایی را ارائه می‌دهد[20]. برای مثال، می‌تواند دو نرون داشته باشد: یکی احتمال وجود سرطان و دیگری احتمال سالم بودن بافت را نشان می‌دهد[15][18].

### 🔬 تمرین تحلیلی: طراحی یک نرون تصمیم‌گیر

**سناریو:** می‌خواهیم یک نرون مصنوعی ساده طراحی کنیم که تصمیم بگیرد آیا یک سلول باید تقسیم شود یا خیر. این تصمیم بر اساس دو سیگنال ورودی است:

- **ورودی ۱ (فاکتور رشد):** اگر وجود داشته باشد ۱، وگرنه ۰.
- **ورودی ۲ (مهار تماسی):** اگر وجود داشته باشد ۱، وگرنه ۰.

**هدف:** شما باید وزن‌های w1 (برای فاکتور رشد) و w2 (برای مهار تماسی) را طوری تعیین کنید که نرون فقط زمانی فعال (خروجی > ۰) شود که سیگنال رشد وجود داشته باشد و همزمان سیگنال مهار وجود نداشته باشد.
(فرض کنید نرون زمانی فعال می‌شود که: `(ورودی۱ * w1) + (ورودی۲ * w2) > 0`)

**پاسخ:** بر اساس تحلیل ریاضی، مقادیر مناسب برای وزن‌ها عبارتند از:

- **w1 = 1, w2 = -1** (یا هر مقدار مثبت برای w1 و منفی برای w2 که |w2| ≥ |w1|)
- **w1 = 1, w2 = -2** (حل دیگر مناسب)

این وزن‌ها تضمین می‌کنند که نرون فقط زمانی فعال شود که فاکتور رشد وجود داشته باشد (x1=1) و مهار تماسی وجود نداشته باشد (x2=0).

### 💡 نکات کلیدی این بخش

- **الهام از طبیعت:** شبکه‌های عصبی مصنوعی از ساختار مغز انسان (نرون‌ها و سیناپس‌ها) الهام گرفته‌اند[30][10][31].

- **واحد پایه:** یک نرون مصنوعی یک واحد محاسباتی ساده است که ورودی‌های وزن‌دار را دریافت کرده و یک خروجی تولید می‌کند[9][14].

- **قدرت در شبکه:** قدرت اصلی شبکه‌های عصبی در اتصال تعداد زیادی از این نرون‌های ساده در لایه‌های مختلف به یکدیگر است[15][18].

- **یادگیری عمیق:** به شبکه‌های عصبی‌ای گفته می‌شود که دارای لایه‌های پنهان متعدد هستند و قابلیت یادگیری الگوهای بسیار پیچیده را دارند[28][32].

"یادگیری" در یک شبکه عصبی، در واقع فرآیند تنظیم دقیق **وزن‌ها (Weights)** در تمام اتصالات بین نرون‌هاست[33][34]. این فرآیند از طریق الگوریتم‌هایی مانند **انتشار معکوس (Backpropagation)** و **گرادیان کاهشی (Gradient Descent)** انجام می‌شود[35][36]. در بخش بعدی، خواهیم دید که ماشین چگونه با استفاده از داده‌ها، این وزن‌ها را به گونه‌ای تنظیم می‌کند که بهترین تصمیم‌ها را بگیرد[37][38].

[1] https://www.brainfacts.org/in-the-lab/meet-the-researcher/2018/how-many-neurons-are-in-the-brain-120418
[2] https://www.nature.com/scitable/blog/brain-metrics/are_there_really_as_many/
[3] https://pmc.ncbi.nlm.nih.gov/articles/PMC2776484/
[4] https://hms.harvard.edu/news/new-field-neuroscience-aims-map-connections-brain
[5] https://www.healthline.com/health/neurons
[6] https://www.khanacademy.org/science/biology/human-biology/neuron-nervous-system/a/overview-of-neuron-structure-and-function
[7] https://www.nature.com/articles/s41598-022-24813-2
[8] https://qbi.uq.edu.au/brain-basics/brain/brain-physiology/action-potentials-and-synapses
[9] https://en.wikipedia.org/wiki/Artificial_neuron
[10] https://news.mit.edu/2017/explained-neural-networks-deep-learning-0414
[11] https://study.com/learn/lesson/what-is-an-axon-terminal-function-types.html
[12] https://health.google/caregivers/mammography/
[13] https://pubs.rsna.org/doi/full/10.1148/radiol.232479
[14] https://www.philadelphia.edu.jo/academics/qhamarsheh/uploads/Lecture%202%20%20-%20Components%20of%20ANN%20and%20MATLAB%20representation.pdf
[15] https://www.geeksforgeeks.org/artificial-neural-networks-and-its-applications/
[16] https://en.wikipedia.org/wiki/Synapse
[17] https://www.geeksforgeeks.org/activation-functions/
[18] https://www.enjoyalgorithms.com/blog/components-of-ann/
[19] https://en.wikipedia.org/wiki/Layer_(deep_learning)
[20] https://www.geeksforgeeks.org/layers-in-artificial-neural-networks-ann/
[21] https://www.coursera.org/articles/what-is-deep-learning
[22] https://www.linkedin.com/learning/artificial-intelligence-foundations-neural-networks-22853427/layers-input-hidden-and-output
[23] https://www.codecademy.com/article/understanding-neural-networks-and-their-components
[24] https://www.coursera.org/articles/hidden-layer-neural-network
[25] https://gwcet.ac.in/uploaded_files/DL-UNIT_1.pdf
[26] https://www.oaepublish.com/articles/ais.2021.15
[27] https://www.nature.com/articles/s41746-020-00376-2
[28] https://en.wikipedia.org/wiki/Deep_learning
[29] https://www.geeksforgeeks.org/introduction-deep-learning/
[30] https://www.linkedin.com/pulse/neural-networks-from-biological-inspiration-hazome-hayashi-msc-cqf-4zjxf
[31] https://en.wikipedia.org/wiki/History_of_artificial_neural_networks
[32] https://www.ibm.com/think/topics/deep-learning
[33] https://www.geeksforgeeks.org/machine-learning/backpropagation-in-neural-network/
[34] https://www.ibm.com/think/topics/backpropagation
[35] https://www.ibm.com/think/topics/gradient-descent
[36] https://www.geeksforgeeks.org/gradient-descent-algorithm-and-its-variants/
[37] https://www.sap.com/products/artificial-intelligence/what-is-machine-learning.html
[38] https://www.coursera.org/articles/what-is-machine-learning
[39] https://www.geeksforgeeks.org/deep-learning/implementing-models-of-artificial-neural-network/
[40] https://www.kdnuggets.com/a-brief-history-of-the-neural-networks
[41] https://jqub.ece.gmu.edu/2022/09/01/ML4Emb22F/Reading/W1/Lec1_Reading.pdf
[42] https://www.cse.iitm.ac.in/~miteshk/CS7015/Slides/Handout/Lecture2.pdf
[43] https://cs.stanford.edu/people/eroberts/courses/soco/projects/neural-networks/History/history1.html
[44] https://en.wikipedia.org/wiki/Perceptron
[45] https://en.wikipedia.org/wiki/Neural_network_(biology)
[46] https://home.csulb.edu/~cwallis/artificialn/History.htm
[47] https://objectivegroup.com/insights/artificial-neurons-structure-operation-and-practical-applications/
[48] https://cpic-sistemas.or.cr/revista/index.php/technology-inside/article/download/36/27/51
[49] https://towardsdatascience.com/the-complete-interesting-and-convoluted-history-of-neural-networks-2764a54e9e76/
[50] https://collab.dvb.bayern/x/oq8eB
[51] https://openbooks.lib.msu.edu/neuroscience/chapter/synapse-structure/
[52] https://pubmed.ncbi.nlm.nih.gov/39602822/
[53] https://byjus.com/biology/neurons/
[54] https://www.youtube.com/watch?v=i-XwPjN3ZtI
[55] https://academic.oup.com/brain/article/148/3/689/7909879
[56] https://en.wikipedia.org/wiki/Neuron
[57] https://psych.athabascau.ca/html/Psych289/Biotutorials/1/synapse.shtml
[58] https://en.wikipedia.org/wiki/List_of_animals_by_number_of_neurons
[59] https://www.youtube.com/watch?v=6qS83wD29PY
[60] https://dana.org/resources/neurotransmission-the-synapse/
[61] https://www.dataversity.net/brief-history-deep-learning/
[62] https://www.learnbymarketing.com/methods/neural-networks/
[63] https://builtin.com/machine-learning/relu-activation-function
[64] https://www.nomidl.com/deep-learning/what-is-relu-and-sigmoid-activation-function/
[65] https://wandb.ai/ayush-thakur/dl-question-bank/reports/ReLU-vs-Sigmoid-Function-in-Deep-Neural-Networks--VmlldzoyMDk0MzI
[66] https://developers.google.com/machine-learning/crash-course/neural-networks/nodes-hidden-layers
[67] https://www.shiksha.com/online-courses/articles/relu-and-sigmoid-activation-function/
[68] https://en.wikipedia.org/wiki/Neural_network_(machine_learning)
[69] https://www.geeksforgeeks.org/machine-learning/activation-functions-neural-networks/
[70] https://www.ibm.com/think/topics/neural-networks
[71] https://www.wesleymc.com/healthy-living/blog/artificial-intelligence-for-cancer-detection-and-treatment-planning
[72] https://lumenalta.com/insights/15-computer-vision-applications-in-healthcare
[73] https://news.harvard.edu/gazette/story/2024/09/new-ai-tool-can-diagnose-cancer-guide-treatment-predict-patient-survival/
[74] https://pmc.ncbi.nlm.nih.gov/articles/PMC8946688/
[75] https://www.thelancet.com/journals/landig/article/PIIS2589-7500(23)00153-X/fulltext
[76] https://pubmed.ncbi.nlm.nih.gov/37796946/
[77] https://www.nature.com/articles/s41467-025-57469-3
[78] https://sigma.software/about/media/revolutionizing-medical-imaging-with-computer-vision
[79] https://www.cancer.gov/research/infrastructure/artificial-intelligence
[80] https://www.komen.org/blog/ai-assisted-mammogram/
[81] https://viso.ai/applications/computer-vision-in-healthcare/
[82] https://www.sciencedirect.com/science/article/abs/pii/S0010482523008211
[83] https://www.nature.com/articles/s41591-024-03408-6
[84] https://premioinc.com/blogs/blog/what-is-computer-vision-for-medical-imaging
[85] https://www.cancerresearch.org/blog/ai-cancer
[86] https://myebcdmammo.com
[87] https://www.spiceworks.com/tech/artificial-intelligence/articles/what-is-ml/
[88] https://towardsdatascience.com/neural-networks-backpropagation-by-dr-lihi-gur-arie-27be67d8fdce/
[89] https://en.wikipedia.org/wiki/Gradient_descent
[90] https://www.geeksforgeeks.org/machine-learning/machine-learning/
[91] https://en.wikipedia.org/wiki/Backpropagation
[92] https://builtin.com/data-science/gradient-descent
[93] https://www.iso.org/artificial-intelligence/machine-learning
[94] https://www.linkedin.com/pulse/understanding-backpropagation-neural-networks-beginners-monirul-islam-b4tbc
[95] https://www.digitalocean.com/community/tutorials/intro-to-optimization-in-deep-learning-gradient-descent
[96] https://ai.engineering.columbia.edu/ai-vs-machine-learning/
[97] https://neptune.ai/blog/backpropagation-algorithm-in-neural-networks-guide
[98] https://www.ruder.io/optimizing-gradient-descent/
[99] https://www.ibm.com/think/topics/machine-learning
[100] https://drive.uqu.edu.sa/_/takawady/files/NeuralNetworks.pdf
