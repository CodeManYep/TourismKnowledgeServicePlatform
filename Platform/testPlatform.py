# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 20:28:21 2020

网站并发测试
@author: zhangwz
"""
#!/usr/bin/python3

import sys, time, json, _thread
import http.client
import logging
import datetime

#thread_count  = 100    #并发数量
#thread_count  = 500
#thread_count  = 1000
thread_count  = 5000
now_count = 0
error_count = 0
begin_time = ''

lock_obj = _thread.allocate()

def test_http_engine():
    global now_count
    global error_count
    global thread_count
    global begin_time
    conn = None
    if now_count == 0:
        begin_time = int(round(time.time() * 1000))
    try:
        conn = http.client.HTTPConnection("10.150.21.196", 8080)
        conn.request('GET', '/TourismKnowledgeServicePlatform/tksp/home')

        response = conn.getresponse()
        data = response.read()
        #print (data)

        if json.dumps(response.status) != '200':
            error_count += 1;
            print ('error count: ' + str(error_count))

        sys.stdout.flush()
        now_count += 1
        if now_count == thread_count:
            print ('### error count: ' + str(error_count) + ' ###')
            print ('### begin time : ' + str(begin_time))
            print ('### end time   : ' + str(int(round(time.time() * 1000))))

    except Exception as e:
        print (e)
    finally:
        if conn:
            conn.close()

def test_thread_func():
    global now_count
    global lock_obj
    cnt = 0

    lock_obj.acquire()
    print ('')
    print ('=== Request: ' + str(now_count) + ' ===')

    cnt += 1
    test_http_engine()
    sys.stdout.flush()
    lock_obj.release()


def test_main():
    global thread_count
    for i in range(thread_count):
        _thread.start_new_thread(test_thread_func, ())

if __name__=='__main__':
    program = "testPlatform.py"
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(program))
    # 开始运行时间
    starttime = datetime.datetime.now()
    print("程序开始运行时间：" + str(starttime))
    test_main()
    while True:
        time.sleep(5)
        
    print('程序运行结束...')
    # 结束运行时间
    endtime = datetime.datetime.now()
    print("程序结束运行时间：" + str(endtime))
    # 运行时间
    runAllTime = endtime - starttime
    print("程序运行时长：" + str(runAllTime))

