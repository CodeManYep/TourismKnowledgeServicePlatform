# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 16:36:53 2020

文章(Abstract)抽取
@author: zhangwz
"""
import logging
import datetime

#旅游知识库三元组数据文件位置
tourismTripleFile = './tourismKnowledgev2.txt'
#Abstract文本存储位置
abstractFile = './abstract.txt'
#reg = r'<a></a>'

def extractAbstract():
    #遍历旅游三元组文件
    with open(tourismTripleFile, encoding = 'utf-8') as f:
        for triple in f:
            tripleArr = triple.split('\t')
            card = tripleArr[1]
            if(card == 'BaiduCARD'):
                abstract = tripleArr[2].replace('<a>', '').replace('</a>', '').replace('|||', '')
    
                #把abstrac存储到文本中
                i = 0
                with open(abstractFile, 'a', encoding='utf-8') as fw:
                    i = i + 1
                    if(i%1000 == 0):
                        print('%d:%s' %(i, abstract))
                    fw.write(abstract)
        
    f.close()

if __name__ == '__main__':
    program = "abstractExtraction.py"
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(program))
    # 开始运行时间
    starttime = datetime.datetime.now()
    print("程序开始运行时间：" + str(starttime))
    
    extractAbstract()
    
    # 结束运行时间
    endtime = datetime.datetime.now()
    print("程序结束运行时间：" + str(endtime))
    # 运行时间
    runAllTime = endtime - starttime
    print("程序运行时长：" + str(runAllTime))
    print('程序运行结束...')

