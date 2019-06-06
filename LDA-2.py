# -*- coding: utf-8 -*-
import numpy as np
from gensim import corpora, models, similarities
import time

def load_stopword():
    f = open(r'D:\\LDA\\stopword.txt','rb')
    words = [line.strip() for line in f]
    f.close()
    return words
 
 
if __name__ == '__main__':
 
    print('1.初始化停止词列表 ------')
    stop_words = load_stopword()
 
    print('2.开始读入语料数据 ------ ')
    f = open('D:\\LDA\\XLW1.txt','rb')
    texts = [[word for word in line.strip().lower().split() if word not in stop_words] for line in f]
    f.close()
     
    M = len(texts)
    print('文本数目：%d个' % M)
 
    print('3.正在建立词典 ------')
    dic = corpora.Dictionary(texts)
    V = len(dic)
 
    print ('4.正在计算文本向量 ------')
    # 转换文本数据为索引，并计数
    corpus = [dic.doc2bow(text) for text in texts]
 
    print ('5.正在计算文档TF-IDF ------')
    corpus_tfidf = models.TfidfModel(corpus)[corpus]
 
    print ('6.LDA模型拟合推断 ------')
    # 训练模型
    num_topics = 7
    t_start = time.time()
    lda = models.LdaModel(corpus_tfidf, num_topics=num_topics, id2word=dic,
                            alpha=0.01, eta=0.01, minimum_probability=0.001,
                            update_every = 1, chunksize = 100, passes = 1)
 
    # 随机打印某5个文档的主题
    num_show_topic = 5 # 每个文档显示前几个主题
    print('7.结果：8个文档的主题分布：--')
    doc_topics = lda.get_document_topics(corpus_tfidf)  # 所有文档的主题分布
    idx = np.arange(M)
    np.random.shuffle(idx)
    idx = idx[:10]
    for i in idx:
        topic = np.array(doc_topics[i])
        topic_distribute = np.array(topic[:, 1])
        topic_idx = topic_distribute.argsort()[:-num_show_topic-1:-1]
        print('第%d个文档的前%d个主题：' % (i, num_show_topic)), topic_idx
        print(topic_distribute[topic_idx])
 
    num_show_term = 5   # 每个主题显示几个词
    print('8.结果：每个主题的词分布：--')
    for topic_id in range(num_topics):
        print('\n#主题 %d:\t' % (topic_id+1))
        term_distribute_all = lda.get_topic_terms(topicid=topic_id)
        term_distribute = term_distribute_all[:num_show_term]
        term_distribute = np.array(term_distribute)
        term_id = term_distribute[:, 0].astype(np.int)
        print('#主题关键词：\t',)
        for t in term_id:
            print(dic.id2token[t],)
        print('\n#每个词的概率:\n', term_distribute[:, 1])