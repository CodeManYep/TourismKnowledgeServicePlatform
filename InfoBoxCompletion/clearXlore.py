# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 22:36:43 2020

清洗XLore数据
@author: zhangwz
"""
import logging
import datetime

instanceOldFile = './xlore.instance.list.ttl'       #原实例文本文件
instanceNewFile = './instance2index.txt'  #清洗后的实例索引文件 格式： index instance

propertyOldFile = './xlore.property.list.ttl'       #原属性文本文件
propertyNewFile = './property2index.txt'  #清洗后的属性索引文件 格式： index property

infoboxOldFile = './xlore.infobox.ttl'       #原infobox文本文件
infoboxNewFile = './infobox2index.txt'  #清洗后的infobox索引文件 格式： index infobox

def instanceToIndex():
    i = 0       #用于每匹配到1000次输出一次，便于了解匹配进度
    with open(instanceOldFile, encoding='utf-8') as fr:
        for line in fr:
            i = i + 1
            if(i%10000 == 0):
                print('%d:%s' %(i,line))
            if 'rdf:type' in line or '@en' in line:
                continue
            else:
                with open(instanceNewFile, 'a', encoding='utf-8') as fw:
                    fw.write(line)
    return instanceNewFile

def propertyToIndex():
    j = 0       #用于每匹配到1000次输出一次，便于了解匹配进度
    with open(propertyOldFile, encoding='utf-8') as fr:
        for line in fr:
            j = j + 1
            if(j%10000 == 0):
                print('%d:%s' %(j,line))
            if 'rdf:type' in line or '@en' in line:
                continue
            else:
                with open(propertyNewFile, 'a', encoding='utf-8') as fw:
                    fw.write(line)
    return instanceNewFile

def infoboxToIndex():
    k = 0       #用于每匹配到1000次输出一次，便于了解匹配进度
    with open(infoboxOldFile, encoding='utf-8') as fr:
        for line in fr:
            k = k + 1
            if(k%10000 == 0):
                print('%d:%s' %(k,line))
            if 'rdf:type' in line or '@en' in line:
                continue
            else:
                with open(infoboxNewFile, 'a', encoding='utf-8') as fw:
                    fw.write(line)
    return instanceNewFile

if __name__ == '__main__':
    program = "clearInstance.py"
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(program))
    # 开始运行时间
    starttime = datetime.datetime.now()
    print("程序开始运行时间：" + str(starttime))
    #instanceToIndex()
    #print('start to clear property...')
    #propertyToIndex()
    infoboxToIndex()
    print('程序运行结束...')
    # 结束运行时间
    endtime = datetime.datetime.now()
    print("程序结束运行时间：" + str(endtime))
    # 运行时间
    runAllTime = endtime - starttime
    print("程序运行时长：" + str(runAllTime))
