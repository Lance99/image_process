from PIL import Image
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import math

# shear function
def shear(v,h):
	global img #image
	col,row = img.size
	# shear matrix
	r = np.array([[1, v],
	              [h, 1]])
	ri = np.linalg.inv(r) # inverse shear matrix
	newrow = int(row+v*col)
	newcol = int(col+h*row)
	newImage_list = np.empty((newrow, newcol),dtype=np.uint8) # a new image list

	for i in range(0,newrow):
	    for j in range(0,newcol):
	        m = [j, i] # pixel in new image list
	        c = np.dot(m,ri) # matrix multiplication
	        i1 = round(c[1],0)
	        j1 = round(c[0],0)
	        if j1 >= col or j1 < 0 or i1 >= row or i1 < 0: # if index out of range
	            newImage_list[i][j] = 0
	        else:
	            newImage_list[i][j] = img.getpixel((j1,i1))
	img = Image.fromarray(newImage_list) # return image
	# img.show()

# rotation function
def rotation(theta):
	global img_o # origional image
	global img
	col,row = img_o.size
	# rotation matrix
	r = np.array([[np.cos(np.deg2rad(theta)), -np.sin(np.deg2rad(theta))],
				  [np.sin(np.deg2rad(theta)),np.cos(np.deg2rad(theta))]])
	# inverse rotation matrix
	ri = np.linalg.inv(r)

	c_col = math.floor(col/2) # centrol column of image
	c_row = math.floor(row/2) # centrol row of image
	newImage_list = np.empty((row, col),dtype=np.uint8)

	for i in range(0,row):
	    for j in range(0,col):
	    	i1 = i - c_row # distance between every pixel and centrol
	    	j1 = j - c_col # distance between every pixel and centrol
	    	m = [j1, i1]
	    	c = np.dot(m,ri)
	    	i1 = round((c[1] + c_row),0)
	    	j1 = round((c[0] + c_col),0)
	    	if j1+dh >= col or j1+dh < 0 or i1+dv >= row or i1+dv < 0:
	    		newImage_list[i][j] = 0
	    	else:
	    		newImage_list[i][j] = img.getpixel((j1+dh,i1+dv))
	img = Image.fromarray(newImage_list)
	# img.show()

# translation function
def translation(v,h):
	global img
	global dh # total negative horizontal translation
	global dv # total negative vertical translation
	if v < 0:
		dv =  dv - v
	if h < 0:
		dh = dh - h
	col,row = img.size
	v1 = int(fabs(v)) # absolute value of v
	h1 = int(fabs(h))
	newrow = row + v1
	newcol = col + h1
	newImage_list = np.empty((newrow, newcol),dtype=np.uint8)
	for i in range(0,newrow):
	    for j in range(0,newcol):
	    	i1 = i - v
	    	j1 = j - h
	        if (-1 < j1 and j1 < col) and ( -1 < i1 and i1 < row) and v >= 0 and h >= 0:
	            newImage_list[i][j] = img.getpixel((j1,i1))
	        elif j < col and i < row and v < 0 and h < 0:
	            newImage_list[i][j] = img.getpixel((j,i))
	        elif (-1 < j1 and j1 < col) and i < row and v < 0 and h >= 0:
	            newImage_list[i][j] = img.getpixel((j1,i))
	        elif j < col and ( -1 < i1 and i1 < row) and v >= 0 and h < 0:
	            newImage_list[i][j] = img.getpixel((j,i1))
	        else:
	    	   newImage_list[i][j] = 0
	img = Image.fromarray(newImage_list)

