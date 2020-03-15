# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 17:08:49 2019

@author: zhangwz
本程序用于统计旅游知识三元组的实体和关系数量
先统计西安景点数量，后按身份统计，最后统计全部
"""
import logging
import datetime
import xlwt
import os

shannxiTourismFile = './spotsKnowledge.txt'  #存储陕西景点知识文件
tourismFile = './tourismKnowledge.txt'  #存储全国景点知识文件
shannxiTourismxlsx = './shannxiAmoSta.xlsx'  #存储陕西统计结果Excel文件
tourismxlsx = './tourismAmoSta.xlsx'  #存储全国统计结果Excel文件
filePath = './provinceData'       #景点名称文本路径

#遍历并获取全国省份景点文件名称
def getFileList(dir):
    fileList = []
    for home, dirs, files in os.walk(filePath):
        for filename in files:
            # 文件名列表，包含完整路径
            #fileList.append(os.path.join(home, filename))
            #文件名列表，只包含文件名
            fileList.append(filename)
    return fileList

def obtainAmountSta():
    entityNum = 0     #统计实体个数
    #relaNum = 0       #统计关系个数
    i = 0
    entityStaList = []      #统计实体数量列表，去重后统计数量
    #relationStaList = []    #统计关系数量列表，去重后统计数量
    with open(tourismFile, encoding='utf-8') as tf:
        for line in tf:
            i= i + 1
            #print('%d:%s' %(i, line))
            lineArr = line.split('\t')
            entity = lineArr[0]
            #relation = lineArr[1]
            
            if(i % 1000 == 0):
                print('%d:%s' %(i, line))
            
            entityStaList.append(entity)
            entityResultList = list(set(entityStaList))
            entityResultList.sort(key=entityStaList.index)
            #print(entityResultList)
            
            """
            relationStaList.append(relation)
            relaResultList = list(set(relationStaList))
            relaResultList.sort(key=relationStaList.index)
            #print(relaResultList)
            """
            
    entityNum = len(entityResultList)
    #relaNum = len(relaResultList)
    
    print('entity = %s' %(str(entityNum)))
    #print('entity = %s, relation = %s' %(str(entityNum), str(relaNum)))
    tourismxlsx = xlwt.Workbook(encoding='utf-8') #创建一个excel
    #创建名为 amountSta 的sheet
    amountSta = tourismxlsx.add_sheet("amountSta", cell_overwrite_ok=True)
    amountSta.write(0, 0, '国家')
    amountSta.write(0, 1, 'Entity')
    amountSta.write(0, 2, 'Relation')
    amountSta.write(1, 0, '中国')
    amountSta.write(1, 1, entityNum)
    amountSta.write(1, 2, 0)
    tourismxlsx.save(tourismxlsx)
    
    print("saveFile = %s" % tourismxlsx)
    
    return tourismxlsx

def obtainallAmountSta():
    entityNum = 0     #统计实体个数
    relaNum = 0       #统计关系个数
    i = 0
    entityStaList = []      #统计实体数量列表，去重后统计数量
    relationStaList = []    #统计关系数量列表，去重后统计数量
    tourismFileList = getFileList(filePath)
    for tourismFile in tourismFileList:
        tourismFile = './provinceData/' + tourismFile
        with open(tourismFile, encoding='utf-8') as tf:
            for line in tf:
                i= i + 1
                lineArr = line.strip().split('\t')
                entity = lineArr[0]
                relation = lineArr[1]
                
                if(i % 1000 == 0):
                    print('%d:%s' %(i, line))
                
                entityStaList.append(entity)
                entityResultList = list(set(entityStaList))
                entityResultList.sort(key=entityStaList.index)
                #print(entityResultList)
                
                relationStaList.append(relation)
                relaResultList = list(set(relationStaList))
                relaResultList.sort(key=relationStaList.index)
                #print(relaResultList)
            
    entityNum = len(entityResultList)
    relaNum = len(relaResultList)
    
    print('entity = %s, relation = %s' %(str(entityNum), str(relaNum)))
    allTourism = xlwt.Workbook(encoding='utf-8') #创建一个excel
    #创建名为 amountSta 的sheet
    amountSta = allTourism.add_sheet("amountSta", cell_overwrite_ok=True)
    amountSta.write(0, 0, '国家')
    amountSta.write(0, 1, 'Entity')
    amountSta.write(0, 2, 'Relation')
    amountSta.write(1, 0, '中国')
    amountSta.write(1, 1, entityNum)
    amountSta.write(1, 2, relaNum)
    allTourism.save(tourismxlsx)
    
    print("saveFile = %s" % tourismxlsx)
    
    return allTourism

if __name__ == '__main__':
    program = "amountStatiss=tics.py"
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(program))
    # 开始运行时间
    starttime = datetime.datetime.now()
    print("程序开始运行时间：" + str(starttime))
    print('开始执行统计陕西旅游知识三元组实体和关系数量...')
    obtainAmountSta()
    print('执行统计陕西旅游知识三元组实体和关系数量结束...')
    print('开始执行统计全国旅游知识三元组实体和关系数量...')
    #obtainallAmountSta()
    print('执行统计全国旅游知识三元组实体和关系数量结束...')
    print('程序运行结束...')
    # 结束运行时间
    endtime = datetime.datetime.now()
    print("程序结束运行时间：" + str(endtime))
    # 运行时间
    runAllTime = endtime - starttime
    print("程序运行时长：" + str(runAllTime))
