## Survey
google "language detection corpus" to find more
### CMU Survey & corpus
[CMU Language Identification Notes!](http://www.cs.cmu.edu/~ralf/langid.html)  
[Automatic Language Identification in Texts: A Survey](https://arxiv.org/pdf/1804.08186)

### some refs
[Microsoft Azure solution](https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/how-tos/text-analytics-how-to-language-detection)  
[Tencent API](https://ai.qq.com/doc/textdetect.shtml)  
[ALI Language info](https://docs.alipay.com/l10ncenter/vv5u7s/cf8xxu)  
[基于NGram的文本语种识别研究(PDF download)](http://manu44.magtech.com.cn/Jwk_infotech_wk3/CN/article/downloadArticleFile.do?attachType=PDF&id=3723)


[科大讯飞语种识别系统介绍(ppt)](https://wenku.baidu.com/view/295969896137ee06eff918a0.html)  
[各种数据集(不太相关)](https://zhuanlan.zhihu.com/p/35455475)
### [zhihu](https://www.zhihu.com/question/20295339/answer/166999178)
- D. Imseng, H. Bourlard, and M. Magimai-Doss, “Towards mixed language speech recognition systems.,” in INTERSPEECH, pp. 278–281, 2010
- C.-H. Wu, Y.-H. Chiu, C.-J. Shia, and C.-Y. Lin, “Automatic segmentation and identification of mixed-language speech using delta-bic and lsa-based gmms,” Audio, Speech, and Language Processing, IEEE Transactions on,
 vol. 14, no. 1, pp. 266–276, 2006
 - H. Lin, L. Deng, D. Yu, Y.-f. Gong, A. Acero, and C.-H. Lee, “A study on multilingual acoustic modeling for large vocabulary asr,” in Acoustics, Speech and Signal Processing, 2009. ICASSP 2009. IEEE International Conference on, pp. 4333–4336, IEEE, 2009.
 
### [langid](https://github.com/saffsd/langid.py)

a standalone Language Identification (LangID) tool.

- [1] Lui, Marco and Timothy Baldwin (2011) Cross-domain Feature Selection for Language Identification, In Proceedings of the Fifth International Joint Conference on Natural Language Processing (IJCNLP 2011), Chiang Mai, Thailand, pp. 553—561. Available from http://www.aclweb.org/anthology/I11-1062

- [2] Lui, Marco and Timothy Baldwin (2012) langid.py: An Off-the-shelf Language Identification Tool, In Proceedings of the 50th Annual Meeting of the Association for Computational Linguistics (ACL 2012), Demo Session, Jeju, Republic of Korea. Available from www.aclweb.org/anthology/P12-3005

- [3] Kenneth Heafield and Rohan Kshirsagar and Santiago Barona (2015) Language Identification and Modeling in Specialized Hardware, In Proceedings of the 53rd Annual Meeting of the Association for Computational Linguistics and the 7th International Joint Conference on Natural Language Processing (Volume 2: Short Papers). Available from http://aclweb.org/anthology/P15-2063

```
[1]Marco Lui 安定Timothy Baldwin, langid.py: An Off-the-shelf Language Identification Tool.

[2] Andrew McCallum, Kamal Nigam, AComparison of Event Models for Naive Bayes Text Classification

[3] Marco Lui and Timothy Baldwin, Cross-domainFeature Selection for Language Identification

[4] William B. Cavnar and John M. Trenkle, N-Gram-BasedText Categorization

[5] Timothy Baldwin and Marco Lui, LanguageIdentification: The Long and the Short of the Matter

```
### [用Java进行语种识别(blog)](http://www.meilongkui.com/archives/431)

- [language-detector(github)](https://github.com/optimaize/language-detector)  
- [another github project](https://github.com/shuyo/language-detection)



## corpora
[ref paper: (2017)Evaluation of language identification methods using 285 languages](https://www.ep.liu.se/ecp/131/021/ecp17131021.pdf)
- [wikipedias](https://www.wikipedia.org/)
- [bible translations](http://gospelgo.com/biblespage.html)
- [some religious texts](https://www.lds.org/?lang=eng)
- [UDHR(FOR TEST)](http://www.unicode.org/udhr/)
- [Tatoeba(sentence translation system)(for test)](https://tatoeba.org/eng/)
- 
other  
[LID Tutorial](http://alias-i.com/lingpipe/demos/tutorial/langid/read-me.html)
- [Leipzig collection(252 Languages)](http://corpora.uni-leipzig.de/en?corpusId=zho-simp_news_2010)
- [Language of the world](https://www.ethnologue.com/browse/names/c)
- 

## paper
- [paper: Language Identification on the web](https://radimrehurek.com/cicling09.pdf)
- [paper: NLI using corpus-based models(traditional method)](https://tidsskrift.dk/her/article/view/25083/22006)
- [paper: Automatic Language Identification: Unsupervised approach](http://www.tmrfindia.org/ijcsa/v7i16.pdf)

- [paper: (2014)A Survey of Language Identification Techniques and Applications](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.689.5252&rep=rep1&type=pdf)


## support
- [beautiful soup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/)
- 

## compute trick
- [log probability](https://en.wikipedia.org/wiki/Log_probability)
- [exp norm](https://timvieira.github.io/blog/post/2014/02/11/exp-normalize-trick/)



## Open-source proect to C#
- [a language detection project](https://blog.csdn.net/chndata/article/details/44835071)
- [google lanuage-detection github(Java)](https://code.google.com/archive/p/language-detection/)

- [a c# solution](https://download.csdn.net/download/snngimfk/5146257)
- 


- [language detector class C#(code download)](http://idsyst.hu/development/language_detector.html)
- 

- [google's language detection API of C#](https://codelabs.developers.google.com/codelabs/cloud-translation-csharp/index.html?index=..%2F..index#7)
- 
- [langid(github)](https://github.com/saffsd/langid.py)


## langid-python
---

# langid [python](https://github.com/saffsd/langid.py)
- PAPER
    - [01](http://www.aclweb.org/anthology/I11-1062)
    - [02](www.aclweb.org/anthology/P12-3005)
    - [03](http://aclweb.org/anthology/P15-2063)

- where it comes frm
```python
  # output the model
  output_path = os.path.join(model_dir, 'model')
  model = nb_ptc, nb_pc, nb_classes, tk_nextmove, tk_output
  # compress and encode here
  string = base64.b64encode(bz2.compress(cPickle.dumps(model)))
  with open(output_path, 'w') as f:
    f.write(string)
  print "wrote model to %s (%d bytes)" % (output_path, len(string))
```

## python 方法解读
- base64[..](https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001399413803339f4bbda5c01fc479cbea98b1387390748000)  
用记事本打开`exe`、`jpg`、`pdf`这些文件时，我们都会看到一大堆乱码，因为二进制文件包含很多无法显示和打印的字符，所以，如果要让记事本这样的文本处理软件能处理二进制数据，就需要一个`二进制`到`字符串`的转换方法。Base64是一种最常见的`二进制编码`方法。
    ```python
    >>> import base64
    >>> base64.b64encode('binary\x00string')
    'YmluYXJ5AHN0cmluZw=='
    >>> base64.b64decode('YmluYXJ5AHN0cmluZw==')
    'binary\x00string'
    ```
- bz2  
Decompress data (a `bytes-like object`), returning `uncompressed data as bytes`. Some of data may be buffered internally, for use in later calls to decompress(). The returned data should be concatenated with the output of any previous calls to decompress().

## C# 二进制读写
- C# 二进制读写
```csharp
// 写
FileStream fs = new FileStream(sFileName, FileMode.OpenOrCreate);
BinaryWriter binWriter = new BinaryWriter(fs);

binWriter.Write(labelContent, 0, labelContent.Length);

binWriter.Close();

//读
byte[] bBuffer;

FileStream fs = new FileStream(sFileName, FileMode.Open);
BinaryReader binReader = new BinaryReader(fs);

bBuffer = new byte[fs.Length];
binReader.Read(bBuffer, 0, (int)fs.Length);

binReader.Close();
fs.close()
```
- c#文件读写[..](http://www.runoob.com/csharp/csharp-binary-files.html)
```csharp
using System;
using System.IO;

namespace BinaryFileApplication
{
    class Program
    {
        static void Main(string[] args)
        {
            BinaryWriter bw;
            BinaryReader br;
            int i = 25;
            double d = 3.14157;
            bool b = true;
            string s = "I am happy";
            // 创建文件
            try
            {
                bw = new BinaryWriter(new FileStream("mydata",
                FileMode.Create));
            }
            catch (IOException e)
            {
                Console.WriteLine(e.Message + "\n Cannot create file.");
                return;
            }
            // 写入文件
            try
            {
                bw.Write(i);
                bw.Write(d);
                bw.Write(b);
                bw.Write(s);
            }
            catch (IOException e)
            {
                Console.WriteLine(e.Message + "\n Cannot write to file.");
                return;
            }

            bw.Close();
            // 读取文件
            try
            {
                br = new BinaryReader(new FileStream("mydata",
                FileMode.Open));
            }
            catch (IOException e)
            {
                Console.WriteLine(e.Message + "\n Cannot open file.");
                return;
            }
            try
            {
                i = br.ReadInt32();
                Console.WriteLine("Integer data: {0}", i);
                d = br.ReadDouble();
                Console.WriteLine("Double data: {0}", d);
                b = br.ReadBoolean();
                Console.WriteLine("Boolean data: {0}", b);
                s = br.ReadString();
                Console.WriteLine("String data: {0}", s);
            }
            catch (IOException e)
            {
                Console.WriteLine(e.Message + "\n Cannot read from file.");
                return;
            }
            br.Close();
            Console.ReadKey();
        }
    }
}
```
















```python
#!/usr/bin/env python

from __future__ import print_function
import base64
import bz2
import sys
import logging
import numpy as np
from collections import defaultdict
from pre_model import pretrain_model
from pickle import loads

FORCE_WSGIREF = False
NORM_PROBS = False  # Normalize output probabilities.


logger = logging.getLogger(__name__)

# Convenience methods defined below will initialize this when first called.
identifier = None

model = pretrain_model


def classify(instance):
    global identifier
    if identifier is None:
        load_model()

    return identifier.classify(instance)


def load_model(path=None):
    global identifier
    logger.info('initializing identifier')
    if path is None:
        identifier = LanguageIdentifier.from_modelstring(model)


class LanguageIdentifier(object):
    @classmethod
    def from_modelstring(cls, string, *args, **kwargs):
        b = base64.b64decode(string)
        z = bz2.decompress(b)
        model = loads(z)
        nb_ptc, nb_pc, nb_classes, tk_nextmove, tk_output = model
        # print(nb_ptc,nb_pc,nb_classes,tk_nextmove,tk_output)
        nb_numfeats = int(len(nb_ptc) / len(nb_pc))

        # reconstruct pc and ptc
        nb_pc = np.array(nb_pc)
        nb_ptc = np.array(nb_ptc).reshape(nb_numfeats, len(nb_pc))

        return cls(nb_ptc, nb_pc, nb_numfeats, nb_classes, tk_nextmove, tk_output, *args, **kwargs)

    @classmethod
    def from_modelpath(cls, path, *args, **kwargs):
        with open(path) as f:
            return cls.from_modelstring(f.read().encode(), *args, **kwargs)

    def __init__(self, nb_ptc, nb_pc, nb_numfeats, nb_classes, tk_nextmove, tk_output,
                 norm_probs=NORM_PROBS):
        self.nb_ptc = nb_ptc
        self.nb_pc = nb_pc
        self.nb_numfeats = nb_numfeats
        self.nb_classes = nb_classes
        self.tk_nextmove = tk_nextmove
        self.tk_output = tk_output

        if norm_probs:
            def norm_probs(pd):
                with np.errstate(over='ignore'):
                    pd_exp = np.exp(pd)
                    pd = pd_exp / pd_exp.sum()
                return pd
        else:
            def norm_probs(pd):
                return pd

        self.norm_probs = norm_probs

        # Maintain a reference to the full model, in case we change our language set
        # multiple times.
        self.__full_model = nb_ptc, nb_pc, nb_classes

    def instance2fv(self, text):
        """
        Map an instance into the feature space of the trained model.
        """
        if (sys.version_info > (3, 0)):
            if isinstance(text, str):
                text = text.encode('utf8')

        arr = np.zeros((self.nb_numfeats,), dtype='uint32')

        # Count the number of times we enter each state
        state = 0
        statecount = defaultdict(int)
        for letter in text:
            state = self.tk_nextmove[(state << 8) + letter]
            statecount[state] += 1

        # Update all the productions corresponding to the state
        for state in statecount:
            for index in self.tk_output.get(state, []):
                arr[index] += statecount[state]

        return arr

    def nb_classprobs(self, fv):
        # compute the partial log-probability of the document given each class
        pdc = np.dot(fv, self.nb_ptc)
        # compute the partial log-probability of the document in each class
        pd = pdc + self.nb_pc
        return pd

    def classify(self, text):
        """
        Classify an instance.
        """
        fv = self.instance2fv(text)
        probs = self.norm_probs(self.nb_classprobs(fv))
        cl = np.argmax(probs)
        conf = float(probs[cl])
        pred = str(self.nb_classes[cl])
        return pred, conf
```



## keyboard

1. `~` 波浪号`tilde`，源于西班牙语和葡语中的发音符号。

2. `!` 感叹号`exclamation mark/exclamation point/bang`，无需多解释，在这个 “咆哮体”盛行的时代，想不懂这个都难。

3. `#`汉语中因形似“井”，通常读作井号，真正的含义是数字符号(Number sign)，如在一些国家‘#1’代表No.1的意思。在美式英语中一般称作`pound sign`，电话上的“#”叫做`pound key`，而加拿大英语则称之为`number sign key`；北美以外的其他英语国家一般称“#”为`hash`，相应的电话键叫做`hash key`。注意：数字符号（#）极易和乐谱中的升音符（? 读作sharp）相混淆。但是，乐谱的sharp和数字符号的字形不完全一样。标准数字符号(#)横线水平，而竖线向右倾斜；而乐谱的升号（?）为了在五线谱中容易识别，横线改为斜向上但竖线垂直。我猜此时有人就会举出一个极好的反例来否定上述说法，那就是C#（C Sharp）。的确，乍一看确实不相符！但事实上，C#并不违背上述结论，C Sharp中符号Sharp的创意正是来源于升音符?在乐谱中的含义——紧跟其后的音符的音高比实际标定的高半音，表示技术进一步提升之意（要不直接把C#本土化，翻译成“C优”算了^_^，这个命名方法有点类似于C++中“++”表示变量增1）。由于“?”在计算机显示、输入中不方便，因此在书写体中用“#”代替“?”，但读音保持不变。于是就出现了书写成“C#”但念作“C Sharp”的情形，了解渊源之后发现其实并不矛盾。

4. `\$` `dollar/peso sign`，我们通常把这个当作美元（USD）的符号，但拉丁美洲一些国家的人们会认为“$” 代表比索（peso），所以，不引起误解，最好用“US$”代表美元。这个符号的起源还存在争议，其中有一种说法是这样的：在18世纪末，货币单位比索的手写缩写符号是“ps”，随着时间推移，p和s感情渐进、关系日益密切，最后重叠在一起形成了现在的“$”。

5. `%` 百分号，`percent sign`。

6. `^` a读`caret`，表示间距符 “^ ”或 “?”，也称作`wedge, up-arrow, hat`，数学中通常叫做`hat`；b读circumflex (^)，是发音符号，常见用法如?。

7. `&` `ampersand/and`，单词“and”的简写形式。

8. `*` `asterisk/star`，计算机和数学中称作“star”更常见。

9. `()` `round brackets/open bracket`s; `[ ]` `square brackets/closed brackets`; `{ }` `curly brackets/definite brackets`; `< >` `angle brackets/triangular brackets`，除了用作尖括号，也用作不等号，小于号<（less-than），大于号>（greater-than）。

10. `/` 斜杠，`slash`，为与“\”相区别，通常也叫`forward slash`。

11. `\` 反斜杠，`backslash`。

12. `+`加号，`plus sign`； `-` 减号，`minus sign`。

13. `-` – — `dash`，英文中dash


