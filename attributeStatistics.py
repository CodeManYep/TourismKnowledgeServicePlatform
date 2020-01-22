# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 16:47:36 2020

统计旅游知识库中三元组属性(关系)的数量
@author: zhangwz
"""
import logging
import datetime

#旅游知识库三元组数据文件位置
tourismTripleFile = './tourismKnowledge.txt'
#属性统计存储位置
attributeStaFile = './attributeStatistic.txt'

def getAttributeSta():
    attributeDic = {}   #属性字典 属性 - 数量
    attributes = []     #全部属性数组
    sortedDic = {}      #降序排列后的属性字典
    #遍历旅游三元组文件
    with open(tourismTripleFile, encoding = 'utf-8') as f:
        for triple in f:
            tripleArr = triple.split('\t')
            attribute = tripleArr[1]
            attributes.append(attribute)
    
    #统计属性数量
    for att in attributes:
        if att in attributeDic:
            attributeDic[att] += 1
        else:
            attributeDic[att] = 1
    
    #遍历属性字典并存储到统计文本中
    i = 0
    sortedDic = sorted(attributeDic.items(), key = lambda x : x[1], reverse = True)
    #print(sortedDic)
    print(type(sortedDic))
    with open(attributeStaFile, 'a', encoding='utf-8') as fw:
        for k in range(len(sortedDic)):
            i = i + 1
            if(i%1000 == 0):
                print('%d:%s' %(i, str(sortedDic[k])))
            fw.write(str(sortedDic[k]) + '\n')
        
    f.close()

if __name__ == '__main__':
    program = "attributeStatistics.py"
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(program))
    # 开始运行时间
    starttime = datetime.datetime.now()
    print("程序开始运行时间：" + str(starttime))
    
    getAttributeSta()
    
    # 结束运行时间
    endtime = datetime.datetime.now()
    print("程序结束运行时间：" + str(endtime))
    # 运行时间
    runAllTime = endtime - starttime
    print("程序运行时长：" + str(runAllTime))
    print('程序运行结束...')