# -*- coding: utf-8 -*-

"""
@author: zhangwz
统计各个省份的实体和关系数量
遍历各个省份的景点名称，与总的知识文件进行匹配，每匹配完一个省份，
把知识写入到相应的省份知识文件中
最后再用已经编写好的Java文件，获取到各个省份的实体和关系统计结果
"""
import os
import logging
import datetime


#景点名称文本路径
filePath = './provinceData'      
#存储景点知识文件
tourismKnowledgeFile = './tourismKnowledge.txt'  
#统计所有省份景点实体、关系文本路径
provinceFilePath = './provinceTourismKnowledge'   



#遍历获取所有省份存储景点的文件名称
def getFileList(dir):
    fileList = []
    for home, dirs, files in os.walk(filePath):
        for filename in files:
            # 文件名列表，包含完整路径
            #fileList.append(os.path.join(home, filename))
            #文件名列表，只包含文件名
            fileList.append(filename)
    return fileList
def getProvinceSpotsKnowledge():
    i = 0       #用于每匹配到100次输出一次，便于了解匹配进度
    provinceSpotsFileList = getFileList(filePath)
    for provinceSpotsFile in provinceSpotsFileList:
        #获取各个省份名称的汉语拼音
        provinceName = provinceSpotsFile.split(".")[0][:-9]
        provinceTourismKnowledge = provinceFilePath + "/" + provinceName + "TourismKnowledge.txt"
        provinceSpotsFile = './provinceData/' + provinceSpotsFile
        with open(provinceSpotsFile, encoding='utf-8') as psf:
            for line in psf:
                name = line.strip()
                #print('%d:%s' %(i,name))
                with open(tourismKnowledgeFile, 'rb') as tkf:
                    for tripletLine in tkf:
                        entity = tripletLine.strip().split(str.encode('\t'))[0]
                        if(i%100 == 0):
                            print('%d:%s' %(i, entity.decode()))
                        if(name == entity.decode()):
                            i = i + 1
                            with open(provinceTourismKnowledge, 'a', encoding='utf-8') as ptkw:
                                provinceSpotsKnowledge = '%s' % (tripletLine.decode())
                                if(i%100 == 0):
                                    print('%d:%s' %(i,provinceSpotsKnowledge))
                                ptkw.write(provinceSpotsKnowledge)
    return tourismKnowledgeFile

if __name__ == '__main__':
    program = "getProvinceTourismKnowledge.py"
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(program))
    # 开始运行时间
    starttime = datetime.datetime.now()
    print("程序开始运行时间：" + str(starttime))
    getProvinceSpotsKnowledge()
    print('程序运行结束...')
    # 结束运行时间
    endtime = datetime.datetime.now()
    print("程序结束运行时间：" + str(endtime))
    # 运行时间
    runAllTime = endtime - starttime
    print("程序运行时长：" + str(runAllTime))