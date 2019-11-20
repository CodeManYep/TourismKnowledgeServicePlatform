# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 20:57:18 2019

@author: zhangwz
发现数据集中有重复数据
把数据集中重复的三元组删除
"""
import logging
import datetime

#三元组数据集路径
tripletDataFile = './tourismKnowledge.txt'
#最终数据集路径
tourismDataFile = './tourismKB.txt'


#去重操作
def getUniqueKB():
    lines_seen = set()
    outfile=open(tourismDataFile, "a", encoding='utf-8')
    f = open(tripletDataFile,"r", encoding='utf-8')
    for line in f:
        if line not in lines_seen:
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()
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
    getUniqueKB()
    print('程序运行结束...')
    # 结束运行时间
    endtime = datetime.datetime.now()
    print("程序结束运行时间：" + str(endtime))
    # 运行时间
    runAllTime = endtime - starttime
    print("程序运行时长：" + str(runAllTime))

