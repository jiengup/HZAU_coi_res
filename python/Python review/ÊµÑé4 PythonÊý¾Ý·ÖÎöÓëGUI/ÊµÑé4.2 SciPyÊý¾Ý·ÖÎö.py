#实验4.2 SciPy数据分析

import numpy
import scipy
#from scipy import linalg
from numpy import linalg

#（1）线性方程组求解
print("方程求解：",end='\n')
a=scipy.mat("[5 2 3; 2 3 -4; 3 -4 -5]")
b=scipy.mat("[6; 7; 8]")
result=linalg.solve(a,b)
print(result)

print("----------------------------------------")
#（2）图像处理
from scipy import ndimage
from scipy import misc
import pandas
import matplotlib
import pylab as pl

ascent=misc.ascent()
shifted_ascent=ndimage.shift(ascent,(50,50))
shifted_ascent2=ndimage.shift(ascent,(50,50),mode="nearest")
rotated_ascent=ndimage.rotate(ascent,30)

#1）预处理灰度图片
pl.imshow(ascent,cmap=pl.cm.gray)
pl.figure()

#2）平移处理后的图片（未自动填充）
pl.imshow(shifted_ascent,cmap=pl.cm.gray)
pl.figure()

#3）平移处理后的图片（自动填充）
pl.imshow(shifted_ascent2,cmap=pl.cm.gray)
pl.figure()

#4）旋转处理后的图片
pl.imshow(rotated_ascent,cmap=pl.cm.gray)
pl.show()




