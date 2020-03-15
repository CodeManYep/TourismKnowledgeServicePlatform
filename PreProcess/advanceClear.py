# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 11:45:57 2020

进一步处理XLore数据
@author: zhangwz
"""
import logging
import datetime

instanceNewFile = './instance2index.txt'  #清洗后的实例索引文件 格式： index instance
instance2idFile = './instance2id.txt'

propertyNewFile = './property2index.txt'  #清洗后的属性索引文件 格式： index property
property2idFile = './property2id.txt'

def instance2id():
    i = 0       #用于每匹配到1000次输出一次，便于了解匹配进度
    with open(instanceNewFile, encoding='utf-8') as fr:
        for line in fr:
            i = i + 1
            if(i%10000 == 0):
                print('%d:%s' %(i,line))
            if 'supplement' in line or 'alias' in line:
                continue
            else:
                with open(instance2idFile, 'a', encoding='utf-8') as fw:
                    fw.write(line)
    return instance2idFile

def property2id():
    j = 0       #用于每匹配到1000次输出一次，便于了解匹配进度
    with open(propertyNewFile, encoding='utf-8') as fr:
        for line in fr:
            j = j + 1
            if(j%10000 == 0):
                print('%d:%s' %(j,line))
            if 'fullname' in line:
                continue
            else:
                with open(property2idFile, 'a', encoding='utf-8') as fw:
                    fw.write(line)
    return property2idFile

if __name__ == '__main__':
    program = "clearInstance.py"
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(program))
    # 开始运行时间
    starttime = datetime.datetime.now()
    print("程序开始运行时间：" + str(starttime))
    instance2id()
    print('start to clear property...')
    property2id()
    print('程序运行结束...')
    # 结束运行时间
    endtime = datetime.datetime.now()
    print("程序结束运行时间：" + str(endtime))
    # 运行时间
    runAllTime = endtime - starttime
    print("程序运行时长：" + str(runAllTime))
