from PIL import Image
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import math

def b():
	im = Image.open("/Users/lance/Desktop/project2/p2test.tif")#.convert('L')
	col, row = im.size
	newImage_list = np.empty((row, col),dtype=np.uint8)
	mi = 255
	for i in range(1,row-1):
		for j in range(1,col-1):
			a = (8*im.getpixel((j,i)))-im.getpixel((j-1,i-1))-im.getpixel((j,i-1))-im.getpixel((j+1,i-1))-im.getpixel((j-1,i))-im.getpixel((j+1,i))-im.getpixel((j-1,i+1))-im.getpixel((j,i+1))-im.getpixel((j+1,i+1))
			if a < mi:
				mi = a
			if a > 255:
				newImage_list[i][j] = 255
			elif a < 0:
				newImage_list[i][j] = 0
			else:
				newImage_list[i][j] = a
	for i in range(0, row-1):
		for j in range(0, col-1):
			# print mi
			newImage_list[i][j] += abs(mi)
			if newImage_list[i][j] > 255:
				newImage_list[i][j] = 255
	img = Image.fromarray(newImage_list)
	img.save('/Users/lance/Desktop/p2test(b).tif')

def b_1():
	im = Image.open("/Users/lance/Desktop/project2/p2test.tif")#.convert('L')
	col, row = im.size
	newImage_list = np.empty((row, col),dtype=np.uint8)
	# mi = 255
	for i in range(1,row-1):
		for j in range(1,col-1):
			a = (8*im.getpixel((j,i)))-im.getpixel((j-1,i-1))-im.getpixel((j,i-1))-im.getpixel((j+1,i-1))-im.getpixel((j-1,i))-im.getpixel((j+1,i))-im.getpixel((j-1,i+1))-im.getpixel((j,i+1))-im.getpixel((j+1,i+1))
			# if a < mi:
			# 	mi = a
			if a > 255:
				newImage_list[i][j] = 255
			elif a < 0:
				newImage_list[i][j] = 0
			else:
				newImage_list[i][j] = a
	# for i in range(0, row-1):
	# 	for j in range(0, col-1):
	# 		# print mi
	# 		newImage_list[i][j] += abs(mi)
	# 		if newImage_list[i][j] > 255:
	# 			newImage_list[i][j] = 255
	img = Image.fromarray(newImage_list)
	img.save('/Users/lance/Desktop/p2test(b).tif')

def c():
	im = Image.open("/Users/lance/Desktop/project2/p2test.tif")#.convert('L')
	im2 = Image.open("/Users/lance/Desktop/p2test(b).tif")#.convert('L')
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
	img.save('/Users/lance/Desktop/p2test(c).tif')

def d():
	im = Image.open("/Users/lance/Desktop/project2/p2test.tif")#.convert('L')
	col, row = im.size
	newImage_list = np.empty((row, col),dtype=np.uint8)

	for i in range(1,row-1):
		for j in range(1,col-1):

			a = fabs(-im.getpixel((j-1,i-1))-3*im.getpixel((j,i-1))-im.getpixel((j+1,i-1))+im.getpixel((j-1,i+1))+3*im.getpixel((j,i+1))+im.getpixel((j+1,i+1)))
			b = fabs(-im.getpixel((j-1,i-1))+im.getpixel((j+1,i-1))-3*im.getpixel((j-1,i))+3*im.getpixel((j+1,i))-im.getpixel((j-1,i+1))+im.getpixel((j+1,i+1)))
			c = a + b
			if c > 255:
				newImage_list[i][j] = 255
			elif c < 0:
				newImage_list[i][j] = 0
			else:
				newImage_list[i][j] = c
	img = Image.fromarray(newImage_list)
	img.save('/Users/lance/Desktop/p2test(d).tif')

def e():
	im = Image.open("/Users/lance/Desktop/p2test(d).tif")#.convert('L')
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
	img.save('/Users/lance/Desktop/p2test(e).tif')

def e_2():
	im = Image.open("/Users/lance/Desktop/p2test(e).tif")#.convert('L')
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
	img.save('/Users/lance/Desktop/p2test(e).tif')

def f():
	im = Image.open("/Users/lance/Desktop/p2test(c).tif")#.convert('L')
	im2 = Image.open("/Users/lance/Desktop/p2test(e).tif")#.convert('L')
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
	img.save('/Users/lance/Desktop/p2test(f).tif')

def g():
	im = Image.open("/Users/lance/Desktop/project2/p2test.tif")#.convert('L')
	# im2 = Image.open("/Users/lance/Desktop/p2test(f).tif")#.convert('L')
	im3 = Image.open("/Users/lance/Desktop/p2test(e).tif")
	col, row = im.size
	newImage_list = np.empty((row, col),dtype=np.uint8)

	for i in range(0,row):
		for j in range(0,col):
			a = im.getpixel((j,i))+1.5*im3.getpixel((j,i))
			if a > 255:
				newImage_list[i][j] = 255
			elif a < 0:
				newImage_list[i][j] = 0
			else:
				newImage_list[i][j] = a
	img = Image.fromarray(newImage_list)
	img.save('/Users/lance/Desktop/p2test(g).tif')

def h():
	gamma = 0.55 #should between [0, 2.41]
	c = 10
	im = Image.open("/Users/lance/Desktop/p2test(g).tif")#.convert('L')
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
	img.save('/Users/lance/Desktop/p2test(h).tif')

# b()
# b_1()
# c()
# d()
# e()
# e_2()
# f()
# g()
# h()