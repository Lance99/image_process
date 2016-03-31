from PIL import Image
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import math

def accumu(lis):
    total = 0
    for x in lis:
        total += x
        yield total

def histeq(im,im2,col,row):
   #get image histogram
   imhist,bins = np.histogram(im.flatten(),range(0,257))

   k = []
   l = range(257)

   cdf = imhist.cumsum() #cumulative distribution function
   for i in range(0,256):

		k.append(imhist[i]/float(cdf[255]))

   k = list(accumu(k))

   plt.bar(l[:-1], imhist)
   plt.show()
   for i in range(0,row-1):
   		for j in range(0,col-1):
   			newImage_list[i][j] = round(k[im2.getpixel((j,i))]*255)

   imhist2,bins = np.histogram(newImage_list.flatten(),range(0,257))
   plt.bar(l[:-1], imhist2)
   plt.show()


#Laplacian
def b():
	im = Image.open("Fig0343.tif").convert('L')
	col, row = im.size
	newImage_list = np.empty((row, col),dtype=np.uint8)
	mi = 255
	ma = 0
	for i in range(1,row-1):
		for j in range(1,col-1):
			a = (8*im.getpixel((j,i)))-im.getpixel((j-1,i-1))-im.getpixel((j,i-1))-im.getpixel((j+1,i-1))-im.getpixel((j-1,i))-im.getpixel((j+1,i))-im.getpixel((j-1,i+1))-im.getpixel((j,i+1))-im.getpixel((j+1,i+1))
			if a < mi:
				mi = a
			if a > ma:
				ma = a
			if a > 255:
				newImage_list[i][j] = 255
			elif a < 0:
				newImage_list[i][j] = 0
			else:
				newImage_list[i][j] = a
	print mi, ma
	for i in range(0, row-1):
		for j in range(0, col-1):
			# print mi
			newImage_list[i][j] = ((newImage_list[i][j]+abs(mi))/float(ma+abs(mi)))*255
			if newImage_list[i][j] > 255:
				newImage_list[i][j] = 255
	img = Image.fromarray(newImage_list)
	img.save('0343(b).tif')
#enhance
def c():
	im = Image.open("Fig0343.tif").convert('L')
	im2 = Image.open("0343(b).tif").convert('L')
	col, row = im.size
	newImage_list = np.empty((row, col),dtype=np.uint8)

	for i in range(0,row):
		for j in range(0,col):
			a = im.getpixel((j,i))+im2.getpixel((j,i))
			if a > 255:
				newImage_list[i][j] = 255
			elif a < 0:
				newImage_list[i][j] = 0
			else:
				newImage_list[i][j] = a
	img = Image.fromarray(newImage_list)
	img.save('0343(c).tif')
#Sobel
def d():
	im = Image.open("Fig0343.tif").convert('L')
	col, row = im.size
	newImage_list = np.empty((row, col),dtype=np.uint8)

	for i in range(1,row-1):
		for j in range(1,col-1):

			a = fabs(-im.getpixel((j-1,i-1))-2*im.getpixel((j,i-1))-im.getpixel((j+1,i-1))+im.getpixel((j-1,i+1))+2*im.getpixel((j,i+1))+im.getpixel((j+1,i+1)))
			b = fabs(-im.getpixel((j-1,i-1))+im.getpixel((j+1,i-1))-2*im.getpixel((j-1,i))+2*im.getpixel((j+1,i))-im.getpixel((j-1,i+1))+im.getpixel((j+1,i+1)))
			c = a + b
			if c > 255:
				newImage_list[i][j] = 255
			elif c < 0:
				newImage_list[i][j] = 0
			else:
				newImage_list[i][j] = c
	img = Image.fromarray(newImage_list)
	img.save('0343(d).tif')
#blur
def e():
	im = Image.open("0343(d).tif").convert('L')
	col, row = im.size
	newImage_list = np.empty((row, col),dtype=np.uint8)

	for i in range(2,row-2):
		for j in range(2,col-2):
			a = (im.getpixel((j-2,i-2))+im.getpixel((j-1,i-2))+im.getpixel((j,i-2))+im.getpixel((j+1,i-2))+im.getpixel((j+2,i-2))+
				 im.getpixel((j-2,i-1))+im.getpixel((j-1,i-1))+im.getpixel((j,i-1))+im.getpixel((j+1,i-1))+im.getpixel((j+2,i-1))+
				 im.getpixel((j-2,i))+im.getpixel((j-1,i))+im.getpixel((j,i))+im.getpixel((j+1,i))+im.getpixel((j+2,i))+
				 im.getpixel((j-2,i+1))+im.getpixel((j-1,i+1))+im.getpixel((j,i+1))+im.getpixel((j+1,i+1))+im.getpixel((j+2,i+1))+
				 im.getpixel((j-2,i+2))+im.getpixel((j-1,i+2))+im.getpixel((j,i+2))+im.getpixel((j+1,i+2))+im.getpixel((j+2,i+2)))/25
			if a > 255:
				newImage_list[i][j] = 255
			elif a < 0:
				newImage_list[i][j] = 0
			else:
				newImage_list[i][j] = a
	img = Image.fromarray(newImage_list)
	img.save('0343(e).tif')
#enhance
def f():
	im = Image.open("0343(c).tif")#.convert('L')
	im2 = Image.open("0343(e).tif")#.convert('L')
	col, row = im.size
	newImage_list = np.empty((row, col),dtype=np.uint8)

	for i in range(0,row):
		for j in range(0,col):
			a = (im.getpixel((j,i))*im2.getpixel((j,i)))/255
			if a > 255:
				newImage_list[i][j] = 255
			elif a < 0:
				newImage_list[i][j] = 0
			else:
				newImage_list[i][j] = a
	img = Image.fromarray(newImage_list)
	img.save('0343(f).tif')
#enhance
def g():
	im = Image.open("Fig0343.tif")#.convert('L')
	im2 = Image.open("0343(f).tif")#.convert('L')
	col, row = im.size
	newImage_list = np.empty((row, col),dtype=np.uint8)

	for i in range(0,row):
		for j in range(0,col):
			a = im.getpixel((j,i))+im2.getpixel((j,i))
			if a > 255:
				newImage_list[i][j] = 255
			elif a < 0:
				newImage_list[i][j] = 0
			else:
				newImage_list[i][j] = a
	img = Image.fromarray(newImage_list)
	img.save('0343(g).tif')
#result
def h():
	gamma = 0.7 #should between [0, 2.41]
	c = 10
	im = Image.open("0343(g).tif")#.convert('L')
	col, row = im.size
	newImage_list = np.empty((row, col),dtype=np.uint8)

	for i in range(0,row):
		for j in range(0,col):
			a = c*(im.getpixel((j,i))**gamma);
			if a > 255:
				newImage_list[i][j] = 255
			elif a < 0:
				newImage_list[i][j] = 0
			else:
				newImage_list[i][j] = a
	img = Image.fromarray(newImage_list)
	img.save('0343(h).tif')

# # histeq
# im = np.array(Image.open("/Users/lance/Desktop/project2/Fig0316_low.tif").convert('L'))
# im2 = Image.open("/Users/lance/Desktop/project2/Fig0316_low.tif")
# col, row = im2.size
# newImage_list = np.empty((row, col),dtype=np.uint8)
# histeq(im,im2,col,row)
# img = Image.fromarray(newImage_list)
# img.save('/Users/lance/Desktop/light_output.tif')

b()
# c()
# d()
# e()
# f()
# g()
# h()