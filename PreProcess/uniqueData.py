# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 21:09:12 2020

清洗XLore数据、CN-DBpedia数据保持唯一性
@author: zhangwz
"""
import logging
import datetime


xloreInfoboxFile = './xloreInfobox.txt'    #XLore旅游三元组文本 - 未去掉中文名称属性
tourismKBFile = './tourismKB.txt' #CN-DBpedia旅游三元组数据
infoboxCompletionDataFile = './infoboxCompletionData.txt' #XLore可以用于补全的数据
xloreTKBFile = './xloreTKB.txt'    #XLore旅游三元组文本 - 保证唯一值
cndbpediaTKBFile = './cndbpediaTKB.txt' #CN-DBpedia旅游三元组文本 - 保证唯一值
infoboxCTDFile = './infoboxCTD.txt' #XLore用于补全的数据 - 保证唯一值

def uniqueData():
    xloreInfoboxLines = open(xloreInfoboxFile, 'r', encoding='utf-8').readlines()
    xloreTKB = open(xloreTKBFile, 'w', encoding='utf-8')
    setData0 = set(xloreInfoboxLines)
    xloreTKB.write(''.join(setData0))
    
    tourismKBLines = open(tourismKBFile, 'r', encoding='utf-8').readlines()
    cndbpediaTKB = open(cndbpediaTKBFile, 'w', encoding='utf-8')
    setData1 = set(tourismKBLines)
    cndbpediaTKB.write(''.join(setData1))
    
    infoboxCompletionLines = open(infoboxCompletionDataFile, 'r', encoding='utf-8').readlines()
    infoboxCTD = open(infoboxCTDFile, 'w', encoding='utf-8')
    setData2 = set(infoboxCompletionLines)
    infoboxCTD.write(''.join(setData2))


    return xloreTKBFile

if __name__ == '__main__':
    program = "uniqueData.py"
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(program))
    # 开始运行时间
    starttime = datetime.datetime.now()
    print("程序开始运行时间：" + str(starttime))
    uniqueData()
    print('程序运行结束...')
    # 结束运行时间
    endtime = datetime.datetime.now()
    print("程序结束运行时间：" + str(endtime))
    # 运行时间
    runAllTime = endtime - starttime
    print("程序运行时长：" + str(runAllTime))
