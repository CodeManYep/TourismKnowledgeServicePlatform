# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 10:52:32 2020


1、获取XLore中用于旅游知识库infobox补全的三元组
2、获取完整旅游知识库三元组

@author: zhangwz
"""
import logging
import datetime

tourismKBFile = './tourismKB.txt'
xloreTripleFile = './xloreInfobox.txt'
xloreinboxFile = './completionInfobox.txt'    #不能够用于补全的三元组文本
tourismTripleFile = './tourismTriple.txt'    #全部旅游三元组文本

triple = ''
def getCompletion():
    i = 0       #用于每匹配到1000次输出一次，便于了解匹配进度
    with open(tourismKBFile, encoding='utf-8') as fr:
        for line in fr:
            i = i + 1
            if(i%1000 == 0):
                print('%d:%s' %(i,line))
            lineArr = line.split('\t')
            hentity = lineArr[0]
            relation = lineArr[1]
            #tentity = lineArr[2]
            """
            with open(tourismTripleFile, 'a', encoding='utf-8') as tfw:
                tfw.write(line)
            """    
            with open(xloreTripleFile, encoding='utf-8') as xfr:
                for xline in xfr:
                    xlineArr = xline.split('\t')
                    xhentity = xlineArr[0]
                    xrelation = xlineArr[1]
                    if(hentity == xhentity and relation == xrelation):
                        with open(xloreinboxFile, 'a', encoding='utf-8') as fw:
                            fw.write(xline)



    return tourismTripleFile

if __name__ == '__main__':
    program = "completion.py"
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(program))
    # 开始运行时间
    starttime = datetime.datetime.now()
    print("程序开始运行时间：" + str(starttime))
    getCompletion()
    print('程序运行结束...')
    # 结束运行时间
    endtime = datetime.datetime.now()
    print("程序结束运行时间：" + str(endtime))
    # 运行时间
    runAllTime = endtime - starttime
    print("程序运行时长：" + str(runAllTime))
