DeepFM tutorial:

- [DeepFM-detail-TensorFlow-手把手带你实现DeepFM！](https://cloud.tencent.com/developer/article/1450677)
	- [notebook-github](https://github.com/princewen/tensorflow_practice/blob/master/recommendation/Basic-DeepFM-model/DeepFM-StepByStep.ipynb)

- [bilibili:ctr prediction](https://www.bilibili.com/video/BV1CJ411i7Yx?p=6)
tf:
- [other:deepFM-TensorFlow](https://www.jianshu.com/p/71d819005fed)


TensorFlow tips:
- [reduce_sum](https://www.jianshu.com/p/30b40b504bae)
```py 
tf.reduce_sum(
    input_tensor, 
    axis=None, 
    keepdims=None,
    name=None,
    reduction_indices=None, 
    keep_dims=None)

input_tensor：待求和的tensor;
axis：指定的维，如果不指定，则计算所有元素的总和;
keepdims：是否保持原有张量的维度，设置为True，结果保持输入tensor的形状，设置为False，结果会降低维度，如果不传入这个参数，则系统默认为False;
name：操作的名称;
reduction_indices：在以前版本中用来指定轴，已弃用;
keep_dims：在以前版本中用来设置是否保持原张量的维度，已弃用;

 - [substract]()
 ```
tf.subtract(
    x,
    y,
    name=None
)
返回 x-y 的元素.

 ```