# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 21:54:40 2019

@author: zhangwz
将三元组数据集做预处理，使之符合TransE系列训练格式要求
主要工作是数据清洗，去掉脏数据 + 头尾实体相同的数据
同时把标注语料去掉
"""
import logging
import datetime
import re

#三元组数据集路径
tripletDataFile = './tourismKB.txt'
#清洗之后数据集路径
trainDataFile = './trainKB.txt'

#数据清洗操作
def getClearedKB():
    #读文件
    i = 0
    with open(tripletDataFile, 'r', encoding = 'utf-8') as rf:
        for line in rf:
            i += 1
            if(i%1000 == 0):
                print('%d:%s' %(i,line))
            lineArr = line.split('\t')
            #relation
            relation = lineArr[1]
            #print(relation)
            if relation == 'BaiduCARD' or relation == 'BaiduTAG' or relation == '中文名':
                continue
            else:
                line = re.sub(r'(<\/?a.*?>)','',line)
                with open(trainDataFile, 'a', encoding = 'utf-8') as wf:
                    wf.write(line)
             
    print ("success")

if __name__ == '__main__':
    program = "getUnique.py"
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(program))
    # 开始运行时间
    starttime = datetime.datetime.now()
    print("程序开始运行时间：" + str(starttime))
    getClearedKB()
    #areg = re.compile('(<\/?a.*?>)')
    #areg = re.compile('(?<=\>).*?(?=\<)')
    line = '<a>仙岩</a>寺'
    #s2 = re.sub(r'(<\/?a.*?>)','',line)
    #line = ''.join(re.compile('(<\/?a.*?>)').findall(line))
    #line = ''.join(re.compile('>(.*?)<').findall(line))
    #print(line)
    print('程序运行结束...')
    # 结束运行时间
    endtime = datetime.datetime.now()
    print("程序结束运行时间：" + str(endtime))
    # 运行时间
    runAllTime = endtime - starttime
    print("程序运行时长：" + str(runAllTime))

