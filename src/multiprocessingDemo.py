#多进程对比
import multiprocessing as mp
import threading as td

def job(a,d):
    print('aaaaa')
# t1 = td.Thread(target=job,args=(1,2))
# p1= mp.Process(target=job,args=(1,2))
# t1.start()
# p1.start()
if __name__ =='__main__':
    p1= mp.Process(target=job,args=(1,2))
    p1.start()
