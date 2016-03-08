from PIL import Image
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import math

def fft2d(c, col, row, dir, m):
	real = np.zeros(1024,dtype=double)
	imag = np.zeros(1024,dtype=double)
	for j in range(0,row):
		for i in range(0,col):
			real[i] = c[i][j].real
			imag[i] = c[i][j].imag
		fft(dir,m,real,imag)
		for i in range(0,col):
			c[i][j] = real[i]+1j*imag[i]
	# print "KKKK"
	for i in range(0,col):
		for j in range(0,row):
			real[j] = c[i][j].real
			imag[j] = c[i][j].imag

		fft(dir,m,real,imag)
		for j in range(0,row):
			c[i][j] = real[j]+1j*imag[j]

def fft(dir, m, x, y):
	nn = 1
	for i in range(0,m):
		nn *= 2
	i2 = nn >> 1
	j = 0
	for i in range(0,nn-1):
		if i < j:
			tx = x[i]
			ty = y[i]
			x[i] = x[j]
			y[i] = y[j]
			x[j] = tx
			y[j] = ty
		k = i2
		while k <= j:
			j -= k
			k >>= 1
		j += k

	c1 = -1.0
	c2 = 0.0
	l2 = 1
	for l in range(0,m):
		l1 = l2
		l2 <<= 1
		u1 = 1.0
		u2 = 0.0
		for j in range(0,l1):
			for i in range(j,nn,l2):
				i1 = i + l1
				t1 = u1*x[i1]-u2*y[i1]
				t2 = u1*y[i1]+u2*x[i1]
				x[i1] = x[i] - t1
				y[i1] = y[i] - t2
				x[i] += t1
				y[i] += t2
			z = u1*c1-u2*c2
			u2 = u1*c2+u2*c1
			u1 = z
		c2 = sqrt((1.0-c1)/2.0)
		if dir == 1:
			c2 = -c2
		c1 = sqrt((1.0+c1)/2.0)

	if dir == -1:
		for i in range(0,nn):
			x[i] /= double(nn)
			y[i] /= double(nn)


def accumu(lis):
    total = 0
    for x in lis:
        total += x
        yield total

def histeq(im,im2,col,row):
    #get image histogram
    imhist,bins = np.histogram(im.flatten(),range(0,257))
    newImage_list = np.empty((row, col),dtype=np.uint8)
    k = []

    cdf = imhist.cumsum() #cumulative distribution function
    for i in range(0,256):
		k.append(imhist[i]/float(cdf[255]))

    k = list(accumu(k))

    for i in range(0,row):
   		for j in range(0,col):
   			newImage_list[i][j] = round(k[int(im2.getpixel((j,i)))]*255)
    img = Image.fromarray(newImage_list)
    img.show()

def BHPF():
	im = np.asarray(Image.open("/Users/lance/Desktop/Project3/Fig0516(a)(applo17_boulder_noisy).tif"))
	im2 = Image.open("/Users/lance/Desktop/Project3/Fig0516(a)(applo17_boulder_noisy).tif")
	imz = np.asarray(Image.open("/Users/lance/Desktop/Project3/c.tif"))
	col, row = im2.size
	freq = np.fft.fft2(im)
	freq_shift = np.fft.fftshift(freq)
	freq_log = log(freq_shift+1)
	max = np.amax(freq_log)
	freq_result = (255/max)*freq_log
	img = Image.fromarray(abs(freq_result))
	img.show()
	H = np.ones((row, col), dtype=np.uint8)
	for i in range(0,row):
		for j in range(0,col):
			if imz[i][j] < 100:
				H[i][j] = 0
			else:
				H[i][j] = 1

	freqc = H*freq_shift
	freq_ifftc = abs(np.fft.ifft2(freqc))
	max = np.amax(freq_ifftc)
	freq_result = (255/max)*freq_ifftc
	img = Image.fromarray(freq_result)
	img.show()


def GHPF():
	im = np.asarray(Image.open("/Users/lance/Desktop/Project3/Fig0459(a)(orig_chest_xray).tif"))
	im2 = Image.open("/Users/lance/Desktop/Project3/Fig0459(a)(orig_chest_xray).tif")
	col, row = im2.size
	freq = np.fft.fft2(im)
	freq_shift = np.fft.fftshift(freq)
	H = np.ones((row, col))
	center_y = row/2
	center_x = col/2
	d0 = 40
	k1 = 0.5
	k2 = 0.75
	t1 = d0*2

	for y in range(0,row):
		for x in range(0,col):
			r1 = (y - center_y)**2+(x - center_x)**2
			r = math.sqrt(r1)
			if 0 < r < d0:
				H[y,x] = 1 - math.exp(-r**2/t1**2)
	b = freq_shift*H
	c = freq_shift*(k1+k2*H)
	freq_ifftb = abs(np.fft.ifft2(b))
	freq_ifftc = abs(np.fft.ifft2(c))
	img = Image.fromarray(freq_ifftb)
	img.show()
	max = np.amax(freq_ifftc)
	freq_result = (255/max)*freq_ifftc
	img = Image.fromarray(freq_result)
	img.show()
	histeq(freq_result,img,col,row)

def spectrum():
	im = np.asarray(Image.open("/Users/lance/Desktop/Project3/Fig0424(a)(rectangle).tif"))
	im2 = Image.open("/Users/lance/Desktop/Project3/Fig0424(a)(rectangle).tif")
	col, row = im2.size
	rpower = ceil(math.log(row,2))
	cpower = ceil(math.log(col,2))
	row2 = 2**rpower
	col2 = 2**cpower
	C = np.zeros((row2,col2),dtype=np.complex_)
	for i in range(0,row):
		for j in range(0,col):
			C[i][j] += im[i][j]
	fft2d(C, int(row2), int(col2), 1, int(rpower))
	absc = abs(C)
	max = np.amax(absc)
	freq_result = (255/max)*absc
	img_b = Image.fromarray(freq_result)
	img_b.show()

	freq_shift = np.fft.fftshift(C)
	freq_abs = abs(freq_shift)
	max = np.amax(freq_abs)
	freq_result = (255/max)*freq_abs
	img_c = Image.fromarray(freq_result)
	img_c.show()
	freq_log = log(freq_abs+1)
	max = np.amax(freq_log)
	freq_result = (255/max)*freq_log
	img_d = Image.fromarray(freq_result)
	img_d.show()

# BHPF()
# GHPF()
spectrum()
