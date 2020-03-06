# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 19:33:17 2020

将XLore数据转化成三元组格式：实体 关系 属性值
把instance和property汉字匹配到infobox中，形成最终版三元组

@author: zhangwz
"""
import logging
import datetime

infobox2indexFile = './infobox2index.txt'
entity2idFile = './entity2id.txt'
instance2idFile = './instance2id.txt'
property2idFile = './property2id.txt'
#最终存储位置 - 后续还需要过滤掉一部分
xloreTripleFile = './xloreTriple.txt'

triple = ''
def getTriple():
    i = 0       #用于每匹配到10000次输出一次，便于了解匹配进度
    with open(infobox2indexFile, encoding='utf-8') as fr:
        for line in fr:
            i = i + 1
            if(i%10000 == 0):
                print('%d:%s' %(i,line))
            lineArr = line.split(' ')
            bdi = lineArr[0]
            bdp = lineArr[1]
            pval = lineArr[2]

            with open(entity2idFile, encoding='utf-8') as fir:
                for iline in fir:
                    ilineArr = iline.split(' ')
                    instanceid = ilineArr[0]
                    instance = ilineArr[1]
                    if(instanceid == bdi):
                        bdi = instance
                        with open(property2idFile, encoding='utf-8') as fpr:
                            for pline in fpr:
                                plineArr = pline.split(' ')
                                propertyid = plineArr[0]
                                pro = plineArr[1]
                                if(propertyid == bdp):
                                    bdp = pro
                                    triple = bdi.strip() + '\t' + bdp.strip() + '\t' + pval.strip()
                                    print(triple)
                                    # triple = (bdi, bdp, pval)
                                    if (i % 1000 == 0):
                                        print('%d:%s' % (i, triple))
                                    with open(xloreTripleFile, 'a', encoding='utf-8') as fw:
                                        fw.write(triple + '\n')



    return xloreTripleFile

if __name__ == '__main__':
    program = "xloreTriple.py"
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(program))
    # 开始运行时间
    starttime = datetime.datetime.now()
    print("程序开始运行时间：" + str(starttime))
    getTriple()
    print('程序运行结束...')
    # 结束运行时间
    endtime = datetime.datetime.now()
    print("程序结束运行时间：" + str(endtime))
    # 运行时间
    runAllTime = endtime - starttime
    print("程序运行时长：" + str(runAllTime))