#bicubic function
def bicubic(factor):
	global img
	col,row = img.size
	newcol = int(col*factor)
	newrow = int(row*factor)
	newImage_list = np.empty((newrow, newcol),dtype=np.uint8)
	for i in range(0,newrow):
	    for j in range(0,newcol):
	    	a = math.floor(i/factor) #new image row index
	    	b = math.floor(j/factor) #new image col index

	    	#deal with the image border
	        if a < 1:
	            a = 1
	        if b < 1:
	            b = 1
	        if a >= row-2:
	            a = row-3
	        if b >= col-2:
	            b = col-3
	        #find the nearest pixel
	        i1 = round((i/float(factor)),2)
	        j1 = round((j/float(factor)),2)
	        if i1 < 1:
	            i1 = 1
	        if j1 < 1:
	            j1 = 1
	        if i1 >= row-2:
	            i1 = row-3
	        if j1 >= col-2:
	            j1 = col-3
	        v = j1 - b
	        u = i1 - a
	        A = np.array([s(u+1),s(u),s(u-1),s(u-2)])
	        B = np.array([[img.getpixel((b-1,a-1)), img.getpixel((b,a-1)), img.getpixel((b+1,a-1)), img.getpixel((b+2,a-1))],
	                      [img.getpixel((b-1,a)), img.getpixel((b,a)), img.getpixel((b+1,a)), img.getpixel((b+2,a))],
	                      [img.getpixel((b-1,a+1)), img.getpixel((b,a+1)), img.getpixel((b+1,a+1)), img.getpixel((b+2,a+1))],
	                      [img.getpixel((b-1,a+2)), img.getpixel((b,a+2)), img.getpixel((b+1,a+2)), img.getpixel((b+2,a+2))]])
	        C = np.array([s(v+1),s(v),s(v-1),s(v-2)])
	        f = np.dot(np.dot(A,B),C) #matrix A*B*c
	        if f < 0:
	            f = 0
	        elif f > 255:
	            f = 255
	    	newImage_list[i][j] = f

	img = Image.fromarray(newImage_list)

#bilinear function
def bilinear(factor):
	global img
	t = 0
	u = 0
	col,row = img.size
	newcol = int(col*factor)
	newrow = int(row*factor)
	newImage_list = np.empty((newrow, newcol),dtype=np.uint8)

	for i in range(0,newrow):
	    for j in range(0,newcol):
	    	a = math.floor(i/factor)
	    	b = math.floor(j/factor)
	    	#deal with the image border
	    	if a >= row-1:
	            a = a-1
	        if b >= col-1:
	            b = b-1

	    	i1 = round((i/float(factor)),2)
	    	j1 = round((j/float(factor)),2)

	    	if i1 >= row-1:
	            i1 = row-1
	        if j1 >= col-1:
	            j1 = col-1

		    t = i1 - a
		    u = j1 - b

	    	z11 = img.getpixel((b,a))*(1-u)*(1-t)
	    	z12 = img.getpixel((b+1,a))*u*(1-t)
	    	z23 = img.getpixel((b,a+1))*t*(1-u)
	    	z24 = img.getpixel((b+1,a+1))*u*t

	    	newImage_list[i][j] = z11+z12+z23+z24

	img = Image.fromarray(newImage_list)

# nearest_neighbor function
def nearest_neighbor(factor):
	global img
	col,row = img.size
	newcol = int(col*factor)
	newrow = int(row*factor)
	newImage_list = np.empty((newrow, newcol),dtype=np.uint8)

	for i in range(0,newrow):
	    for j in range(0,newcol):
	    	a = round((i/factor),0)
	    	b = round((j/factor),0)
	    	newImage_list[i][j] = img.getpixel((b,a))
	img = Image.fromarray(newImage_list)

def s(w):
    w = fabs(w)
    if w>=0 and w<1:
        return 1 - 2 * w**2 + w**3
    elif w>=1 and w<2:
        return 4 - 8*w + 5*w**2 - w**3
    else:
        return 0

img_o = Image.open("2.png").convert('L')#read image
col,row = img_o.size #image size
dv = 0 #sum of translation negative height
dh = 0 #sum of translation negative horizontal move
newImage_list = np.empty((row, col),dtype=np.uint8)
img = img_o
# translation(100,100) # translation(v,h)
# shear(0,0.3) # shear(v,h)
rotation(25) # rotation(theta)
# bicubic(0.3) # bicubic(factor)
# bilinear(0.3) # bilinear(factor)
# nearest_neighbor(1.3) # nearest_neighbor(factor)

img.save('2_output.png')

