# -*- coding: utf-8 -*-
"""
拼接和交换行列
"""
import numpy as np
t1 = np.arange(10).reshape(2,5)
t2 = np.arange(20,30).reshape(2,5)
#拼接
#竖直
t3 = np.vstack((t1,t2))
print(t3)
'''
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [20 21 22 23 24]
 [25 26 27 28 29]]
'''
#水平
t4 = np.hstack((t1,t2))
print(t4)
'''
[[ 0  1  2  3  4 20 21 22 23 24]
 [ 5  6  7  8  9 25 26 27 28 29]]
'''