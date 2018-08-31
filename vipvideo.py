# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 21:51:52 2018

@author: 2271057973
"""




import requests
from multiprocessing import Pool


def templ(n):
    url='https://v-acfun.com/20180805/5787_a8ada711/1000k/hls/4f10a74e7a7%03d.ts'%n
    headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
            }
    print(url)
    r=requests.get(url,headers=headers)
    f=open('C:\\Users\\2271057973\\Desktop\\beau\\{}'.format(url[-10:]),'ab')
    f.write(r.content)
    f.close()
    
    
    

if __name__ == '__main__':
    pool=Pool(20)
    for i in range(100):
        print(i)
        pool.apply_async(templ,(i,))
    pool.close()
    pool.join()
   
    
    
    

    
    
    
    






