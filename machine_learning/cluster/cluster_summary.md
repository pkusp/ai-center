

最近在做一个聚类的任务，数据量比较大，且高维稀疏，于是梳理了一下聚类相关算法，与大家分享。

提到聚类，大家的第一印象基本都是$KMeans$，这是一个非常经典的聚类算法，但它的局限性其实也很明显，比如它通常采用欧式距离$\sqrt(x_i^2-x_j^2)$ 作为距离，适合稠密有序的特征，而对于分类特征（比如颜色,红/黄/蓝）则无法很好的处理。

聚类算法可以粗分为两类：（1）传统聚类方法；（2）深度聚类方法。

本文首先介绍传统的聚类算法以及适应场景，优缺点等内容，然后介绍深度学习聚类相关方法，最后介绍一些聚类的小trick。

下面先列举一些常见的聚类算法，然后一一解读















### cluster:



NAME|ABSTRACT|TYPE
---|---|---
KMeans| dense feature
KModes| sparse feature
KPrototype| mixed feature
DBSCAN|
[BIRCH](https://grid.cs.gsu.edu/~wkim/index_files/papers/birch.pdf)|
GMM|
### deeplearning-cluster

一般的聚类算法例如K-means，GMM，这些方法速度快，适用于各种各样的问题， 但是，它们的距离度量仅限于原始数据空间，当输入维度较高时，它们往往无效。


NAME|ABSTRACT|REF
---|---|---
[Deepcluster](https://github.com/facebookresearch/deepcluster)| CV-FAIR|CV
DEC|AE => KL-divergence|[intro](https://blog.csdn.net/AndyViky/article/details/94159565) [keras impl](https://github.com/XifengGuo/DEC-keras)



### text cluster:
1. split_words
2. stop_words
3. TFIDF
4. clustering








### ref:
DEC
- https://zhuanlan.zhihu.com/p/50365577
- https://flashgene.com/archives/7798.html
- https://zhuanlan.zhihu.com/p/28967965
- http://proceedings.mlr.press/v48/xieb16.pdf
- https://www.cnblogs.com/wzyj/p/9827584.html


---

[聚类总结(aliyun zhenghan)](https://www.cnblogs.com/LittleHann/p/6595148.html)


- kmeans(适合连续特征)
- [kmodes(适合分类特征)](https://gw.alipayobjects.com/os/rmsportal/UuRoTJVHJhPQIVbUyGBX.pdf)
- [kprototype（适合混合特征）](https://gw.alipayobjects.com/os/rmsportal/EYrbHejvSOyhjwHTabmm.pdf)
    -  k-prototype算法结合k-means和k-modes算法而来，可以对具有数值型属性和标称型属性的数据对象进行聚类。对于数值型属性，使用欧氏距离来衡量对象之间的相似性；对于标称型属性，使用汉明距离来衡量对象的相似性。簇中心的计算：对于数值型属性，使用每个簇中数据对象的相应属性的平均值；对于标称性属性，使用每个簇中数据对象相应属性出现次数最多的值。
- [DBSCAN(密度聚类)](https://baike.baidu.com/item/DBSCAN)

-

#### 评测
- [评测](https://blog.csdn.net/sinat_33363493/article/details/52496011)

#### 有监督聚类
资源不够或需要可解释时：
- [用RF做聚类](https://www.stat.berkeley.edu/~breiman/RandomForests/cc_home.htm#unsup) http://sofasofa.io/forum_main_post.php?postid=1000365

#### 深度学习聚类


思路：
1. 基于autoencoder
[为什么稀疏自编码器很少见到多层的？
](https://www.zhihu.com/question/41490383)
[DEC(deep embedded cluster)]()

2. [基于RBM(paper)](http://www.cs.toronto.edu/~rsalakhu/papers/rbmcf.pdf)
    - [RBM介绍](https://www.cnblogs.com/pinard/p/6530523.html)

3. [SOM](https://www.cnblogs.com/LittleHann/p/7101992.html)
4. [基于GRAPH LEARNING](https://zhuanlan.zhihu.com/c_1025445798976176128)
[NETWORK/GRAPH EMBEDDING (intentGC)](https://arxiv.org/pdf/1907.12377.pdf)
    - [HIN(异构信息网络)]



start-of-the-art：
- [FAIR-DeepCluster-2018-CV](https://arxiv.org/abs/1807.05520v1)

demo：
- [keras deep cluster (github)](https://github.com/Tony607/Keras_Deep_Clustering)



### DEC
[dec-tf-github](https://github.com/HaebinShin/dec-tensorflow)
- [Unsupervised Deep Embedding for Clustering Analysis](https://arxiv.org/pdf/1511.06335.pdf)
- visulization: t-SNE
> 计算量大，耗时间是PCA的百倍，内存占用大。
专用于可视化，即嵌入空间只能是2维或3维。
需要尝试不同的初始化点，以防止局部次优解的影响。

- [KL-divergence(简书)](https://www.jianshu.com/p/43318a3dc715)
```
Kullback-Leibler Divergence，即K-L散度，是一种量化两种概率分布P和Q之间差异的方式，又叫相对熵。在概率学和统计学上，我们经常会使用一种更简单的、近似的分布来替代观察数据或太复杂的分布。K-L散度能帮助我们度量使用一个分布来近似另一个分布时所损失的信息量。

```
- T-分布 $Z = \frac{N(0,1)}{\sqrt(χ2/n)} $  ，$Z服从t(n)$
```
1.t分布式统计分布的一种，同卡方分布(χ2分布)、F分布并称为三大分布。
2. t分布又叫student-t分布，常常用于根据小样本来估计呈正态分布且方差值为知的样本的均值。（如果总体的方差已知的话，则应该用正态分布来估计总体的均值。）(所以一个前提是：t分布的样本的总体必须符合正态分布)
3.t分布一般用于小样本(样本量比较小)的情形。
4.假设X服从标准正态分布即X~N(0,1)，Y服从自由度n的卡方分布即Y~χ2（n），且X与Y是相互独立的，那么Z=X/sqrt(Y/n)的分布成为自由的为n的t分布，记为Z~t(n).
5.对于Z~t(n)，其数学期望E(Z) = 0，n>1;方差D(Z)=n/n-2 , n>2 。
6.特征：
(1)．以0为中心，左右对称的单峰分布；
(2)．t分布是一簇曲线，其形态变化与n（即其自由度）大小有关。自由度n越小，t分布曲线越低平；自由度n越大，t分布曲线越接近标准正态分布（u分布）曲线，当自由度无限大时，t分布就成了正态分布，如图.
t(n)分布与其密度函数。

```






### 推荐算法

关键词推荐类似基于<user,item>的协同过滤，只是此处将user替换为query,即<query,item>，可以借鉴协同过滤方式，也可以借鉴intentGC构建<query，item>网络


- [协同过滤](https://www.cnblogs.com/pinard/p/6349233.html)







## kmeans

##### 簇个数确定

- 手肘法

```py
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df_features = pd.read_csv(r'C:\预处理后数据.csv',encoding='gbk') # 读入数据
'利用SSE选择k'
SSE = []  # 存放每次结果的误差平方和
for k in range(1,9):
    estimator = KMeans(n_clusters=k)  # 构造聚类器
    estimator.fit(df_features[['R','F','M']])
    SSE.append(estimator.inertia_)
X = range(1,9)
plt.xlabel('k')
plt.ylabel('SSE')
plt.plot(X,SSE,'o-')
plt.show()

```

## DBSCAN
- [*Density-Based Spatial Clustering of Applications with Noise*](https://www.cnblogs.com/pinard/p/6208966.html)

- 定义
```
    假设我的样本集是D=(𝑥1,𝑥2,...,𝑥𝑚),则DBSCAN具体的密度描述定义如下：

    1） 𝜖-邻域：对于𝑥𝑗∈𝐷，其𝜖-邻域包含样本集D中与𝑥𝑗的距离不大于𝜖的子样本集，即𝑁𝜖(𝑥𝑗)={𝑥𝑖∈𝐷|𝑑𝑖𝑠𝑡𝑎𝑛𝑐𝑒(𝑥𝑖,𝑥𝑗)≤𝜖}, 这个子样本集的个数记为|𝑁𝜖(𝑥𝑗)|

    2) 核心对象：对于任一样本𝑥𝑗∈𝐷，如果其𝜖-邻域对应的𝑁𝜖(𝑥𝑗)至少包含MinPts个样本，即如果|𝑁𝜖(𝑥𝑗)|≥𝑀𝑖𝑛𝑃𝑡𝑠，则𝑥𝑗是核心对象。

    3）密度直达：如果𝑥𝑖位于𝑥𝑗的𝜖-邻域中，且𝑥𝑗是核心对象，则称𝑥𝑖由𝑥𝑗密度直达。注意反之不一定成立，即此时不能说𝑥𝑗由𝑥𝑖密度直达, 除非且𝑥𝑖也是核心对象。

    4）密度可达：对于𝑥𝑖和𝑥𝑗,如果存在样本样本序列𝑝1,𝑝2,...,𝑝𝑇,满足𝑝1=𝑥𝑖,𝑝𝑇=𝑥𝑗, 且𝑝𝑡+1由𝑝𝑡密度直达，则称𝑥𝑗由𝑥𝑖密度可达。也就是说，密度可达满足传递性。此时序列中的传递样本𝑝1,𝑝2,...,𝑝𝑇−1均为核心对象，因为只有核心对象才能使其他样本密度直达。注意密度可达也不满足对称性，这个可以由密度直达的不对称性得出。

    5）密度相连：对于𝑥𝑖和𝑥𝑗,如果存在核心对象样本𝑥𝑘，使𝑥𝑖和𝑥𝑗均由𝑥𝑘密度可达，则称𝑥𝑖和𝑥𝑗密度相连。注意密度相连关系是满足对称性的。
```
- 算法
```
输入：样本集D=(𝑥1,𝑥2,...,𝑥𝑚)，邻域参数(𝜖,𝑀𝑖𝑛𝑃𝑡𝑠), 样本距离度量方式

    输出： 簇划分C.

    1）初始化核心对象集合Ω=∅, 初始化聚类簇数k=0，初始化未访问样本集合Γ = D,  簇划分C = ∅
    2) 对于j=1,2,...m, 按下面的步骤找出所有的核心对象：

      a) 通过距离度量方式，找到样本𝑥𝑗的𝜖-邻域子样本集𝑁𝜖(𝑥𝑗)
      b) 如果子样本集样本个数满足|𝑁𝜖(𝑥𝑗)|≥𝑀𝑖𝑛𝑃𝑡𝑠， 将样本𝑥𝑗加入核心对象样本集合：Ω=Ω∪{𝑥𝑗}
    3）如果核心对象集合Ω=∅，则算法结束，否则转入步骤4.

    4）在核心对象集合Ω中，随机选择一个核心对象𝑜，初始化当前簇核心对象队列Ω𝑐𝑢𝑟={𝑜}, 初始化类别序号k=k+1，初始化当前簇样本集合𝐶𝑘={𝑜}, 更新未访问样本集合Γ=Γ−{𝑜}
    5）如果当前簇核心对象队列Ω𝑐𝑢𝑟=∅，则当前聚类簇𝐶𝑘生成完毕, 更新簇划分C={𝐶1,𝐶2,...,𝐶𝑘}, 更新核心对象集合Ω=Ω−𝐶𝑘， 转入步骤3。

    6）在当前簇核心对象队列Ω𝑐𝑢𝑟中取出一个核心对象𝑜′,通过邻域距离阈值𝜖找出所有的𝜖-邻域子样本集𝑁𝜖(𝑜′)，令Δ=𝑁𝜖(𝑜′)∩Γ, 更新当前簇样本集合𝐶𝑘=𝐶𝑘∪Δ, 更新未访问样本集合Γ=Γ−Δ,  更新Ω𝑐𝑢𝑟=Ω𝑐𝑢𝑟∪(Δ∩Ω)−𝑜′，转入步骤5.

    输出结果为： 簇划分C={𝐶1,𝐶2,...,𝐶𝑘}
```
- 优缺点

```
   DBSCAN的主要优点有：

    1） 可以对任意形状的稠密数据集进行聚类，相对的，K-Means之类的聚类算法一般只适用于凸数据集。

    2） 可以在聚类的同时发现异常点，对数据集中的异常点不敏感。

    3） 聚类结果没有偏倚，相对的，K-Means之类的聚类算法初始值对聚类结果有很大影响。

    DBSCAN的主要缺点有：

    1）如果样本集的密度不均匀、聚类间距差相差很大时，聚类质量较差，这时用DBSCAN聚类一般不适合。

    2） 如果样本集较大时，聚类收敛时间较长，此时可以对搜索最近邻时建立的KD树或者球树进行规模限制来改进。

    3） 调参相对于传统的K-Means之类的聚类算法稍复杂，主要需要对距离阈值𝜖，邻域样本数阈值MinPts联合调参，不同的参数组合对最后的聚类效果有较大影响。
```

