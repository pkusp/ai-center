# encoding: utf-8
"""
@author: pkusp
@contact: pkusp@outlook.com

@version: 1.0
@file: baseline.py
@time: 2018/7/31 上午1:13

这一行开始写关于本文件的说明与解释
"""
import os
from competitions import config

proj_path = os.path.join(config.PROJECT_PATH, 'article_class_2018_DataCastle')
art_doc = os.path.join(config.PROJECT_PATH, 'article_class_2018_DataCastle/article_class_2018/doc')


def baseline_1():
    import pandas as pd, numpy as np
    from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
    from sklearn import svm

    column = "word_seg"
    train = pd.read_csv(os.path.join(proj_path, 'data_raw/train_set.csv'))
    train = train[train['class'] > -1]
    test = pd.read_csv(os.path.join(proj_path, 'data_raw/test_set.csv'))

    test_id = test["id"].copy()
    vec = TfidfVectorizer(ngram_range=(1, 2), min_df=3, max_df=0.9, use_idf=1, smooth_idf=1, sublinear_tf=1)
    trn_term_doc = vec.fit_transform(train[column])
    test_term_doc = vec.transform(test[column])
    fid0 = open(os.path.join(art_doc, 'baseline.csv'), mode='w')

    y = (train["class"] - 1).astype(int)
    lin_clf = svm.LinearSVC()
    lin_clf.fit(trn_term_doc, y)
    preds = lin_clf.predict(test_term_doc)
    i = 0
    fid0.write("id,class" + "\n")
    for item in preds:
        fid0.write(str(i) + "," + str(item + 1) + "\n")
        i = i + 1
    fid0.close()


if __name__ == '__main__':
    import time

    t1 = time.time()
    baseline_1()
    t2 = time.time()
    print('run: {}s'.format(round(t2 - t1, 4)))


def baseline_2():
    """

    :return: tfidf+lr lb：0.77256
    """
    import pandas as pd, numpy as np
    from sklearn.linear_model import LogisticRegression
    from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
    import time
    t1 = time.time()
    train = pd.read_csv('../input/train_set.csv')
    test = pd.read_csv('../input/test_set.csv')
    test_id = pd.read_csv('../input/test_set.csv')[["id"]].copy()

    column = "word_seg"
    n = train.shape[0]
    vec = TfidfVectorizer(ngram_range=(1, 2), min_df=3, max_df=0.9, use_idf=1, smooth_idf=1, sublinear_tf=1)
    trn_term_doc = vec.fit_transform(train[column])
    test_term_doc = vec.transform(test[column])

    y = (train["classify"] - 1).astype(int)
    clf = LogisticRegression(C=4, dual=True)
    clf.fit(trn_term_doc, y)
    preds = clf.predict_proba(test_term_doc)

    # 保存概率文件
    test_prob = pd.DataFrame(preds)
    test_prob.columns = ["class_prob_%s" % i for i in range(1, preds.shape[1] + 1)]
    test_prob["id"] = list(test_id["id"])
    test_prob.to_csv('../sub_prob/prob_lr_baseline.csv', index=None)

    # 生成提交结果
    preds = np.argmax(preds, axis=1)
    test_pred = pd.DataFrame(preds)
    test_pred.columns = ["class"]
    test_pred["class"] = (test_pred["class"] + 1).astype(int)
    print(test_pred.shape)
    print(test_id.shape)
    test_pred["id"] = list(test_id["id"])
    test_pred[["id", "class"]].to_csv('../sub/sub_lr_baseline.csv', index=None)
    t2 = time.time()
    print("time use:", t2 - t1)

# def read_data():
#     # 注意首先先安装feather包，pip install feather-format
#     # 具体的可以百度feather使用方法
#     import feather
#     import pandas as pd
#     def gen_csv_feather(path, path_new):
#         f = open(path)
#         reader = pd.read_csv(f, sep=',', iterator=True)
#         loop = True
#         chunkSize = 10000
#         chunks = []
#         while loop:
#             try:
#                 chunk = reader.get_chunk(chunkSize)
#                 chunks.append(chunk)
#             except StopIteration:
#                 loop = False
#                 print("Iteration is stopped.")
#         df = pd.concat(chunks, ignore_index=True)
#         print(df.count())
#         feather.write_dataframe(df, path_new)
#     gen_csv_feather("../data/train_set.csv", "../data/train_set.feather")
#     gen_csv_feather("../data/test_set.csv", "../data/test_set.feather")
#
