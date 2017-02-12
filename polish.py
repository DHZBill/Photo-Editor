import scipy.stats as st
import numpy as np
import cv2

img = cv2.imread('C:\Users\herry_000\Desktop\oldmancolored.jpg',1)

def Gker(klen):
	sig = klen/7.
	interval = (2*sig+1.)/(klen)
	x = np.linspace(-sig-interval/2., sig+interval/2., klen+1)
	k1d = np.diff(st.norm.cdf(x))
	kraw = np.sqrt(np.outer(k1d,k1d))
	G = kraw/kraw.sum()
	return G

def Gblur(img,klen):
	G = Gker(klen)
	D = cv2.filter2D(img,-1,G)
	return D

def Skin(img,Blen,Glen,Opacity):
	HighPass = img.copy()
	HighPass = cv2.bilateralFilter(img,Blen/7,Blen,Blen)
	HighPass = HighPass - img + 128
	layer1 = Gblur(HighPass,Glen)
	layer2 = HighPass + img - 128
	R = (layer1/2 + layer2/2)
	return R


def DeNoise(img,klen):
	R = cv2.fastNlMeansDenoisingColored(img,None,klen,klen,7,15)
	return R



# def Inpaint(img,l,h):
# 	edges = cv2.Canny(cv2.GaussianBlur(img,(5,5),1),l,h)
# 	cv2.imshow('edges',edges)
# 	dim = edges.shape
	# return cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA)


Isize = img.shape
klen = min(Isize[0],Isize[1])

# Inpaint(img,100,200)
cv2.imshow('dddhhhzzz',DeNoise(img,10))
cv2.imshow('dhz',Skin(img,klen/10,3,50))
cv2.imshow('ddhhzz',cv2.bilateralFilter(img,klen/70,klen/10,klen/10))

cv2.waitKey(0)
cv2.destroyAllWindows()