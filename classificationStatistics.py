# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 16:37:19 2020

统计旅游知识库中三元组 类别(classification) 的数量
@author: zhangwz
"""
import logging
import datetime

#旅游知识库三元组数据文件位置
tourismTripleFile = './tourismKnowledge.txt'
#统计类别文本存储位置
classificationStaFile = './classificationStatistic.txt'

def getClassificationSta():
    classificationDic = {}   #类别字典 类别 - 数量
    classifications = []     #全部分类数组
    sortedDic = {}      #降序排列后的类别字典
    #遍历旅游三元组文件
    with open(tourismTripleFile, encoding = 'utf-8') as f:
        for triple in f:
            tripleArr = triple.split('\t')
            tag = tripleArr[1]
            classification = tripleArr[2].replace('\n', '')
            if(tag == 'BaiduTAG'):
                classifications.append(classification)
    
    #统计类别数量
    for classfi in classifications:
        if classfi in classificationDic:
            classificationDic[classfi] += 1
        else:
            classificationDic[classfi] = 1
    
    #遍历类别字典并存储到统计文本中
    i = 0
    sortedDic = sorted(classificationDic.items(), key = lambda x : x[1], reverse = True)
    print(sortedDic)
    #print(type(sortedDic))
    with open(classificationStaFile, 'a', encoding='utf-8') as fw:
        for k in range(len(sortedDic)):
            i = i + 1
            if(i%1000 == 0):
                print('%d:%s' %(i, str(sortedDic[k])))
            fw.write(str(sortedDic[k]) + '\n')
        
    f.close()

if __name__ == '__main__':
    program = "classificationStatistics.py"
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(program))
    # 开始运行时间
    starttime = datetime.datetime.now()
    print("程序开始运行时间：" + str(starttime))
    
    getClassificationSta()
    
    # 结束运行时间
    endtime = datetime.datetime.now()
    print("程序结束运行时间：" + str(endtime))
    # 运行时间
    runAllTime = endtime - starttime
    print("程序运行时长：" + str(runAllTime))
    print('程序运行结束...')
