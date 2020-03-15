# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 15:36:13 2019

@author: zhangwz
将爬取的景点名称与知识工厂数据集进行匹配，匹配到则把景点的知识获取
分三台机子跑，服务器 + 本机(labProData) + PC(pcProData)
"""
import logging
import datetime
import os

#spotsNameFile = './secSpotsData.txt'       #景点名称文件
knowledgeFile = '../TransE/Data/baike_triples.txt'       #知识工厂三元组文件
tourismKnowledgeFile = './labTourismKnowledge.txt'  #存储景点知识文件
filePath = './labProData'       #景点名称文本路径


def getFileList(dir):
    fileList = []
    for home, dirs, files in os.walk(filePath):
        for filename in files:
            # 文件名列表，包含完整路径
            #fileList.append(os.path.join(home, filename))
            #文件名列表，只包含文件名
            fileList.append(filename)
            
    return fileList


def getSpotsKnowledge():
    count = 0   #用于统计匹配到的景点个数
    i = 0       #用于每匹配到100次输出一次，便于了解匹配进度
    spotsFileList = getFileList(filePath)
    for spotsNameFile in spotsFileList:
        spotsNameFile = './labProData/' + spotsNameFile
        with open(spotsNameFile, encoding='utf-8') as snf:
            for line in snf:
                name = line.strip()
                print('%d:%s' %(i,name))
                with open(knowledgeFile, 'rb') as kf:
                    for tripletLine in kf:
                        entity = tripletLine.strip().split(str.encode('\t'))[0]
                        """
                        if(i%10000 == 0):
                            print('%d:%s' %(i, entity.decode()))
                        """
                        if(name == entity.decode()):
                            count = count + 1
                            with open(tourismKnowledgeFile, 'a', encoding='utf-8') as skfw:
                                spotsKnowledge = '%s' % (tripletLine.decode())
                                i = i + 1
                                if(i%100 == 0):
                                    print('%d:%s' %(i,spotsKnowledge))
                                skfw.write(spotsKnowledge)
    print('count = ' + str(count))
    return tourismKnowledgeFile

if __name__ == '__main__':
    program = "getTourismKnowledge.py"
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(program))
    # 开始运行时间
    starttime = datetime.datetime.now()
    print("程序开始运行时间：" + str(starttime))
    getSpotsKnowledge()
    print('程序运行结束...')
    # 结束运行时间
    endtime = datetime.datetime.now()
    print("程序结束运行时间：" + str(endtime))
    # 运行时间
    runAllTime = endtime - starttime
    print("程序运行时长：" + str(runAllTime))
                            
                            
                    
