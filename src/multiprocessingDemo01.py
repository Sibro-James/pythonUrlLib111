#进程池Pool
import multiprocessing as mp

def job(x):
    return x*x
def moticore():
    pool = mp.Pool()
    # res = pool.map(job,range(100))
    # print(res)
    #apply_async只能放入一个值
    # res1 = pool.apply_async(job, (2,3,4,))  #报错。这相当于一次传3个值。迭代使用下面的方法
    # print(res1.get())
    #apply_async输出多个结果怎么办？使用迭代
    multi_res = [pool.apply_async(job,(i,))for i in range(10)]
    print([res.get() for res in multi_res])
if __name__ =='__main__':
    moticore()
