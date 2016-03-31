from PIL import Image
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import math

def widget_col(img, wavlet_img, height, width):
	for h in range(0,height):
		for w in range(0,width,2):
			p = float(img[h][w])
			p_next = float(img[h][w+1])
			L = (p + p_next)/(2**0.5)
			H = (p - p_next)/(2**0.5)
			wavlet_img[h][w/2] = L
			wavlet_img[h][width/2+w/2] = H

def widget_row(wavlet_img, wavlet_img2, height, width):
	for h in range(0,height,2):
		for w in range(0,width):
			p = wavlet_img[h][w]
			p_next = wavlet_img[h+1][w]
			L = (p + p_next)/(2**0.5)
			H = (p - p_next)/(2**0.5)
			wavlet_img2[h/2][w] = L
			wavlet_img2[height/2+h/2][w] = H

def iwidget_col(ori1, ori2, height, width):
	for w in range(0,width/2):
		for h in range(0,height):
			ori1[h][w*2] = (ori2[h][w]+ori2[h][width/2+w])/(2**0.5)
			ori1[h][w*2+1] = (ori2[h][w]-ori2[h][width/2+w])/(2**0.5)

def iwidget_row(ori2, data, height, width):
	for w in range(0,width):
		for h in range(0,height/2):
			ori2[h*2][w] = (data[h][w]+data[height/2+h][w])/(2**0.5)
			ori2[h*2+1][w] = (data[h][w]-data[height/2+h][w])/(2**0.5)

im = np.asarray(Image.open("Fig0809.tif"))
im2 = Image.open("Fig0809.tif")
col, row = im2.size
col2 = col/2
row2 = row/2
wavlet_img = np.zeros((row, col))
wavlet_img2 = np.zeros((row, col))
wavlet_img3 = np.zeros((row2, col2))
wavlet_img4 = np.zeros((row2, col2))
ori1 = np.zeros((row, col))
ori2 = np.zeros((row, col))
ori3 = np.zeros((row, col))
ori4 = np.zeros((row, col))
widget_col(im, wavlet_img, col, row)
widget_row(wavlet_img, wavlet_img2, col, row)
widget_col(wavlet_img2, wavlet_img3, col2, row2)
widget_row(wavlet_img3, wavlet_img4, col2, row2)
for i in range(0,row2):
	for j in range(0,col2):
		wavlet_img2[i][j] = wavlet_img4[i][j]

np.savetxt('Output.txt', wavlet_img2, fmt="%f")

opendata = np.loadtxt('Output.txt').reshape((512,512))
iwidget_row(ori2, opendata, 256, 256)
iwidget_col(ori1, ori2, 256, 256)
iwidget_row(ori3, ori1, 512, 512)
iwidget_col(ori4, ori3, 512, 512)
np.savetxt('Output2.txt', ori4, fmt="%f")
data = np.loadtxt('Output2.txt').reshape((512,512))
img = Image.fromarray(data)
img.show()
